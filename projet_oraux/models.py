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
    nomOral = db.Column(db.String(500))
    nbElMax = db.Column(db.Integer)
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
    participation = db.Column(db.String(500))
    idSondage = db.Column(db.Integer, db.ForeignKey("sondage.idSondage"), primary_key=True)
    numEtu = db.Column(db.Integer, db.ForeignKey("eleve.numEtu"), primary_key=True)
    dateSondage = db.Column(db.String(500))
    matiereVoulu = db.Column(db.String(500))
    commentaire = db.Column(db.String(800))

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

def get_resultats_qcm_accueil(date, groupe):
    """fonction recuperant les resultats de QCM pour une date en renvoyant les moyennes par groupe et par matiere

    Args:
        date (String): date du QCM
    """
    #on regarde dans quelle semaine on est
    sem = Semaine.query.filter(Semaine.dateDebut <= date).filter(Semaine.dateFin >= date).first()
    #on recupere les resulatats de qcm de la semaine avec le groupe
    resultat_qcm = ResultatQCM.query.filter(ResultatQCM.qcm.dateFin >= sem.dateDebut).filter(ResultatQCM.qcm.dateFin <= sem.dateFin).filter(ResultatQCM.eleve.groupeS1 == groupe).all()
    return resultat_qcm
    

def get_dispo_enseignant_accueil(semaine):
    """fonction recuperant les disponibilites des enseignants pour une date

    Args:
        date (String): date du QCM
    """
    sem = Semaine.query.filter(Semaine.numSemaine == semaine).first()
    dispo = EstDisponible.query.filter(EstDisponible.oral.dateOral >= sem.dateDebut).filter(EstDisponible.oral.dateOral <= sem.dateFin).all()
    return dispo

# def get_res_sondage_accueil(date):
#     """fonction recuperant les resultats du sondage pour une date

#     Args:
#         date (String): date du QCM
#     """
#     sem = Semaine.query.filter(Semaine.dateDebut <= date).filter(Semaine.dateFin >= date).first()
#     res = RepSondage.query.join(Matiere).join(ResultatQCM).filter(ResultatQCM.qcm.dateFin >= sem.dateDebut).filter(ResultatQCM.qcm.dateFin <= sem.dateFin).count()

def moyenne_qcm(idQCM):
    """fonction calculant la moyenne d un qcm

    Args:
        idQCM (int): id du qcm
    """
    qcm = QCM.query.filter(QCM.idQCM == idQCM).first()
    res = ResultatQCM.query.filter(ResultatQCM.idQCM == idQCM).all()
    moyenne = 0
    for r in res:
        moyenne += r.note
    moyenne = moyenne / len(res)
    return moyenne

def res_QCM(id_eleve, date):
    """fonction recuperant les resultats du QCM pour un eleve et une date

    Args:
        id_eleve (int): id de l eleve
        date (String): date du QCM
    """
    sem = Semaine.query.filter(Semaine.dateDebut <= date).filter(Semaine.dateFin >= date).first()
    res_qcm = ResultatQCM.query.filter(ResultatQCM.qcm.dateFin >= sem.dateDebut).filter(ResultatQCM.qcm.dateFin <= sem.dateFin).filter(ResultatQCM.numEtu == id_eleve).all()
    soutien = RepSondage.query.filter(RepSondage.question.dateQuestion >= sem.dateDebut).filter(RepSondage.question.dateQuestion <= sem.dateFin).filter(RepSondage.numEtu == id_eleve).all()
    return res_qcm, soutien

def get_eleve(id_eleve):
    """fonction recuperant un eleve

    Args:
        id_eleve (int): id de l eleve
    """
    eleve = Eleve.query.filter(Eleve.numEtu == id_eleve).first()
    return eleve

def get_eleve(groupe, date):
    """fonction recuperant les eleves d un groupe pour une date

    Args:
        groupe (String): groupe de l eleve
        date (String): date du QCM
    """
    
    sem = Semaine.query.filter(Semaine.dateDebut <= date).filter(Semaine.dateFin >= date).first()
    #on verifie si on est en periode 1 ou 2
    if Periode.query.filter(Periode.dateDebut <= date).filter(Periode.dateFin >= date).first().numPeriode == 1:
        eleves = Eleve.query.filter(Eleve.groupeS1 == groupe).filter(Eleve.dateDebut >= sem.dateDebut).filter(Eleve.dateDebut <= sem.dateFin).all()
    eleves = Eleve.query.filter(Eleve.groupeS2 == groupe).filter(Eleve.dateFin >= sem.dateDebut).filter(Eleve.dateFin <= sem.dateFin).all()
    return eleves

def get_eleve(soutien, date):
    """fonction recuperant les eleves qui ont besoin de soutien pour une date

    Args:
        soutien (String): "oui" ou "non" ou "~"
        date (String): date du QCM
    """
    #select eleve from Eleve NJ repSondage where repSondage.participation = "Oui" and eleve.dateDebut >= sem.dateDebut and eleve.dateDebut <= sem.dateFin
    sem = Semaine.query.filter(Semaine.dateDebut <= date).filter(Semaine.dateFin >= date).first()
    eleves = Eleve.query.join(RepSondage).join(Semaine).filter(RepSondage.participation == soutien).filter(Semaine.dateDebut >= sem.dateDebut).filter(Semaine.dateDebut <= sem.dateFin).all()
    return eleves

