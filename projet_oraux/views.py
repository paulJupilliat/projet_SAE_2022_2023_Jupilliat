##views permet de definir les routes de l app donc des differents pages

from .app import app
from flask import render_template, request,url_for , redirect
from .models import *
from flask_wtf import FlaskForm
from wtforms import StringField , HiddenField,PasswordField
# from wtforms.validators import DataRequired
from hashlib import sha256
from flask_login import login_user , current_user,logout_user

# class AuthorForm(FlaskForm):
#     id = HiddenField("id")
#     name = StringField("Name",validators=[DataRequired()])
# class BookForm(FlaskForm):
#     id = HiddenField("id")
#     title = StringField("Title",validators=[DataRequired()])
#     price = StringField("Price",validators=[DataRequired()])
#     url = StringField("Url",validators=[DataRequired()])
#     img = StringField("Picture(link)",validators=[DataRequired()])
#     #champ pour le choix de l auteur liste déroulante
#     author = StringField("Author",validators=[DataRequired()])
#     genres = StringField("Genres(separated by comma)",validators=[DataRequired()])
# class GenreForm(FlaskForm):
#     id = HiddenField("id")
#     name = StringField("Name",validators=[DataRequired()])
# class FiltersForm(FlaskForm):
#     author = StringField("Author")
#     genre = StringField("Genre")
#     price_min = StringField("Price min")
#     price_max = StringField("Price max")
#     order = StringField("Order(by title, author, genre, price)")

class LoginForm ( FlaskForm ):
    username = StringField("Username")
    password = PasswordField("Password")
    
    def get_authenticated_user(self):
        # user = User.query.get(self.username.data)
        user = None
        if self.username.data == "celine":
            m = sha256()
            user = {"password" : m.update("01234")}
        if user is None:
            return None
        m = sha256()
        m.update(self.password.data.encode())
        passwd = m.hexdigest()
        return user if passwd == user.password else None

# class RegisterForm ( FlaskForm ):
#     username = StringField("Username")
#     password = PasswordField("Password")
#     confirm = PasswordField("Confirm password")

# class EditUserForm ( FlaskForm ):
#     username = StringField("Actual username")
#     password = PasswordField("Actual password")
#     newpsswd = PasswordField("New password")
#     confirm = PasswordField("Confirm new password")


@app.route("/")
def route():
    return render_template("index.html",title="Projet soutien", admin=True)

@app.route("/ResQCM")
def ResQCM():
    return render_template("ResQCM.html",title="Resultat QCM", admin=True)

@app.route("/Acceuil")
def Acceuil():
    return render_template("Acceuil.html",title="Acceuil", admin=False)

@app.route("/connexionAdm")
def connexionAdm():
    return render_template("connexionAdm.html",title="Connexion Administrateur")

@app.route("/connexionProf")
def connexionProf():
    return render_template("connexionProf.html",title="Connexion Professeur")

@app.route("/Dispo")
def Dispo():
    return render_template("Dispo.html",title="Disponibilité", admin=False)

@app.route("/paramAdm")
def paramAdm():
    return render_template("paramAdm.html",title="Paramètres Administrateur")

@app.route("/save/paramAdm",methods=("POST",))
def save_paramAdm():
    return render_template("paramAdm.html",title="Paramètres Administrateur")

@app.route("/paramEns")
def paramEns():
    return render_template("paramEns.html",title="Paramètres Enseignant")

@app.route("/save/paramEns",methods=("POST",))
def save_paramEns():
    return render_template("paramEns.html",title="Paramètres Enseignant")
@app.route("/res_sond")
def res_sond():
    return render_template("res_sond.html",title="Resultat sondage", admin=True)

@app.route("/Soutien")
def Soutien():
    return render_template("Soutien.html",title="Soutien", admin=True)

@app.route("/Suivie_etu")
def Suivie_etu():
    return render_template("Suivie_etu.html",title="Suivie étudiant", admin=True)

@app.route("/SuivieGenEtu")
def SuivieGenEtu():
    return render_template("SuiviGenEtu.html",title="Suivie général étudiant", admin=True)

@app.route("/search/",methods=("POST",))
def search():
    search = request.form.get("recherche")
    search = search.lower()
    eleve = Eleve.query.filter(Eleve.nom.lower().like("%"+search+"%")).all()
    prof = Professeur.query.filter(Professeur.nom.lower().like("%"+search+"%")).all()
    return render_template("SuivieGenEtu.html",title="Recherche", eleve=eleve, prof=prof)


@app.route("/Connexion/<origin>", methods = ("POST",))
def Connexion(origin):
    f = LoginForm()
    if f.validate_on_submit():
        user = f.get_authenticated_user()
        if user:
            login_user(user)
            return redirect(url_for("Acceuil"))
    if origin == "Admin":
        return redirect(url_for("connexionAdm"))
    else:
        return redirect(url_for("connexionProf"))

