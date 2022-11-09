from Oraux import Oraux
from Prof import Prof
from Eleve import Eleve
from QCM import QCM

def ajouter_prof_pour_un_oral(connexion, prof,oral):
    """
    ajoute un professeur pour un oral, les contraintes sont vérifiées par la BD
    paramètres:
       connexion (connexion) la connexion à la base de données
       prof      (str) le nom du professeur
       oral      (str) le nom de l'oral
    résultat: aucun
    """
    resultat = connexion.execute("update ORAUX set idProf = %s where idOral = %s", (prof.get_idProf(),oral.get_idOral()))
    
def ajouter_elev_pour_un_oral(connexion, eleve,oral):
    """
    ajoute un élève pour un oral, les contraintes sont vérifiées par la BD
    paramètres:
       connexion (connexion) la connexion à la base de données
       eleve     (str) le nom de l'élève
       oral      (str) le nom de l'oral
    résultat: aucun
    """
    resultat = connexion.execute("update ORAUX set numEtu = %s where idOral = %s", (eleve.get_numEtu(),oral.get_idOral()))

def ajouter_commentaire(connexion,eleve, commentaire, oral):
    """
    ajoute un commentaire pour un oral, les contraintes sont vérifiées par la BD
    paramètres:
       connexion (connexion) la connexion à la base de données
       eleve     (str) le nom de l'élève
       commentaire (str) le commentaire
       oral      (str) le nom de l'oral
    résultat: aucun
    """
    # je verifie que l'élève est bien inscrit à l'oral
    res = connexion.execute("select numEtu from ORAUX where idOral = %s", (oral.get_idOral(),))
    if eleve.get_numEtu() not in res :
        raise ValueError("l'élève n'est pas inscrit à l'oral")
    else:
        resultat = connexion.execute("update PARTICIPE set commentaire = %s where idOral = %s and numEtu = %s", (commentaire,oral.get_idOral(),eleve.get_numEtu()))

def max_idQCM(connexion) -> int:
    idQCM = connexion.execute("SELECT MAX(idQCM) from QCM")
    for id in idQCM:
        return id[0]
    return None

def ajouter_resultat_eleve(connexion, eleve :Eleve, qcm :QCM, resultat: int):
    """ajoute une note une note à un élève pour un QCM

    Args:
        connexion (_type_): la connexion à la base de données
        eleve (Eleve): l'élève
        QCM (QCM): le QCM
        resultat (int): le résultat
    """
    res = connexion.execute("SELECT COUNT(nomEleve) from ELEVE where ELEVE.numEtu=%s",(eleve.get_numEtu()))
    if res[0] == 0:
        connexion.execute("INSERT INTO ELEVE (numEtu, nomEleve, prenomEleve) VALUES (%s,'%s','%s')",(eleve.get_numEtu(),eleve.get_nom(),eleve.get_prenom()))
    res = connexion.execute("SELECT COUNT(nomQCM) from QCM where QCM.idQCM = %s",(qcm.get_idQCM()))
    if res[0] == 0:
        idQCM = max_idQCM(connexion)
        if idQCM is None:
            idQCM = 1
        else:
            idQCM += 1
        qcm.set_idQCM(idQCM)
        connexion.execute("Insert INTO QCM (idQCM,nomQCM,) values (%s,'%s')",(idQCM,qcm.get_nomQCM()))
    nbresultat = connexion.execute("SELECT COUNT(note) FROM RESULTAT where RESULTAT.idQCM=%s and RESULTAT.numEtu=%s",(qcm.get_idQCM(),eleve.get_numEtu()))
    if nbresultat[0] == 0:
        connexion.execute("INSERT INTO RESULTAT values (%s,%s,%s)",(resultat,qcm.get_idQCM(),eleve.get_numEtu()))
    else:
        connexion.execute("UPDATE RESULTAT set note=%s where RESULTAT.idQCM=%s and RESULTAT.numEtu=%s",(resultat,qcm.get_idQCM(),eleve.get_numEtu()))
