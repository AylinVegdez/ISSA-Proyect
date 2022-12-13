


from flask import render_template, request

from . import iniciousuario, evaluacion, informacion, lista
from ..models import Alumno
from ..extensiones import db

#definir el Blueprint



#crear los endpoints
#ruta http://127.0.0.1:5000/productos/
@iniciousuario.route('/inicialusuario')
def iniciousuario():

    return render_template('/usuario/Menuusuario.html')

@evaluacion.route('/evaluacion')
def inicio_evaluacion():

    return render_template('/usuario/evaluacionAlumno.html')

@informacion.route('/informacion')
def inicio_informacion():

    return render_template('/usuario/informacionAlumno.html')

@lista.route('/lista')
def inicio_lista():
    usuarios = db.session.query(Alumno.cve_alum, Alumno.alum_nombre, Alumno).all()
    print(usuarios)
    if (request.args.get('idUsuario') != None):
        usuario = Alumno()
        # avance boletas
        # imprimir boleta
        usuarios = db.session.query(Alumno.cve_alum, Alumno.alum_nombre).all()
    return render_template('/usuario/listaUsuario.html', usuarios=usuarios)

