import connexion_BD
from Eleve import Eleve
from QCM import QCM

def main(fichier_ouvrir):
    for fic in fichier_ouvrir:
        fichier = open("./Traitement_Selenium/"+fic,"r")
        entete = fichier.readline()
        ligne_en_tete = entete.split(",")
        nom = 0
        prenom = 0
        idenfiant = 0
        note = 0
        sur_combien = 0
        print(ligne_en_tete)
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
                print("l'étudiant d'identifiant " + separe[idenfiant] + " souhaite participer à la consolidation : " + separe[consolidation] )
                if separe[consolidation] != "Non":
                    print("Dans la matière : "+ separe[matiere])
                print("commentaire : " + separe[precision][:-1])
        else:
            list_resultat = []
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
                        print(separe[nom])
                        print(separe[prenom])
                        print(separe[idenfiant])
                        note_total = float(separe[note][1:]) + float(separe[note + 1][:-1])
                        print((note_total/sur_combien)*20)

# main(["SAE _QCM -Test QCM (26102022)-notes.csv"])
