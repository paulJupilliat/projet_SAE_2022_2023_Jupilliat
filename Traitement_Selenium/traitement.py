from sqlalchemy import create_engine
from sqlalchemy import func
from sqlalchemy.orm import declarative_base
engine = create_engine('mysql+mysqlconnector://lidec:lidec@localhost/enginelidec')

Base = declarative_base()

class Sondage(Base):
    __tablename__ = "sondage"
    idSond = engine.Column(engine.Integer, primary_key=True)
    urlSond = engine.Column(engine.String(500))
    dateSondage = engine.Column(engine.String(500))
    def __repr__(self):
        return f"Sondage({self.idSond}, {self.urlSond})"

class Matiere(Base):
    __tablename__ = "matiere"
    idMatiere = engine.Column(engine.Integer, primary_key=True)
    nomMatiere = engine.Column(engine.String(50))
    def __repr__(self):
        return f"Matiere({self.idMatiere}, {self.nomMatiere})"

class QCM(Base):
    __tablename__ = "qcm"
    idQCM = engine.Column(engine.Integer, primary_key=True)
    nomQCM = engine.Column(engine.String(50))
    urlQCM = engine.Column(engine.String(500))
    #relation pour avoir la matiere d un qcm
    idMatiere = engine.Column(engine.Integer, engine.ForeignKey("matiere.idMatiere"))
    #relation inverse pour avoir les qcm d une matiere
    matiere = engine.relationship("Matiere", backref=engine.backref("qcm", lazy="dynamic"))
    dateDebut = engine.Column(engine.String(500))
    dateFin = engine.Column(engine.String(500))
    def __repr__(self):
        return f"QCM({self.idQCM}, {self.nomQCM}, {self.urlQCM}, {self.dateDebut}, {self.dateFin})"

class Eleve(Base):
    __tablename__ = "eleve"
    numEtu = engine.Column(engine.Integer, primary_key=True)
    nom = engine.Column(engine.String(50))
    prenom = engine.Column(engine.String(50))
    groupeS1 = engine.Column(engine.String(50))
    groupeS2 = engine.Column(engine.String(50))
    def __repr__(self):
        return f"Eleve({self.nom}, {self.prenom}, {self.groupeS1}, {self.groupeS2})"

class ResultatQCM(Base):
    __tablename__ = "resultatqcm"
    idQCM = engine.Column(engine.Integer, engine.ForeignKey("qcm.idQCM"), primary_key=True)
    numEtu = engine.Column(engine.Integer, engine.ForeignKey("eleve.numEtu"), primary_key=True)
    note = engine.Column(engine.Integer)
    #un eleve peut avoir qu'une seule note pour un qcm
    eleve = engine.relationship(Eleve, backref=engine.backref("eleves", cascade="all, delete-orphan"),overlaps="qcm,eleve")
    #un qcm peut avoir qu'une seule note pour un eleve
    qcm = engine.relationship(QCM, backref=engine.backref("qcm", cascade="all, delete-orphan"),overlaps="qcm,eleve")
    def __repr__(self):
        return f"ResultatQCM({self.idQCM}, {self.numEtu}, {self.note})"

class RepSondage(Base):
    __tablename__ = "repsondage"
    idSondage = engine.Column(engine.Integer, engine.ForeignKey("sondage.idSondage"), primary_key=True)
    numEtu = engine.Column(engine.Integer, engine.ForeignKey("eleve.numEtu"), primary_key=True)
    
    matiereVoulu = engine.Column(engine.String(100))
    volontaire = engine.Column(engine.String(50))
    #relation pour avoir le sondage d une reponse
    sondage = engine.relationship(Sondage, backref=engine.backref("sondage", cascade="all, delete-orphan"),overlaps="sondage,eleve")
    #relation pour avoir l eleve d une reponse
    eleve = engine.relationship(Eleve, backref=engine.backref("eleves", cascade="all, delete-orphan"),overlaps="sondage,eleve")

    def __repr__(self):
        return f"RepSondage({self.participation}, {self.idSondage}, {self.numEtu}, {self.dateSondage}, {self.matiereVoulu}, {self.commentaire})"

def ajouter_resultat_eleve(id_QCM,num_etu,note):
    nb_rep = ResultatQCM.quety.filter(numEtu = num_etu).filter(idQCM = id_QCM).count()
    if nb_rep == 0:
        res = ResultatQCM(idQCM = id_QCM, numEtu = num_etu, note = note)
        engine.session.add(res)
        engine.session.commit()
    else:
        pass

def ajouter_reponse_sondage(participation : str, id_sondage: int, num_etu: str, date_sondage: str, matiere_voulu: str, commentaire: str):
    nb_rep = RepSondage.quety.filter(numEtu = num_etu).filter(idSondage = id_sondage).filter(dateSondage = date_sondage).count()
    if nb_rep == 0:
        rep = RepSondage(participation = participation, idSondage = id_sondage, numEtu = num_etu, dateSondage = date_sondage,
                        matiereVoulu = matiere_voulu, commentaire = commentaire)
        engine.session.add(rep)
        engine.session.commit()
    else:
        pass

def creation_existe(num_etu, nom, prenom, groupeS1, groupeS2):
    res = Eleve.query.filter(numEtu = num_etu).count()
    if res == 0:
        eleve = Eleve(numEtu = num_etu, nom = nom, prenom = prenom, groupeS1 = groupeS1, groupeS2 = groupeS2)
        engine.session.add(eleve)
        engine.session.commit()


def main(fichier_ouvrir):
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
                    models.ajouter_reponse_sondage(separe[consolidation],idpartie,separe[idenfiant],date,separe[matiere],separe[precision][:-1])
                except Exception as e:
                    print(e)
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
                        models.creation_existe(separe[idenfiant],separe[nom],separe[prenom],None,None)
                        note_total = float(separe[note][1:]) + float(separe[note + 1][:-1])
                        models.ajouter_resultat_eleve(idpartie,separe[idenfiant],(note_total/sur_combien)*20)

# main(["SAE _QCM -Test QCM (26102022)-notes.csv"])
