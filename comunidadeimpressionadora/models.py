from comunidadeimpressionadora import database
from datetime import datetime

class Usuarios(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String(100), nullable=False)
    email = database.Column(database.String(200), nullable=False, unique=True)
    senha = database.Column(database.String(300), nullable=False)
    foto_perfil = database.Column(database.String(200), default='default.jpg')
    cursos = database.Column(database.String(300), nullable=False, default='Não informado')
    #post = database.relationship('Post', backref='autor', lazy=True)

class Post(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    titulo = database.Column(database.String(100), nullable=False)
    corpo = database.Column(database.Text(500), nullable=False)
    data_criacao = database.Column(database.DateTime, nullable=False, default=datetime.utcnow())
    id_usuario = database.Column(database.Integer, database.ForeignKey('usuarios.id'), nullable=False)