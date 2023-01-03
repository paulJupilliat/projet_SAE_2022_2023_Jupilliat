from Oraux import Oraux
from Prof import Prof
from Eleve import Eleve
from Matiere import Matiere
from QCM import QCM
from Sondage import Sondage
from Reponse_sondage import Reponse_sondage
import connexion_BD


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

def max_idmatiere(connexion) -> int:
    idMatiere = connexion.execute("SELECT MAX(idMatiere) from MATIERE")
    for id in idMatiere:
        return id[0]
    return None

def id_matiere(connexion,matiere: Matiere):
    res = connexion.execute("SELECT idMatiere from MATIERE where MATIERE.nomMatiere=%s",(matiere.get_nomMatiere()))
    id_matiere = res.first()
    if id_matiere is None:
        idMatiere = max_idmatiere(connexion)
        if idMatiere is None:
            idMatiere = 1
        else:
            idMatiere += 1
        matiere.set_idMatiere(idMatiere)
        connexion.execute("INSERT INTO MATIERE values (%s,'%s')"%(matiere.get_idMatiere(),matiere.get_nomMatiere()))
    else:
        matiere.set_idMatiere(id_matiere[0])
    return matiere.get_idMatiere()

def max_idQCM(connexion) -> int:
    idQCM = connexion.execute("SELECT MAX(idQCM) from QCM")
    for id in idQCM:
        return id[0]
    return None

def id_QCM(connexion,QCM: QCM):
    res = connexion.execute("SELECT idQCM from QCM where QCM.nomQCM = %s",(QCM.get_nomQCM()))
    id_QCM = res.first()
    if id_QCM is None:
        idQCM = max_idQCM(connexion)
        if idQCM is None:
            idQCM = 1
        else:
            idQCM += 1
        QCM.set_idQCM(idQCM)
        connexion.execute("Insert INTO QCM (idQCM,nomQCM,urlQCM,idMatiere) values (%s,'%s','%s',%s)"%(idQCM,QCM.get_nomQCM(),QCM.get_urlQCM(),QCM.get_matiere()))
    else:
        QCM.set_idQCM(id_QCM[0])
    return QCM.get_idQCM()

def max_idSondage(connexion) -> int:
    idSondage = connexion.execute("SELECT MAX(idSondage) from SONDAGE")
    for id in idSondage:
        return id[0]
    return None

def id_sondage(connexion, sondage : Sondage):
    res = connexion.execute("SELECT idSondage from SONDAGE where SONDAGE.urlSondage = %s",(sondage.get_urlSondage()))
    id_sondage = res.first()
    if id_sondage is None:
        id_sondage = max_idSondage(connexion)
        if id_sondage is None:
            id_sondage = 1
        else:
            id_sondage += 1
        sondage.set_idSondage(id_sondage)
        connexion.execute("Insert INTO SONDAGE values (%s,'%s')"%(id_sondage,sondage.get_urlSondage()))
    else:
        sondage.set_urlSondage(id_sondage[0])
    return sondage.get_idSondage()

def creation_existe(connexion,etudiant:Eleve):
    res = connexion.execute("SELECT count(nomEleve) from ELEVE where ELEVE.numEtu= %s"%(etudiant.get_numEtu()))
    if res.first()[0] == 0:
        connexion.execute("INSERT INTO ELEVE(numEtu, nomEleve,prenomEleve) values (%s,'%s','%s')"%(etudiant.get_numEtu(),etudiant.get_nom(),etudiant.get_prenom()))
    #créer une vérification

def ajouter_reponse_sondage(connexion,rep_sondage: Reponse_sondage):
    nbsondage = connexion.execute("SELECT COUNT(participation) from REPSONDAGE where REPSONDAGE.numEtu=%s and REPSONDAGE.dateSondage=STR_TO_DATE(%s,'%s/%s/%s') and REPSONDAGE.idSondage=%s"%(rep_sondage.getEleve(),rep_sondage.getDateSondage(),"%d","%m","%Y",rep_sondage.getIdSondage()))
    res = nbsondage.first()
    print(res[0])
    if res[0] == 0:
        connexion.execute("INSERT INTO REPSONDAGE values ('%s','%s','%s',STR_TO_DATE('%s','%s/%s/%s'),%s,%s)"%(rep_sondage.getParticipation(),rep_sondage.getMatiere(),rep_sondage.getCommentaire(),rep_sondage.getDateSondage(),'%d',"%m","%Y",rep_sondage.getEleve(),rep_sondage.getIdSondage()))
    # else:
    #     connexion.execute("UPDATE REPONDAGE SET ")

def ajouter_resultat_eleve(connexion, id_eleve :int, id_qcm :int, resultat: int):
    """ajoute une note une note à un élève pour un QCM

    Args:
        connexion (_type_): la connexion à la base de données
        eleve (int): l'id de l'élève
        QCM (int): l'id du QCM
        resultat (int): le résultat
    """
    nbresultat = connexion.execute("SELECT COUNT(note) FROM RESULTAT where RESULTAT.idQCM=%s and RESULTAT.numEtu=%s"%(id_qcm,id_eleve))
    if nbresultat.first()[0] == 0:
        connexion.execute("INSERT INTO RESULTAT values (%s,%s,%s)"%(resultat,id_qcm,id_eleve))
    else:
        connexion.execute("UPDATE RESULTAT set note=%s where RESULTAT.idQCM=%s and RESULTAT.numEtu=%s"%(resultat,id_qcm,id_eleve))

# print(id_matiere(connexion_BD.ouvrir_connexion("manach","manach","servinfo-mariadb","DBmanach"),Matiere(0,"R1.01 test")))
