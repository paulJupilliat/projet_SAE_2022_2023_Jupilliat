## Models permet de definir les données de l app


from .app import db
from flask_login import UserMixin
from .app import login_manager

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
    id_sond = db.Column(db.Integer, db.ForeignKey("sondage.id_sond"), primary_key=True)
    id_quest = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(500))
    #relation pour avoir le sondage d une question
    sondage = db.relationship("Sondage", backref=db.backref("questionsondage", lazy="dynamic"))
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
    matiere = db.relationship("Matiere", backref=db.backref("qcm", lazy="dynamic"))
    date_debut = db.Column(db.String(500))
    date_fin = db.Column(db.String(500))
    def __repr__(self):
        """representation de l objet QCM"""
        return f"QCM({self.id_qcm}, {self.nom_qcm}, {self.url_qcm}, {self.date_debut}, {self.date_fin})"

class Professeur(db.Model):
    """classe Professeur qui contient les professeurs
    """
    __tablename__ = "professeur"
    id_prof = db.Column(db.String(500), primary_key=True)
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
    password = db.Column(db.String(50))
    est_admin = db.Column(db.String(10))
    def get_id(self):
        return self.username
    def est_admin(self):
        return self.est_admin=="T"
    def __repr__(self):
        """representation de l objet User"""
        return f"User({self.username}, {self.password}, {self.est_admin()})"

class Oral(db.Model):
    """classe Oral qui contient les oraux(soutien)
    """
    __tablename__ = "oraux"
    id_oral = db.Column(db.Integer, primary_key=True)
    date_oral = db.Column(db.String(500))
    heure_oral = db.Column(db.String(500))
    #relation pour avoir la matiere d un oral
    id_matiere = db.Column(db.Integer, db.ForeignKey("matiere.id_matiere"))
    #relation inverse pour avoir les oraux d une matiere
    matiere = db.relationship("Matiere", backref=db.backref("oral", lazy="dynamic"))
    #relation pour avoir le professeur d un oral
    id_prof = db.Column(db.String(500), db.ForeignKey("professeur.id_prof"))
    #relation inverse pour avoir les oraux d un professeur
    professeur = db.relationship("Professeur", backref=db.backref("oral", lazy="dynamic"))
    def __repr__(self):
        """representation de l objet Oral"""
        return f"Oral({self.id_oral}, {self.date_oral}, {self.heure_oral})"

class ParticipantsOral(db.Model):
    """classe ParticipantsOral qui fait la 
    relation entre les oraux et les eleves"""
    __tablename__ = "participantsoral"
    id_oral = db.Column(db.Integer, db.ForeignKey("oral.idOralz"), primary_key=True)
    num_etu = db.Column(db.Integer, db.ForeignKey("eleve.num_etu"), primary_key=True)
    commentaire = db.Column(db.String(800))
    #relation pour avoir l oral d un participant
    oral= db.relationship(Oral, backref=db.backref("oraux", cascade="all, delete-orphan"),overlaps="oral,eleve")
    #relation pour avoir l eleve d un participant
    eleve= db.relationship(Eleve, backref=db.backref("eleves", cascade="all, delete-orphan"),overlaps="oral,eleve")
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
    eleve = db.relationship(Eleve, backref=db.backref("eleves", cascade="all, delete-orphan"),overlaps="qcm,eleve")
    #un qcm peut avoir qu'une seule note pour un eleve
    qcm = db.relationship(QCM, backref=db.backref("qcm", cascade="all, delete-orphan"),overlaps="qcm,eleve")
    def __repr__(self):
        """representation de l objet ResultatQCM"""
        return f"ResultatQCM({self.id_qcm}, {self.num_etu}, {self.note})"

class RepSondage(db.Model):
    """classe RepSondage qui fait la
    relation entre les sondages et les eleves -> reponses"""
    __tablename__ = "repsondage"
    id_sondage = db.Column(db.Integer, db.ForeignKey("sondage.id_sondage"), primary_key=True)
    num_etu = db.Column(db.Integer, db.ForeignKey("eleve.num_etu"), primary_key=True)
    matiere_voulue = db.Column(db.String(100))
    volontaire = db.Column(db.String(50))
    #relation pour avoir le sondage d une reponse
    sondage = db.relationship(Sondage, backref=db.backref("sondage", cascade="all, delete-orphan"),overlaps="sondage,eleve")
    #relation pour avoir l eleve d une reponse
    eleve = db.relationship(Eleve, backref=db.backref("eleves", cascade="all, delete-orphan"),overlaps="sondage,eleve")
    def __repr__(self):
        """representation de l objet RepSondage"""
        return f"RepSondage({self.participation}, {self.id_sondage}, {self.num_etu}, {self.date_sond}, {self.matiere_voulue}, {self.commentaire})"
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
    periode = db.relationship("Periode", backref=db.backref("semaine", lazy="dynamic"))
    def __repr__(self):
        """representation de l objet Semaine"""
        return f"Semaine({self.id_semaine}, {self.date_debut}, {self.date_fin})"

