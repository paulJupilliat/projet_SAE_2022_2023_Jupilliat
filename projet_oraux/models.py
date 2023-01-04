## Models permet de definir les données de l app


from .app import db
from flask_login import UserMixin
from .app import login_manager

class Eleve(db.Model):
    __tablename__ = "eleve"
    numEtu = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50))
    prenom = db.Column(db.String(50))
    groupeS1 = db.Column(db.String(50))
    groupeS2 = db.Column(db.String(50))
    def __repr__(self):
        return f"Eleve({self.nom}, {self.prenom}, {self.groupeS1}, {self.groupeS2})"
class Sondage(db.Model):
    __tablename__ = "sondage"
    idSond = db.Column(db.Integer, primary_key=True)
    urlSond = db.Column(db.String(500))
    dateSondage = db.Column(db.String(500))
    def __repr__(self):
        return f"Sondage({self.idSond}, {self.urlSond})"
class QuestionSondage(db.Model):
    __tablename__ = "questionsondage"
    idSond = db.Column(db.Integer, db.ForeignKey("sondage.idSond"), primary_key=True)
    idQuestion = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(500))
    #relation pour avoir le sondage d une question
    sondage = db.relationship("Sondage", backref=db.backref("questionsondage", lazy="dynamic"))
    
    def __repr__(self):
        return f"QuestionSondage({self.idSond}, {self.idQuestion}, {self.question})"
class Matiere(db.Model):
    __tablename__ = "matiere"
    idMatiere = db.Column(db.Integer, primary_key=True)
    nomMatiere = db.Column(db.String(50))
    def __repr__(self):
        return f"Matiere({self.idMatiere}, {self.nomMatiere})"
class QCM(db.Model):
    __tablename__ = "qcm"
    idQCM = db.Column(db.Integer, primary_key=True)
    nomQCM = db.Column(db.String(50))
    urlQCM = db.Column(db.String(500))
    #relation pour avoir la matiere d un qcm
    idMatiere = db.Column(db.Integer, db.ForeignKey("matiere.idMatiere"))
    #relation inverse pour avoir les qcm d une matiere
    matiere = db.relationship("Matiere", backref=db.backref("qcm", lazy="dynamic"))
    dateDebut = db.Column(db.String(500))
    dateFin = db.Column(db.String(500))
    def __repr__(self):
        return f"QCM({self.idQCM}, {self.nomQCM}, {self.urlQCM}, {self.dateDebut}, {self.dateFin})"

class Professeur(db.Model):
    __tablename__ = "professeur"
    idProf = db.Column(db.String(500), primary_key=True)
    nomProf = db.Column(db.String(50))
    prenomProf = db.Column(db.String(50))
    emailProf = db.Column(db.String(500))
    def __repr__(self):
        return f"Professeur({self.idProf}, {self.nomProf}, {self.prenomProf}, {self.emailProf})"
class User(db.Model, UserMixin):
    __tablename__ = "user"
    username = db.Column(db.String(50), primary_key=True)
    password = db.Column(db.String(50))
    est_admin = db.Column(db.Boolean)
    def get_id(self):
        return self.username
    def est_admin(self):
        return self.est_admin
    def __repr__(self):
        return f"User({self.username}, {self.password}, {self.est_admin})"

class Oral(db.Model):
    __tablename__ = "oraux"
    idOral = db.Column(db.Integer, primary_key=True)
    dateOral = db.Column(db.String(500))
    heureOral = db.Column(db.String(500))
    #relation pour avoir la matiere d un oral
    idMatiere = db.Column(db.Integer, db.ForeignKey("matiere.idMatiere"))
    #relation inverse pour avoir les oraux d une matiere
    matiere = db.relationship("Matiere", backref=db.backref("oral", lazy="dynamic"))
    #relation pour avoir le professeur d un oral
    idProf = db.Column(db.String(500), db.ForeignKey("professeur.idProf"))
    #relation inverse pour avoir les oraux d un professeur
    professeur = db.relationship("Professeur", backref=db.backref("oral", lazy="dynamic"))
    def __repr__(self):
        return f"Oraux({self.idOral}, {self.dateOral}, {self.nomOral}, {self.nbElMax})"

