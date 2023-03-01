## Models permet de definir les données de l app


import datetime
from .app import db
from flask_login import UserMixin
from .app import login_manager
from .commands import lecture_parametre_def
from sqlalchemy import func

class Eleve(db.Model):
    """classe Eleve
    """
    __tablename__ = "eleve"
    num_etu = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50))
    prenom = db.Column(db.String(50))
    groupe_s1 = db.Column(db.String(50))
    groupe_s2 = db.Column(db.String(50))
    def __repr__(self):
        """representation de l objet Eleve"""
        return f"Eleve({self.nom}, {self.prenom}, {self.groupe_s1}, {self.groupe_s2})"
class Sondage(db.Model):
    """classe Sondage qui contient les sondages
    """
    __tablename__ = "sondage"
    id_sond = db.Column(db.Integer, primary_key=True)
    url_sond = db.Column(db.String(500))
    date_sond = db.Column(db.String(500))
    def __repr__(self):
        """representation de l objet Sondage"""
        return f"Sondage({self.id_sond}, {self.url_sond})"
class QuestionSondage(db.Model):
    """classe QuestionSondage qui contient 
    les questions speciales facultatives"""
    __tablename__ = "questionsondage"
    id_sond = db.Column(db.Integer, db.ForeignKey("sondage.id_sond"))
    id_quest = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(500))
    #relation pour avoir le sondage d une question
    sondage = db.relationship(Sondage, backref=db.backref("fk_questionsondage", lazy="dynamic"))
    def __repr__(self):
        """representation de l objet QuestionSondage"""
        return f"QuestionSondage({self.id_sond}, {self.id_quest}, {self.question})"
class Matiere(db.Model):
    """classe Matiere qui contient les matieres
    """
    __tablename__ = "matiere"
    id_matiere = db.Column(db.Integer, primary_key=True)
    nom_matiere = db.Column(db.String(50))
    def __repr__(self):
        """representation de l objet Matiere"""
        return f"Matiere({self.id_matiere}, {self.nom_matiere})"
class QCM(db.Model):
    """classe QCM qui contient les qcm
    """
    __tablename__ = "qcm"
    id_qcm = db.Column(db.Integer, primary_key=True)
    nom_qcm = db.Column(db.String(50))
    url_qcm = db.Column(db.String(500))
    #relation pour avoir la matiere d un qcm
    id_matiere = db.Column(db.Integer, db.ForeignKey("matiere.id_matiere"))
    #relation inverse pour avoir les qcm d une matiere
    matiere = db.relationship(Matiere, backref=db.backref("fk_matiere_qcm", lazy="dynamic"))
    date_debut = db.Column(db.String(500))
    date_fin = db.Column(db.String(500))
    def __repr__(self):
        """representation de l objet QCM"""
        return f"QCM({self.id_qcm}, {self.nom_qcm}, {self.url_qcm}, {self.date_debut}, {self.date_fin})"

class Professeur(db.Model):
    """classe Professeur qui contient les professeurs
    """
    __tablename__ = "professeur"
    id_prof = db.Column(db.String(50), primary_key=True)
    nom_prof = db.Column(db.String(50))
    prenom_prof = db.Column(db.String(50))
    email_prof = db.Column(db.String(500))
    def __repr__(self):
        """representation de l objet Professeur"""
        return f"Professeur({self.id_prof}, {self.nom_prof}, {self.prenom_prof}, {self.email_prof})"
class User(db.Model, UserMixin):
    """classe User qui contient les utilisateurs
    attribut est_admin pour savoir si l utilisateur est admin ou non (T ou F)
    """
    __tablename__ = "user"
    username = db.Column(db.String(50), primary_key=True)
    password = db.Column(db.String(64))
    est_admin = db.Column(db.String(1))
    def get_id(self):
        return self.username
    def get_est_admin(self):
        return self.est_admin=="T"
    def __repr__(self):
        """representation de l objet User"""
        return f"User({self.username}, {self.password}, {self.est_admin()})"

class Oral(db.Model):
    """classe Oral qui contient les oraux(soutien)
    """
    __tablename__ = "oral"
    id_oral = db.Column(db.Integer, primary_key=True)
    date_oral = db.Column(db.String(500))
    heure_oral = db.Column(db.String(500))
    #relation pour avoir la matiere d un oral
    id_matiere = db.Column(db.Integer, db.ForeignKey("matiere.id_matiere"))
    #relation inverse pour avoir les oraux d une matiere
    matiere = db.relationship(Matiere, backref=db.backref("fk_matiere_oral", lazy="dynamic"))
    #relation pour avoir le professeur d un oral
    id_prof = db.Column(db.String(50), db.ForeignKey("professeur.id_prof"))
    #relation inverse pour avoir les oraux d un professeur
    professeur = db.relationship(Professeur, backref=db.backref("fk_professeur_oral", lazy="dynamic"))
    def __repr__(self):
        """representation de l objet Oral"""
        return f"Oral({self.id_oral}, {self.date_oral}, {self.heure_oral})"

class ParticipantsOral(db.Model):
    """classe ParticipantsOral qui fait la 
    relation entre les oraux et les eleves"""
    __tablename__ = "participantsoral"
    id_oral = db.Column(db.Integer, db.ForeignKey("oral.id_oral"), primary_key=True)
    num_etu = db.Column(db.Integer, db.ForeignKey("eleve.num_etu"), primary_key=True)
    commentaire = db.Column(db.String(800))
    #relation pour avoir l oral d un participant
    oral= db.relationship(Oral, backref=db.backref("fk_participantOral_oral", cascade="all, delete-orphan"),overlaps="oral,eleve")
    #relation pour avoir l eleve d un participant
    eleve= db.relationship(Eleve, backref=db.backref("fk_participantOral_eleve", cascade="all, delete-orphan"),overlaps="oral,eleve")
    def __repr__(self):
        """representation de l objet ParticipantsOral"""
        return f"ParticipantsOral({self.id_oral}, {self.num_etu}, {self.commentaire})"
class ResultatQCM(db.Model):
    """classe ResultatQCM qui fait la
    relation entre les qcm et les eleves -> note"""
    __tablename__ = "resultatqcm"
    id_qcm = db.Column(db.Integer, db.ForeignKey("qcm.id_qcm"), primary_key=True)
    num_etu = db.Column(db.Integer, db.ForeignKey("eleve.num_etu"), primary_key=True)
    note = db.Column(db.Integer)
    #un eleve peut avoir qu'une seule note pour un qcm
    eleve = db.relationship(Eleve, backref=db.backref("fk_resqcm_eleve", cascade="all, delete-orphan"),overlaps="qcm,eleve")
    #un qcm peut avoir qu'une seule note pour un eleve
    qcm = db.relationship(QCM, backref=db.backref("fk_resqcm_qcm", cascade="all, delete-orphan"),overlaps="qcm,eleve")
    def __repr__(self):
        """representation de l objet ResultatQCM"""
        return f"ResultatQCM({self.id_qcm}, {self.num_etu}, {self.note})"

class RepSondage(db.Model):
    """classe RepSondage qui fait la
    relation entre les sondages et les eleves -> reponses"""
    __tablename__ = "repsondage"
    id_sondage = db.Column(db.Integer, db.ForeignKey("sondage.id_sond"), primary_key=True)
    num_etu = db.Column(db.Integer, db.ForeignKey("eleve.num_etu"), primary_key=True)
    matiere_voulue = db.Column(db.String(100))
    volontaire = db.Column(db.String(50))
    commentaire = db.Column(db.String(800))
    #relation pour avoir le sondage d une reponse
    sondage = db.relationship(Sondage, backref=db.backref("fk_repsond_sondage", cascade="all, delete-orphan"),overlaps="sondage,eleve")
    #relation pour avoir l eleve d une reponse
    eleve = db.relationship(Eleve, backref=db.backref("fk_repsond_eleve", cascade="all, delete-orphan"),overlaps="sondage,eleve")
    def __repr__(self):
        """representation de l objet RepSondage"""
        return f"RepSondage({self.volontaire}, {self.id_sondage}, {self.num_etu}, {self.matiere_voulue}, {self.commentaire})"
