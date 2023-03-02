##views permet de definir les routes de l app donc des differents pages

import os
from .app import app
from flask import render_template, request,url_for , redirect
from .models import *
from .commands import ecriture_js_suivi
from flask_wtf import FlaskForm
from wtforms import StringField , HiddenField,PasswordField
from wtforms.validators import DataRequired
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

class LoginForm(FlaskForm):
    username = StringField("identifiant")
    password = PasswordField("password")

    def get_authenticated_user(self):
        user = User.query.get(self.username.data)
        if user is None:
            return None
        m = sha256()
        avec_sel = self.password.data+"21rt"
        m.update(avec_sel.encode())
        passwd = m.hexdigest()
        print(user.password)
        print(passwd)
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
    return render_template("index.html",title="Projet soutien")
@app.route("/ResQCM")
def ResQCM():
    semaines= get_semaines()
    groupes=["11A","11B","11C","12A","12B","12C"]
    matieres=["Python","Java","C++","Projet QCM (BUT2)"]

    res_bandeau=[("Python", 12), ("Java", 15), ("C++", 18)]
    reps={"matiere_voulue":"Python", "volontaire":"oui"}
    el={"num_etu":1, "nom":"Dupont", "prenom":"Jean", "groupe_s1":"11A", "groupe_s2":"11A"}
    resultats= get_res_QCMs(1, groupes)
    return render_template("ResQCM.html",title="Resultat QCM",
    semaines=semaines,matieres=matieres, groupes=groupes,res_bandeau=res_bandeau, resultats=resultats)

@app.route("/Acceuil")
def Acceuil():
    #moyennes["generale"][nom_matiere]=get_moyenne_generale(qcm.id_qcm)
    #matieres_demandées[r.matiere_voulue]={"nb":1,"Moyenne":None}
    sondage = get_res_sondage_accueil()
    matieres=get_matiere()
    possibles=get_possibilite_soutien()
    semaines=[{"id_semaine":1,"date_debut":"02/01/2023","date_fin":"08/01/2023"},
    {"id_semaine":2,"date_debut":"09/01/2023","date_fin":"15/01/2023"},{"id_semaine":3,"date_debut":"16/01/2023","date_fin":"22/01/2023"},
    {"id_semaine":4,"date_debut":"23/01/2023","date_fin":"29/01/2023"}, {"id_semaine":5,"date_debut":"30/01/2023","date_fin":"05/02/2023"},
    {"id_semaine":6,"date_debut":"06/02/2023","date_fin":"12/02/2023"},{"id_semaine":7,"date_debut":"13/02/2023","date_fin":"19/02/2023"},
    {"id_semaine":8,"date_debut":"20/02/2023","date_fin":"26/02/2023"},{"id_semaine":9,"date_debut":"27/02/2023","date_fin":"05/03/2023"}]
    return render_template(
        "Acceuil.html",title="Acceuil",qcm=get_resultats_qcm_accueil(), matieres_demandées=sondage,
        matieres=matieres, possibles=possibles,semaines=semaines)

@app.route("/connexionAdm")
def connexionAdm():
    return render_template("connexionAdm.html",title="Connexion Administrateur")
@app.route("/connexionProf")
def connexionProf():
    return render_template("connexionProf.html",title="Connexion Professeur")
@app.route("/Disponibilite")
def Disponibilite():
    semaines=[{"id_semaine":1,"date_debut":"02/01/2023","date_fin":"08/01/2023"},{"id_semaine":2,"date_debut":"09/01/2023","date_fin":"15/01/2023"},{"id_semaine":3,"date_debut":"16/01/2023","date_fin":"22/01/2023"},
    {"id_semaine":4,"date_debut":"23/01/2023","date_fin":"29/01/2023"}, {"id_semaine":5,"date_debut":"30/01/2023","date_fin":"05/02/2023"},
    {"id_semaine":6,"date_debut":"06/02/2023","date_fin":"12/02/2023"},{"id_semaine":7,"date_debut":"13/02/2023","date_fin":"19/02/2023"},
    {"id_semaine":8,"date_debut":"20/02/2023","date_fin":"26/02/2023"},{"id_semaine":9,"date_debut":"27/02/2023","date_fin":"05/03/2023"}]
    matieres=get_matiere()
    possibles=get_possibilite_soutien()
    dispos = disponibilites_enseignant(1)
    return render_template("Dispo.html",title="Disponibilité", semaines=semaines, dispos = dispos, matieres=matieres, possibles= possibles)

