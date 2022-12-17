


from flask import render_template, request, g, redirect, url_for, session

from . import iniciousuario, evaluacion, informacion, lista
from ..models import Alumno, Grupo, Materia, calif_alumno
from ..extensiones import db

#definir el Blueprint



#crear los endpoints
#ruta http://127.0.0.1:5000/productos/




@iniciousuario.route('/inicialusuario')
def iniciousuario():

    return render_template('/usuario/Menuusuario.html')



@evaluacion.route('/evaluacion', methods=["POST", "GET"])
def inicio_evaluacion():
    gpo = Grupo.query.filter(Grupo.cveprof == g.id).first()
    materias = Materia.query.filter(Materia.grado == gpo.grado)
    alumno = Alumno.query.filter(Alumno.cvegrupo == gpo.cvegrupo)



        #return redirect(url_for("evaluacion.inicio_evaluacion<i>"), i = i)



    return render_template('/usuario/evaluacionAlumno.html', materias=materias, alumnos=alumno)

@evaluacion.route('/evaluacion_agregada', methods=["POST", "GET"])
def evaluacion_agregada():
    gpo = Grupo.query.filter(Grupo.cveprof == g.id).first()
    materias = Materia.query.filter(Materia.grado == gpo.grado)
    alumno = Alumno.query.filter(Alumno.cvegrupo == gpo.cvegrupo)
    if request.method == "POST":

        listatodo = []
        for al in alumno:
            dicc = {}

            dicc["cve_alum"] = al.cve_alum
            dicc["nombre"] = al.alum_nombre, al.alum_apellidop, al.alum_apellidom
            listacalis = []
            for mat in materias:
                diccmateria = {}
                diccmateria[mat.cve_materia] = request.form["cal1" + str(mat.cve_materia) + str(al.cve_alum)]
                listacalis.append(diccmateria)
            dicc["calificaciones"] = listacalis
            listatodo.append(dicc)
        print(listatodo)

        for l in listatodo:
            json_calif = {}
            json_calif["cvealumno"] = l["cve_alum"]
            json_calif["trimestre"] = 1
            for cal in l["calificaciones"]:
                for value in cal:

                    json_calif["cve_materia"] = str(value)
                for value in cal.values():
                    json_calif["calificacion"] = value

                calif = calif_alumno()

                calif.registrar_calif(json_calif)
    return redirect(url_for("evaluacion.inicio_evaluacion"))


@informacion.route('/informacion')
def inicio_informacion():

    return render_template('/usuario/informacionAlumno.html')

@lista.route('/lista')
def inicio_lista():
    usuarios = db.session.query(Alumno.cve_alum, Alumno.alum_nombre, Alumno).all()
    if (request.args.get('idUsuario') != None):
        usuario = Alumno()
        # avance boletas
        # imprimir boleta
        usuarios = db.session.query(Alumno.cve_alum, Alumno.alum_nombre).all()
    return render_template('/usuario/listaUsuario.html', usuarios=usuarios)

