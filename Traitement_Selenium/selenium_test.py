from getpass import getpass
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import subprocess
import traitement
import os
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy import func
from sqlalchemy.orm import declarative_base, Session, relationship, backref
engine = create_engine('mysql+mysqlconnector://lidec:lidec@servinfo-mariadb/DBlidec', echo=True, future=True)
session = Session(engine)
Base = declarative_base()

class Sondage(Base):
    __tablename__ = "sondage"
    idSond = Column(Integer, primary_key=True)
    urlSond = Column(String(500))
    dateSondage = Column(String(500))
    def __repr__(self):
        return f"Sondage({self.idSond}, {self.urlSond})"

class Matiere(Base):
    __tablename__ = "matiere"
    idMatiere = Column(Integer, primary_key=True)
    nomMatiere = Column(String(50))
    def __repr__(self):
        return f"Matiere({self.idMatiere}, {self.nomMatiere})"

class QCM(Base):
    __tablename__ = "qcm"
    idQCM = Column(Integer, primary_key=True)
    nomQCM = Column(String(50))
    urlQCM = Column(String(500))
    #relation pour avoir la matiere d un qcm
    idMatiere = Column(Integer, ForeignKey("matiere.idMatiere"))
    #relation inverse pour avoir les qcm d une matiere
    matiere = relationship("Matiere", backref=backref("qcm", lazy="dynamic"))
    dateDebut = Column(String(500))
    dateFin = Column(String(500))
    def __repr__(self):
        return f"QCM({self.idQCM}, {self.nomQCM}, {self.urlQCM}, {self.dateDebut}, {self.dateFin})"

def get_id_QCM(nom_matiere, url, id_matiere):
    id_qcm = 0
    res = session.query(QCM).filter(QCM.urlQCM == url).count()
    if res == 0:
        qcm = QCM(idQCM = id_qcm, nomQCM = nom_matiere, urlQCM = url, idMatiere = id_matiere)
        session.add(qcm)
        session.commit()
        id_qcm = get_id_QCM_max()
    else:
        id_qcm = session.query(QCM.idQCM).filter(QCM.urlQCM == url).first()[0]
    return id_qcm

def get_id_sondage(url):
    id = 0
    res = session.query(Sondage).filter(Sondage.urlSond == url).count()
    if res == 0:
        sondage = Sondage(idSond = 0, urlSond = url)
        session.add(sondage)
        session.commit()
        id = get_id_sondage_max()
        return id
    else:
        id = session.query(Sondage.idSond).filter(Sondage.urlSond == url).first()[0]
    return id

def get_id_matiere(nom_matiere):
    id = 0
    # select([func.count()]).select_from(select(Matiere).where(Matiere.nomMatiere.in_([nom_matiere])))
    res = session.query(Matiere).filter(Matiere.nomMatiere == nom_matiere).count()
    if res == 0:
        matiere = Matiere(idMatiere = 0, nomMatiere = nom_matiere)
        session.add(matiere)
        session.commit()
        id = get_id_matiere_max()
        return id
    else:
        id = session.query(Matiere.idMatiere).filter(Matiere.nomMatiere == nom_matiere).first()[0]
        print(id)
    return id
        
def get_id_matiere_max():
    res = session.query(func.max(Matiere.idMatiere)).scalar()
    return res
        
def get_id_QCM_max():
    return session.query(func.max(QCM.idQCM)).scalar()
        
def get_id_sondage_max():
    return session.query(func.max(Sondage.idSond)).scalar()

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

        bouton_matiere = browser.find_element(By.PARTIAL_LINK_TEXT,partie[0])
        id_matiere = get_id_matiere(bouton_matiere.text.split("\n")[1])
        bouton_matiere.click()

        for i in range(1,len(partie)):
            bouton_questionnaire = browser.find_element(By.PARTIAL_LINK_TEXT,partie[i])
            nom_partie = bouton_questionnaire.text
            bouton_questionnaire.click()
            if "QCM" in partie[i]:
                nom_matiere = browser.find_element(By.XPATH,"/html/body/div[2]/div[4]/div/header/div/div[1]/div[1]/nav/ol/li[1]/a")
                id_QCM = get_id_QCM(nom_matiere.text,browser.current_url,id_matiere)
                nom = nom_matiere.text +" -"+ nom_partie +"-notes.csv"
                list_move.insert(0,(id_QCM,nom.replace("/",""),None))
                browser.find_element(By.PARTIAL_LINK_TEXT,"Résultats").click()
            else:
                nom = nom_partie.split("\n")[0] + ".csv"
                id_sondage = get_id_sondage(browser.current_url)
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