class ParticipantsOral(db.Model):
    __tablename__ = "participantsoral"
    idOral = db.Column(db.Integer, db.ForeignKey("oral.idOralz"), primary_key=True)
    numEtu = db.Column(db.Integer, db.ForeignKey("eleve.numEtu"), primary_key=True)
    commentaire = db.Column(db.String(800))
    #relation pour avoir l oral d un participant
    oral= db.relationship(Oral, backref=db.backref("oraux", cascade="all, delete-orphan"),overlaps="oral,eleve")
    #relation pour avoir l eleve d un participant
    eleve= db.relationship(Eleve, backref=db.backref("eleves", cascade="all, delete-orphan"),overlaps="oral,eleve")
    def __repr__(self):
        return f"ParticipantsOral({self.idOral}, {self.numEtu})"
class ResultatQCM(db.Model):
    __tablename__ = "resultatqcm"
    idQCM = db.Column(db.Integer, db.ForeignKey("qcm.idQCM"), primary_key=True)
    numEtu = db.Column(db.Integer, db.ForeignKey("eleve.numEtu"), primary_key=True)
    note = db.Column(db.Integer)
    #un eleve peut avoir qu'une seule note pour un qcm
    eleve = db.relationship(Eleve, backref=db.backref("eleves", cascade="all, delete-orphan"),overlaps="qcm,eleve")
    #un qcm peut avoir qu'une seule note pour un eleve
    qcm = db.relationship(QCM, backref=db.backref("qcm", cascade="all, delete-orphan"),overlaps="qcm,eleve")
    def __repr__(self):
        return f"ResultatQCM({self.idQCM}, {self.numEtu}, {self.note})"

class RepSondage(db.Model):
    __tablename__ = "repsondage"
    idSondage = db.Column(db.Integer, db.ForeignKey("sondage.idSondage"), primary_key=True)
    numEtu = db.Column(db.Integer, db.ForeignKey("eleve.numEtu"), primary_key=True)
    matiereVoulu = db.Column(db.String(100))
    volontaire = db.Column(db.String(50))
    #relation pour avoir le sondage d une reponse
    sondage = db.relationship(Sondage, backref=db.backref("sondage", cascade="all, delete-orphan"),overlaps="sondage,eleve")
    #relation pour avoir l eleve d une reponse
    eleve = db.relationship(Eleve, backref=db.backref("eleves", cascade="all, delete-orphan"),overlaps="sondage,eleve")

    def __repr__(self):
        return f"RepSondage({self.participation}, {self.idSondage}, {self.numEtu}, {self.dateSondage}, {self.matiereVoulu}, {self.commentaire})"
class Periode(db.Model):
    __tablename__ = "periode"
    idPeriode = db.Column(db.Integer, primary_key=True)
    dateDebut = db.Column(db.String(500))
    dateFin = db.Column(db.String(500))
    semestre = db.Column(db.Integer)
    def __repr__(self):
        return f"Periode({self.idPeriode}, {self.dateDebut}, {self.dateFin})"
class Semaine(db.Model):
    __tablename__ = "semaine"
    idSemaine = db.Column(db.Integer, primary_key=True)
    dateDebut = db.Column(db.String(500))
    dateFin = db.Column(db.String(500))
    #ajout de la periode pour faciliter la recherche
    idPeriode = db.Column(db.Integer, db.ForeignKey("periode.idPeriode"))
    periode = db.relationship("Periode", backref=db.backref("semaine", lazy="dynamic"))
    def __repr__(self):
        return f"Semaine({self.idSemaine}, {self.dateDebut}, {self.dateFin})"