class Periode(db.Model):
    """classe Periode qui contient les periodes
    assignées a leur semestres avec des dates limites"""
    __tablename__ = "periode"
    id_periode = db.Column(db.Integer, primary_key=True)
    date_debut = db.Column(db.String(500))
    date_fin = db.Column(db.String(500))
    semestre = db.Column(db.Integer)
    def __repr__(self):
        """representation de l objet Periode """
        return f"Periode({self.id_periode}, {self.date_debut}, {self.date_fin})"
class Semaine(db.Model):
    """classe Semaine qui contient les semaines 
    avec une periode associée"""
    __tablename__ = "semaine"
    id_semaine = db.Column(db.Integer, primary_key=True)
    date_debut = db.Column(db.String(500))
    date_fin = db.Column(db.String(500))
    #ajout de la periode pour faciliter la recherche
    id_periode = db.Column(db.Integer, db.ForeignKey("periode.id_periode"))
    periode = db.relationship(Periode, backref=db.backref("fk_semaine_Periode", lazy="dynamic"))
    def __repr__(self):
        """representation de l objet Semaine"""
        return f"Semaine({self.id_semaine}, {self.date_debut}, {self.date_fin})"

class PossibiliteSoutien(db.Model):
    """classe PossibiliteSoutien qui fait la
    relation entre les professeurs et les matieres et les periodes"""
    __tablename__ = "possibilitesoutien"
    id_prof = db.Column(db.String(50), db.ForeignKey("professeur.id_prof"), primary_key=True)
    id_matiere = db.Column(db.Integer, db.ForeignKey("matiere.id_matiere"), primary_key=True)
    id_periode = db.Column(db.Integer, db.ForeignKey("periode.id_periode"), primary_key=True)
    #relation pour avoir le professeur d une possibilite de soutien
    professeur = db.relationship(Professeur, backref=db.backref("fk_idprofesseur_professeur", cascade="all, delete-orphan"),overlaps="professeur,matiere,periode")
    #relation pour avoir la matiere d une possibilite de soutien
    matiere = db.relationship(Matiere, backref=db.backref("fk_idmatiere_matiere", cascade="all, delete-orphan"),overlaps="professeur,matiere,periode")
    #relation pour avoir la periode d une possibilite de soutien
    periode = db.relationship(Periode, backref=db.backref("fk_idperiode_periode", cascade="all, delete-orphan"),overlaps="professeur,matiere,periode")
    def __repr__(self):
        """representation de l objet PossibiliteSoutien"""
        return f"PossibiliteSoutien({self.id_prof}, {self.id_matiere}, {self.id_periode})"
class EstDisponible(db.Model):
    """classe EstDisponible qui fait la
    relation entre les professeurs et les oraux(inscriptions)"""
    __tablename__ = "estdisponible"
    id_prof = db.Column(db.String(50), db.ForeignKey("professeur.id_prof"), primary_key=True)
    id_oral = db.Column(db.Integer, db.ForeignKey("oral.id_oral"), primary_key=True)
    #relation pour avoir le professeur d une disponibilite
    professeur = db.relationship(Professeur, backref=db.backref("fk_estdisponible_professeur", cascade="all, delete-orphan"),overlaps="professeur,oral")
    #relation pour avoir l oral d une disponibilite
    oral = db.relationship(Oral, backref=db.backref("fk_estdisponible_oral", cascade="all, delete-orphan"),overlaps="professeur,oral")
    def __repr__(self):
        """representation de l objet EstDisponible"""
        return f"EstDisponible({self.id_prof}, {self.id_oral})"

class ReponseQuestionSondage(db.Model):
    """classe ReponseQuestionSondage qui fait la
    relation entre les eleves et les questions facultatives et les reponses"""
    __tablename__ = "reponsequestionsondage"
    num_etu = db.Column(db.Integer, db.ForeignKey(Eleve.num_etu), primary_key=True)
    id_quest = db.Column(db.Integer, db.ForeignKey(QuestionSondage.id_quest), primary_key=True)
    reponse = db.Column(db.String(500))
    #relation pour avoir l eleve d une reponse a une question
    eleve = db.relationship(Eleve, backref=db.backref("fk_ReponseQuestionSondage_eleve", cascade="all, delete-orphan"),overlaps="eleve,questionSondage")
    #relation pour avoir la question d une reponse a une question
    question = db.relationship(QuestionSondage, backref=db.backref("fk_ReponseQuestionSondage_questionSondage", cascade="all, delete-orphan"),overlaps="eleve,questionSondage")
    def __repr__(self):
        """representation de l objet ReponseQuestionSondage"""
        return f"ReponseQuestionSondage({self.num_etu}, {self.id_quest}, {self.reponse})"

def get_moyenne_generale(id_qcm: int)->float:
    """fonction qui recupere la moyenne de la promo pour un qcm
    Args:
        id_qcm: l id du qcm dont on veut la moyenne
    Return:
        moyenne: la moyenne de la promo pour le qcm"""
    qcm_eleves = ResultatQCM.query.filter(ResultatQCM.id_qcm == id_qcm).all()
    moyenne = 0
    for qcm_eleve in qcm_eleves:
        moyenne += qcm_eleve.note
    moyenne = moyenne / len(qcm_eleves)
    return moyenne

def get_recap_etudiant(id_etu:int,num_semaine:int)->tuple:
    """fonction qui recupere les qcms et les soutiens de l etudiant
    pour une semaine donnee
    Args:
        id_etu: l id de l etudiant
        num_semaine: le numero de la semaine
    Return:
        qcms: les qcms de l etudiant
        soutien: les soutiens de l etudiant"""
    sem=Semaine.query.filter(Semaine.numSemaine==num_semaine).first().id_semaine
    qcms=get_res_QCM_eleve(id_etu,sem)
    soutien=get_soutiens_etudiant(id_etu,sem)
    sondage=get_sondage_etudiant(id_etu,sem)
    return qcms,soutien,sondage

def get_res_QCM_eleve(id_etu:int,id_semaine:int)->list:
    """fonction qui recupere les qcms de l etudiant
    Args:
        id_etu: l id de l etudiant
        id_semaine: l id de la semaine
    Return:
        qcms: les qcms de l etudiant"""
    ids_qcms = ResultatQCM.query.filter(ResultatQCM.num_etu == id_etu).filter(ResultatQCM.id_semaine==id_semaine).all()
    qcms = []
    for id_qcm in ids_qcms:
        qcm=QCM.query.join(ResultatQCM).filter(QCM.id_qcm == id_qcm.id_qcm).first()
        qcms.append(qcm)
    return qcms

def get_sondage_etudiant(id_etu:int,id_semaine:int)->list:
    """fonction qui recupere les sondages de l etudiant
    Args:
        id_etu: l id de l etudiant
        id_semaine: l id de la semaine
    Return:
        sondage: les reponses au sondage de l etudiant"""
    sem=Semaine.query.filter(Semaine.id_semaine==id_semaine).first()
    sondage_sem=Sondage.query.filter(Sondage.date_sond >= sem.date_debut).filter(Sondage.date_sond <= sem.date_fin).first()
    question_sondage=QuestionSondage.query.filter(QuestionSondage.id_sondage==sondage_sem.id_sondage).all()
    reponse=RepSondage.query.filter(RepSondage.id_quest==sondage_sem.id_sondage).filter(RepSondage.num_etu==id_etu).first()
    if question_sondage is not None:
        reponse_quest=ReponseQuestionSondage.query.join(QuestionSondage).filter(ReponseQuestionSondage.id_quest==question_sondage.id_quest).filter(ReponseQuestionSondage.num_etu==id_etu).first()
    else:
        reponse_quest=None
    return reponse,reponse_quest

def get_soutiens_etudiant(id_etu:int)->list:
    """fonction qui recupere les soutiens de l etudiant
    Args:
        id_etu: l id de l etudiant
    Return:
        oraux: les soutiens de l etudiant"""
    ids_oraux = ParticipantsOral.query.filter(ParticipantsOral.num_etu == id_etu).all()
    oraux = []
    for id_oral in ids_oraux:
        oral=Oral.query.join(ParticipantsOral).join(Matiere).filter(Oral.id_oral == id_oral.id_oral).first()
        semaine=Semaine.query.filter(Semaine.date_debut <= oral.date).filter(Semaine.date_fin >= oral.date).first().id_semaine
        oraux.append((oral,semaine))
    return oraux