@app.route("/GererSesDispo")
def GererSesDispo():
    semaines=[{"id_semaine":1,"date_debut":"02/01/2023","date_fin":"08/01/2023"},
    {"id_semaine":2,"date_debut":"09/01/2023","date_fin":"15/01/2023"},{"id_semaine":3,"date_debut":"16/01/2023","date_fin":"22/01/2023"},
    {"id_semaine":4,"date_debut":"23/01/2023","date_fin":"29/01/2023"}, {"id_semaine":5,"date_debut":"30/01/2023","date_fin":"05/02/2023"},
    {"id_semaine":6,"date_debut":"06/02/2023","date_fin":"12/02/2023"},{"id_semaine":7,"date_debut":"13/02/2023","date_fin":"19/02/2023"},
    {"id_semaine":8,"date_debut":"20/02/2023","date_fin":"26/02/2023"},{"id_semaine":9,"date_debut":"27/02/2023","date_fin":"05/03/2023"}]
    oraux=[{"date_oral":"02/01/2023","heure_oral":"15:00","nom_matiere":"Python"},
    {"date_oral":"02/01/2023","heure_oral":"15:00","nom_matiere":"Python"}, {"date_oral":"02/01/2023","heure_oral":"15:00","nom_matiere":"Python"},
    {"date_oral":"02/01/2023","heure_oral":"15:00","nom_matiere":"Python"}, {"date_oral":"02/01/2023","heure_oral":"15:00","nom_matiere":"Python"},]
    return render_template("GererSesDispo.html", title="Gerer ses disponibilitées",semaines=semaines,oraux=oraux)

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
    semaines=[{"id_semaine":1,"date_debut":"02/01/2023","date_fin":"08/01/2023"},
    {"id_semaine":2,"date_debut":"09/01/2023","date_fin":"15/01/2023"},{"id_semaine":3,"date_debut":"16/01/2023","date_fin":"22/01/2023"},
    {"id_semaine":4,"date_debut":"23/01/2023","date_fin":"29/01/2023"}, {"id_semaine":5,"date_debut":"30/01/2023","date_fin":"05/02/2023"},
    {"id_semaine":6,"date_debut":"06/02/2023","date_fin":"12/02/2023"},{"id_semaine":7,"date_debut":"13/02/2023","date_fin":"19/02/2023"},
    {"id_semaine":8,"date_debut":"20/02/2023","date_fin":"26/02/2023"},{"id_semaine":9,"date_debut":"27/02/2023","date_fin":"05/03/2023"}]
    groupes=["11A","11B","11C","12A","12B","12C"]
    # res_eleve,groupe,res_qs in sondages
    res_eleve=get_res_sondages(1, groupes)
    groupe="11A"
    res_qs=[{"question":"Quelle matière voulez vous voir en priorité ?","reponse":"Java","id_quest":1}, {"question":"Etes vous volontaire pour aider les autres ?","reponse":"oui","id_quest":2}, {"question":"Avez vous des remarques ?","reponse":"Je suis motivé","id_quest":3}]
    sondages=[[res_eleve,groupe,res_qs],[ res_eleve,groupe,res_qs], [res_eleve,groupe,res_qs]]
    questions=[{"question":"Quelle matière voulez vous voir en priorité ?","id_quest":1}, {"question":"Etes vous volontaire pour aider les autres ?","id_quest":2}, {"question":"Avez vous des remarques ?","id_quest":3}]
    colspan=len(questions)+5
    return render_template("res_sond.html",title="Resultat sondage",groupes=groupes,sondages=sondages,questions=questions,semaines=semaines,colspan=colspan)
