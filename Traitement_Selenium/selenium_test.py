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