def get_graphe_etudiant(id_etu:int,date_deb:str,date_fin:str,liste_mat:list):
    """fonction qui recupere les donnees pour le graphe de l etudiant*
    Args:
        id_etu: l id de l etudiant
        date_deb: la date de debut du seuil
        date_fin: la date de fin du seuil
        liste_mat: la liste des matieres
    Return:
        str_js: le code javascript pour le graphe"""
    str_js="google.charts.load('current', {'packages':['line']});\n"
    str_js+="google.charts.setOnLoadCallback(drawChart);\n"
    str_js+="function drawChart() {\n"
    str_js+="\tvar data = new google.visualization.DataTable();\n"
    str_js+="\tdata.addColumn('number', 'Semaine');\n"
    for matiere in liste_mat:
        str_js+="\tdata.addColumn('number', '"+matiere+"');\n"
    semaines = Semaine.query.filter(Semaine.date_debut >= date_deb).filter(Semaine.date_fin <= date_fin).all()
    for sem in semaines:
        liste_sem=[sem.numSemaine]
        for mat in liste_mat:
            #recupere la note si elle existe pour la semaine et la matiere
            idmat=Matiere.query.filter(Matiere.nom_matiere==mat).first().id_matiere
            qcm=QCM.query.filter(QCM.num_etu == id_etu).filter(QCM.id_matiere == idmat).filter(QCM.date_fin >= sem.date_debut).filter(QCM.date_fin <= sem.date_fin).first()
            if note is None:
                liste_sem.append(0)
            else:
                #recupere la moyenne generale
                moyenne=get_moyenne_generale(qcm.id_qcm)
                #recupere la note de l etudiant
                note=ResultatQCM.query.filter(ResultatQCM.id_qcm == qcm.id_qcm).filter(ResultatQCM.num_etu == id_etu).first().note
                #calcule l ecart
                ecart=note-moyenne
                liste_sem.append(ecart)
        str_js+="\tdata.addRow("+liste_sem+");\n"
    str_js+= "var options = {\n"
    str_js+=" chart: {\n"
    str_js+=" title: 'Ecart par rapport à la moyenne de la promo',\n"
    str_js+=" subtitle: 'en nombre'\n"
    str_js+=" },\n"
    str_js+=" width: 900,\n"
    str_js+=" height: 500\n"
    str_js+=" };\n"
    str_js+=" var chart = new google.charts.Line(document.getElementById('linechart_material'));\n"
    str_js+=" chart.draw(data, google.charts.Line.convertOptions(options));\n"
    str_js+=" }"
    return str_js

def get_matieres_etu(id_etu):
    """fonction qui recupere les matieres d un etudiant
    Args:
        id_etu: l id de l etudiant
    Return:
        liste_matieres: la liste des matieres"""
    liste_qcms=QCM.query.filter(QCM.num_etu == id_etu).all()
    return Matiere.query.filter(Matiere.id_matiere.in_(liste_qcms)).all()

def get_moyenne_groupe(groupe:str,id_qcm:int)->float:
    """fonction qui recupere la moyenne d un groupe pour un qcm
    Args:
        groupe: le groupe
        id_qcm: l id du qcm
    Return:
        moyenne: la moyenne du groupe"""
    qcm_eleves = ResultatQCM.query.filter(ResultatQCM.id_qcm == id_qcm).all()
    dateqcm = QCM.query.filter(QCM.id_qcm == id_qcm).first().date_fin
    periode = Periode.query.filter(Periode.date_debut <= dateqcm).filter(Periode.date_fin >= dateqcm).first()
    semestre = periode.semestre
    moyenne = 0
    for qcm_eleve in qcm_eleves:
        eleve=Eleve.query.filter(Eleve.num_etu == qcm_eleve.num_etu).first()
        if semestre == 1:
            if eleve.groupe_s1 == groupe:
                moyenne += qcm_eleve.note
        else:
            if eleve.groupe_s2 == groupe:
                moyenne += qcm_eleve.note
    moyenne = moyenne / len(qcm_eleves)
    return moyenne

def get_resultats_qcm_accueil()->dict:
    """fonction recuperant les resultats de QCM pour une date en renvoyant les moyennes par groupe et par matiere

    Args:
        date (String): date du QCM

    Returns:
        dict: dictionnaire contenant les moyennes par matiere et par groupe
    """
    #on regarde dans quelle semaine on est
    sem = get_semaine_act()
    #calcul periode
    periode = Periode.query.filter(Periode.id_periode == 1).first()
    semestre="S"+str(periode.semestre)
    eleves=Eleve.query.all()
    groupes=[]
    for eleve in eleves:
        if semestre == "S1":
            groupe=eleve.groupe_s1
        else:
            groupe=eleve.groupe_s2
        if groupe not in groupes:
            groupes.append(groupe)
    #recup qcms
    qcms=QCM.query.filter(QCM.date_fin >= '2023/02/27').filter(QCM.date_fin <= '2023/03/05').all()
    #recup moyennes
    moyennes={}
    for qcm in qcms:
        moyennes[groupe]={}
        nom_matiere=Matiere.query.filter(Matiere.id_matiere == qcm.id_matiere).first().nom_matiere
        for groupe in groupes:
            moyennes[groupe][nom_matiere]=get_moyenne_groupe(groupe,qcm.id_qcm)   
        #ajout moyenne generale
        moyennes["generale"]={}
        moyennes["generale"][nom_matiere]=get_moyenne_generale(qcm.id_qcm)
    return moyennes

def get_dispo_enseignant_accueil(semaine:int):
    """fonction recuperant les disponibilites des enseignants pour une date

    Args:
        date (String): date du QCM

    Returns:
        list: liste des disponibilites
    """
    # select nom_prof from Enseignant natural join EstDisponible natural join Oral where date_oral = semaine
    sem = get_semaine_act()
    profs_dispo = EstDisponible.query.join(Professeur).filter(EstDisponible.oral.date_oral >= sem.date_debut).filter(EstDisponible.oral.date_oral <= sem.date_fin).all()
     
    #recup des matieres par prof
    possibles={}
    matieres_tot=[]
    for p in profs_dispo:
        possibles[p]=[]
        matieres_prof=PossibiliteSoutien.query.join(Matiere).filter(PossibiliteSoutien.id_prof == p).all()
        for m in matieres_prof:
            possibles[p].append(m.nom_matiere)
            if m.nom_matiere not in matieres_tot:
                matieres_tot.append(m.nom_matiere)
    return possibles,matieres_tot

def get_res_sondage_accueil(date:str)->dict:
    """fonction recuperant les resultats du sondage pour une date

    Args:
        date (String): date du QCM
    Returns:
        dict: dictionnaire contenant les resultats du sondage
        pour l acceuil
    """
    sem = Semaine.query.filter(Semaine.date_debut <= date).filter(Semaine.date_fin >= date).first()
    matieres_demandées={}
    rep_sondage = RepSondage.query.join(Sondage).filter(Sondage.date_sond >= sem.date_debut).filter(Sondage.date_sond <= sem.date_fin).all()
    for r in rep_sondage:
        if r.matiere_voulue in matieres_demandées:
            matieres_demandées[r.matiere_voulue]["nb"]+=1
        else:
            matieres_demandées[r.matiere_voulue]={"nb":1,"Moyenne":None}
    for nom_m in matieres_demandées:
        mat=Matiere.query.filter(Matiere.nom_matiere==nom_m).first()
        if mat is not None:
            qcm=QCM.query.filter(QCM.id_matiere==mat.id_matiere).filter(QCM.date_fin >= sem.date_debut).filter(QCM.date_fin <= sem.date_fin).first()
            if qcm is not None:
                moyenne=get_moyenne_generale(qcm.id_qcm)
                matieres_demandées[nom_m]["Moyenne"]=moyenne
    return matieres_demandées

