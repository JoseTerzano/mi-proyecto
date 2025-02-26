from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, session, redirect
import random

app = Flask(__name__)
app.config.from_pyfile('config.py')
app.secret_key = 'Clave_Secreta'

from models import Sucursal, Transporte, Repartidor, Paquete, db

@app.route('/')
def Inicio():
    return render_template('inicio.html', Sucursales=Sucursal.query.order_by(Sucursal.numero).all())

@app.route('/opciones', methods = ['POST', 'GET'])
def opciones():
        session['id'] = request.form.get('Sucursales')
        if session['id']:
            return render_template('opciones.html')
    
@app.route('/registrar_paquete', methods = ['GET', 'POST'])
def registrar_paquete():
    if session["id"]:
        ultimo_paquete = Paquete.query.order_by(Paquete.id.desc()).first()
        numeroenvio = ultimo_paquete.numeroenvio + 20
        nomdestinatario = request.form.get('nomdestinatario')
        peso = request.form.get('peso')
        dirdestinatario = request.form.get('dirdestinatario')
        idrepartidor = 0
        idtransporte = 0
        observaciones = 0
        idsucursal = session["id"]
        if not nomdestinatario and not peso and not dirdestinatario:
            return render_template('registrar_paquete.html')
        elif not nomdestinatario or not peso or not dirdestinatario:
            return render_template('aviso.html', nota = "Ups! Ocurrio un Error")
        else:
            nuevo_paquete = Paquete(numeroenvio = numeroenvio, peso = peso, nomdestinatario = nomdestinatario, dirdestinatario = dirdestinatario, entregado = 0 , observaciones = observaciones, idsucursal = idsucursal, idtransporte = idtransporte, idrepartidor = idrepartidor)
            db.session.add(nuevo_paquete)
            db.session.commit()
            return render_template('aviso.html', nota = 'Paquete Registrado Con Exito!')

@app.route('/seleccionar_transporte', methods = ['POST', 'GET'])
def seleccionar_transporte():
    numerotransporte = random.randint(220, 300)
    fechahorasalida = datetime.now()
    fechahorallegada = None
    idsucursal = request.form.get("Sucursales")
    if not idsucursal:
        return render_template('selec_destino.html', Sucursales=Sucursal.query.order_by(Sucursal.numero).all(), Paquetes = Paquete.query.filter_by(entregado=0, idrepartidor=0).all())
    elif not numerotransporte or not fechahorasalida:
        return render_template('aviso.html', nota = "Ups! Ocurrio un Error")
    else: 
        nuevo_transporte = Transporte(numerotransporte = numerotransporte, fechahorasalida = fechahorasalida, fechahorallegada = fechahorallegada, idsucursal = idsucursal)
        db.session.add(nuevo_transporte)
        db.session.commit()
        paquetes_selec = request.form.getlist('Paquetes[]')
        for idpaquete in paquetes_selec:
            paquete = Paquete.query.filter_by(id = idpaquete).first()
            paquete.entregado = 1
            db.session.commit()
        return render_template('aviso.html', nota = 'Transporte Registrado correctamente')

    
@app.route('/llegada_transporte', methods = ['POST', 'GET'])
def llegada_transporte():
    idtrans = request.form.get('Transportes')
    if session['id']:
        if idtrans:
            transporte = Transporte.query.filter_by(id=idtrans, fechahorallegada=None, idsucursal=session['id']).first()
            if transporte:
                transporte.fechahorallegada = datetime.now()
                db.session.commit()
                return render_template('aviso.html', nota='Registrado Con Exito!')
            else:
                return render_template('aviso.html', nota='Ups! Ocurrio un Error')
    transportes = Transporte.query.filter_by(fechahorallegada=None, idsucursal=session['id']).all()
    return render_template('llegada_transporte.html', Transportes=transportes)



if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True) 