class PossibiliteSoutien(db.Model):
    __tablename__ = "possibilitesoutien"
    idProf = db.Column(db.String(500), db.ForeignKey("professeur.idProf"), primary_key=True)
    idMatiere = db.Column(db.Integer, db.ForeignKey("matiere.idMatiere"), primary_key=True)
    idPeriode = db.Column(db.Integer, db.ForeignKey("periode.idPeriode"), primary_key=True)

    #relation pour avoir le professeur d une possibilite de soutien
    professeur = db.relationship(Professeur, backref=db.backref("professeur", cascade="all, delete-orphan"),overlaps="professeur,matiere,periode")
    #relation pour avoir la matiere d une possibilite de soutien
    matiere = db.relationship(Matiere, backref=db.backref("matiere", cascade="all, delete-orphan"),overlaps="professeur,matiere,periode")
    #relation pour avoir la periode d une possibilite de soutien
    periode = db.relationship(Periode, backref=db.backref("periode", cascade="all, delete-orphan"),overlaps="professeur,matiere,periode")

    def __repr__(self):
        return f"PossibiliteSoutien({self.idProf}, {self.idMatiere}, {self.idPeriode})"
class EstDisponible(db.Model):
    __tablename__ = "estdisponible"
    idProf = db.Column(db.String(500), db.ForeignKey("professeur.idProf"), primary_key=True)
    idOral = db.Column(db.Integer, db.ForeignKey("oral.idOral"), primary_key=True)
    #relation pour avoir le professeur d une disponibilite
    professeur = db.relationship(Professeur, backref=db.backref("professeur", cascade="all, delete-orphan"),overlaps="professeur,oral")
    #relation pour avoir l oral d une disponibilite
    oral = db.relationship(Oral, backref=db.backref("oral", cascade="all, delete-orphan"),overlaps="professeur,oral")
    def __repr__(self):
        return f"EstDisponible({self.idProf}, {self.idOral})"

class ReponseQuestionSondage(db.Model):
    __tablename__ = "reponsequestionsondage"
    numEtu = db.Column(db.Integer, db.ForeignKey("eleve.numEtu"), primary_key=True)
    idQuestion = db.Column(db.Integer, db.ForeignKey("questionSondage.idQuestion"), primary_key=True)
    reponse = db.Column(db.String(500))
    #relation pour avoir l eleve d une reponse a une question
    eleve = db.relationship(Eleve, backref=db.backref("eleves", cascade="all, delete-orphan"),overlaps="sondage,eleve,questionSondage")
    #relation pour avoir la question d une reponse a une question
    question = db.relationship(QuestionSondage, backref=db.backref("questionSondage", cascade="all, delete-orphan"),overlaps="sondage,eleve,questionSondage")
    def __repr__(self):
        return f"ReponseQuestionSondage({self.numEtu}, {self.idQuestion}, {self.reponse})"

def get_moyenne_generale(id_qcm):
    #recupere la moyenne de la classe pour un qcm
    qcm_eleves = ResultatQCM.query.filter(ResultatQCM.idQCM == id_qcm).all()
    moyenne = 0
    for qcm_eleve in qcm_eleves:
        moyenne += qcm_eleve.note
    moyenne = moyenne / len(qcm_eleves)
    return moyenne

def get_recap_etudiant(id_etu,num_semaine):
    #recupere les qcms et le soutien eventuel de l etudiant pour la semaine donnée
    sem=Semaine.query.filter(Semaine.numSemaine==num_semaine).first().idSemaine
    qcms=get_res_QCM_eleve(id_etu,sem)
    soutien=get_soutiens_etudiant(id_etu,sem)
    return qcms,soutien

def get_soutiens_etudiant(id_etu):
    #recupere les soutiens de l etudiant
    ids_oraux = ParticipantsOral.query.filter(ParticipantsOral.numEtu == id_etu).all()
    oraux = []
    for id_oral in ids_oraux:
        oral=Oral.query.join(ParticipantsOral).filter(Oral.idOral == id_oral.idOral).first()
        semaine=Semaine.query.filter(Semaine.dateDebut <= oral.date).filter(Semaine.dateFin >= oral.date).first()
        oraux.append((oral,semaine))
    return oraux