def get_res_QCMs(semaine:int,liste_groupes=[])->list:
    """fonction recuperant les resultats de QCM pour une date

    Args:
        date (String): date du QCM
    Returns:
        list: liste des resultats de QCM
    """
    sem = Semaine.query.filter(Semaine.id_semaine == semaine).first()
    semestre="S"+str(Periode.query.filter(Periode.id_periode == sem.id_periode).first().semestre)
    qcms=QCM.query.join(Matiere).filter(QCM.date_fin >= sem.date_debut).filter(QCM.date_fin <= sem.date_fin).all().order_by(Matiere.nom_matiere)
    resultats=[]
    if len(liste_groupes)==0:
        #recup les eleves qui ont fait le QCM
        eleves=Eleve.query.join(ResultatQCM).join(QCM).filter(QCM.date_fin >= sem.date_debut).filter(QCM.date_fin <= sem.date_fin).all()
        for eleve in eleves:
            el=Eleve.query.filter(Eleve.num_etu == eleve.num_etu).first()
            rep=[]
            res_eleve=[el]
            if semestre == "S1":
                res_eleve.append(el.groupe_s1)
            else:
                res_eleve.append(el.groupe_s2)
            res_eleve.append(rep)
            for qcm in qcms:
                res_QCM=ResultatQCM.query.join(QCM).join(Eleve).filter(ResultatQCM.id_qcm==qcm.id_qcm).filter(Eleve.num_etu==el.num_etu).first()
                res_eleve[2].append(res_QCM.note)
            rep_sond=RepSondage.query.join(Sondage).filter(RepSondage.num_etu==el.num_etu).filter(Sondage.date_sond >= sem.date_debut).filter(Sondage.date_sond <= sem.date_fin).first()
            res_eleve.append(rep_sond)
            resultats.append(res_eleve)
    else:
        if semestre == "S1":
            eleves=Eleve.query.join(ResultatQCM).join(QCM).filter(QCM.date_fin >= sem.date_debut).filter(QCM.date_fin <= sem.date_fin).filter(Eleve.groupe_s1.in_(liste_groupes)).all()
            for eleve in eleves:
                el=Eleve.query.filter(Eleve.num_etu == eleve.num_etu).first()
                rep=[]
                res_eleve=[el,el.groupe_s1,rep]
                for qcm in qcms:
                    res_QCM=ResultatQCM.query.join(QCM).join(Eleve).filter(ResultatQCM.id_qcm==qcm.id_qcm).filter(Eleve.num_etu==el.num_etu).first()
                    res_eleve[2].append(res_QCM.note)
                rep_sond=RepSondage.query.join(Sondage).filter(RepSondage.num_etu==el.num_etu).filter(Sondage.date_sond >= sem.date_debut).filter(Sondage.date_sond <= sem.date_fin).first()
                res_eleve.append(rep_sond)
                resultats.append(res_eleve)
        else:
            eleves=Eleve.query.join(ResultatQCM).join(QCM).filter(QCM.date_fin >= sem.date_debut).filter(QCM.date_fin <= sem.date_fin).filter(Eleve.groupe_s2.in_(liste_groupes)).all()
            for eleve in eleves:
                rep=[]
                el=Eleve.query.filter(Eleve.num_etu == eleve.num_etu).first()
                res_eleve=[el,el.groupe_s2,rep]
          
                rep_sond=RepSondage.query.join(Sondage).filter(RepSondage.num_etu==el.num_etu).filter(Sondage.date_sond >= sem.date_debut).filter(Sondage.date_sond <= sem.date_fin).first()
                res_eleve.append(rep_sond)
                resultats.append(res_eleve)
    return resultats

def get_moyennes_res_QCMs(semaine:int,id:str)->dict:
    """fonction recuperant les resultats de QCM pour une date
    en fonction de l id de groupe
    Args:
        date (String): date du QCM
    Returns:
        dict: dico des resultats de QCM
    """
    sem = Semaine.query.filter(Semaine.id_semaine == semaine).first()
    qcms=QCM.query.join(Matiere).filter(QCM.date_fin >= sem.date_debut).filter(QCM.date_fin <= sem.date_fin).all().order_by(Matiere.nom_matiere)
    resultats={}
    if id=="generale":
        for qcm in qcms:
            res_QCM=get_moyenne_generale(qcm.id_qcm)
            resultats[qcm.nom_matiere]=res_QCM
    else:
        for qcm in qcms:
            res_QCM=get_moyenne_groupe(id,qcm.id_qcm)
            resultats[qcm.nom_matiere]=res_QCM
    return resultats
        
def get_semaines()->list:
    """fonction recuperant les semaines

    Returns:
        list: liste des semaines
    """
    semaines=Semaine.query.join(Periode).all()
    return semaines

def get_groupes(semestre:int)->list:
    """fonction recuperant les groupes

    Returns:
        list: liste des groupes
    """
    if semestre == 1:
        eleves=Eleve.query.filter(Eleve.groupe_s1 != None).all()
        groupes=[]
        for e in eleves:
            if e.groupe_s1 not in groupes:
                groupes.append(e.groupe_s1)
    else:
        eleves=Eleve.query.filter(Eleve.groupe_s2 != None).all()
        groupes=[]
        for e in eleves:
            if e.groupe_s2 not in groupes:
                groupes.append(e.groupe_s2)
    return groupes
def get_res_sondages(semaine:int,liste_groupes=[])->list:
    """fonction recuperant les resultats de sondage pour une date

    Args:
        date (String): date du QCM
    Returns:
        list: liste des resultats de sondage
    """
    sem = Semaine.query.filter(Semaine.id_semaine == semaine).first()
    semestre="S"+str(Periode.query.filter(Periode.id_periode == sem.id_periode).first().semestre)      
    sondages=Sondage.query.filter(Sondage.date_sond >= sem.date_debut).filter(Sondage.date_sond <= sem.date_fin).all()
    resultats=[]
    questions=[]
    if len(liste_groupes)==0:
        for sondage in sondages:
            questions=ReponseQuestionSondage.query.join(QuestionSondage).filter(ReponseQuestionSondage.id_sond==sondage.id_sond).all()
            eleves=Eleve.query.join(RepSondage).filter(RepSondage.id_sondage==sondage.id_sondage).all()
            for eleve in eleves:
                res_eleve=RepSondage.query.join(Eleve).filter(RepSondage.id_sondage==sondage.id_sondage).filter(Eleve.num_etu==eleve.num_etu).first()
                groupe=res_eleve.groupe_s1 if semestre=="S1" else res_eleve.groupe_s2
                if questions is not None:
                    res_qs=[]
                    for q in questions:
                        if q.question not in questions:
                                questions.append(q.question)
                        res_q=ReponseQuestionSondage.query.join(QuestionSondage).filter(ReponseQuestionSondage.id_question==q.id_question).filter(ReponseQuestionSondage.num_etu==eleve.num_etu).first()
                        res_qs.append(res_q)
                resultats.append([res_eleve,groupe,res_qs])
    else:
        if semestre == "S1":
            for sondage in sondages:
                questions=ReponseQuestionSondage.query.join(QuestionSondage).filter(ReponseQuestionSondage.id_sond==sondage.id_sond).all()
                eleves=Eleve.query.join(RepSondage).filter(RepSondage.id_sondage==sondage.id_sondage).filter(Eleve.groupe_s1.in_(liste_groupes)).all()
                for eleve in eleves:
                    res_eleve=RepSondage.query.join(Eleve).filter(RepSondage.id_sondage==sondage.id_sondage).filter(Eleve.num_etu==eleve.num_etu).first()
                    if questions is not None:
                        res_qs=[]
                        for q in questions:
                            if q.question not in questions:
                                questions.append(q.question)
                            res_q=ReponseQuestionSondage.query.join(QuestionSondage).filter(ReponseQuestionSondage.id_question==q.id_question).filter(ReponseQuestionSondage.num_etu==eleve.num_etu).first()
                            res_qs.append(res_q)
                    resultats.append([res_eleve,res_eleve.groupe_s1,res_qs])
        else:
            for sondage in sondages:
                questions=ReponseQuestionSondage.query.join(QuestionSondage).filter(ReponseQuestionSondage.id_sond==sondage.id_sond).all()
                eleves=Eleve.query.join(RepSondage).filter(RepSondage.id_sondage==sondage.id_sondage).filter(Eleve.groupe_s2.in_(liste_groupes)).all()
                for eleve in eleves:
                    res_eleve=RepSondage.query.join(Eleve).filter(RepSondage.id_sondage==sondage.id_sondage).filter(Eleve.num_etu==eleve.num_etu).first()
                    if questions is not None:
                        res_qs=[]
                        for q in questions:
                            if q.question not in questions:
                                questions.append(q.question)
                            res_q=ReponseQuestionSondage.query.join(QuestionSondage).filter(ReponseQuestionSondage.id_question==q.id_question).filter(ReponseQuestionSondage.num_etu==eleve.num_etu).first()
                            res_qs.append(res_q)
                    resultats.append([res_eleve,res_eleve.groupe_s2,res_qs])
    return resultats,questions