class PossibiliteSoutien(db.Model):
    """classe PossibiliteSoutien qui fait la
    relation entre les professeurs et les matieres et les periodes"""
    __tablename__ = "possibilitesoutien"
    id_prof = db.Column(db.String(500), db.ForeignKey("professeur.id_prof"), primary_key=True)
    id_matiere = db.Column(db.Integer, db.ForeignKey("matiere.id_matiere"), primary_key=True)
    id_periode = db.Column(db.Integer, db.ForeignKey("periode.id_periode"), primary_key=True)
    #relation pour avoir le professeur d une possibilite de soutien
    professeur = db.relationship(Professeur, backref=db.backref("professeur", cascade="all, delete-orphan"),overlaps="professeur,matiere,periode")
    #relation pour avoir la matiere d une possibilite de soutien
    matiere = db.relationship(Matiere, backref=db.backref("matiere", cascade="all, delete-orphan"),overlaps="professeur,matiere,periode")
    #relation pour avoir la periode d une possibilite de soutien
    periode = db.relationship(Periode, backref=db.backref("periode", cascade="all, delete-orphan"),overlaps="professeur,matiere,periode")
    def __repr__(self):
        """representation de l objet PossibiliteSoutien"""
        return f"PossibiliteSoutien({self.id_prof}, {self.id_matiere}, {self.id_periode})"
class EstDisponible(db.Model):
    """classe EstDisponible qui fait la
    relation entre les professeurs et les oraux(inscriptions)"""
    __tablename__ = "estdisponible"
    id_prof = db.Column(db.String(500), db.ForeignKey("professeur.id_prof"), primary_key=True)
    id_oral = db.Column(db.Integer, db.ForeignKey("oral.id_oral"), primary_key=True)
    #relation pour avoir le professeur d une disponibilite
    professeur = db.relationship(Professeur, backref=db.backref("professeur", cascade="all, delete-orphan"),overlaps="professeur,oral")
    #relation pour avoir l oral d une disponibilite
    oral = db.relationship(Oral, backref=db.backref("oral", cascade="all, delete-orphan"),overlaps="professeur,oral")
    def __repr__(self):
        """representation de l objet EstDisponible"""
        return f"EstDisponible({self.id_prof}, {self.id_oral})"

class ReponseQuestionSondage(db.Model):
    """classe ReponseQuestionSondage qui fait la
    relation entre les eleves et les questions facultatives et les reponses"""
    __tablename__ = "reponsequestionsondage"
    num_etu = db.Column(db.Integer, db.ForeignKey("eleve.num_etu"), primary_key=True)
    id_quest = db.Column(db.Integer, db.ForeignKey("questionSondage.id_quest"), primary_key=True)
    reponse = db.Column(db.String(500))
    #relation pour avoir l eleve d une reponse a une question
    eleve = db.relationship(Eleve, backref=db.backref("eleves", cascade="all, delete-orphan"),overlaps="sondage,eleve,questionSondage")
    #relation pour avoir la question d une reponse a une question
    question = db.relationship(QuestionSondage, backref=db.backref("questionSondage", cascade="all, delete-orphan"),overlaps="sondage,eleve,questionSondage")
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
    return qcms,soutien

def get_soutiens_etudiant(id_etu:int)->list:
    """fonction qui recupere les soutiens de l etudiant
    Args:
        id_etu: l id de l etudiant
    Return:
        oraux: les soutiens de l etudiant"""
    ids_oraux = ParticipantsOral.query.filter(ParticipantsOral.num_etu == id_etu).all()
    oraux = []
    for id_oral in ids_oraux:
        oral=Oral.query.join(ParticipantsOral).filter(Oral.id_oral == id_oral.id_oral).first()
        semaine=Semaine.query.filter(Semaine.date_debut <= oral.date).filter(Semaine.date_fin >= oral.date).first()
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
        str_js+="\tdata.addRow("+liste_sem+");"
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

def get_resultats_qcm_accueil(date:str)->dict:
    """fonction recuperant les resultats de QCM pour une date en renvoyant les moyennes par groupe et par matiere

    Args:
        date (String): date du QCM

    Returns:
        dict: dictionnaire contenant les moyennes par matiere et par groupe
    """
    #on regarde dans quelle semaine on est
    sem = Semaine.query.filter(Semaine.date_debut <= date).filter(Semaine.date_fin >= date).first()
    #calcul periode
    periode = Periode.query.filter(Periode.id_periode == sem.id_periode).first()
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
    qcms=QCM.query.filter(QCM.date_fin >= sem.date_debut).filter(QCM.date_fin <= sem.date_fin).all()
    #recup moyennes
    moyennes={}
    for qcm in qcms:
        nom_matiere=Matiere.query.filter(Matiere.id_matiere == qcm.id_matiere).first().nom_matiere
        moyennes[nom_matiere]={}
        for groupe in groupes:
            moyennes[nom_matiere][groupe]=get_moyenne_groupe(groupe,qcm.id_qcm,semestre)   
        #ajout moyenne generale
        moyennes[nom_matiere]["generale"]=get_moyenne_generale(qcm.id_qcm)
    return moyennes