@app.route("/Soutien")
def Soutien():
    matieres= get_matieres()
    semaines=get_semaines()
    eleve_ret={"nom_eleve":"Paul",
               "volontaire":"oui",
               "matiere_voulue":"Python",
               "matiere_retenue":{"matiere":"Python","note":12}}
    retenus ={1:{"eleve":eleve_ret,
                 "notes_qcm":[15,12],
                 "profs":{"profs_dispos":[{"nom_prof":"Chabin"}],
                          "profs_possibles":[{"nom_prof":"Chabin"}]}},
              2:{"eleve":eleve_ret,"notes_qcm":[15,12],"profs":{"profs_dispos":[{"nom_prof":"Chabin"}],"profs_possibles":[{"nom_prof":"Chabin"}]}},
                3:{"eleve":eleve_ret,"notes_qcm":[15,12],"profs":{"profs_dispos":[{"nom_prof":"Chabin"}],"profs_possibles":[{"nom_prof":"Chabin"}]}},
                4:{"eleve":eleve_ret,"notes_qcm":[15,12],"profs":{"profs_dispos":[{"nom_prof":"Chabin"}],"profs_possibles":[{"nom_prof":"Chabin"}]}},
                5:{"eleve":eleve_ret,"notes_qcm":[15,12],"profs":{"profs_dispos":[{"nom_prof":"Chabin"}],"profs_possibles":[{"nom_prof":"Chabin"}]}}}
    eleve_non_ret={"nom_eleve":"Paul","volontaire":"~","matiere_voulue":"Python"}
    non_retenus = {1:{"eleve":eleve_non_ret,"notes_qcm":[18,16],"profs":{"profs_dispos":[{"nom_prof":"Chabin"}],"profs_possibles":[{"nom_prof":"Chabin"}]}},
                2:{"eleve":eleve_non_ret,"notes_qcm":[18,16],"profs":{"profs_dispos":[{"nom_prof":"Chabin"}],"profs_possibles":[{"nom_prof":"Chabin"}]}},
                3:{"eleve":eleve_non_ret,"notes_qcm":[18,16],"profs":{"profs_dispos":[{"nom_prof":"Chabin"}],"profs_possibles":[{"nom_prof":"Chabin"}]}}}
    eleve_bes={"nom_eleve":"Paul","volontaire":"non"}
    eleves_besoin = {1:{"eleve":eleve_bes,"notes_qcm":[17,12]}, 2:{"eleve":eleve_bes,"notes_qcm":[17,12]},
                    3:{"eleve":eleve_bes,"notes_qcm":[17,12]}}
    oraux =[{"id_oral":1,"date_oral":"02/01/2023","heure_oral":"15:00","nom_matiere":"Python"},
    {"id_oral":2,"date_oral":"02/01/2023","heure_oral":"15:00","nom_matiere":"Python"}]
    return render_template("Soutien.html",title="Soutien",matieres=matieres,semaines=semaines,retenus=retenus,non_retenus=non_retenus,eleves_besoin=eleves_besoin,oraux=oraux,num_qcm=len(matieres))
@app.route("/Suivie_etu/") #<num_etu>
def Suivie_etu():#num_etudiant
    eleve = {"prenom" : "paul", "nom":"jupilliat", "groupe_s1" : "1a5" ,"groupe_s2": "1a3"}
    # eleve = get_eleve(num_etudiant)
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
    semaines=[{"id_semaine":1,"date_debut":"02/01/2023","date_fin":"08/01/2023", "semestre" : "1"},
    {"id_semaine":2,"date_debut":"09/01/2023","date_fin":"15/01/2023"},{"id_semaine":3,"date_debut":"16/01/2023","date_fin":"22/01/2023"},
    {"id_semaine":4,"date_debut":"23/01/2023","date_fin":"29/01/2023"}, {"id_semaine":5,"date_debut":"30/01/2023","date_fin":"05/02/2023"},
    {"id_semaine":6,"date_debut":"06/02/2023","date_fin":"12/02/2023"},{"id_semaine":7,"date_debut":"13/02/2023","date_fin":"19/02/2023"},
    {"id_semaine":8,"date_debut":"20/02/2023","date_fin":"26/02/2023"},{"id_semaine":9,"date_debut":"27/02/2023","date_fin":"05/03/2023"}]
    semaine_actu = semaines[0]
    #cree une liste de 3 qcms avec les resultats
    qcms=[]
    for i in range(len(liste_matieres)):
        mat={"id_matiere":i,"nom_matiere":liste_matieres[i]}
        res ={ "num_etu": 22107932, "note": 9}
        qcm={"id_qcm":i,"id_mat": mat["id_matiere"],"nom_matiere":mat["nom_matiere"],"note_qcm":res["note"]}
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
       matieres=liste_modif,qcms=qcms,
        soutien=soutien,questions=questions,oraux=oraux,
        semaines=semaines, eleve=eleve, semaine_actu = semaine_actu)

