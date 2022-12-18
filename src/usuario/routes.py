


from flask import render_template, request, g, redirect, url_for, session, flash

from . import iniciousuario, evaluacion, informacion, lista, avance, relacion, promedio
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
    materias = Materia.query.filter(Materia.grado == gpo.grado)
    trimestre = Trimestres.query.filter(Trimestres.cve_tri == 1).first()

    alumno = Alumno.query.filter(Alumno.cvegrupo == gpo.cvegrupo)
    #usuarios = db.session.query(Alumno.cve_alum, Alumno.alum_nombre, Alumno).all()

    if (request.args.get('idMostrarAlumno') != None):
        alum = Alumno()
        al = alum.consultar_alumno(request.args.get('idMostrarAlumno'))


        return render_template('/usuario/informacionAlumno.html', al=al)
    if (request.args.get('idAlumnoAvance') != None):
        alum = Alumno()
        al = alum.consultar_alumno(request.args.get('idAlumnoAvance'))
        listacalis = []

        if(trimestre.trimestre==2):
            calis = calif_alumno.query.filter(calif_alumno.CVE_ALUM == al.cve_alum, calif_alumno.NUMERO_TRIMESTRE == 1)
            for c1 in calis:
                prom = c1.CALIF_TRIM_ALUM/3
                listacalis.append("{:.2f}".format(prom))
        elif(trimestre.trimestre==3):
            calis = calif_alumno.query.filter(calif_alumno.CVE_ALUM == al.cve_alum, calif_alumno.NUMERO_TRIMESTRE == 1)
            calis2 = calif_alumno.query.filter(calif_alumno.CVE_ALUM == al.cve_alum, calif_alumno.NUMERO_TRIMESTRE == 2)
            for c1, c2 in zip(calis, calis2):
                prom = (c1.CALIF_TRIM_ALUM+c1.CALIF_TRIM_ALUM) / 3
                listacalis.append("{:.2f}".format(prom))
        elif(trimestre.trimestre==4):
            calis = calif_alumno.query.filter(calif_alumno.CVE_ALUM == al.cve_alum, calif_alumno.NUMERO_TRIMESTRE == 1)
            calis2 = calif_alumno.query.filter(calif_alumno.CVE_ALUM == al.cve_alum, calif_alumno.NUMERO_TRIMESTRE == 2)
            calis3 = calif_alumno.query.filter(calif_alumno.CVE_ALUM == al.cve_alum, calif_alumno.NUMERO_TRIMESTRE == 3)

            for c1, c2, c3 in zip(calis, calis2, calis3):
               # print("jjjjjjj",c1,c2,c3)
                prom = (c1.CALIF_TRIM_ALUM + c2.CALIF_TRIM_ALUM + c3.CALIF_TRIM_ALUM)/3
                listacalis.append("{:.2f}".format(prom))

        return render_template('/usuario/avance.html', alumno = al, materias = materias, calis = calis, grupo = gpo, promedio = listacalis, trimestre = trimestre.trimestre)

    if (request.args.get('idAlumnoBoleta') != None):
        if trimestre.trimestre == 4:
            alum = Alumno()
            al = alum.consultar_alumno(request.args.get('idAlumnoBoleta'))
            calis = calif_alumno.query.filter(calif_alumno.CVE_ALUM == al.cve_alum, calif_alumno.NUMERO_TRIMESTRE == 1)
            calis2 = calif_alumno.query.filter(calif_alumno.CVE_ALUM == al.cve_alum, calif_alumno.NUMERO_TRIMESTRE == 2)
            calis3 = calif_alumno.query.filter(calif_alumno.CVE_ALUM == al.cve_alum, calif_alumno.NUMERO_TRIMESTRE == 3)
            listacalis = []
            for c1, c2, c3 in zip(calis, calis2, calis3):
                # print("jjjjjjj",c1,c2,c3)
                prom = (c1.CALIF_TRIM_ALUM + c2.CALIF_TRIM_ALUM + c3.CALIF_TRIM_ALUM) / 3
                listacalis.append("{:.2f}".format(prom))
            promediogeneral = 0
            for l in listacalis:
                promediogeneral = promediogeneral + float(l)
            listamaterias = []
            for mat in materias:
                listamaterias.append(mat)
            promediogeneral = "{:.2f}".format(promediogeneral/len(listamaterias))
            rango = len(listamaterias)
            return render_template('/usuario/promedio.html', grupo= gpo, materias = materias, alumno = al, general = promediogeneral, lcalis = listacalis, rango=rango, calis = calis, calis2 = calis2, calis3 = calis3)
        else:
            flash("NO PUEDE VER BOLETA")
        # avance boletas
        # imprimir boleta

    return render_template('/usuario/listaUsuario.html', usuarios=alumno)

@avance.route("/avance")
def inicio_avance():
    return render_template('/usuario/avance.html')

@relacion.route("/relacion")
def inicio_relacion():
    gpo = Grupo.query.filter(Grupo.cveprof == g.id).first()
    alumno = Alumno.query.filter(Alumno.cvegrupo == gpo.cvegrupo)



    return render_template('/usuario/relacion.html', alumnos = alumno, grupo = gpo)

@promedio.route("/promedo")
def inicio_promedio():
    return render_template('/usuario/promedio.html')
