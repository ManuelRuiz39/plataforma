from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from plataformaSOM import app



app = Flask(__name__)
# de forma directa
# agregando la configuración en Flask
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/som'
db = SQLAlchemy(app)
db.engine.echo = True

class User(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column('id',db.Integer,primary_key=True)
    nombre = db.Column('nombre',db.String)
    apellido = db.Column('apellido',db.String)
    compania = db.Column('compania',db.String(50))
    email = db.Column('email',db.String(20))
    puesto = db.Column('puesto',db.String)
    usuario = db.Column('usuario',db.String(25))
    contra = db.Column('password',db.String(200))
    foto = db.Column('foto',db.String(200))
    fecha = db.Column('fecha',db.DateTime)
    tipo = db.Column('tipo',db.String)



    """def __init__(self,nombre,apellido,compania,email,puesto,usuario,contra,foto,fecha,tipo):
        self.id  = id
        self.nombre = nombre
        self.apellido = apellido
        self.compania = compania
        self.email = email
        self.puesto = puesto
        self.usuario = usuario
        self.contra = contra
        self.foto = foto
        self.fecha = fecha
        self.tipo = tipo"""



class Servicios(db.Model):
    __tablename__ = 'precios'
    id = db.Column('Articulo',db.String,primary_key = True)
    nombreCorto = db.Column('NombreCorto',db.String(21))

    def __init__(self,nombreCorto):
        #self.id  = id
        self.nombreCorto = nombreCorto