def res_sond(id_eleve, date):
    """fonction recuperant les resultats du sondage pour un eleve et une date

    Args:
        id_eleve (int): id de l eleve
        date (String): date du QCM
    """
    sem = Semaine.query.filter(Semaine.dateDebut <= date).filter(Semaine.dateFin >= date).first()
    res_sond = RepSondage.query.filter(RepSondage.question.dateQuestion >= sem.dateDebut).filter(RepSondage.question.dateQuestion <= sem.dateFin).filter(RepSondage.numEtu == id_eleve).all()
    return res_sond
    
def disponibilites_enseignant(id_enseignant, date):
    """fonction recuperant les disponibilites d un enseignant pour une date

    Args:
        id_enseignant (int): id de l enseignant
        date (String): date du QCM
    """
    sem = Semaine.query.filter(Semaine.dateDebut <= date).filter(Semaine.dateFin >= date).first()
    dispo = EstDisponible.query.filter(EstDisponible.oral.dateOral >= sem.dateDebut).filter(EstDisponible.oral.dateOral <= sem.dateFin).filter(EstDisponible.numEnseignant == id_enseignant).all()
    return dispo






# def get_book(id):
#     return Book.query.get(id)
# def get_books():
#     return Book.query.order_by(Book.title).all()
# def get_books_sample(nb_by_page, page):
#     return Book.query.order_by(Book.title).limit(nb_by_page).offset((page-1)*nb_by_page).all()
# def get_books_sample_filtered(nb_by_page,page,author,genre,price_min,price_max,order):
#     query = Book.query.join(Author).join(BookGenre).join(Genre)
#     if author != "":
#         query = query.filter(Author.name.like("%"+author+"%"))
#     if genre != "":
#         query = query.filter(Genre.name.like("%"+genre+"%"))
#     if price_min != "":
#         query = query.filter(Book.price>=price_min)
#     if price_max != "":
#         query = query.filter(Book.price<=price_max)
#     if order == "":
#         order = "title"
#     if order == "title":
#         query = query.order_by(Book.title)
#     elif order == "price":
#         query = query.order_by(Book.price)
#     elif order == "author":
#         query = query.order_by(Author.name)
#     elif order == "genre":
#         query = query.order_by(Genre.name)
#     return query.limit(nb_by_page).offset((page-1)*nb_by_page).all()
# def get_nb_books_filtered(nb_by_page,author,genre,price_min,price_max):
#     query = Book.query.join(Author).join(BookGenre).join(Genre)
#     if author is not None:
#         query = query.filter(Author.name.like("%"+author+"%"))
#     if genre is not None:
#         query = query.filter(Genre.name.like("%"+genre+"%"))
#     if price_min is not None:
#         query = query.filter(Book.price>=price_min)
#     if price_max is not None:
#         query = query.filter(Book.price<=price_max)
#     return int(query.count()/nb_by_page)+1
# def get_nb_pages(nb_by_page,types):
#     if types=="books":
#         return int(Book.query.count()/nb_by_page)+1
#     elif types=="authors":
#         return int(Author.query.count()/nb_by_page)+1
#     elif types=="genres":
#         return int(Genre.query.count()/nb_by_page)+1
# def get_nb_books():
#     return Book.query.count()
# def get_author(id):
#     return Author.query.get(id)
# def get_author_by_name(name):
#     return Author.query.filter_by(name=name).first()
# def get_authors():
#     return Author.query.order_by(Author.name).all()
# def get_authors_sample(nb_by_page, page):
#     #authors are ordered by name
#     return Author.query.order_by(Author.name).limit(nb_by_page).offset((page-1)*nb_by_page).all()
# def get_nb_authors():
#     return Author.query.count()
# def get_genre(id):
#     return Genre.query.get(id)
# def get_genres():
#     return Genre.query.order_by(Genre.name).all()
# def get_genres_sample(nb_by_page, page):
#     return Genre.query.order_by(Genre.name).limit(nb_by_page).offset((page-1)*nb_by_page).all()
# def get_genre_by_name(name):
#     return Genre.query.filter_by(name=name).first()
# def get_nb_genres():
#     return Genre.query.count()
# def get_book_genres(id):
#     genres=[]
#     for g in BookGenre.query.filter_by(book_id=id).all():
#         genres.append(get_genre(g.genre_id))
#     return genres
# def get_genre_books(id):
#     books=[]
#     for b in BookGenre.query.filter_by(genre_id=id).all():
#         books.append(get_book(b.book_id))
#     return books
# def get_nb_book_genres(id):
#     return BookGenre.query.filter_by(book_id=id).count()
# def add_genre_to_book(book_id, genre_id):
#     book_genre = BookGenre(id=get_nb_book_genres(book_id)+1, book_id=book_id, genre_id=genre_id)
#     db.session.add(book_genre)
#     db.session.commit()
# def remove_genre_from_book(book_id, genre_id):
#     book_genre = BookGenre.query.filter_by(book_id=book_id, genre_id=genre_id).first()
#     db.session.delete(book_genre)
#     db.session.commit()
# def supress_book_genres(book_id):
#     for book_genre in BookGenre.query.filter_by(book_id=book_id).all():
#         db.session.delete(book_genre)
#     db.session.commit()

# @login_manager.user_loader
# def load_user(username):
#     return User.query.get(username)