@app.route("/SuivieGenEtu")
def SuivieGenEtu():
    eleves=[{"eleve":{"nom":"DUPONT","prenom":"Jean","num_etu":22107932,"groupe_s1":"14A","groupe_s2":"12B"},"nb_part":0,"moyenne":18,"dern_comm":""},
    {"eleve":{"nom":"DUPONT","prenom":"Jean","num_etu":22107932,"groupe_s1":"14A","groupe_s2":"12B"},"nb_part":3,"moyenne":11,"dern_comm":"Progrès considérable"},
    {"eleve":{"nom":"DUPONT","prenom":"Jean","num_etu":22107932,"groupe_s1":"14A","groupe_s2":"12B"},"nb_part":0,"moyenne":18,"dern_comm":""},
    {"eleve":{"nom":"DUPONT","prenom":"Jean","num_etu":22107932,"groupe_s1":"14A","groupe_s2":"12B"},"nb_part":4,"moyenne":8,"dern_comm":"Il reste encore du travail"},
    {"eleve":{"nom":"DUPONT","prenom":"Jean","num_etu":22107932,"groupe_s1":"14A","groupe_s2":"12B"},"nb_part":0,"moyenne":18,"dern_comm":""},
    {"eleve":{"nom":"DUPONT","prenom":"Jean","num_etu":22107932,"groupe_s1":"14A","groupe_s2":"12B"},"nb_part":1,"moyenne":14,"dern_comm":""},
    {"eleve":{"nom":"DUPONT","prenom":"Jean","num_etu":22107932,"groupe_s1":"14A","groupe_s2":"12B"},"nb_part":0,"moyenne":18,"dern_comm":""},
    {"eleve":{"nom":"DUPONT","prenom":"Jean","num_etu":22107932,"groupe_s1":"14A","groupe_s2":"12B"},"nb_part":2,"moyenne":13,"dern_comm":""},
    {"eleve":{"nom":"DUPONT","prenom":"Jean","num_etu":22107932,"groupe_s1":"14A","groupe_s2":"12B"},"nb_part":2,"moyenne":13,"dern_comm":""},
    {"eleve":{"nom":"DUPONT","prenom":"Jean","num_etu":22107932,"groupe_s1":"14A","groupe_s2":"12B"},"nb_part":7,"moyenne":5,"dern_comm":"C'est pas ouf"}]
    semaine_act={"id_sem":1,"semestre":1,"annee":2018}
    semaines=[{"id_semaine":1,"date_debut":"02/01/2023","date_fin":"08/01/2023"},
    {"id_semaine":2,"date_debut":"09/01/2023","date_fin":"15/01/2023"},{"id_semaine":3,"date_debut":"16/01/2023","date_fin":"22/01/2023"},
    {"id_semaine":4,"date_debut":"23/01/2023","date_fin":"29/01/2023"}, {"id_semaine":5,"date_debut":"30/01/2023","date_fin":"05/02/2023"},
    {"id_semaine":6,"date_debut":"06/02/2023","date_fin":"12/02/2023"},{"id_semaine":7,"date_debut":"13/02/2023","date_fin":"19/02/2023"},
    {"id_semaine":8,"date_debut":"20/02/2023","date_fin":"26/02/2023"},{"id_semaine":9,"date_debut":"27/02/2023","date_fin":"05/03/2023"}]
    groupes=["11A","11B","11C","12A","12B","12C"]
    return render_template("SuiviGenEtu.html",title="Suivi général étudiant",suivi_gen=eleves,semaine_act=semaine_act,semaines=semaines,groupes=groupes)
@app.route("/search/",methods=("POST",))
def search():
    search = request.form.get("recherche")
    search = search.lower()
    eleve = Eleve.query.filter(Eleve.nom.lower().like("%"+search+"%")).all()
    prof = Professeur.query.filter(Professeur.nom.lower().like("%"+search+"%")).all()
    return render_template("SuivieGenEtu.html",title="Recherche", eleve=eleve, prof=prof)

@app.route("/Connexion/<origin>", methods = ("POST","GET"))
def Connexion(origin):
    f = LoginForm()
    if f.validate_on_submit():
        user = f.get_authenticated_user()
        if user:
            print("ok")
            if origin == "Admin":
                if not user.get_est_admin():
                    return redirect(url_for('Connexion',origin="Prof"))
            else:
                if user.get_est_admin():
                    user.est_admin = "F"
            login_user(user)
            return redirect(url_for("Acceuil"))
    if origin == "Admin":
        return render_template("connexionAdm.html", form=f)
    else:
        return render_template("connexionProf.html", form=f)


@app.route("/supprimer_etu_soutien/<id_etu>")
def supprimer_eleve_soutien(id_etu):
    eleve = ParticipantsOral.query.filter_by(id_etu=id_etu).first()
    if eleve != None:
        db.session.delete(eleve)
        db.session.commit()
    return redirect(url_for("Soutien"))

@app.route("/ajouter_etu_oral/<id_etu>")
def ajouter_eleve_oral(id_etu):
    eleve = PossibiliteSoutien.query.filter_by(id_etu=id_etu).first()
    if eleve:
        db.session.delete(eleve)
        db.session.commit()
        # ajouter mtn l'éléve dans la table des participants
        ele = ParticipantsOral(id_etu=id_etu)
        db.session.add(ele)
        db.session.commit()
    return redirect(url_for("Soutien"))

