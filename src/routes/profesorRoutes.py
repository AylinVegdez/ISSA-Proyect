from flask import Blueprint, request
from ..extensiones import db
from ..models import Profesor

#Definir blue print para cliente
profesor = Blueprint('profesor',__name__)
#Definir la ruta CLIENTES
@profesor.route('/api/profesores',methods=['GET','POST'])
def consultar_profesor():
    profesores=db.session.query(Profesor).all()
    print(profesores)
    return {'mensaje':'Consultando Profesores'}
#Definir la ruta CLIENTES
@profesor.route('/api/profesores/registrar',methods=['POST'])
def insertar_profesor():
    # Leer los datos enviados
    # REcibir desde un formulario request.form['nombre']
    json_profesor = request.get_json()
    profesor = Profesor()
    print(json_profesor)
    obj=profesor.registrar_profesor(json_profesor)
    return obj
    
    # for clave,valor in json_cliente.items():
    #     print(clave,valor)
    
    # return {'mensaje':'Insertando Cliente'}
@profesor.route('/api/profesores/login',methods=['POST'])
def login_profesor():
    # Leer los datos enviados
    # REcibir desde un formulario request.form['nombre']
    json_profesor = request.get_json()
    prof = Profesor()
    obj=prof.validar_cliente(json_profesor['nombre_usuario'],json_profesor['clave'])

    

    return obj
    