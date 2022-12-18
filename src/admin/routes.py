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
@inicio.route('/paginaprincipal')
def inicioprincipal():

    return render_template('/admin/adminMenuP.html')




@adminprofesor.route('/profesores')
def inicio_profesores():
    profesores = db.session.query(Profesor.cveprof, Profesor.prof_nombre).all()
    grupos = db.session.query(Grupo.cvegrupo, Grupo.grado,Grupo.grupo, Grupo.cveprof).all()


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

    return render_template('/admin/adminProfesores.html', profesores=profesores, grupos = grupos)
@admingrupo.route('/grupos')
def inicio_grupos():


    grupos = db.session.query(Grupo.cvegrupo, Grupo.grado, Grupo.nombre,Grupo.grupo).all()

    return render_template('/admin/adminGrupos.html', grupos = grupos)



@admincalificacion.route('/calificaciones')
def inicio_calificaciones():
    return render_template('/admin/adminCalificaciones.html')


@adminmateria.route('/materias')
def inicio_materias():
    materias = db.session.query(Materia.cve_materia, Materia.nombre_materia, Materia.grado).all()

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
    alumnos = db.session.query(Alumno.cve_alum, Alumno.alum_nombre,
                               Alumno.alum_apellidop, Alumno.alum_apellidom, Alumno.cvegrupo).filter(Alumno.alum_estado==0).all()

    print('Id eliminar')
    print(request.args.get('idAlumnoEliminar'))
    if (request.args.get('idAlumnoEliminar') != None):
        alumno = Alumno()
        alumno.eliminar_alumno(request.args.get("idAlumnoEliminar"))
        alumnos = db.session.query(Alumno.cve_alum, Alumno.alum_nombre,
                               Alumno.alum_apellidop, Alumno.alum_apellidom, Alumno.cvegrupo).filter(Alumno.alum_estado==0).all()


    print(request.args.get('idAlumnoActualizar'))
    if (request.args.get('idAlumnoActualizar') != None):

        alumno = Alumno()
        alum = alumno.consultar_alumno(request.args.get("idAlumnoActualizar"))
        # profesores = db.session.query(Profesor.cveprof, Profesor.prof_nombre).all()
        print(alum)
        print("Entro al actualizar")
        idActualizar = request.args.get('idAlumnoActualizar')
        cvegrupo = list(db.session.query(Grupo.cvegrupo).all())
        gg = db.session.query(Grupo.grado, Grupo.grupo, Grupo.cvegrupo)
        json_alum = {
            "clave": idActualizar,
            "curp": alum["alum_curp"],
            "edad": alum["alum_edad"],
            "nameAlumno": alum["alum_nombre"],
            "apellidoP": alum["alum_apellidop"],
            "apellidoM": alum["alum_apellidom"],
            "sexo": alum["alum_sexo"],
            "grupo": alum["cvegrupo"]
        }

        json_botones = {
            "texto": "ACTUALIZAR PROFESOR",
            "boton": 'Actualizar Profesor'
        }

        # return json_prof
        return render_template('/admin/agregarAlumno.html', alumnos=json_alum, botones=json_botones, bandera=False, id=idActualizar, grupos=cvegrupo, gg=gg)

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

        profesor.actualizar_profesor(json_profesor, request.form["id"])
        return redirect(url_for('agregarprofesor.agregar_profesor'))
    else:
        return 'no holis'


@agregaralumno.route('/agregar_alumno', methods=['GET', 'POST'])
def agregar_alumno():
    cvegrupo = list(db.session.query(Grupo.cvegrupo).all())
    gg = db.session.query(Grupo.grado, Grupo.grupo, Grupo.cvegrupo)
    return render_template('/admin/agregarAlumno.html', grupos=cvegrupo, gg=gg, bandera=True)


@agregaralumno.route('/alumno_agregado', methods=['GET', 'POST'])
def alumno_agregado():
    print('Entro al alumno agregado')
    if request.method == 'POST':
        if request.form["Sexo"] == "Hombre":
            sexo = 'H'
        else:
            sexo = 'M'
        json_alumno = {
            "curp": request.form["curp"],
            "edad": request.form["edad"],
            "nombre": request.form["nameAlumno"],
            "p": request.form["apellidoP"],
            "m": request.form["apellidoM"],
            "sexo": sexo,
            "cvegp": request.form["grado"]
        }
        alumno = Alumno()
        print(json_alumno)
        alumno.registrar_alumno(json_alumno)
        # url_for('agregaralumno.alumno_agregado')
        return redirect(url_for("adminalumno.inicio_alumnos"))
    else:
        return 'no holis'


@agregaralumno.route('/alumno_actualizado', methods=['POST'])
def alumno_actualizado():
    print(id)
    if request.method == 'POST':
        if request.form["Sexo"] == "Hombre":
            sexo = 'H'
        else:
            sexo = 'M'
        json_alumno = {

            "curp": request.form["curp"],
            "edad": request.form["edad"],
            "nombre": request.form["nameAlumno"],
            "p": request.form["apellidoP"],
            "m": request.form["apellidoM"],
            "sexo": sexo,
            "cvegp": request.form["grado"]
        }
        alumno = Alumno()
        print(json_alumno)
        alumno.actualizar_alumno(json_alumno, request.form["id"])
        # url_for('agregaralumno.alumno_agregado')
        return redirect(url_for("adminalumno.inicio_alumnos"))

    else:
        return 'no holis'

@asignarmateria.route('/asignar_materia')
def asigar_materia():
    return render_template('/admin/asignarMaterias.html')


@asignarmateria.route('/materia_agregado', methods=['POST'])
def materia_agregado():
    if request.method == 'POST':

        json_materia = {
            "nombremateria": request.form["Materia"],
            "grado": request.form["grado"]
        }
        materia = Materia()
        print(json_materia)
        materia.registrar_materia(json_materia)
        return redirect(url_for('adminmateria.inicio_materias'))
    else:
        return 'no holis'

@asignargrupo.route('/asignar_grupo', methods=['GET', 'POST'])
def asigar_grupo():
    #profesores = os.listdir(Profesor.prof_nombre)
    profesores = list(db.session.query(Profesor.prof_nombre, Profesor.habilitado).all())
    habilitado = db.session.query(Profesor.habilitado).all()
    print(habilitado)
    print(type(profesores))
    return render_template('/admin/asignarGrupo.html', profesores=profesores, habilitados = habilitado)


@asignargrupo.route('/grupo_agregado', methods=['POST'])
def grupo_agregado():
    if request.method == 'POST':

        # cve = db.session.query(Profesor.cveprof).all()
        # nom = db.session.query(Profesor.prof_nombre).all()

        nom_prof = request.form["nameProf"]
        print(nom_prof + "--->")
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

        json_hab = {
            "habilitado": "0"
        }
        prof = Profesor()
        prof.habilitar_profesor(json_hab, cveprof[0])

        grupo.registrar_grupo(json_grupo)
        return redirect(url_for('admingrupo.inicio_grupos'))

    else:
        return 'no holis'