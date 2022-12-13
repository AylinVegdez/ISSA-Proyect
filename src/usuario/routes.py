


from flask import render_template, request, g

from . import iniciousuario, evaluacion, informacion, lista
from ..models import Alumno
from ..extensiones import db

#definir el Blueprint



#crear los endpoints
#ruta http://127.0.0.1:5000/productos/

@iniciousuario.before_request
def before_request():
    g.usuario = "NO HA CAMBIADO NADA"

@iniciousuario.after_request
def after_request(response):
    g.usuario = g.remplazo
    print(g.usuario, "jaloooooooooo")
    return response
@iniciousuario.route('/inicialusuario/<usu>')
def iniciousuario(usu):
    print(usu, "usuario")
    print(g.usuario)
    g.remplazo = usu

    print(usu, g.usuario, g.remplazo, "inicioooooooo")

    return render_template('/usuario/Menuusuario.html', usuario=usu)


@evaluacion.route('/evaluacion')
def inicio_evaluacion():
    print(g.usuario, "evaluaciooooooooooon")
    return render_template('/usuario/evaluacionAlumno.html', usuario = g.usuario)

@informacion.route('/informacion')
def inicio_informacion():

    return render_template('/usuario/informacionAlumno.html', usuario = g.usuario)

@lista.route('/lista')
def inicio_lista():
    usuarios = db.session.query(Alumno.cve_alum, Alumno.alum_nombre, Alumno).all()
    print(usuarios)
    if (request.args.get('idUsuario') != None):
        usuario = Alumno()
        # avance boletas
        # imprimir boleta
        usuarios = db.session.query(Alumno.cve_alum, Alumno.alum_nombre).all()
    return render_template('/usuario/listaUsuario.html', usuarios=usuarios, usuario = g.usuario)

