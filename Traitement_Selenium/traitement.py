from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy import func
from sqlalchemy.orm import declarative_base, Session, relationship, backref
Base = declarative_base()
engine = create_engine('mysql+mysqlconnector://paul:paul@localhost/soutien', echo=True, future=True)
# engine = create_engine('mysql+mysqlconnector://mathys:mathys@localhost/Poney', echo=True, future=True)
session = Session(engine)

class Eleve(Base):
    """classe Eleve
    """
    __tablename__ = "eleve"
    num_etu = Column(Integer, primary_key=True)
    nom = Column(String(50))
    prenom = Column(String(50))
    groupe_s1 = Column(String(50))
    groupe_s2 = Column(String(50))
    def __repr__(self):
        """representation de l objet Eleve"""
        return f"Eleve({self.nom}, {self.prenom}, {self.groupe_s1}, {self.groupe_s2})"

class Sondage(Base):
    """classe Sondage qui contient les sondages
    """
    __tablename__ = "sondage"
    id_sond = Column(Integer, primary_key=True)
    url_sond = Column(String(50))
    date_debut_sond = Column(String(50))
    def __repr__(self):
        """representation de l objet Sondage"""
        return f"Sondage({self.id_sond}, {self.url_sond})"
class Matiere(Base):
    """classe Matiere qui contient les matieres
    """
    __tablename__ = "matiere"
    id_matiere = Column(Integer, primary_key=True)
    nom_matiere = Column(String(50))
    def __repr__(self):
        """representation de l objet Matiere"""
        return f"Matiere({self.id_matiere}, {self.nom_matiere})"
class QCM(Base):
    """classe QCM qui contient les qcm
    """
    __tablename__ = "qcm"
    id_qcm = Column(Integer, primary_key=True)
    nom_qcm = Column(String(50))
    url_qcm = Column(String(50))
    #relation pour avoir la matiere d un qcm
    id_matiere = Column(Integer, ForeignKey("matiere.id_matiere"))
    #relation inverse pour avoir les qcm d une matiere
    matiere = relationship(Matiere, backref=backref("fk_matiere_qcm", lazy="dynamic"))
    date_debut = Column(String(50))
    date_fin = Column(String(50))
    def __repr__(self):
        """representation de l objet QCM"""
        return f"QCM({self.id_qcm}, {self.nom_qcm}, {self.url_qcm}, {self.date_debut}, {self.date_fin})"

class ResultatQCM(Base):
    """classe ResultatQCM qui fait la
    relation entre les qcm et les eleves -> note"""
    __tablename__ = "resultatqcm"
    id_qcm = Column(Integer, ForeignKey("qcm.id_qcm"), primary_key=True)
    num_etu = Column(Integer, ForeignKey("eleve.num_etu"), primary_key=True)
    note = Column(Integer)
    #un eleve peut avoir qu'une seule note pour un qcm
    eleve = relationship(Eleve, backref=backref("fk_resqcm_eleve", cascade="all, delete-orphan"),overlaps="qcm,eleve")
    #un qcm peut avoir qu'une seule note pour un eleve
    qcm = relationship(QCM, backref=backref("fk_resqcm_qcm", cascade="all, delete-orphan"),overlaps="qcm,eleve")
    def __repr__(self):
        """representation de l objet ResultatQCM"""
        return f"ResultatQCM({self.id_qcm}, {self.num_etu}, {self.note})"

class RepSondage(Base):
    """classe RepSondage qui fait la
    relation entre les sondages et les eleves -> reponses"""
    __tablename__ = "repsondage"
    id_sondage = Column(Integer, ForeignKey("sondage.id_sond"), primary_key=True)
    num_etu = Column(Integer, ForeignKey("eleve.num_etu"), primary_key=True)
    matiere_voulue = Column(String(100))
    volontaire = Column(String(50))
    commentaire = Column(String(80))
    #relation pour avoir le sondage d une reponse
    sondage = relationship(Sondage, backref=backref("fk_repsond_sondage", cascade="all, delete-orphan"),overlaps="sondage,eleve")
    #relation pour avoir l eleve d une reponse
    eleve = relationship(Eleve, backref=backref("fk_repsond_eleve", cascade="all, delete-orphan"),overlaps="sondage,eleve")
    def __repr__(self):
        """representation de l objet RepSondage"""
        return f"RepSondage({self.volontaire}, {self.id_sondage}, {self.num_etu}, {self.matiere_voulue}, {self.commentaire})"

def ajouter_resultat_eleve(id_QCM,num_etu,note):
    nb_rep = session.query(ResultatQCM).filter(ResultatQCM.num_etu == num_etu).count()
    if nb_rep == 0:
        res = ResultatQCM(id_qcm = id_QCM, num_etu = num_etu, note = note)
        session.add(res)
        session.commit()
    else:
        pass

def ajouter_reponse_sondage(participation : str, id_sondage: int, num_etu: str, date_debut_sondage: str, matiere_voulu: str, commentaire: str):
    nb_rep = session.query(RepSondage).filter(RepSondage.num_etu == num_etu).filter(RepSondage.id_sondage == id_sondage).count()
    if nb_rep == 0:
        rep = RepSondage(volontaire = participation, id_sondage = id_sondage, num_etu = num_etu,
                        matiere_voulue = matiere_voulu, commentaire = commentaire)
        session.add(rep)
        session.commit()
    else:
        pass

def creation_existe(num_etu, nom, prenom, groupe_S1, groupe_S2):
    res = session.query(Eleve).filter(Eleve.num_etu == num_etu).count()
    if res == 0:
        eleve = Eleve(num_etu = num_etu, nom = nom, prenom = prenom, groupe_s1 = groupe_S1, groupe_s2 = groupe_S2)
        session.add(eleve)
        session.commit()

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
                        print("l'étudiant d'identifiant " + separe[idenfiant] + " a eu la note de " + separe[note][1:] + " et " + separe[note + 1][:-1] + " sur " + str(sur_combien))
                        
                        