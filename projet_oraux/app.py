## App permet de configurer l'application Flask

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os.path

app = Flask(__name__)
app.config['SECRET_KEY']='41001fb5-a88c-4779-ac84-0baf15daffdc'
app.config['BOOTSTRAP_SERVE_LOCAL'] = True
bootstrap = Bootstrap(app)
def mkpath (p):
    return os.path. normpath (
        os.path.join(
            os.path. dirname ( __file__ ),
            p))
app.config['SQLALCHEMY_DATABASE_URI']=(
    'mysql+mysqlconnector://mathys:'+
        'mathys@localhost/Poney?charset=utf8mb4')
db = SQLAlchemy(app)

login_manager = LoginManager(app)