def get_graphe_etudiant(id_etu,date_deb,date_fin,liste_mat):
    str_js="google.charts.load('current', {'packages':['line']});\n"
    str_js+="google.charts.setOnLoadCallback(drawChart);\n"
    str_js+="function drawChart() {\n"
    str_js+="\tvar data = new google.visualization.DataTable();\n"
    str_js+="\tdata.addColumn('number', 'Semaine');\n"
    for matiere in liste_mat:
        str_js+="\tdata.addColumn('number', '"+matiere+"');\n"
    semaines = Semaine.query.filter(Semaine.dateDebut >= date_deb).filter(Semaine.dateFin <= date_fin).all()
    for sem in semaines:
        liste_sem=[sem.numSemaine]
        for mat in liste_mat:
            #recupere la note si elle existe pour la semaine et la matiere
            idmat=Matiere.query.filter(Matiere.nomMatiere==mat).first().idMatiere
            qcm=QCM.query.filter(QCM.numEtu == id_etu).filter(QCM.idMatiere == idmat).filter(QCM.dateFin >= sem.dateDebut).filter(QCM.dateFin <= sem.dateFin).first()
            if note is None:
                liste_sem.append(0)
            else:
                #recupere la moyenne generale
                moyenne=get_moyenne_generale(qcm.idQCM)
                #recupere la note de l etudiant
                note=ResultatQCM.query.filter(ResultatQCM.idQCM == qcm.idQCM).filter(ResultatQCM.numEtu == id_etu).first().note
                #calcule l ecart
                ecart=note-moyenne
                liste_sem.append(ecart)
        str_js+="\tdata.addRow("+liste_sem+");"


def get_moyenne_groupe(groupe,id_qcm):
    qcm_eleves = ResultatQCM.query.filter(ResultatQCM.idQCM == id_qcm).all()
    dateqcm = QCM.query.filter(QCM.idQCM == id_qcm).first().dateFin
    periode = Periode.query.filter(Periode.dateDebut <= dateqcm).filter(Periode.dateFin >= dateqcm).first()
    semestre = periode.semestre
    moyenne = 0
    for qcm_eleve in qcm_eleves:
        eleve=Eleve.query.filter(Eleve.numEtu == qcm_eleve.numEtu).first()
        if semestre == 1:
            if eleve.groupeS1 == groupe:
                moyenne += qcm_eleve.note
        else:
            if eleve.groupeS2 == groupe:
                moyenne += qcm_eleve.note
    moyenne = moyenne / len(qcm_eleves)
    return moyenne

def get_resultats_qcm_accueil(date):
    """fonction recuperant les resultats de QCM pour une date en renvoyant les moyennes par groupe et par matiere

    Args:
        date (String): date du QCM
    """
    #on regarde dans quelle semaine on est
    sem = Semaine.query.filter(Semaine.dateDebut <= date).filter(Semaine.dateFin >= date).first()
    #calcul periode
    periode = Periode.query.filter(Periode.idPeriode == sem.idPeriode).first()
    semestre="S"+str(periode.semestre)
    eleves=Eleve.query.all()
    groupes=[]
    for eleve in eleves:
        if semestre == "S1":
            groupe=eleve.groupeS1
        else:
            groupe=eleve.groupeS2
        if groupe not in groupes:
            groupes.append(groupe)
    #recup qcms
    qcms=QCM.query.filter(QCM.dateFin >= sem.dateDebut).filter(QCM.dateFin <= sem.dateFin).all()
    #recup moyennes
    moyennes={}
    for qcm in qcms:
        nom_matiere=Matiere.query.filter(Matiere.idMatiere == qcm.idMatiere).first().nomMatiere
        moyennes[nom_matiere]={}
        for groupe in groupes:
            moyennes[nom_matiere][groupe]=get_moyenne_groupe(groupe,qcm.idQCM,semestre)   
        #ajout moyenne generale
        moyennes[nom_matiere]["generale"]=get_moyenne_generale(qcm.idQCM)
    return moyennes

def get_dispo_enseignant_accueil(semaine):
    """fonction recuperant les disponibilites des enseignants pour une date

    Args:
        date (String): date du QCM
    """
    sem = Semaine.query.filter(Semaine.numSemaine == semaine).first()
    dispo = EstDisponible.query.filter(EstDisponible.oral.dateOral >= sem.dateDebut).filter(EstDisponible.oral.dateOral <= sem.dateFin).all()
    return dispo