def get_oraux(id_sem:int)->list:
    """fonction recuperant les oraux pour une date

    Args:
        date (String): date du QCM
    Returns:
        list: liste des oraux
    """
    sem = Semaine.query.filter(Semaine.id_semaine == id_sem).first()
    oraux=Oral.query.filter(Oral.date_oral >= sem.date_debut).filter(Oral.date_oral <= sem.date_fin).all()
    return oraux


def get_semaine_act()->Semaine:
    """fonction recuperant la semaine actuelle

    Returns:
        Semaine: semaine actuelle
    """
    date_act = datetime.datetime.now()
    sem = Semaine.query.join(Periode).filter(Semaine.date_debut <= date_act).filter(Semaine.date_fin >= date_act).first()
    return sem

def get_semaines_choix(soutien=False)->list:
    """recupere les semaines jusqu'a la semaine actuelle comprise
    si soutien alors recupere aussi la semaine prochaine"""
    sem_act = get_semaine_act()
    semaines = Semaine.query.join(Periode).filter(Semaine.id_semaine <= sem_act.id_semaine).all()
    if soutien:
        semaines.append(Semaine.query.filter(Semaine.id_semaine == sem_act.id_semaine+1).first())
    return semaines


def get_res_QCM_eleve(id_eleve:int, id_sem:int)->list:
    """fonction recuperant les resultats du QCM pour un eleve et une date

    Args:
        id_eleve (int): id de l eleve
        date (String): date du QCM
    Returns:
        list: liste des resultats de QCM pour un eleve
    """
    sem = Semaine.query.filter(Semaine.id_semaine == id_sem).first()
    res_qcm = ResultatQCM.query.filter(ResultatQCM.qcm.date_fin >= sem.date_debut).filter(ResultatQCM.qcm.date_fin <= sem.date_fin).filter(ResultatQCM.num_etu == id_eleve).all()
    return res_qcm

def get_res_sond_eleve(id_eleve:int, id_sem:int)->list:
    """fonction recuperant les resultats du sondage pour un eleve et une date

    Args:
        id_eleve (int): id de l eleve
        date (String): date du QCM
    Returns:
        list: liste des resultats de sondage pour un eleve
    """
    sem = Semaine.query.filter(Semaine.id_semaine == id_sem).first()
    res_sond = RepSondage.query.join(Sondage).join(ReponseQuestionSondage).filter(RepSondage.num_etu == id_eleve).filter(Sondage.date_sond >= sem.date_debut).filter(Sondage.date_sond <= sem.date_fin).all()
    return res_sond
def get_eleve(id_eleve:int)->Eleve:
    """fonction recuperant un eleve

    Args:
        id_eleve (int): id de l eleve
    Returns:
        Eleve: eleve
    """
    eleve = Eleve.query.filter(Eleve.num_etu == id_eleve).first()
    return eleve

def get_eleves_groupe(groupe:int, date:str):
    """fonction recuperant les eleves d un groupe pour une date

    Args:
        groupe (String): groupe de l eleve
        date (String): date du QCM
    Returns:
        list: liste des eleves
    """
    sem = Semaine.query.filter(Semaine.date_debut <= date).filter(Semaine.date_fin >= date).first()
    #on verifie si on est en periode 1 ou 2
    if Periode.query.filter(Periode.id_periode==sem.id_periode).first().semestre==1:
        eleves = Eleve.query.filter(Eleve.groupe_s1 == groupe).filter(Eleve.date_debut >= sem.date_debut).filter(Eleve.date_debut <= sem.date_fin).all()
    eleves = Eleve.query.filter(Eleve.groupe_s2 == groupe).filter(Eleve.date_fin >= sem.date_debut).filter(Eleve.date_fin <= sem.date_fin).all()
    return eleves

def disponibilites_enseignant(id_enseignant:int, date:str)->list:
    """fonction recuperant les disponibilites d un enseignant pour une date

    Args:
        id_enseignant (int): id de l enseignant
        date (String): date du QCM
    Returns:
        list: liste des disponibilites
    """
    sem = Semaine.query.filter(Semaine.date_debut <= date).filter(Semaine.date_fin >= date).first()
    dispo = EstDisponible.query.join(Oral).filter(Oral.date_oral >= sem.date_debut).filter(Oral.date_oral <= sem.date_fin).filter(EstDisponible.id_prof == id_enseignant).all()
    return dispo

def ajouter_resultat_eleve(id_QCM:int,num_etu:int,note:float)->None:
    """fonction ajoutant un resultat de QCM pour un eleve

    Args:
        id_QCM (int): id du QCM
        num_etu (int): id de l eleve
        note (float): note du QCM
    Returns:
        None
    """
    nb_rep = ResultatQCM.quety.filter(num_etu = num_etu).filter(id_qcm = id_QCM).count()
    if nb_rep == 0:
        res = ResultatQCM(id_qcm = id_QCM, num_etu = num_etu, note = note)
        db.session.add(res)
        db.session.commit()
    else:
        pass
