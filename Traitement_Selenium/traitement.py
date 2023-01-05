from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy import func
from sqlalchemy.orm import declarative_base, Session, relationship, backref
Base = declarative_base()
engine = create_engine('mysql+mysqlconnector://lidec:lidec@servinfo-mariadb/DBlidec', echo=True, future=True)
session = Session(engine)

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

class Eleve(Base):
    __tablename__ = "eleve"
    numEtu = Column(Integer, primary_key=True)
    nom = Column(String(50))
    prenom = Column(String(50))
    groupeS1 = Column(String(50))
    groupeS2 = Column(String(50))
    def __repr__(self):
        return f"Eleve({self.nom}, {self.prenom}, {self.groupeS1}, {self.groupeS2})"

class ResultatQCM(Base):
    __tablename__ = "resultatqcm"
    idQCM = Column(Integer, ForeignKey("qcm.idQCM"), primary_key=True)
    numEtu = Column(Integer, ForeignKey("eleve.numEtu"), primary_key=True)
    note = Column(Integer)
    #un eleve peut avoir qu'une seule note pour un qcm
    eleve = relationship(Eleve, backref=backref("eleverepqcm", lazy="dynamic"))
    #un qcm peut avoir qu'une seule note pour un eleve
    qcm = relationship(QCM, backref=backref("qcm", lazy="dynamic"))
    def __repr__(self):
        return f"ResultatQCM({self.idQCM}, {self.numEtu}, {self.note})"

class RepSondage(Base):
    __tablename__ = "repsondage"
    idSondage = Column(Integer, ForeignKey("sondage.idSond"), primary_key=True)
    numEtu = Column(Integer, ForeignKey("eleve.numEtu"), primary_key=True)
    matiereVoulu = Column(String(100))
    volontaire = Column(String(50))
    #relation pour avoir le sondage d une reponse
    sondage = relationship(Sondage, backref=backref("sondage", lazy="dynamic"))
    #relation pour avoir l eleve d une reponse
    eleve = relationship(Eleve, backref=backref("eleverepsondage", lazy="dynamic"))

    def __repr__(self):
        return f"RepSondage({self.participation}, {self.idSondage}, {self.numEtu}, {self.dateSondage}, {self.matiereVoulu}, {self.commentaire})"

def ajouter_resultat_eleve(id_QCM,num_etu,note):
    nb_rep = session.query(ResultatQCM).filter(ResultatQCM.numEtu == num_etu).count()
    if nb_rep == 0:
        res = ResultatQCM(idQCM = id_QCM, numEtu = num_etu, note = note)
        session.add(res)
        session.commit()
    else:
        pass

def ajouter_reponse_sondage(participation : str, id_sondage: int, num_etu: str, date_sondage: str, matiere_voulu: str, commentaire: str):
    nb_rep = session.query(RepSondage).filter(RepSondage.numEtu == num_etu).filter(RepSondage.idSondage == id_sondage).count()
    if nb_rep == 0:
        rep = RepSondage(volontaire = participation, idSondage = id_sondage, numEtu = num_etu,
                        matiereVoulu = matiere_voulu, commentaire = commentaire)
        session.add(rep)
        session.commit()
    else:
        pass

def creation_existe(num_etu, nom, prenom, groupeS1, groupeS2):
    res = session.query(Eleve).filter(Eleve.numEtu == num_etu).count()
    if res == 0:
        eleve = Eleve(numEtu = num_etu, nom = nom, prenom = prenom, groupeS1 = groupeS1, groupeS2 = groupeS2)
        session.add(eleve)
        session.commit()

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
                    ajouter_reponse_sondage(separe[consolidation],idpartie,separe[idenfiant],date,separe[matiere],separe[precision][:-1])
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
                        creation_existe(separe[idenfiant],separe[nom],separe[prenom],None,None)
                        note_total = float(separe[note][1:]) + float(separe[note + 1][:-1])
                        ajouter_resultat_eleve(idpartie,separe[idenfiant],(note_total/sur_combien)*20)

main([(1,"Sondage (11112022).csv","")])
