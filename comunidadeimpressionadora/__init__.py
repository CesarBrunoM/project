from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
# csrf_token
app.config['SECRET_KEY'] = 'ba803396da27d250f78029201b019681'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:ROOT@localhost/comunidade'

bcrypt = Bcrypt(app)
database = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message = 'Necessário esta logado para acessar a pagina.'
login_manager.login_message_category = 'alert-info'

from comunidadeimpressionadora import routes