def gen_soutien(num_sem:int):
    """fonction generant les soutiens pour une semaine donnee

    Args:
        num_sem (int): numero de la semaine
        seuil (float): seuil de la moyenne
    """
    #genere les soutiens pour la semaine donnee
    sem=Semaine.query.filter(Semaine.numSemaine==num_sem).first()
    semaine_suivante=Semaine.query.filter(Semaine.numSemaine==num_sem+1).first()
    if Oral.query.filter(Oral.date_oral>=semaine_suivante.date_debut).filter(Oral.date_oral<=semaine_suivante.date_fin).count()==0:
        jour_sout=lecture_parametre_def("Jour de soutien")
        heure_sout=lecture_parametre_def("Heure de soutien")
        date_sout=semaine_suivante.date_debut+datetime.timedelta(days=jour_sout)
        max_id_oral=Oral.query.order_by(Oral.id_oral.desc()).first().id_oral
        oral=Oral(id_oral=max_id_oral+1,date_oral=date_sout,heure_debut=heure_sout,heure_fin=heure_sout+datetime.timedelta(hours=1))
        db.session.add(oral)
        db.session.commit()
    oraux=Oral.query.filter(Oral.date_oral>=semaine_suivante.date_debut).filter(Oral.date_oral<=semaine_suivante.date_fin).all()
    seuil=float(lecture_parametre_def("Seuil"))
    qcms_trouve=False
    while not qcms_trouve:
        #cherche une semaine avec des qcms
        qcms=QCM.query.join(Matiere).filter(QCM.date_fin >= sem.date_debut).filter(QCM.date_fin <= sem.date_fin).order_by(Matiere.nom_matiere).all()
        if len(qcms)==0:
            sem=Semaine.query.filter(Semaine.numSemaine==num_sem-1).first()
            num_sem-=1
        else:
            qcms_trouve=True
    eleves_ret_besoin={}
    non_retenus={}
    retenus={}
    matieres=[]
    for qcm in qcms:
        moyenne=get_moyenne_generale(qcm.id_qcm)
        if qcm.nom_matiere not in matieres:
            matieres.append(qcm.nom_matiere)
        eleves_volontaires_besoin=ResultatQCM.join(RepSondage,ResultatQCM.num_etu==RepSondage.num_etu)
        eleves_volontaires_besoin.join(QCM,ResultatQCM.id_qcm==QCM.id_qcm).join(Matiere,QCM.id_matiere==Matiere.id_matiere)
        eleves_volontaires_besoin.join(Eleve,ResultatQCM.num_etu==Eleve.num_etu).filter(ResultatQCM.id_qcm == qcm.id_qcm)
        eleves_volontaires_besoin.filter(ResultatQCM.note < seuil*moyenne).filter(RepSondage.volontaire=='oui')
        eleves_volontaires_besoin.filter(Matiere.nom_matiere==qcm.matiere.nom_matiere).order_by(ResultatQCM.note).all()

        eleves_hesitants=ResultatQCM.join(RepSondage,ResultatQCM.num_etu==RepSondage.num_etu)
        eleves_hesitants.join(QCM,ResultatQCM.id_qcm==QCM.id_qcm).join(Matiere,QCM.id_matiere==Matiere.id_matiere)
        eleves_hesitants.join(Eleve,ResultatQCM.num_etu==Eleve.num_etu).filter(ResultatQCM.id_qcm == qcm.id_qcm)
        eleves_hesitants.filter(ResultatQCM.note < seuil*moyenne).filter(RepSondage.volontaire=='~')
        eleves_hesitants.filter(Matiere.nom_matiere==qcm.matiere.nom_matiere).order_by(ResultatQCM.note).all()
        possibles=eleves_volontaires_besoin+eleves_hesitants
        if len(eleves_volontaires_besoin+eleves_hesitants)>=3:
            cpt_retenu=0
            while cpt_retenu<5 or len(possibles)!=0:
                #verif si l'eleve est dans retenus
                #si oui alors on ajoute la matiere a ses matieres necessaires et on ajoute la note qcm aux dico note qcm
                if possibles[0].num_etu in retenus:
                    retenus[possibles[0].num_etu]["notes_qcm"].append(possibles[0].note)
                    if retenus[possibles[0].num_etu]["matiere_retenue"]["note"] < possibles[0].note:
                        retenus[possibles[0].num_etu]["matiere_retenue"]["note"]=possibles[0].note
                        retenus[possibles[0].num_etu]["matiere_retenue"]["matiere"]=qcm.nom_matiere
                    profs_dispos=Professeur.query.join(EstDisponible).join(Oral).join(PossibiliteSoutien)
                    profs_dispos.filter(Oral.date_oral >= semaine_suivante.date_debut).filter(Oral.date_oral <= semaine_suivante.date_fin)
                    profs_dispos.filter(PossibiliteSoutien.id_matiere==qcm.id_matiere).all()
                    for prof in profs_dispos:
                        if not retenus[possibles[0]]["profs"]["profs_dispos"]:
                            retenus[possibles[0].num_etu]["profs"]["profs_dispos"]=[prof]
                        else:
                            if prof not in retenus[possibles[0]]["profs"]["profs_dispos"]:
                                retenus[possibles[0].num_etu]["profs"]["profs_dispos"].append(prof)
                    profs_possibles=Professeur.query.join(PossibiliteSoutien).filter(PossibiliteSoutien.id_matiere==qcm.id_matiere).all()
                    for prof in profs_possibles:
                        if not retenus[possibles[0].num_etu]["profs"]["profs_possibles"]:
                            retenus[possibles[0].num_etu]["profs"]["profs_possibles"]=[prof]
                        else:
                            if prof not in retenus[possibles[0].num_etu]["profs"]["profs_possibles"]:
                                retenus[possibles[0].num_etu]["profs"]["profs_possibles"].append(prof)
                    possibles.pop(0)
                #si non alors on ajoute l'eleve a retenus et on ajoute la matiere a ses matieres necessaires et on ajoute la note qcm aux dico note qcm
                else:
                    retenus[possibles[0].num_etu]={"eleve":possibles[0],"notes_qcm":[possibles[0].note],"matiere_retenue":{"note":possibles[0].note,"matiere":qcm.nom_matiere}}
                    profs_dispos=Professeur.query.join(EstDisponible).join(Oral).join(PossibiliteSoutien)
                    profs_dispos.filter(Oral.date_oral >= semaine_suivante.date_debut).filter(Oral.date_oral <= semaine_suivante.date_fin)
                    profs_dispos.filter(PossibiliteSoutien.id_matiere==qcm.id_matiere).all()
                    for prof in profs_dispos:
                        if not retenus[possibles[0].num_etu]["profs"]["profs_dispos"]:
                            retenus[possibles[0].num_etu]["profs"]["profs_dispos"]=[prof]
                        else:
                            if prof not in retenus[possibles[0].num_etu]["profs"]["profs_dispos"]:
                                retenus[possibles[0].num_etu]["profs"]["profs_dispos"].append(prof)
                    profs_possibles=Professeur.query.join(PossibiliteSoutien).filter(PossibiliteSoutien.id_matiere==qcm.id_matiere).all()
                    for prof in profs_possibles:
                        if not retenus[possibles[0].num_etu]["profs"]["profs_possibles"]:
                            retenus[possibles[0].num_etu]["profs"]["profs_possibles"]=[prof]
                        else:
                            if prof not in retenus[possibles[0].num_etu]["profs"]["profs_possibles"]:
                                retenus[possibles[0].num_etu]["profs"]["profs_possibles"].append(prof)
                    possibles.pop(0)
                cpt_retenu+=1
        while len(possibles)>0:
            if possibles[0].num_etu in non_retenus:
                non_retenus[possibles[0].num_etu]["notes_qcm"].append(possibles[0].note)
                if non_retenus[possibles[0].num_etu]["matiere_retenue"]["note"] < possibles[0].note:
                    non_retenus[possibles[0].num_etu]["matiere_retenue"]["note"]=possibles[0].note
                    non_retenus[possibles[0].num_etu]["matiere_retenue"]["matiere"]=qcm.nom_matiere
                profs_dispos=Professeur.query.join(EstDisponible).join(Oral).join(PossibiliteSoutien)
                profs_dispos.filter(Oral.date_oral >= semaine_suivante.date_debut).filter(Oral.date_oral <= semaine_suivante.date_fin)
                profs_dispos.filter(PossibiliteSoutien.id_matiere==qcm.id_matiere).all()
                for prof in profs_dispos:
                    if not non_retenus[possibles[0].num_etu]["profs"]["profs_dispos"]:
                        non_retenus[possibles[0].num_etu]["profs"]["profs_dispos"]=[prof]
                    else:
                        if prof not in non_retenus[possibles[0].num_etu]["profs"]["profs_dispos"]:
                            non_retenus[possibles[0].num_etu]["profs"]["profs_dispos"].append(prof)
                profs_possibles=Professeur.query.join(PossibiliteSoutien).filter(PossibiliteSoutien.id_matiere==qcm.id_matiere).all()
                for prof in profs_possibles:
                    if not non_retenus[possibles[0].num_etu]["profs"]["profs_possibles"]:
                        non_retenus[possibles[0].num_etu]["profs"]["profs_possibles"]=[prof]
                    else:
                        if prof not in non_retenus[possibles[0].num_etu]["profs"]["profs_possibles"]:
                            non_retenus[possibles[0].num_etu]["profs"]["profs_possibles"].append(prof)
                
                possibles.pop(0)
            else:
                non_retenus[possibles[0].num_etu]={"eleve":possibles[0],"notes_qcm":[possibles[0].note],"matieres_retenue":{"note":possibles[0].note,"matiere":qcm.nom_matiere}}
                profs_dispos=Professeur.query.join(EstDisponible).join(Oral).join(PossibiliteSoutien)
                profs_dispos.filter(Oral.date_oral >= semaine_suivante.date_debut).filter(Oral.date_oral <= semaine_suivante.date_fin)
                profs_dispos.filter(PossibiliteSoutien.id_matiere==qcm.id_matiere).all()
                for prof in profs_dispos:
                    if not non_retenus[possibles[0].num_etu]["profs"]["profs_dispos"]:
                        non_retenus[possibles[0].num_etu]["profs"]["profs_dispos"]=[prof]
                    else:
                        if prof not in non_retenus[possibles[0].num_etu]["profs"]["profs_dispos"]:
                            non_retenus[possibles[0].num_etu]["profs"]["profs_dispos"].append(prof)
                profs_possibles=Professeur.query.join(PossibiliteSoutien).filter(PossibiliteSoutien.id_matiere==qcm.id_matiere).all()
                for prof in profs_possibles:
                    if not non_retenus[possibles[0].num_etu]["profs"]["profs_possibles"]:
                        non_retenus[possibles[0].num_etu]["profs"]["profs_possibles"]=[prof]
                    else:
                        if prof not in non_retenus[possibles[0].num_etu]["profs"]["profs_possibles"]:
                            non_retenus[possibles[0].num_etu]["profs"]["profs_possibles"].append(prof)
                
                possibles.pop(0)

        eleves_besoin=ResultatQCM.join(RepSondage,ResultatQCM.num_etu==RepSondage.num_etu)
        eleves_besoin.join(QCM,ResultatQCM.id_qcm==QCM.id_qcm).join(Matiere,QCM.id_matiere==Matiere.id_matiere)
        eleves_besoin.join(Eleve,ResultatQCM.num_etu==Eleve.num_etu)
        eleves_besoin.filter(ResultatQCM.id_qcm == qcm.id_qcm)
        eleves_besoin.filter(ResultatQCM.note < seuil*moyenne).filter(RepSondage.volontaire=='non')
        eleves_besoin.order_by(ResultatQCM.note).all()
        for eleve in eleves_besoin:
            if eleve.num_etu in eleves_ret_besoin:
                eleves_ret_besoin[eleve.num_etu]["notes_qcm"].append(eleve.note)
                if eleves_ret_besoin[eleve.num_etu]["matiere_retenue"]["note"] < eleve.note:
                    eleves_ret_besoin[eleve.num_etu]["matiere_retenue"]["note"]=eleve.note
                    eleves_ret_besoin[eleve.num_etu]["matiere_retenue"]["matiere"]=qcm.nom_matiere
                profs_dispos=Professeur.query.join(EstDisponible).join(Oral).join(PossibiliteSoutien)
                profs_dispos.filter(Oral.date_oral >= semaine_suivante.date_debut).filter(Oral.date_oral <= semaine_suivante.date_fin)
                profs_dispos.filter(PossibiliteSoutien.id_matiere==qcm.id_matiere).all()
                for prof in profs_dispos:
                    if not eleves_ret_besoin[eleve.num_etu]["profs"]["profs_dispos"]:
                        eleves_ret_besoin[eleve.num_etu]["profs"]["profs_dispos"]=[prof]
                    else:
                        if prof not in eleves_ret_besoin[eleve.num_etu]["profs"]["profs_dispos"]:
                            eleves_ret_besoin[eleve.num_etu]["profs"]["profs_dispos"].append(prof)
                profs_possibles=Professeur.query.join(PossibiliteSoutien).filter(PossibiliteSoutien.id_matiere==qcm.id_matiere).all()
                for prof in profs_possibles:
                    if not eleves_ret_besoin[eleve.num_etu]["profs"]["profs_possibles"]:
                        eleves_ret_besoin[eleve.num_etu]["profs"]["profs_possibles"]=[prof]
                    else:
                        if prof not in eleves_ret_besoin[eleve.num_etu]["profs"]["profs_possibles"]:
                            eleves_ret_besoin[eleve.num_etu]["profs"]["profs_possibles"].append(prof)
                
            else:
                eleves_ret_besoin[eleve.num_etu]={"eleve":eleve,"notes_qcm":[eleve.note],"matieres_retenue":{"note":eleve.note,"matiere":qcm.nom_matiere}}
                profs_dispos=Professeur.query.join(EstDisponible).join(Oral).join(PossibiliteSoutien)
                profs_dispos.filter(Oral.date_oral >= semaine_suivante.date_debut).filter(Oral.date_oral <= semaine_suivante.date_fin)
                profs_dispos.filter(PossibiliteSoutien.id_matiere==qcm.id_matiere).all()
                for prof in profs_dispos:
                    if not eleves_ret_besoin[eleve.num_etu]["profs"]["profs_dispos"]:
                        eleves_ret_besoin[eleve.num_etu]["profs"]["profs_dispos"]=[prof]
                    else:
                        if prof not in eleves_ret_besoin[eleve.num_etu]["profs"]["profs_dispos"]:
                            eleves_ret_besoin[eleve.num_etu]["profs"]["profs_dispos"].append(prof)
                profs_possibles=Professeur.query.join(PossibiliteSoutien).filter(PossibiliteSoutien.id_matiere==qcm.id_matiere).all()
                for prof in profs_possibles:
                    if not eleves_ret_besoin[eleve.num_etu]["profs"]["profs_possibles"]:
                        eleves_ret_besoin[eleve.num_etu]["profs"]["profs_possibles"]=[prof]
                    else:
                        if prof not in eleves_ret_besoin[eleve.num_etu]["profs"]["profs_possibles"]:
                            eleves_ret_besoin[eleve.num_etu]["profs"]["profs_possibles"].append(prof)
    return retenus,non_retenus,eleves_ret_besoin,oraux,matieres

