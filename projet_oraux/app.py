## App permet de configurer l'application Flask

from flask import Flask
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import os.path
app = Flask(__name__)
app.config['BOOTSTRAP_SERVE_LOCAL'] = True
bootstrap = Bootstrap5(app)
def mkpath (p):
    return os.path. normpath (
        os.path.join(
            os.path. dirname ( __file__ ),
            p))

app.config['SQLALCHEMY_DATABASE_URI']=(
    'mysql+mysqlconnector://lidec:lidec@localhost/DBlidec')
db = SQLAlchemy(app)

app.config['SECRET_KEY']="020d884c-1cf8-475f-b4b5-2a56787a12c5"

login_manager = LoginManager(app)
