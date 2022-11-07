from getpass import getpass
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

user = input("Entrer votre nom utilisateur :")
mdp = getpass("Entrer votre mot de passe :")

list_telechargement = [["(BUT2)","QCM (26/10/2022)","sondage (26/10/2022)"]]

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

for partie in list_telechargement:

    browser.find_element(By.PARTIAL_LINK_TEXT,partie[0]).click()

    for i in range(1,len(partie)):
        browser.find_element(By.PARTIAL_LINK_TEXT,partie[i]).click()
        if "QCM" in partie[i]:
            browser.find_element(By.PARTIAL_LINK_TEXT,"Résultats").click()
        else:
            browser.find_element(By.PARTIAL_LINK_TEXT,"Réponses").click()
        browser.find_element(By.XPATH ,"//button[text()='Télécharger']").click()
        browser.back()
        browser.back()
    browser.back()
    
browser.close()