def get_res_sondage_accueil(date):
    """fonction recuperant les resultats du sondage pour une date

    Args:
        date (String): date du QCM
    """
    sem = Semaine.query.filter(Semaine.dateDebut <= date).filter(Semaine.dateFin >= date).first()
    matieres_demandées={}
    rep_sondage = RepSondage.query.join(Sondage).filter(Sondage.dateSondage >= sem.dateDebut).filter(Sondage.dateSondage <= sem.dateFin).all()
    for r in rep_sondage:
        if r.matiereVoulu in matieres_demandées:
            matieres_demandées[r.matiereVoulu]["nb"]+=1
        else:
            matieres_demandées[r.matiereVoulu]={"nb":1,"Moyenne":None}
    for nom_m in matieres_demandées:
        mat=Matiere.query.filter(Matiere.nomMatiere==nom_m).first()
        if mat is not None:
            qcm=QCM.query.filter(QCM.idMatiere==mat.idMatiere).filter(QCM.dateFin >= sem.dateDebut).filter(QCM.dateFin <= sem.dateFin).first()
            if qcm is not None:
                moyenne=get_moyenne_generale(qcm.idQCM)
                matieres_demandées[nom_m]["Moyenne"]=moyenne
    return matieres_demandées

def get_res_QCMs(semaine,liste_groupes=[]):
    """fonction recuperant les resultats de QCM pour une date

    Args:
        date (String): date du QCM
    """
    sem = Semaine.query.filter(Semaine.idSemaine == semaine).first()
    qcms=QCM.query.filter(QCM.dateFin >= sem.dateDebut).filter(QCM.dateFin <= sem.dateFin).all()
    resultats=[]
    if len(liste_groupes)==0:
        for qcm in qcms:
            res_QCM=ResultatQCM.query.join(QCM).join(Eleve).join(Matiere).filter(ResultatQCM.idQCM==qcm.idQCM).all()
            resultats.append(res_QCM)
    else:
        semestre="S"+str(Periode.query.filter(Periode.idPeriode == sem.idPeriode).first().semestre)
        if semestre == "S1":
            for qcm in qcms:
                res_QCM=ResultatQCM.query.join(QCM).join(Eleve).join(Matiere).filter(ResultatQCM.idQCM==qcm.idQCM).filter(Eleve.groupeS1.in_(liste_groupes)).all()
                resultats.append(res_QCM)
        else:
            for qcm in qcms:
                res_QCM=ResultatQCM.query.join(QCM).join(Eleve).join(Matiere).filter(ResultatQCM.idQCM==qcm.idQCM).filter(Eleve.groupeS2.in_(liste_groupes)).all()
                resultats.append(res_QCM)
    return resultats

def get_res_sondages(semaine,liste_groupes=[]):
    """fonction recuperant les resultats de sondage pour une date

    Args:
        date (String): date du QCM
    """
    sem = Semaine.query.filter(Semaine.idSemaine == semaine).first()
    sondages=Sondage.query.filter(Sondage.dateSondage >= sem.dateDebut).filter(Sondage.dateSondage <= sem.dateFin).all()
    resultats=[]
    if len(liste_groupes)==0:
        for sondage in sondages:
            res_sondage=RepSondage.query.join(Eleve).filter(RepSondage.idSondage==sondage.idSondage).all()
            resultats.append(res_sondage)
    else:
        semestre="S"+str(Periode.query.filter(Periode.idPeriode == sem.idPeriode).first().semestre)
        if semestre == "S1":
            for sondage in sondages:
                res_sondage=RepSondage.query.join(Eleve).filter(RepSondage.idSondage==sondage.idSondage).filter(Eleve.groupeS1.in_(liste_groupes)).all()
                resultats.append(res_sondage)
        else:
            for sondage in sondages:
                res_sondage=RepSondage.query.join(Eleve).filter(RepSondage.idSondage==sondage.idSondage).filter(Eleve.groupeS2.in_(liste_groupes)).all()
                resultats.append(res_sondage)
    return resultats