def get_moyenne_gen_etu(id_etu:int)->float:
    """Retourne la moyenne generale d'un etudiant"""
    moyenne=0
    nb_notes=0
    notes=ResultatQCM.query.filter(ResultatQCM.num_etu==id_etu).all()
    for note in notes:
        moyenne+=note.note
        nb_notes+=1
    if nb_notes==0:
        return 0
    else:
        return moyenne/nb_notes

def get_dern_comm(id_sem:int,id_etu:int)->str:
    """Retourne le dernier commentaire d'oral présent à cette semaine
    """
    sem_act=Semaine.query.filter(Semaine.id_semaine==id_sem).first()
    part=ParticipantsOral.query.join(Oral).filter(ParticipantsOral.num_etu==id_etu).filter(Oral.date_oral>=sem_act.date_debut).filter(Oral.date_oral<=sem_act.date_fin)
    if part:
        return part.commentaire
    cpt_sem=id_sem-1
    while not part and cpt_sem>0:
        part = ParticipantsOral.query.join(Oral).filter(ParticipantsOral.num_etu == id_etu).filter(
            Oral.date_oral >= sem_act.date_debut).filter(Oral.date_oral <= sem_act.date_fin)
        if part:
            return part.commentaire
        cpt_sem-=1
    return ""   


def get_suivi_gen(id_sem:int)->list:
    """Retourne les donnees pour le suivi general d'une semaine
    {% for eleve in eleves %}
                    <tr>
                        <td><a href="{{url_for ('Suivie_etu',num_etu=eleve.num_etu)}}">{{ eleve.eleve.nom }} {{ eleve.eleve.prenom }}</a></td>
                        <td>{{ eleve.nb_part }}</td>
                        {% if semaine_act.semestre == 1 %}
                            <td>{{ eleve.eleve.groupe_s1 }}</td>
                        {% else %}
                            <td>{{ eleve.eleve.groupe_s2 }}</td>
                        {% endif %}
                        <td>{{ eleve.moyenne }}</td>
                        <td>{{ eleve.dern_comm }}</td>
                    </tr>
                {% endfor %} 
    """
    eleves=Eleve.query.all()
    suivi_gen=[]
    for eleve in eleves:
        suivi_et={"eleve":eleve,"nb_part":0,"moyenne":0,"dern_comm":""}
        parts=ParticipantsOral.query.filter(ParticipantsOral.num_etu==eleve.num_etu).all().count()
        suivi_et["nb_part"]=parts
        moyenne=get_moyenne_gen_etu(eleve.num_etu)
        suivi_et["moyenne"]=moyenne
        dern_comm=get_dern_comm(id_sem,eleve.num_etu)
        suivi_et["dern_comm"]=dern_comm
        suivi_gen.append(suivi_et)
    return suivi_gen

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
  
def ajouter_reponse_sondage(participation : str, id_sondage: int, num_etu: str, date_sondage: str, matiere_voulu: str, commentaire: str)->None:
    """fonction ajoutant une reponse a un sondage

    Args:
        participation (str): participation a l'oral
        id_sondage (int): id du sondage
        num_etu (str): numero de l'etudiant
        date_sondage (str): date du sondage
        matiere_voulu (str): matiere voulu
        commentaire (str): commentaire
    """
    nb_rep = RepSondage.quety.filter(num_etu = num_etu).filter(id_sondage = id_sondage).filter(date_sond = date_sondage).count()
    if nb_rep == 0:
        rep = RepSondage(participation = participation, id_sondage = id_sondage, num_etu = num_etu, date_sond = date_sondage,
                        matiere_voulue = matiere_voulu, commentaire = commentaire)
        db.session.add(rep)
        db.session.commit()

