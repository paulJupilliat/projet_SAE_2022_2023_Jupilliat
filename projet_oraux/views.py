##views permet de definir les routes de l app donc des differents pages

from .app import app
from flask import render_template, request,url_for , redirect
from .models import *
from .commands import ecriture_js_suivi
from flask_wtf import FlaskForm
from wtforms import StringField , HiddenField,PasswordField
# from wtforms.validators import DataRequired
# from hashlib import sha256
# from flask_login import login_user , current_user,logout_user

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

# class LoginForm ( FlaskForm ):
#     username = StringField("Username")
#     password = PasswordField("Password")
#     next = HiddenField()
#     id = HiddenField()
#     def get_authenticated_user(self):
#         user = User.query.get(self.username.data)
#         if user is None:
#             return None
#         m = sha256()
#         m.update(self.password.data.encode())
#         passwd = m.hexdigest()
#         return user if passwd == user.password else None

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
    semaines=[37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
    groupes=["11A","11B","11C","12A","12B","12C"]
    matieres=["Python","Java","C++"]
    res_bandeau=[("Python", 12), ("Java", 15), ("C++", 18)]
    # el=Eleve(num_etu=1, nom="Dupont", prenom="Jean", groupe_s1="11A", groupe_s2="11A")
    # s=Sondage(id_sondage=1, date_sond="2020-10-10")
    # reps=RepSondage(num_etu=1, id_sondage=1, matiere_voulue="Python", volontaire="oui")
    reps={"matiere_voulue":"Python", "volontaire":"oui"}
    el={"num_etu":1, "nom":"Dupont", "prenom":"Jean", "groupe_s1":"11A", "groupe_s2":"11A"}
    resultats=[[el,el["groupe_s2"],[18,17,12],reps],[el,el["groupe_s2"],[18,17,12],reps],
    [el,el["groupe_s2"],[18,17,12],reps],[ el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps],
    [el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps],
    [el,el["groupe_s2"],[18,17,12],reps],[ el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps],
    [el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps],
    [el,el["groupe_s2"],[18,17,12],reps],[ el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps],
    [el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps],
    [el,el["groupe_s2"],[18,17,12],reps],[ el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps],
    [el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps],
    [el,el["groupe_s2"],[18,17,12],reps],[ el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps],
    [el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps],
    [el,el["groupe_s2"],[18,17,12],reps],[ el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps],
    [el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps],
    [el,el["groupe_s2"],[18,17,12],reps],[ el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps],
    [el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps],
    [el,el["groupe_s2"],[18,17,12],reps],[ el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps],
    [el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps],
    [el,el["groupe_s2"],[18,17,12],reps],[ el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps],
    [el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps],
    [el,el["groupe_s2"],[18,17,12],reps],[ el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps],
    [el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps],
    [el,el["groupe_s2"],[18,17,12],reps],[ el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps],
    [el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps],
    [el,el["groupe_s2"],[18,17,12],reps],[ el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps],
    [el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps],
    [el,el["groupe_s2"],[18,17,12],reps],[ el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps],
    [el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps],
    [el,el["groupe_s2"],[18,17,12],reps],[ el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps],
    [el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps],
    [el,el["groupe_s2"],[18,17,12],reps],[ el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps],
    [el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps],
    [el,el["groupe_s2"],[18,17,12],reps],[ el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps],
    [el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps],
    [el,el["groupe_s2"],[18,17,12],reps],[ el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps],
    [el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps],
    [el,el["groupe_s2"],[18,17,12],reps],[ el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps],
    [el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps],
    [el,el["groupe_s2"],[18,17,12],reps],[ el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps],
    [el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps],
    [el,el["groupe_s2"],[18,17,12],reps],[ el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps],
    [el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps],
    [el,el["groupe_s2"],[18,17,12],reps],[ el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps],
    [el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps],
    [el,el["groupe_s2"],[18,17,12],reps],[ el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps],
    [el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps],
    [el,el["groupe_s2"],[18,17,12],reps],[ el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps],
    [el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps],
    [el,el["groupe_s2"],[18,17,12],reps],[ el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps],
    [el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps],
    [el,el["groupe_s2"],[18,17,12],reps],[ el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps],
    [el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps],
    [el,el["groupe_s2"],[18,17,12],reps],[ el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps],
    [el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps],
    [el,el["groupe_s2"],[18,17,12],reps],[ el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps],
    [el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps],
    [el,el["groupe_s2"],[18,17,12],reps],[ el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps],
    [el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps],
    [el,el["groupe_s2"],[18,17,12],reps],[ el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps],
    [el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps],
    [el,el["groupe_s2"],[18,17,12],reps],[ el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps],
    [el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps],
    [el,el["groupe_s2"],[18,17,12],reps],[ el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps],
    [el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps],
    [el,el["groupe_s2"],[18,17,12],reps],[ el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps],
    [el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps],
    [el,el["groupe_s2"],[18,17,12],reps],[ el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps],
    [el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps],
    [el,el["groupe_s2"],[18,17,12],reps],[ el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps],
    [el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps],
    [el,el["groupe_s2"],[18,17,12],reps],[ el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps],
    [el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps],
    [el,el["groupe_s2"],[18,17,12],reps],[ el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps],
    [el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps], [el,el["groupe_s2"],[18,17,12],reps]]
    return render_template("ResQCM.html",title="Resultat QCM", admin=True,
    semaines=semaines,matieres=matieres, groupes=groupes,res_bandeau=res_bandeau, resultats=resultats)

@app.route("/Acceuil")
def Acceuil():
    #moyennes["generale"][nom_matiere]=get_moyenne_generale(qcm.id_qcm)
    qcms= {"generale":{"Python": 12, "Java": 15, "C++": 18},
    "11A":{"Python": 12, "Java": 15, "C++": 18},
    "12A":{"Python": 12, "Java": 15, "C++": 18},
    "11B":{"Python": 12, "Java": 15, "C++": 18},
    "12B":{"Python": 12, "Java": 15, "C++": 18},
    "11C":{"Python": 12, "Java": 15, "C++": 18},
    "12C":{"Python": 12, "Java": 15, "C++": 18}}
    #matieres_demandées[r.matiere_voulue]={"nb":1,"Moyenne":None}
    sondage = {"Python": { "nb": 10, "Moyenne": 15}, "BDD": { "nb": 8, "Moyenne": 11}, "Java": { "nb": 4, "Moyenne": 13}}
    matieres=["Python","Java","C++"]
    possibles={"Chabin":["BDD","Java","Reseau"],"Adobet":["IHM","Java","BDD"],"Arsouze":["Web","Python","Dev Efficace"]}
    semaines=[37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
    return render_template(
        "Acceuil.html",title="Acceuil", admin=False,qcm=qcms, matieres_demandées=sondage,
        matieres=matieres, possibles=possibles,semaines=semaines)

@app.route("/connexionAdm")
def connexionAdm():
    return render_template("connexionAdm.html",title="Connexion Administrateur",admin = False)
@app.route("/connexionProf")
def connexionProf():
    return render_template("connexionProf.html",title="Connexion Professeur",admin = False)
@app.route("/Dispo")
def Dispo():
    return render_template("Dispo.html",title="Disponibilité", admin=False)

@app.route("/GererSesDispo")
def GererSesDispo():
    return render_template("GererSesDispo.html", title="Gerer ses disponibilitées", admin = True)

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
    liste_matieres=["Python","Java","C++","BDD","Reseau","IHM","Web"]
    liste_modif=[]
    cpt=0
    while len(liste_matieres)<0:
        if cpt %2 ==0:
            mat={"id_matiere":cpt,"nom_matiere":liste_matieres[cpt]}
            liste_modif.append(mat)
        else:
            mat={"id_matiere":cpt,"nom_matiere":liste_matieres[cpt]}
            liste_modif[-1].append(mat)
        cpt+=1
    semaines=[37,38,39,40,41,42,43,44,45,46,47,48]
    #cree une liste de 3 qcms avec les resultats
    qcms=[]
    for i in range(len(liste_matieres)):
        mat={"id_matiere":i,"nom_matiere":liste_matieres[i]}
        res ={ "num_etu": 22107932, "note": 15}
        qcm={"id_qcm":i,"id_mat":mat["id_matiere"],"nom_matiere":mat["nom_matiere"],"note_qcm":res["note"]}
        qcms.append(qcm)
    soutien={"id_sondage":1,"num_etu":22107932,"matiere_voulue":"Python","volontaire":"oui","commentaire":"Je veux du soutien"}
    questions=None
    oraux =[]
    for i in range(len(semaines)):
        if i%3!=0:
            oral={"id_oral":i,"id_matiere":i%len(liste_matieres),"date_oral":"2020-10-10",
            "heure_oral":"10:00","num_etu":22107932,"commentaire":liste_matieres[i%len(liste_matieres)]+" oral "}
            oraux.append((oral,i))
        else:
            oraux.append((None,i))
    str_js="google.charts.load('current', {'packages':['line']});\n"
    str_js+="google.charts.setOnLoadCallback(drawChart);\n"
    str_js+="function drawChart() {\n"
    str_js+="\tvar data = new google.visualization.DataTable();\n"
    str_js+="\tdata.addColumn('number', 'Day');\n"
    str_js+="\tdata.addColumn('number', 'Guardians of the Galaxy');\n"
    str_js+="\tdata.addColumn('number', 'The Avengers');\n"
    str_js+="\tdata.addColumn('number', 'Transformers: Age of Extinction');\n"
    str_js+="\tdata.addRows([\n"
    str_js+="\t\t[1,37.8,80.8,41.8],\n"
    str_js+="\t\t[2,30.9,69.5,32.4],\n"
    str_js+="\t\t[3,25.4,57,25.7],\n"
    str_js+="\t\t[4,11.7,18.8,10.5],\n"
    str_js+="\t\t[5,11.9,17.6,10.4],\n"
    str_js+="\t\t[6,8.8,13.6,7.7],\n"
    str_js+="\t\t[7,7.6,12.3,9.6],\n"
    str_js+="\t\t[8,12.3,29.2,10.6],\n"
    str_js+="\t\t[9,16.9,42.9,14.8],\n"
    str_js+="\t\t[10,12.8,30.9,11.6],\n"
    str_js+="\t\t[11,5.3,7.9,4.7],\n"
    str_js+="\t\t[12,6.6,8.4,5.2]\n"
    str_js+="\t]);\n"
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
    ecriture_js_suivi(str_js)
    return render_template("Suivie_etu.html",title="Suivie étudiant",
        admin=True,matieres=liste_modif,qcms=qcms,
        soutien=soutien,questions=questions,oraux=oraux,
        semaines=semaines)

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