def get_res_QCM_eleve(id_eleve, id_sem):
    """fonction recuperant les resultats du QCM pour un eleve et une date

    Args:
        id_eleve (int): id de l eleve
        date (String): date du QCM
    """
    sem = Semaine.query.filter(Semaine.idSemaine == id_sem).first()
    res_qcm = ResultatQCM.query.filter(ResultatQCM.qcm.dateFin >= sem.dateDebut).filter(ResultatQCM.qcm.dateFin <= sem.dateFin).filter(ResultatQCM.numEtu == id_eleve).all()
    return res_qcm

def get_res_sond_eleve(id_eleve, id_sem):
    """fonction recuperant les resultats du sondage pour un eleve et une date

    Args:
        id_eleve (int): id de l eleve
        date (String): date du QCM
    """
    sem = Semaine.query.filter(Semaine.idSemaine == id_sem).first()
    res_sond = RepSondage.query.join(Sondage).join(ReponseQuestionSondage).filter(RepSondage.numEtu == id_eleve).filter(Sondage.dateSondage >= sem.dateDebut).filter(Sondage.dateSondage <= sem.dateFin).all()
    return res_sond
def get_eleve(id_eleve):
    """fonction recuperant un eleve

    Args:
        id_eleve (int): id de l eleve
    """
    eleve = Eleve.query.filter(Eleve.numEtu == id_eleve).first()
    return eleve

def get_eleves(groupe, date):
    """fonction recuperant les eleves d un groupe pour une date

    Args:
        groupe (String): groupe de l eleve
        date (String): date du QCM
    """
    sem = Semaine.query.filter(Semaine.dateDebut <= date).filter(Semaine.dateFin >= date).first()
    #on verifie si on est en periode 1 ou 2
    if Periode.query.filter(Periode.idPeriode==sem.idPeriode).first().semestre==1:
        eleves = Eleve.query.filter(Eleve.groupeS1 == groupe).filter(Eleve.dateDebut >= sem.dateDebut).filter(Eleve.dateDebut <= sem.dateFin).all()
    eleves = Eleve.query.filter(Eleve.groupeS2 == groupe).filter(Eleve.dateFin >= sem.dateDebut).filter(Eleve.dateFin <= sem.dateFin).all()
    return eleves
    
def disponibilites_enseignant(id_enseignant, date):
    """fonction recuperant les disponibilites d un enseignant pour une date

    Args:
        id_enseignant (int): id de l enseignant
        date (String): date du QCM
    """
    sem = Semaine.query.filter(Semaine.dateDebut <= date).filter(Semaine.dateFin >= date).first()
    dispo = EstDisponible.query.join(Oral).filter(Oral.dateOral >= sem.dateDebut).filter(Oral.dateOral <= sem.dateFin).filter(EstDisponible.idProf == id_enseignant).all()
    return dispo

