


from flask import render_template, request, g, redirect, url_for, session

from . import iniciousuario, evaluacion, informacion, lista
from ..models import Alumno, Grupo, Materia, calif_alumno, Trimestres, Trimestrecapturado
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

    trimestre = Trimestres.query.filter(Trimestres.cve_tri == 1).first()
    capturado = Trimestrecapturado.query.filter(Trimestrecapturado.cve_grupo == gpo.cvegrupo).first()

    print(trimestre.trimestre)
    print(capturado)

    if(trimestre.trimestre==1): #ES DE SI EL TRIMESTRE 1 ESTÁ EN CURSO
              #YA TIENE REGISTRADO EL PRIMER TRIMESTRE Y PUES YA NO DEBE PODER MODIFICAR
      listacalis = []
      for al in alumno:
          calis = calif_alumno.query.filter(calif_alumno.CVE_ALUM == al.cve_alum, calif_alumno.NUMERO_TRIMESTRE==1)
          for c in calis:
             print("obj",c.CALIF_TRIM_ALUM)

          listacalis.append(calis)
          print("lista", listacalis)
      for l in listacalis:
        for c in l:
            print("imprimiendo c",c)


      return render_template('/usuario/evaluacionAlumno.html', materias=materias, alumnos=alumno, trimestre=1,
                                       activado=True, calis = listacalis)

    elif trimestre.trimestre == 2:
        listacalis = []
        for al in alumno:
            calis = calif_alumno.query.filter(calif_alumno.CVE_ALUM == al.cve_alum, calif_alumno.NUMERO_TRIMESTRE == 1)
            for c in calis:
                print("obj", c.CALIF_TRIM_ALUM)

            listacalis.append(calis)
            print("lista", listacalis)
        for l in listacalis:
            for c in l:
                print("imprimiendo c", c)

        return render_template('/usuario/evaluacionAlumno.html', materias=materias, alumnos=alumno, trimestre=2,
                               activado=False, calis=listacalis)

    elif trimestre.trimestre == 3:
        listacalis = []
        for al in alumno:
            calis = calif_alumno.query.filter(calif_alumno.CVE_ALUM == al.cve_alum, calif_alumno.NUMERO_TRIMESTRE == 1)
            for c in calis:
                print("obj", c.CALIF_TRIM_ALUM)

            listacalis.append(calis)

        listacalis2 = []
        for al in alumno:
            calis = calif_alumno.query.filter(calif_alumno.CVE_ALUM == al.cve_alum, calif_alumno.NUMERO_TRIMESTRE == 2)
            for c in calis:
                print("obj", c.CALIF_TRIM_ALUM)

            listacalis2.append(calis)


        return render_template('/usuario/evaluacionAlumno.html', materias=materias, alumnos=alumno, trimestre=3,
                               activado=False, calis=listacalis, calis2=listacalis2)
    elif trimestre.trimestre == 4:
        listacalis = []
        for al in alumno:
            calis = calif_alumno.query.filter(calif_alumno.CVE_ALUM == al.cve_alum, calif_alumno.NUMERO_TRIMESTRE == 1)
            for c in calis:
                print("obj", c.CALIF_TRIM_ALUM)

            listacalis.append(calis)

        listacalis2 = []
        for al in alumno:
            calis = calif_alumno.query.filter(calif_alumno.CVE_ALUM == al.cve_alum, calif_alumno.NUMERO_TRIMESTRE == 2)
            for c in calis:
                print("obj", c.CALIF_TRIM_ALUM)

            listacalis2.append(calis)
        listacalis3 = []
        for al in alumno:
            calis = calif_alumno.query.filter(calif_alumno.CVE_ALUM == al.cve_alum, calif_alumno.NUMERO_TRIMESTRE == 3)
            for c in calis:
                print("obj", c.CALIF_TRIM_ALUM)

            listacalis3.append(calis)

        return render_template('/usuario/evaluacionAlumno.html', materias=materias, alumnos=alumno, trimestre=4,
                               activado=False, calis=listacalis, calis2=listacalis2, calis3 = listacalis3)

        #return redirect(url_for("evaluacion.inicio_evaluacion<i>"), i = i)

    return render_template('/usuario/evaluacionAlumno.html', materias=materias, alumnos=alumno)

@evaluacion.route('/evaluacion_agregada', methods=["POST", "GET"])
def evaluacion_agregada():
    gpo = Grupo.query.filter(Grupo.cveprof == g.id).first()
    materias = Materia.query.filter(Materia.grado == gpo.grado)
    alumno = Alumno.query.filter(Alumno.cvegrupo == gpo.cvegrupo)
    trimestre = Trimestres.query.filter(Trimestres.cve_tri == 1).first()

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
        json_trimestre = {}
        json_trimestre["cve_grupo"] = gpo.cvegrupo
        json_trimestre["cve_profe"] = g.id

        for l in listatodo:
            json_calif = {}
            json_calif["cvealumno"] = l["cve_alum"]
            json_calif["trimestre"] = trimestre.trimestre
            for cal in l["calificaciones"]:
                for value in cal:

                    json_calif["cve_materia"] = str(value)
                for value in cal.values():
                    json_calif["calificacion"] = value

                calif = calif_alumno()

                calif.registrar_calif(json_calif)
        json_trimestre["tri"] = trimestre.trimestre + 1
        capturado = Trimestres()
        capturado.actualizar_trimestre(json_trimestre)
    return redirect(url_for("evaluacion.inicio_evaluacion"))


@informacion.route('/informacion')
def inicio_informacion():

    return render_template('/usuario/informacionAlumno.html')

@lista.route('/lista')
def inicio_lista():
    gpo = Grupo.query.filter(Grupo.cveprof == g.id).first()

    alumno = Alumno.query.filter(Alumno.cvegrupo == gpo.cvegrupo)
    #usuarios = db.session.query(Alumno.cve_alum, Alumno.alum_nombre, Alumno).all()
    if (request.args.get('idUsuario') != None):
        usuario = Alumno()
        # avance boletas
        # imprimir boleta
        usuarios = db.session.query(Alumno.cve_alum, Alumno.alum_nombre).all()
    return render_template('/usuario/listaUsuario.html', usuarios=alumno)

