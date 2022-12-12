from flask import render_template, request, redirect, url_for
#definir el Blueprint

from . import inicio, agregarprofesor, agregaralumno, asignargrupo, asignarmateria
from . import admingrupo
from . import adminalumno
from . import adminmateria
from . import adminprofesor
from . import admincalificacion
from ..models import Profesor
from ..extensiones import db


#crear los endpoints
#ruta http://127.0.0.1:5000/productos/
@inicio.route('/paginaprincipal')
def inicioprincipal():

    return render_template('/admin/adminMenuP.html')

@adminprofesor.route('/profesores')
def inicio_profesores():
    profesores = db.session.query(Profesor.cveprof, Profesor.prof_nombre).all()
    for prof in profesores:
        print(prof["cveprof"])

    return render_template('/admin/adminProfesores.html', profesores = profesores)

@admingrupo.route('/grupos')
def inicio_grupos():

    return render_template('/admin/adminGrupos.html')


@admincalificacion.route('/calificaciones')
def inicio_calificaciones():
    return render_template('/admin/adminCalificaciones.html')


@adminmateria.route('/materias')
def inicio_materias():
    return render_template('/admin/adminMaterias.html')

@adminalumno.route('/alumnos')
def inicio_alumnos():
    return render_template('/admin/adminAlumos.html')

@agregarprofesor.route('/agregar_profesor')
def agregar_profesor():
    return render_template('/admin/agregarprofesor.html')




@agregarprofesor.route('/profesor_agregado', methods=['POST'])
def profesor_agregado():
    if request.method == 'POST':
        if request.form["Sexo"] == "Hombre":
           sexo = 'H'
        else:
           sexo = 'M'
        json_profesor = {
            "nombre": request.form["nombre"] +" "+request.form["apellidop"]+" "+request.form["apellidom"],
            "sexo": sexo,
            "nombre_usuario": request.form["usuario"],
            "clave": request.form["contrasena"]
        }
        profesor = Profesor()
        print(json_profesor)
        profesor.registrar_profesor(json_profesor)
        return redirect(url_for('agregarprofesor.agregar_profesor'))
    else:
        return 'no holis'

@agregaralumno.route('/agregar_alumno')
def agregar_alumno():
    return render_template('/admin/agregarAlumno.html')

@asignarmateria.route('/asignar_materia')
def asigar_materia():
    return render_template('/admin/asignarMaterias.html')

@asignargrupo.route('/asignar_grupo')
def asigar_grupo():
    return render_template('/admin/asignarGrupo.html')