def gen_soutien(num_sem,seuil):
    #genere les soutiens pour la semaine donnee
    sem=Semaine.query.filter(Semaine.numSemaine==num_sem).first()
    qcms_trouve=False
    while not qcms_trouve:
        #cherche une semaine avec des qcms
        qcms=QCM.query.filter(QCM.dateFin >= sem.dateDebut).filter(QCM.dateFin <= sem.dateFin).all()
        if len(qcms)==0:
            sem=Semaine.query.filter(Semaine.numSemaine==num_sem-1).first()
            num_sem-=1
        else:
            qcms_trouve=True
    eleves_besoin=[]
    non_retenus=[]
    retenus={}
    for qcm in qcms:
        moyenne=get_moyenne_generale(qcm.idQCM)

        eleves_volontaires_besoin=ResultatQCM.join(RepSondage,ResultatQCM.numEtu==RepSondage.numEtu)
        eleves_volontaires_besoin.join(QCM,ResultatQCM.idQCM==QCM.idQCM).join(Matiere,QCM.idMatiere==Matiere.idMatiere)
        eleves_volontaires_besoin.join(Eleve,ResultatQCM.numEtu==Eleve.numEtu).filter(ResultatQCM.idQCM == qcm.idQCM)
        eleves_volontaires_besoin.filter(ResultatQCM.note < seuil*moyenne).filter(RepSondage.volontaire=='oui')
        eleves_volontaires_besoin.filter(Matiere.nomMatiere==qcm.matiere.nomMatiere).order_by(ResultatQCM.note).all()

        eleves_hesitants=ResultatQCM.join(RepSondage,ResultatQCM.numEtu==RepSondage.numEtu)
        eleves_hesitants.join(QCM,ResultatQCM.idQCM==QCM.idQCM).join(Matiere,QCM.idMatiere==Matiere.idMatiere)
        eleves_hesitants.join(Eleve,ResultatQCM.numEtu==Eleve.numEtu).filter(ResultatQCM.idQCM == qcm.idQCM)
        eleves_hesitants.filter(ResultatQCM.note < seuil*moyenne).filter(RepSondage.volontaire=='~')
        eleves_hesitants.filter(Matiere.nomMatiere==qcm.matiere.nomMatiere).order_by(ResultatQCM.note).all()
        possibles=eleves_volontaires_besoin+eleves_hesitants
        if len(eleves_volontaires_besoin+eleves_hesitants)>=3:
            retenus_mat=[]
            while len(retenus_mat)<5 or len(possibles)!=0:
                retenus_mat.append(possibles.pop(0))
            retenus[qcm.matiere.nomMatiere]=retenus_mat
        non_retenus+=possibles

        eleves_besoin+=ResultatQCM.join(RepSondage,ResultatQCM.numEtu==RepSondage.numEtu)
        eleves_besoin.join(QCM,ResultatQCM.idQCM==QCM.idQCM).join(Matiere,QCM.idMatiere==Matiere.idMatiere)
        eleves_besoin.join(Eleve,ResultatQCM.numEtu==Eleve.numEtu)
        eleves_besoin.filter(ResultatQCM.idQCM == qcm.idQCM)
        eleves_besoin.filter(ResultatQCM.note < seuil*moyenne).filter(RepSondage.volontaire=='non')
        eleves_besoin.order_by(ResultatQCM.note).all()
        
    return retenus,eleves_besoin,non_retenus

def get_profs_dispos(semaine,liste_mat=[]):
    """fonction recuperant les enseignants disponibles pour une semaine

    Args:
        semaine (int): numero de la semaine
        liste_mat (list, optional): liste des matieres. Defaults to [].
    """
    sem=Semaine.query.filter(Semaine.numSemaine==semaine).first()
    dispo=EstDisponible.query.join(Oral).filter(Oral.dateOral >= sem.dateDebut).filter(Oral.dateOral <= sem.dateFin).all()
    profs_dispos={}
    for d in dispo:
        prof=Professeur.query.filter(Professeur.idProf==d.idProf).first()
        mats=PossibiliteSoutien.query.join(Matiere).filter(PossibiliteSoutien.idProf==prof.idProf).all()
        if prof not in profs_dispos:
            profs_dispos[prof.nomProf+" "+prof.prenomProf]=[]
        for mat in mats:
            if mat.matiere.nomMatiere in liste_mat:
                profs_dispos[prof.nomProf+" "+prof.prenomProf].append(mat.matiere.nomMatiere)
    return profs_dispos

def get_suivi_etu(num_etu):
    suivi={"nbPart":0,"moyGen":0}
    oraux=ParticipantsOral.query.filter(ParticipantsOral.numEtu==num_etu).all()
    suivi["nbPart"]=len(oraux)
    qcms=ResultatQCM.query.filter(ResultatQCM.numEtu==num_etu).all()
    if len(qcms)!=0:
        for qcm in qcms:
            suivi["moyGen"]+=qcm.note
        suivi["moyGen"]/=len(qcms)
    return suivi

def get_suivi_etu_gen(liste_groupes=[]):
    suivi_etu={}
    if len(liste_groupes)==0:
        eleves=Eleve.query.all()
        for eleve in eleves:
            suivi_etu[eleve.nom+" "+eleve.prenom]=get_suivi_etu(eleve.numEtu)
    else:
        for groupe in liste_groupes:
            eleves=Eleve.query.filter(Eleve.groupe==groupe).all()
            for eleve in eleves:
                suivi_etu[eleve.nom+" "+eleve.prenom]=get_suivi_etu(eleve.numEtu)
    return suivi_etu

