from datetime import timedelta
import datetime
import click

from .app import app, db
@app.cli.command()
def loaddb():
    '''Creates the tables and populates them with data. '''
    # création de toutes les tables
    db.create_all()
    db.session.commit()
@app.cli.command()
def syncdb():
    """Creates all missing tables"""
    db.create_all()
@app.cli.command ()
@click.argument("username")
@click.argument("password")
def newuser(username , password ):
    """Adds a new user. """
    from .models import User
    from hashlib import sha256
    m =sha256()
    avec_sel = password+"21rt"
    m.update(avec_sel.encode())
    passw = m.hexdigest()
    u = User(username =username , password=passw, est_admin = "F")
    db.session.add(u)
    db.session.commit()
@app.cli.command()
@click.argument("username")
@click.argument("password")
def passwd(username, password):
    """Changes the password of a user. """
    from .models import User
    from hashlib import sha256
    m = sha256()
    avec_sel = password+"21rt"
    m.update(avec_sel.encode())
    u = User.query.get(username)
    passw = m.hexdigest()
    u.password = passw
    db.session.commit()

@app.cli.command()
@click.argument("date_debut")
@click.argument("date_fin")
@click.argument("semestre")
def newperiode(date_debut, date_fin, semestre):
    """Ajoute une nouvelle période. """
    from .models import Periode
    p = Periode(date_debut=date_debut, date_fin=date_fin, semestre=semestre)
    db.session.add(p)
    db.session.commit()
    
@app.cli.command()
@click.argument("id_periode")
def initsemaines(id_periode):
    """Initialise les semaines pour une période. une date est un string au format JJ/MM/AAAA"""
    from .models import Periode, Semaine
    p = Periode.query.get(id_periode)
    date = p.date_debut
    while date.split("/")[0] != p.date_fin.split("/")[0] and date.split("/")[1] != p.date_fin.split("/")[1] and date.split("/")[2] != p.date_fin.split("/")[2]:
        id = Semaine.query.count() + 1
        s = Semaine(id_semaine=id, date_debut=date, date_fin = (datetime.strptime(date, "%d/%m/%Y") + timedelta(days=6)).strftime("%d/%m/%Y"), id_periode=id_periode)
        db.session.add(s)
        date = (datetime.strptime(date, "%d/%m/%Y") + timedelta(days=7)).strftime("%d/%m/%Y")
        db.session.commit()
        
        
@app.cli.command()
@click.argument("date_oral")
@click.argument("heure_oral")
@click.argument("id_matiere")
@click.argument("id_prof")
def neworal(date_oral, heure_oral, id_matiere, id_prof):
    """Ajoute un nouveau oral. """
    from .models import Oral
    o = Oral(date_oral=date_oral, heure_oral=heure_oral, id_matiere=id_matiere, id_prof=id_prof)
    db.session.add(o)
    db.session.commit()
    
@app.cli.command()
@click.argument("nom_prof")
@click.argument("prenom_prof")
@click.argument("email_prof")
def newprof(nom_prof, prenom_prof, email_prof):
    """Ajoute un noueau professeur. """
    from .models import Professeur
    id = Professeur.query.count() + 1
    p = Professeur(id_prof=id, nom_prof=nom_prof, prenom_prof=prenom_prof, email_prof=email_prof)
    db.session.add(p)
    db.session.commit()

def lecture_parametre_def(id_recherche):
    """Lis le fichier par_def.txt et retourne
    la valeur correspondant à l'id recherché
    Si l'id n'est pas trouvé, retourne None
    Args:
        id_recherche : id du paramètre à rechercher
    """
    fichier = open("/Bureau/SAE/projet_SAE_2022_2023_Jupilliat/projet_oraux/static/donnees/pardef.txt", "r")
    for ligne in fichier:
        if ligne[0] != "#":
            id, valeur = ligne.split(":")
            if id == id_recherche:
                fichier.close()
                return valeur.strip()
    fichier.close()
    return None

def ecriture_parametre_def(id, valeur):
    """Ecrit dans le fichier par_def.txt la valeur
    correspondant à l'id recherché
    Args:    
        id : id du paramètre à modifier
        valeur : valeur à écrire"""
    fichier = open("pardef.txt", "r")
    lignes = fichier.readlines()
    fichier.close()
    fichier = open("./par_def.txt", "w")
    for ligne in lignes:
        if ligne[0] != "#":
            id_ligne, _ = ligne.split(":")
            if id_ligne == id:
                fichier.write(id + ":" + valeur)
        else:
            fichier.write(ligne)
    fichier.close()

def ecriture_js_suivi(script_js:str):
    """Ecrit dans le fichier suivi.js le script
    Args:
        script_js : script à écrire"""
    fichier = open("projet_oraux/static/JS/suivi_graphe.js", "w")
    fichier.write(script_js)
    fichier.close()
