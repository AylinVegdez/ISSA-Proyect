from flask import render_template, request, redirect, url_for, g

import src
#definir el Blueprint

from . import inicio, agregarprofesor, agregaralumno, asignargrupo, asignarmateria
from . import admingrupo
from . import adminalumno
from . import adminmateria
from . import adminprofesor
from . import admincalificacion
from ..Globales import Globales
from ..models import Profesor, Alumno, Materia, Grupo
from ..extensiones import db



#crear los endpoints
#ruta http://127.0.0.1:5000/productos/
@inicio.route('/paginaprincipal/<usu>')
def inicioprincipal(usu):
    print(usu, "admiiiiiiiiiiin")

    return render_template('/admin/adminMenuP.html', usuario=usu)




@adminprofesor.route('/profesores')
def inicio_profesores():
    print(g.usuario, "de profesores")
    profesores = db.session.query(Profesor.cveprof, Profesor.prof_nombre).all()
    if (request.args.get('idProfe') != None):
        profesor = Profesor()
        profesor.eliminar_profesor(request.args.get("idProfe"))
        profesores = db.session.query(Profesor.cveprof, Profesor.prof_nombre).all()


    if (request.args.get('idProfeActualizar') != None):
        profesor = Profesor()
        prof =profesor.consultar_profesor(request.args.get("idProfeActualizar"))
       # profesores = db.session.query(Profesor.cveprof, Profesor.prof_nombre).all()
        print(prof)

        idActualizar = request.args.get('idProfeActualizar')

        json_prof = {
            "nombre": prof["prof_nombre"],
            "sexo": prof["sexo"],
            "usuario": prof["nombre_usuario"],

        }

        json_botones= {
            "texto": "ACTUALIZAR PROFESOR",
            "boton": 'Actualizar Profesor'
        }

        #return json_prof
        return render_template('/admin/agregarprofesor.html', profesores = json_prof, botones = json_botones, bandera = False, id = idActualizar)
        #return redirect(url_for('agregarprofesor.agregar_profesor'))

    return render_template('/admin/adminProfesores.html', profesores=profesores)

@admingrupo.route('/grupos')
def inicio_grupos():


    grupos = db.session.query(Grupo.grado, Grupo.nombre,Grupo.grupo).all()

    return render_template('/admin/adminGrupos.html', grupos = grupos)



@admincalificacion.route('/calificaciones')
def inicio_calificaciones():
    return render_template('/admin/adminCalificaciones.html')


@adminmateria.route('/materias')
def inicio_materias():
    materias = db.session.query(Materia.cve_materia, Materia.nombre_materia).all()

    if (request.args.get('cve_materia') != None):
        print("entro al request de eliminar")
        materia = Materia()
        materia.eliminar_materia(request.args.get("cve_materia"))
        materias = db.session.query(Materia.cve_materia, Materia.nombre_materia).all()
        return render_template('/admin/adminMaterias.html', materias=materias)

    if (request.args.get('cvemateriaactualizar') != None):
        materia = Materia()
        mat = materia.consultar_materia(request.args.get("cvemateriaactualizar"))
        # profesores = db.session.query(Profesor.cveprof, Profesor.prof_nombre).all()
        print(mat)

        idActualizar = request.args.get('cvemateriaactualizar')

        json_materia = {
            "nombre_materia": mat["nombre_materia"],
            "clave_materia": idActualizar

        }

        json_botones = {
            "texto": "ACTUALIZAR PROFESOR",
            "boton": 'Actualizar Profesor'
        }

        # return json_prof
        return render_template('/admin/asignarMaterias.html', materias=json_materia, botones=json_botones, bandera=True,
                               id=idActualizar)
        # return redirect(url_for('agregarprofesor.agregar_profesor'))

    return render_template('/admin/adminMaterias.html', materias=materias)

@adminalumno.route('/alumnos')
def inicio_alumnos():
    alumnos = db.session.query(Alumno.cve_alum, Alumno.alum_nombre, Alumno.alum_apellidop, Alumno.alum_apellidom,Alumno.cvegrupo).all()
    for alum in alumnos:
       print(alum["cve_alum"])

    return render_template('/admin/adminAlumos.html', alumnos=alumnos)


@agregarprofesor.route('/agregar_profesor')
def agregar_profesor():
    json_botones = {
        "texto": "ACTUALIZAR PROFESOR",
        "boton": 'Actualizar Profesor'
    }

    return render_template('/admin/agregarprofesor.html', botones = json_botones, bandera = True)




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

@agregarprofesor.route('/profesor_actualizado', methods=['POST'])
def profesor_actualizado():

    print(id)
    if request.method == 'POST':
        if request.form["Sexo"] == "Hombre":
           sexo = 'H'
        else:
           sexo = 'M'
        json_profesor = {
            "nombre": request.form["nombre"] +" "+request.form["apellidop"]+" "+request.form["apellidom"],
            "sexo": sexo,
            "nombre_usuario": request.form["usuario"],
            "clave": request.form["contrasena"],

        }
        profesor = Profesor()
        print(json_profesor)
        print(idActualizar)
        profesor.actualizar_profesor(json_profesor, request.form["id"])
        return redirect(url_for('agregarprofesor.agregar_profesor'))
    else:
        return 'no holis'

@agregaralumno.route('/agregar_alumno')
def agregar_alumno():
    return render_template('/admin/agregarAlumno.html')

@agregaralumno.route('/alumno_agregado', methods=['POST'])
def alumno_agregado():
    if request.method == 'POST':
        if request.form["Sexo"] == "Hombre":
           sexo = 'H'
        else:
           sexo = 'M'
        json_alumno = {
            "curp": request.form["curp"],
            "edad": request.form["edad"],
            "nombre": request.form["nameAlumno"],
            "p":request.form["apellidoP"],
            "m":request.form["apellidoM"],
            "sexo": sexo,
            "cvegp": request.form["grado"]
        }
        alumno = Alumno()
        print(json_alumno)
        alumno.registrar_alumno(json_alumno)
        return redirect(url_for("agregaralumno.agregar_alumno"))#url_for('agregaralumno.alumno_agregado')
    else:
        return 'no holis'

@asignarmateria.route('/asignar_materia')
def asigar_materia():
    return render_template('/admin/asignarMaterias.html')


@asignarmateria.route('/materia_agregado', methods=['POST'])
def materia_agregado():
    if request.method == 'POST':

        json_materia = {
            "nombremateria": request.form["Materia"]
        }
        materia = Materia()
        print(json_materia)
        materia.registrar_materia(json_materia)
        return redirect(url_for('adminmateria.inicio_materias'))
    else:
        return 'no holis'

@asignargrupo.route('/asignar_grupo')
def asigar_grupo():
    return render_template('/admin/asignarGrupo.html')


@asignargrupo.route('/grupo_agregado', methods=['POST'])
def grupo_agregado():
    if request.method == 'POST':

        # cve = db.session.query(Profesor.cveprof).all()
        # nom = db.session.query(Profesor.prof_nombre).all()

        nom_prof = request.form["nameProf"]
        cveprof = 1

        if nom_prof != None:
            name = nom_prof

        cveprof = db.session.query(Profesor.cveprof).filter(Profesor.prof_nombre == nom_prof).first()

        json_grupo = {
            "nameProf": cveprof[0],
            "grado": request.form["grado"],
            "grupo": request.form["grupo"],
            "name": name
        }
        grupo = Grupo()
        print(cveprof)
        grupo.registrar_grupo(json_grupo)
        return redirect(url_for('admingrupo.inicio_grupos'))

    else:
        return 'no holis'
