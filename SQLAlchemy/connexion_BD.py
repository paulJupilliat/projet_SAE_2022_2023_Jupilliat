from calendar import c
from matplotlib.pyplot import connect
from more_itertools import first
import sqlalchemy
import getpass


from Oraux import Oraux
from Prof import Prof
from Eleve import Eleve

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
    resultat = connexion.execute("update ORAUX set idEleve = %s where idOral = %s", (eleve.get_numEtu(),oral.get_idOral()))

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
    res = connexion.execute("select idEleve from ORAUX where idOral = %s", (oral.get_idOral(),))
    if eleve.get_numEtu() not in res :
        raise ValueError("l'élève n'est pas inscrit à l'oral")
    else:
        resultat = connexion.execute("update PARTICIPE set commentaire = %s where idOral = %s and idEleve = %s", (commentaire,oral.get_idOral(),eleve.get_numEtu()))


def ouvrir_connexion(user,passwd,host,database):
    """
    ouverture d'une connexion MySQL
    paramètres:
       user     (str) le login MySQL de l'utilsateur
       passwd   (str) le mot de passe MySQL de l'utilisateur
       host     (str) le nom ou l'adresse IP de la machine hébergeant le serveur MySQL
       database (str) le nom de la base de données à utiliser
    résultat: l'objet qui gère le connection MySQL si tout s'est bien passé
    """
    try:
        #creation de l'objet gérant les interactions avec le serveur de BD
        engine=sqlalchemy.create_engine('mysql+mysqlconnector://'+user+':'+passwd+'@'+host+'/'+database)
        #creation de la connexion
        cnx = engine.connect()
    except Exception as err:
        print(err)
        raise err
    print("connexion réussie")
    return cnx


if __name__ == "__main__":
    login="lemort"
    passwd="lemort"
    serveur="servinfo-mariadb"
    bd="DB"+login

    cnx = ouvrir_connexion(login,passwd,serveur,bd)
    #appel des procedures
    print(ajouter_prof_pour_un_oral(cnx, Prof(10, "arzouz","julien","juju@gmail.com" ), Oraux(2,"oral2",4)))


    