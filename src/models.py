from .extensiones import db
from sqlalchemy import Column, ForeignKey,Integer,String,Boolean,DECIMAL,exc
import bcrypt
class Profesor(db.Model):
    __name__='PROFESOR'
    cveprof=Column(Integer,primary_key=True)
    prof_nombre=Column(String(30),nullable=False)
    sexo=Column(String(1),nullable=False)
    nombre_usuario=Column(String(30),nullable=False )
    password=Column(String(10),nullable=False)

    def registrar_profesor(self,datos):
        msg="Profesor insertado correctamente"
        respuesta={'status': 'OK', 'codigo':'','mensaje':msg}
        self.prof_nombre =  datos['nombre']
        self.sexo = datos['sexo']
        self.nombre_usuario=datos['nombre_usuario']
        self.password = self.cifrar_contrasena(datos['clave'])
        

        try:
            db.session.add(self)
            db.session.commit()
            respuesta["codigo"] = '1'

            
        except exc.SQLAlchemyError as error:
            print(error)
            # valor = (error.__cause__.args[1].split("'"[1]))
            # campo = (error.__cause__.args[1].split("'"[0]))

            # msj_error='Ocurrió un error para el campo: ' + campo + " en la entrada de datos: " + valor
        
            # respuesta["codigo"] = error.__cause__.args[0]
            # respuesta["mensaje"] = msj_error
        return respuesta
    
    def cifrar_contrasena(self, contrasena):
        salt = bcrypt.gensalt()
        contrasena_cifrada = bcrypt.hashpw(contrasena.encode('utf-8'),salt)
        return contrasena_cifrada

    def verificar_contrasena(self, clave, clave_cifrada):
        return bcrypt.checkpw(clave.encode('utf-8'), clave_cifrada.encode('utf-8'))
    
    def validar_cliente(self, nom_usuario,clave):

        #1. Respuestaa
        msg="Cliente Aurorizado"
        respuesta={'status': 'OK', 'codigo':'','mensaje':msg}

        #2.Crear Consulta
        prof = Profesor.query.filter(Profesor.nombre_usuario == nom_usuario).first()

        if prof:
            print(prof.password)
            #Vericificar la contraseña
            if self.verificar_contrasena(clave, prof.password):
                msg = "Cliente Autenticado"
                respuesta["mensaje"] = msg
            else:
                msg = "Cliente No autenticado"
                
        else:
            msg = "Cliente No autenticado"
        respuesta["mensaje"]= msg

        return respuesta
    
    def consultar_general_profesor(self):
        prof = Profesor.query.filter()
        profesores = {}
        for x in prof:
            profesores.append(x)
        print(profesores)

    


class Materia(db.Model):
    __name__='MATERIA'
    cve_materia=Column(Integer,primary_key=True)
    nombre_materia=Column(String(30),nullable=False)



    # productos = db.relationship('Productos', backref='categorias')
class Grupo(db.Model):
    cve_grupo=Column(Integer,primary_key=True)
    cve_prof=Column(Integer,ForeignKey('PROFESOR.cveprof'))
class Alumno(db.Model):
    __name__='ALUMNO'
    cve_alum=Column(Integer,primary_key=True)
    alum_curp=Column(String(18),nullable=False)
    alum_estado=Column(Integer,nullable=False,default=0)
    alum_edad=Column(Integer, nullable=False)
    alum_nombre=Column(String(30),nullable=False)
    alum_sexo=Column(String(1), nullable=False)
    cve_grupo=Column(Integer,ForeignKey('GRUPO.cve_grupo'))

class Promedios_Finales(db.Model):
    __name__='PROMEDIOS_FINALES'
    cve_prom_final=Column(Integer, primary_key=True)
    cve_alum=Column(Integer,ForeignKey('ALUMNO.cve_alum'))
    grado=Column(Integer,nullable=False)
    promedio_final=Column(DECIMAL(4,2),nullable=False)
class Calif_Alumno(db.Model):
    cve_calif_alum=Column(Integer, primary_key=True)
    calif_trim_alumno=Column(DECIMAL(4,2),nullable=False)
    numero_trimestre = Column(Integer,nullable=False)
    cve_alum=Column(Integer,ForeignKey('ALUMNO.cve_alum'))
    cve_materia=Column(Integer,ForeignKey('MATERIA.cve_materia'))
class Prom_Materia_Alumno(db.Model):
    cve_prom_materia=Column(Integer, primary_key=True)
    prom_mat_alum=Column(DECIMAL(4,2),nullable=False)
    cve_materia=Column(Integer,ForeignKey('MATERIA.cve_materia'))
    cve_alum=Column(Integer,ForeignKey('ALUMNO.cve_alum'))