def init_periode_semaines():
    #crea des periodes
    rentree=lecture_parametre_def("Date rentree")
    fin_p1=lecture_parametre_def("Date fin P1")
    fin_p2=lecture_parametre_def("Date fin P2")
    fin_p3=lecture_parametre_def("Date fin P3")
    fin_annee=lecture_parametre_def("Date fin annee")
    date_rentree=datetime.strptime(rentree,"%d/%m/%Y")
    date_fin_p1=datetime.strptime(fin_p1,"%d/%m/%Y")
    date_fin_p2=datetime.strptime(fin_p2,"%d/%m/%Y")
    date_fin_p3=datetime.strptime(fin_p3,"%d/%m/%Y")
    date_fin_annee=datetime.strptime(fin_annee,"%d/%m/%Y")
    p1=Periode(id_periode=1,date_debut=date_rentree,date_fin=date_fin_p1,semestre=1)
    p2=Periode(id_periode=2,date_debut=date_fin_p1+datetime.timedelta(days=1),date_fin=date_fin_p2,semestre=1)
    p3=Periode(id_periode=3,date_debut=date_fin_p2+datetime.timedelta(days=1),date_fin=date_fin_p3,semestre=2)
    p4=Periode(id_periode=4,date_debut=date_fin_p3+datetime.timedelta(days=1),date_fin=date_fin_annee,semestre=2)
    db.session.add(p1)
    db.session.add(p2)
    db.session.add(p3)
    db.session.add(p4)

    #crea des semaines
    date=date_rentree
    id_semaine=1
    while date<date_fin_annee:
        semaine=Semaine(id_semaine=id_semaine,date_debut=date,date_fin=date+datetime.timedelta(days=6))
        date=date+datetime.timedelta(days=7)
        id_semaine=id_semaine+1
        db.session.add(semaine)
    db.session.commit()


def ajouter_commentaire(id_oral,num_etu,commentaire):
    oral=Oral.query.filter(Oral.id_oral==id_oral).first()
    etu=Eleve.query.filter(Eleve.num_etu==num_etu).first()
    part=ParticipantsOral.query.filter(ParticipantsOral.id_oral==oral.id_oral).filter(ParticipantsOral.num_etu==etu.num_etu).first()
    part.commentaire=commentaire
    db.session.commit()

def ajouter_dispo(id_oral,idProf):
    oral=Oral.query.filter(Oral.id_oral==id_oral).first()
    prof=Professeur.query.filter(Professeur.idProf==idProf).first()
    dispo=EstDisponible.query.filter(EstDisponible.id_oral==oral.id_oral).filter(EstDisponible.idProf==prof.idProf).first()
    if dispo is None:
        dispo=EstDisponible(id_oral=oral.id_oral,idProf=prof.idProf)
        db.session.add(dispo)
    else:
        pass

def suppression_oral(date:str,heure:str)->None:
    """fonction supprimant un oral

    Args:
        date (str): date de l'oral
        heure (str): heure de l'oral
    """
    oral=Oral.query.filter(Oral.date_oral==date).filter(Oral.heure_oral==heure).first()
    if oral is not None:
        db.session.delete(oral)
        db.session.commit()

def ajouter_resultat_eleve(id_QCM,num_etu,note):
    nb_rep = ResultatQCM.query.filter(numEtu = num_etu).filter(idQCM = id_QCM).count()
    if nb_rep == 0:
        res = ResultatQCM(idQCM = id_QCM, numEtu = num_etu, note = note)
        db.session.add(res)
        db.session.commit()
    else:
        pass

def ajouter_reponse_sondage(participation : str, id_sondage: int, num_etu: str, date_sondage: str, matiere_voulu: str, commentaire: str):
    nb_rep = RepSondage.query.filter(numEtu = num_etu).filter(idSondage = id_sondage).filter(dateSondage = date_sondage).count()
    if nb_rep == 0:
        rep = RepSondage(participation = participation, idSondage = id_sondage, numEtu = num_etu, dateSondage = date_sondage,
                        matiereVoulu = matiere_voulu, commentaire = commentaire)
        db.session.add(rep)
        db.session.commit()
    else:
        pass

def creation_existe(num_etu, nom, prenom, groupeS1, groupeS2):
    res = Eleve.query.filter(numEtu = num_etu).count()
    if res == 0:
        eleve = Eleve(numEtu = num_etu, nom = nom, prenom = prenom, groupeS1 = groupeS1, groupeS2 = groupeS2)
        db.session.add(eleve)
        db.session.commit()

def get_id_QCM(nom_matiere, url, id_matiere):
    id_qcm = 0
    res = QCM.query.filter(urlQCM = url).count()
    if res == 0:
        id_qcm = get_id_QCM_max() + 1
        qcm = QCM(idQCM = id_qcm, nomQCM = nom_matiere, urlQCM = url, idMatiere = id_matiere)
        db.session.add(qcm)
        db.session.commit()
    else:
        id_qcm = QCM.query.filter(urlQCM = url).first().idQCM
    return id_qcm

def get_id_sondage(url):
    id = 0
    res = Sondage.query.filter(urlQCM = url).count()
    if res == 0:
        id = get_id_sondage_max() + 1
        sondage = Sondage(idSond = id, urlQCM = url)
        db.session.add(sondage)
        db.session.commit()
        return id
    else:
        id = Sondage.query.filter(urlQCM = url).first().idSond
    return id

def get_id_matiere(nom_matiere):
    id = 0
    res = Matiere.query.filter(Matiere = nom_matiere).count()
    if res == 0:
        id = get_id_matiere_max() + 1
        matiere = Matiere(idMatiere = id, Matiere = nom_matiere)
        db.session.add(matiere)
        db.session.commit()
        return id
    else:
        id = Matiere.query.filter(Matiere = nom_matiere).first().idMatiere
    return id
        
def get_id_matiere_max():
    return db.session.query(func.max(Matiere.idMatiere)).scalar()
        
def get_id_QCM_max():
    return db.session.query(func.max(QCM.idQCM)).scalar()
        
def get_id_sondage_max():
    return db.session.query(func.max(Sondage.idSond)).scalar()

@login_manager.user_loader
def load_user(username):
    return User.query.get(username)

# fais une fonction qui renvoi les élèves retenus poir un oral (prioirité aux élèves qui ont des notes en dessous de 10, si ils sont volontaires ou pas, ensuite prioirité aux élèves volontaires, ensuite aux autres))
def eleves_retenus_oral(id_oral):
    oral=Oral.query.filter(Oral.id_oral==id_oral).first()
    liste_eleves=Eleve.query.all()
    liste_eleves_retenus=[]
    matiere = oral.matiere
    for eleve in liste_eleves:
        reponse_sondage = RepSondage.query.filter(RepSondage.idSondage == oral.idSondage, RepSondage.num_etu == eleve.num_etu).first()
        if reponse_sondage is not None:
            if reponse_sondage.volontaire == "oui":
                if reponse_sondage.matiereVoulu == matiere:
                    liste_eleves_retenus.append(eleve)
    return liste_eleves_retenus

def eleves_non_retenus_oral(id_oral):
    oral=Oral.query.filter(Oral.id_oral==id_oral).first()
    liste_eleves=Eleve.query.all()
    liste_eleves_non_retenus=[]
    matiere = oral.matiere
    for eleve in liste_eleves:
        reponse_sondage = RepSondage.query.filter(RepSondage.idSondage == oral.idSondage, RepSondage.num_etu == eleve.num_etu).first()
        if reponse_sondage is not None:
            if reponse_sondage.volontaire == "non":
                if reponse_sondage.matiereVoulu == matiere:
                    liste_eleves_non_retenus.append(eleve)
    return liste_eleves_non_retenus

def eleves_besoin_oral(id_oral):
    oral=Oral.query.filter(Oral.id_oral==id_oral).first()
    liste_eleves=Eleve.query.all()
    liste_eleves_besoin=[]
    matiere = oral.matiere
    qcm = QCM.query.filter(QCM.idMatiere == matiere).first()
    for eleve in liste_eleves:
        res_qcm = ResultatQCM.query.filter(ResultatQCM.idQCM == qcm.idQCM, ResultatQCM.num_etu == eleve.num_etu).first()
        reponse_sondage = RepSondage.query.filter(RepSondage.idSondage == oral.idSondage, RepSondage.num_etu == eleve.num_etu).first()
        if reponse_sondage is not None:
            if reponse_sondage.volontaire == "non":
                if reponse_sondage.matiereVoulu == matiere:
                    if res_qcm is not None:
                        if res_qcm.note < 10:
                            liste_eleves_besoin.append(eleve)
    return liste_eleves_besoin