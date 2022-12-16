from flask import Blueprint, request
from ..extensiones import db
from ..models import calif_alumno
from ..models import prom_materia_alumno
from ..models import Promedios_Finales

#Definir blue print para cliente
calif_trim = Blueprint('calif_trim',__name__)
#Definir la ruta CLIENTES
@calif_trim.route('/api/calif_trim',methods=['GET','POST'])
def consultar_calificacion():
    calificaciones=db.session.query().all()
    print(calificaciones)
    return {'mensaje':'Consultando Profesores'}
#Definir la ruta CLIENTES
@calif_trim.route('/api/calificaciones/registrar',methods=['POST'])
def insertar_calif_trim():
    # Leer los datos enviados
    # REcibir desde un formulario request.form['nombre']
    json_calif = request.get_json()
    calif = calif_alumno()
    print(json_calif)
    obj=calif.registrar_calif(json_calif)
    
    return obj
    
    # for clave,valor in json_cliente.items():
    #     print(clave,valor)
    
    # return {'mensaje':'Insertando Cliente'}
@calif_trim.route('/api/calificaciones/promedios',methods=['POST'])
def actualizar_prom():
    # Leer los datos enviados
    # REcibir desde un formulario request.form['nombre']
    json_prom = request.get_json()
    prom = prom_materia_alumno()
    obj=prom.actualizar_promedio(json_prom)

    

    return obj
    