def ajouter_eleve_oral(nom_etu,prenom_etu,id_oral):
    etu=Eleve.query.filter(Eleve.nom==nom_etu).filter(Eleve.prenom==prenom_etu).first()
    oral = Oral.query.filter(Oral.idOral==id_oral).first()
    part=ParticipantsOral.query.filter(ParticipantsOral.idOral==oral.idOral).filter(ParticipantsOral.numEtu==etu.numEtu).first()
    if part is None:
        part=ParticipantsOral(idOral=oral.idOral,numEtu=etu.numEtu)
        db.session.add(part)
        db.session.commit()
    
def ajouter_commentaire(idOral,numEtu,commentaire):
    oral=Oral.query.filter(Oral.idOral==idOral).first()
    etu=Eleve.query.filter(Eleve.numEtu==numEtu).first()
    part=ParticipantsOral.query.filter(ParticipantsOral.idOral==oral.idOral).filter(ParticipantsOral.numEtu==etu.numEtu).first()
    part.commentaire=commentaire
    db.session.commit()

def ajouter_dispo(idOral,idProf):
    oral=Oral.query.filter(Oral.idOral==idOral).first()
    prof=Professeur.query.filter(Professeur.idProf==idProf).first()
    dispo=EstDisponible.query.filter(EstDisponible.idOral==oral.idOral).filter(EstDisponible.idProf==prof.idProf).first()
    if dispo is None:
        dispo=EstDisponible(idOral=oral.idOral,idProf=prof.idProf)
        db.session.add(dispo)
        db.session.commit()

def ajouter_possibilite_soutien(id_periode,id_prof,nom_mat):
    periode=Periode.query.filter(Periode.idPeriode==id_periode).first()
    prof=Professeur.query.filter(Professeur.idProf==id_prof).first()
    matiere=Matiere.query.filter(Matiere.nomMatiere==nom_mat).first()
    possibilite=PossibiliteSoutien.query.filter(PossibiliteSoutien.idPeriode==periode.idPeriode).filter(PossibiliteSoutien.idProf==prof.idProf).filter(PossibiliteSoutien.idMatiere==matiere.idMatiere).first()
    if possibilite is None:
        possibilite=PossibiliteSoutien(idPeriode=periode.idPeriode,idProf=prof.idProf,idMatiere=matiere.idMatiere)
        db.session.add(possibilite)
        db.session.commit()

def creer_oral(heure,date):
    if Oral.query.filter(Oral.heureOral==heure).filter(Oral.dateOral==date).first() is None:
        soutien=Oral(heureOral=heure,dateOral=date)
        db.session.add(soutien)
        db.session.commit()

def creer_periode(date_debut,date_fin,id):
    if Periode.query.filter(Periode.idPeriode==id).first() is None:
        if id == 1 or id == 2:
            semestre=1
        else:
            semestre=2
        periode=Periode(idPeriode=id,dateDebut=date_debut,dateFin=date_fin,semestre=semestre)
        db.session.add(periode)
        db.session.commit()

def suppr_possibilité_soutien(id_periode,id_prof,nom_mat):
    periode=Periode.query.filter(Periode.idPeriode==id_periode).first()
    prof=Professeur.query.filter(Professeur.idProf==id_prof).first()
    matiere=Matiere.query.filter(Matiere.nomMatiere==nom_mat).first()
    possibilite=PossibiliteSoutien.query.filter(PossibiliteSoutien.idPeriode==periode.idPeriode).filter(PossibiliteSoutien.idProf==prof.idProf).filter(PossibiliteSoutien.idMatiere==matiere.idMatiere).first()
    if possibilite is not None:
        db.session.delete(possibilite)
        db.session.commit()

def suppression_oral(date,heure):
    oral=Oral.query.filter(Oral.dateOral==date).filter(Oral.heureOral==heure).first()
    if oral is not None:
        db.session.delete(oral)
        db.session.commit()


@login_manager.user_loader
def load_user(username):
    return User.query.get(username)
