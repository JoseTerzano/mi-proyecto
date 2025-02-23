from __main__ import app
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy(app)

class Sucursal(db.Model):
    _tablename_ = 'sucursal'
    id = db.Column(db.Integer, primary_key = True)
    numero = db.Column(db.Integer, unique = True, nullable = False)
    provincia = db.Column(db.String(30), nullable = False)
    localidad = db.Column(db.String(30), nullable = False)
    direccion = db.Column(db.String(60), nullable = False)
    transporte = db.relationship('Transporte', backref='sucursal', cascade="all, delete-orphan")
    repartidor = db.relationship('Repartidor', backref='sucursal', cascade="all, delete-orphan")
    paquete = db.relationship('Paquete', backref='sucursal', cascade="all, delete-orphan")

class Transporte(db.Model):
    _tablename_ = 'transporte'
    id = db.Column(db.Integer, primary_key = True)
    numerotransporte = db.Column(db.Integer, unique = True)
    fechahorasalida = db.Column(db.DateTime, nullable = False)
    fechahorallegada = db.Column(db.DateTime, default = None)
    idsucursal = db.Column(db.Integer, db.ForeignKey('sucursal.id'))
    paquete = db.relationship('Paquete', backref='transporte', cascade="all, delete-orphan")

class Repartidor(db.Model):
    _tablename_ = 'repartidor'
    id = db.Column(db.Integer, primary_key = True)
    numero = db.Column(db.Integer, unique = True, nullable = False)
    dni = db.Column(db.String(8), unique = True, nullable = False)
    idsucursal = db.Column(db.Integer, db.ForeignKey('sucursal.id'))
    paquete = db.relationship('Paquete', backref='repartidor', cascade="all, delete-orphan")


class Paquete(db.Model):
    _tablename_ = 'paquete'
    id = db.Column(db.Integer, primary_key = True)
    numeroenvio = db.Column(db.Integer, unique = True)
    peso = db.Column(db.Integer, nullable = False)
    nomdestinatario = db.Column(db.String(60), nullable = False)
    dirdestinatario = db.Column(db.String(100), nullable = False)
    entregado = db.Column(db.Boolean, default = 0)
    observaciones = db.Column(db.Text)
    idsucursal = db.Column(db.Integer, db.ForeignKey('sucursal.id'))
    idtransporte = db.Column(db.Integer, db.ForeignKey('transporte.id'))
    idrepartidor = db.Column(db.Integer, db.ForeignKey('repartidor.id'))