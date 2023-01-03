<<<<<<< HEAD
from exceptiongroup import catch
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

user = input("Entrer votre nom utilisateur :")
mdp = input("Entrer votre mot de passe :")

browser = webdriver.Firefox()
browser.get('https://celene.univ-orleans.fr/login/index.php?authCAS=CAS')

champ_identifiant = browser.find_element(By.ID,"username")
champ_identifiant.clear()
champ_identifiant.send_keys(user)

champ_mdp = browser.find_element(By.ID,"password")
champ_mdp.clear()
champ_mdp.send_keys(mdp)

champ_mdp.send_keys(Keys.RETURN)

browser.implicitly_wait(10)
bouton_cour = browser.find_element(By.CSS_SELECTOR,"a[href=\"https://celene.univ-orleans.fr/my/courses.php\"]")
bouton_cour.send_keys(Keys.RETURN)

browser.find_element(By.PARTIAL_LINK_TEXT,"(BUT2)").click()


browser.find_element(By.PARTIAL_LINK_TEXT,"QCM (26/10/2022)").click()
try:
    browser.find_element(By.PARTIAL_LINK_TEXT,"Résultats").click()
except:
    browser.find_element(By.PARTIAL_LINK_TEXT,"Réponse").click()

browser.find_element(By.XPATH ,"//button[text()='Télécharger']").click()
# browser.close()
=======
import sys

sys.path.append('./SQLAlchemy')
from getpass import getpass
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from connexion_BD import ouvrir_connexion
import fonction_BD
from QCM import QCM
from Sondage import Sondage
from Matiere import Matiere
import subprocess
import traitement
import os
os.environ['MOZ_HEADLESS'] = '1'

user = input("Entrer votre nom utilisateur :")
mdp = getpass("Entrer votre mot de passe :")

connexion = ouvrir_connexion("manach","manach","servinfo-mariadb","DBmanach")

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

        bouton_matiere = browser.find_element(By.PARTIAL_LINK_TEXT,partie[0])
        id_matiere = fonction_BD.id_matiere(connexion,Matiere(0,bouton_matiere.text.split("\n")[1]))
        bouton_matiere.click()

        for i in range(1,len(partie)):
            bouton_questionnaire = browser.find_element(By.PARTIAL_LINK_TEXT,partie[i])
            nom_partie = bouton_questionnaire.text
            bouton_questionnaire.click()
            if "QCM" in partie[i]:
                nom_matiere = browser.find_element(By.XPATH,"/html/body/div[2]/div[4]/div/header/div/div[1]/div[1]/nav/ol/li[1]/a")
                id_QCM = fonction_BD.id_QCM(connexion,QCM(0,nom_matiere.text,browser.current_url,id_matiere))
                nom = nom_matiere.text +" -"+ nom_partie +"-notes.csv"
                list_move.insert(0,(id_QCM,nom.replace("/",""),None))
                browser.find_element(By.PARTIAL_LINK_TEXT,"Résultats").click()
            else:
                nom = nom_partie.split("\n")[0] + ".csv"
                id_sondage = fonction_BD.id_sondage(connexion,Sondage(0,browser.current_url))
                list_move.append((id_sondage,nom.replace("/",""),nom.split("(")[-1][:-5]))
                browser.find_element(By.PARTIAL_LINK_TEXT,"Réponses").click()
            browser.find_element(By.XPATH ,"//button[text()='Télécharger']").click()
            
            browser.back()
            browser.back()
        browser.back()
except Exception as inst:
    print(inst)
    print("erreur à la connexion")
finally:
    browser.close()

for (_,elem,_) in list_move:
    subprocess.run(["./Traitement_Selenium/move_document.sh",elem])

traitement.main(list_move)
>>>>>>> Dev
