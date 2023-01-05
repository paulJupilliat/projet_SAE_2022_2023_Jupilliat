import click

from .app import app, db
@app.cli.command()
@click.argument('filename')
def loaddb(filename):
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
    m.update(password.encode())
    u = User(username =username , password=m.hexdigest ())
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
    m.update(password.encode())
    u = User.query.get(username)
    u.password = m.hexdigest()
    db.session.commit()

def lecture_parametre_def(id_recherche):
    """Lis le fichier par_def.txt et retourne
    la valeur correspondant à l'id recherché
    Si l'id n'est pas trouvé, retourne None
    Args:
        id_recherche : id du paramètre à rechercher
    """
    fichier = open("../static/donnees/par_def.txt", "r")
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
    fichier = open("../static/donnees/par_def.txt", "r")
    lignes = fichier.readlines()
    fichier.close()
    fichier = open("../static/donnees/par_def.txt", "w")
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