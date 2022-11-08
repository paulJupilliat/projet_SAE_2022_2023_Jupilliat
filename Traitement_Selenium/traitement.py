
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
