<<<<<<< HEAD

def main():
    fichier = open("./SAE _QCM -Test QCM-notes.csv","r")
    entete = fichier.readline()
    ligne_en_tete = entete.split(",")
    nom = 0
    prenom = 0
    idenfiant = 0
    note = 0
    sur_combien = 0
    print(ligne_en_tete)
    if "identifiant" in ligne_en_tete[0]:
        for partie in ligne_en_tete:
            if "Consolidation" == partie:
                print()
    else:
        for partie in ligne_en_tete:
            if "Nom" in partie:
                print("Nom")
                nom = ligne_en_tete.index(partie)
                print(nom)
            elif "Prénom" in partie:
                print("prenom")
                prenom = ligne_en_tete.index(partie)
                print(prenom)
            elif "d\'identification" in partie:
                print("identifiant")
                idenfiant = ligne_en_tete.index(partie)
                print(idenfiant)
            elif "Note" in partie:
                print("Note")
                note = ligne_en_tete.index(partie)
                sur_combien = float(partie.split("/")[1])+float(ligne_en_tete[note + 1][:-1]) * 0.01
                print(sur_combien)
                print(note)
    for ligne in fichier:
        separe = ligne.split(",")
        if "Moyenne globale" not in separe[0]:
            if note != 0:
                print(separe[nom])
                print(separe[prenom])
                note_total = float(separe[note][1:]) + float(separe[note + 1][:-1])
                print((note_total/sur_combien)*20)

main()
=======
import sys
sys.path.append('./SQLAlchemy')
from Reponse_sondage import Reponse_sondage
from connexion_BD import ouvrir_connexion
import fonction_BD
from Eleve import Eleve
from QCM import QCM

def main(fichier_ouvrir):
    connexion = ouvrir_connexion("manach","manach","servinfo-mariadb","DBmanach")
    for (idpartie,fic,date) in fichier_ouvrir:
        fichier = open("./Traitement_Selenium/"+fic,"r")
        entete = fichier.readline()
        ligne_en_tete = entete.split(",")
        nom = 0
        prenom = 0
        idenfiant = 0
        note = 0
        sur_combien = 0
        if "Nom complet" in ligne_en_tete[0]:
            for partie in ligne_en_tete:
                if "Consolidation" in partie:
                    consolidation = ligne_en_tete.index(partie) + 1
                elif "Matière" in partie:
                    matiere = ligne_en_tete.index(partie) + 1
                elif "Précisions et commentaires" in partie:
                    precision = ligne_en_tete.index(partie) + 1
                elif "d\'identification" in partie:
                    idenfiant = ligne_en_tete.index(partie)
            for ligne in fichier:
                separe = ligne.split(",")
                try:
                    fonction_BD.ajouter_reponse_sondage(connexion,Reponse_sondage(separe[consolidation],separe[matiere],separe[precision][:-1],date,separe[idenfiant],idpartie))
                except:
                    print("éleve inconnu")
                print("l'étudiant d'identifiant " + separe[idenfiant] + " souhaite participer à la consolidation : " + separe[consolidation] )
                if separe[consolidation] != "Non":
                    print("Dans la matière : "+ separe[matiere])
                print("commentaire : " + separe[precision][:-1])
        else:
            for partie in ligne_en_tete:
                if "Nom" in partie:
                    nom = ligne_en_tete.index(partie)
                elif "Prénom" in partie:
                    prenom = ligne_en_tete.index(partie)
                elif "d\'identification" in partie:
                    idenfiant = ligne_en_tete.index(partie)
                elif "Note" in partie:
                    note = ligne_en_tete.index(partie)
                    sur_combien = float(partie.split("/")[1])+float(ligne_en_tete[note + 1][:-1]) * 0.01
            for ligne in fichier:
                separe = ligne.split(",")
                if "Moyenne globale" not in separe[0]:
                    if note != 0:
                        fonction_BD.creation_existe(connexion,Eleve(separe[idenfiant],separe[nom],separe[prenom],None,None))
                        note_total = float(separe[note][1:]) + float(separe[note + 1][:-1])
                        fonction_BD.ajouter_resultat_eleve(connexion,separe[idenfiant],idpartie,(note_total/sur_combien)*20)

# main(["SAE _QCM -Test QCM (26102022)-notes.csv"])
>>>>>>> Dev
