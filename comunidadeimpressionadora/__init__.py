from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
# csrf_token
app.config['SECRET_KEY'] = 'ba803396da27d250f78029201b019681'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:ROOT@localhost/comunidade'

bcrypt = Bcrypt(app)
database = SQLAlchemy(app)

from comunidadeimpressionadora import routes