def get_dispo_enseignant_accueil(semaine:int):
    """fonction recuperant les disponibilites des enseignants pour une date

    Args:
        date (String): date du QCM

    Returns:
        list: liste des disponibilites
    """
    sem = Semaine.query.filter(Semaine.numSemaine == semaine).first()
    dispo = EstDisponible.query.filter(EstDisponible.oral.date_oral >= sem.date_debut).filter(EstDisponible.oral.date_oral <= sem.date_fin).all()
    return dispo

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
    qcms=QCM.query.filter(QCM.date_fin >= sem.date_debut).filter(QCM.date_fin <= sem.date_fin).all()
    resultats=[]
    if len(liste_groupes)==0:
        for qcm in qcms:
            res_QCM=ResultatQCM.query.join(QCM).join(Eleve).join(Matiere).filter(ResultatQCM.id_qcm==qcm.id_qcm).all()
            resultats.append(res_QCM)
    else:
        semestre="S"+str(Periode.query.filter(Periode.id_periode == sem.id_periode).first().semestre)
        if semestre == "S1":
            for qcm in qcms:
                res_QCM=ResultatQCM.query.join(QCM).join(Eleve).join(Matiere).filter(ResultatQCM.id_qcm==qcm.id_qcm).filter(Eleve.groupe_s1.in_(liste_groupes)).all()
                resultats.append(res_QCM)
        else:
            for qcm in qcms:
                res_QCM=ResultatQCM.query.join(QCM).join(Eleve).join(Matiere).filter(ResultatQCM.id_qcm==qcm.id_qcm).filter(Eleve.groupe_s2.in_(liste_groupes)).all()
                resultats.append(res_QCM)
    return resultats

def get_res_sondages(semaine:int,liste_groupes=[])->list:
    """fonction recuperant les resultats de sondage pour une date

    Args:
        date (String): date du QCM
    Returns:
        list: liste des resultats de sondage
    """
    sem = Semaine.query.filter(Semaine.id_semaine == semaine).first()
    sondages=Sondage.query.filter(Sondage.date_sond >= sem.date_debut).filter(Sondage.date_sond <= sem.date_fin).all()
    resultats=[]
    if len(liste_groupes)==0:
        for sondage in sondages:
            res_sondage=RepSondage.query.join(Eleve).filter(RepSondage.id_sondage==sondage.id_sondage).all()
            resultats.append(res_sondage)
    else:
        semestre="S"+str(Periode.query.filter(Periode.id_periode == sem.id_periode).first().semestre)
        if semestre == "S1":
            for sondage in sondages:
                res_sondage=RepSondage.query.join(Eleve).filter(RepSondage.id_sondage==sondage.id_sondage).filter(Eleve.groupe_s1.in_(liste_groupes)).all()
                resultats.append(res_sondage)
        else:
            for sondage in sondages:
                res_sondage=RepSondage.query.join(Eleve).filter(RepSondage.id_sondage==sondage.id_sondage).filter(Eleve.groupe_s2.in_(liste_groupes)).all()
                resultats.append(res_sondage)
    return resultats

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
def gen_soutien(num_sem:int,seuil:float)->dict:
    """fonction generant les soutiens pour une semaine donnee

    Args:
        num_sem (int): numero de la semaine
        seuil (float): seuil de la moyenne
    Returns:
        dict: dictionnaire contenant les soutiens
    """
    #genere les soutiens pour la semaine donnee
    sem=Semaine.query.filter(Semaine.numSemaine==num_sem).first()
    qcms_trouve=False
    while not qcms_trouve:
        #cherche une semaine avec des qcms
        qcms=QCM.query.filter(QCM.date_fin >= sem.date_debut).filter(QCM.date_fin <= sem.date_fin).all()
        if len(qcms)==0:
            sem=Semaine.query.filter(Semaine.numSemaine==num_sem-1).first()
            num_sem-=1
        else:
            qcms_trouve=True
    eleves_besoin=[]
    non_retenus=[]
    retenus={}
    for qcm in qcms:
        moyenne=get_moyenne_generale(qcm.id_qcm)

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
            retenus_mat=[]
            while len(retenus_mat)<5 or len(possibles)!=0:
                retenus_mat.append(possibles.pop(0))
            retenus[qcm.matiere.nom_matiere]=retenus_mat
        non_retenus+=possibles

        eleves_besoin+=ResultatQCM.join(RepSondage,ResultatQCM.num_etu==RepSondage.num_etu)
        eleves_besoin.join(QCM,ResultatQCM.id_qcm==QCM.id_qcm).join(Matiere,QCM.id_matiere==Matiere.id_matiere)
        eleves_besoin.join(Eleve,ResultatQCM.num_etu==Eleve.num_etu)
        eleves_besoin.filter(ResultatQCM.id_qcm == qcm.id_qcm)
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

@login_manager.user_loader
def load_user(username):
    return User.query.get(username)
