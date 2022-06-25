from .import db  

from flask_login import UserMixin

from sqlalchemy.sql import func

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150))
    nome_mercado = db.Column(db.String(150))
    password = db.Column(db.String(150))
    password = db.Column(db.String(150))
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())

class Estabelecimentos(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150))
    items = db.relationship('Items')

class Endereco(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    id_Estabelecimento = db.Column(db.Integer, primary_key=True)
    estado = db.Column(db.String(150))
    cidade = db.Column(db.String(150))
    endereco = db.Column(db.String(150))
    numero = db.Column(db.String(150))

class contato(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    id_Estabelecimento = db.Column(db.Integer, primary_key=True)
    ddd = db.Column(db.String(150))
    telefone = db.Column(db.String(150))
    email = db.Column(db.String(150))

class Items(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    #nome_comercio = db.Column(db.String(150))
    tipo_item = db.Column(db.String(150))
    nome_item = db.Column(db.String(150))
    marca_item = db.Column(db.String(150))
    volume_tipo = db.Column(db.String(150))
    volume = db.Column(db.String(150))
    qtd_maxima = db.Column(db.String(150))
    valor = db.Column(db.String(150))
    data_fim_promocao = db.Column(db.String(150))
    foto = db.Column(db.Text, nullable =False)
    estabelecimento_id = db.Column(db.Integer, db.ForeignKey("estabelecimentos.id"))
    


class redes_sociais(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    id_Contato = db.Column(db.Integer, primary_key=True)
    facebook = db.Column(db.String(150))
    instagram = db.Column(db.String(150))
    whatsapp = db.Column(db.String(150))
    twitter = db.Column(db.String(150))