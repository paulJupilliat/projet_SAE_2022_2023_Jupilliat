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
    nbEls = db.Column(db.Integer)
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

class Semaine(db.Model):
    __tablename__ = "semaine"
    idSemaine = db.Column(db.Integer, primary_key=True)
    dateDebut = db.Column(db.String(500))
    dateFin = db.Column(db.String(500))
    def __repr__(self):
        return f"Semaine({self.idSemaine}, {self.dateDebut}, {self.dateFin})"

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
    dateSondage = db.Column(db.String(500))
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
    def __repr__(self):
        return f"Periode({self.idPeriode}, {self.dateDebut}, {self.dateFin})"

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
    qcm = QCM.query.filter(QCM.idQCM == id_qcm).first()
    qcm_eleves = ResultatQCM.query.filter(ResultatQCM.idQCM == id_qcm).all()
    moyenne = 0
    for qcm_eleve in qcm_eleves:
        moyenne += qcm_eleve.note
    moyenne = moyenne / len(qcm_eleves)
    return moyenne

def get_recap_etudiant(id_etu,num_semaine):
    #recupere les qcms et le soutien eventuel de l etudiant pour la semaine donnée
    sem=Semaine.query.filter(Semaine.numSemaine==num_semaine).first()
    qcms = QCM.query.filter(QCM.numEtu == id_etu).filter(QCM.dateFin >= sem.dateDebut).filter(QCM.dateFin <= sem.dateFin).all()
    soutien = Oral.query.filter(Oral.numEtu == id_etu).filter(Oral.dateOral >= sem.dateDebut).filter(Oral.dateOral <= sem.dateFin).all()
    return qcms,soutien

def get_soutiens_etudiant(id_etu):
    #recupere les soutiens de l etudiant
    soutiens = Oral.query.filter(Oral.numEtu == id_etu).all()
    return soutiens

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
    

    str_js+="\tvar options = {\n"
    str_js+="\tchart: {title: 'Ecart par rapport à la moyenne générale'},\n"
    str_js+="\twidth: 900,\n"
    str_js+="\theight: 500\n};\n"
    str_js+="\tvar chart = new google.charts.Line(document.getElementById('linechart_material'));\n"
    str_js+="\tchart.draw(data, google.charts.Line.convertOptions(options));\n"
    str_js+="}\n"
    
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

def ajouter_eleve_oral(nom_etu,prenom_etu,nom_mat,nom_prof,date_sout,heure_sout):
    etu=Eleve.query.filter(Eleve.nom==nom_etu).filter(Eleve.prenom==prenom_etu).first()
    matiere=Matiere.query.filter(Matiere.nomMatiere==nom_mat).first()
    prof=Professeur.query.filter(Professeur.nom==nom_prof).first()
    oral=Oral.query.filter(Oral.idMatiere==matiere.idMatiere).filter(Oral.idProf==prof.idProf).first()
    if oral is None:
        oral=Oral(idMatiere=matiere.idMatiere,idProf=prof.idProf,dateSout=date_sout,heureSout=heure_sout)
        db.session.add(oral)
        db.session.commit()
    if etu not in oral.eleves:
        oral.eleves.append(etu)
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
        
@login_manager.user_loader
def load_user(username):
    return User.query.get(username)