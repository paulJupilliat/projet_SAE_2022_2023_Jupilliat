from getpass import getpass
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import subprocess
import os
import traitement
os.environ['MOZ_HEADLESS'] = '1'

user = input("Entrer votre nom utilisateur :")
mdp = getpass("Entrer votre mot de passe :")

list_telechargement = [["(BUT2)","QCM (26/10/2022)","Sondage (11/11/2022)"]]

list_move = []

browser = webdriver.Firefox()
browser.get('https://celene.univ-orleans.fr/login/index.php?authCAS=CAS')

champ_identifiant = browser.find_element(By.ID,"username")
champ_identifiant.clear()
champ_identifiant.send_keys(user)

champ_mdp = browser.find_element(By.ID,"password")
champ_mdp.clear()
champ_mdp.send_keys(mdp)

champ_mdp.send_keys(Keys.RETURN)

try:
    browser.implicitly_wait(10)
    bouton_cour = browser.find_element(By.CSS_SELECTOR,"a[href=\"https://celene.univ-orleans.fr/my/courses.php\"]")
    bouton_cour.send_keys(Keys.RETURN)

    for partie in list_telechargement:

        browser.find_element(By.PARTIAL_LINK_TEXT,partie[0]).click()

        for i in range(1,len(partie)):
            bouton_questionnaire = browser.find_element(By.PARTIAL_LINK_TEXT,partie[i])
            nom_partie = bouton_questionnaire.text
            bouton_questionnaire.click()
            if "QCM" in partie[i]:
                nom_matiere = browser.find_element(By.XPATH,"/html/body/div[2]/div[4]/div/header/div/div[1]/div[1]/nav/ol/li[1]/a")
                print(nom_matiere.text+"|")
                nom = nom_matiere.text +" -"+ nom_partie +"-notes.csv"
                list_move.append(nom.replace("/",""))
                browser.find_element(By.PARTIAL_LINK_TEXT,"Résultats").click()
            else:
                nom = nom_partie.split("\n")[0] + ".csv"
                list_move.append(nom.replace("/",""))
                browser.find_element(By.PARTIAL_LINK_TEXT,"Réponses").click()
            browser.find_element(By.XPATH ,"//button[text()='Télécharger']").click()
            
            browser.back()
            browser.back()
        browser.back()
except:
    print("erreur à la connexion")
finally:
    browser.close()

for elem in list_move:
    subprocess.run(["./move_document.sh",elem])

traitement.main(list_move)