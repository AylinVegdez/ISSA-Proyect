
from flask import Flask
from flask_cors import CORS

from .admin import inicio, adminalumno, admincalificacion, admingrupo, adminmateria, adminprofesor, agregarprofesor, \
    agregaralumno, asignargrupo, asignarmateria
from .configuracion import DevConfig
from .extensiones import db
from .routes.profesorRoutes import profesor
from .usuario import iniciousuario, evaluacion, informacion, lista, avance, promedio, relacion


# from src.categorias.routes import categoria

def create_app():
    app = Flask(__name__)
    # Configurar las referencias cruzadas, cuando se hacen peticiones de otros dominios
    CORS(app)
    # Agregar configuración desde archivo configuracion.py
    app.config.from_object(DevConfig)

    #Configurar SQLAlchemy
    db.init_app(app)
    # from flask_sqlalchemy import SQLAlchemy
    # db = SQLAlchemy
    
    # Registramos los Blueprints
    app.register_blueprint(profesor)
    app.register_blueprint(inicio)
    app.register_blueprint(adminalumno)
    app.register_blueprint(admincalificacion)
    app.register_blueprint(admingrupo)
    app.register_blueprint(adminmateria)
    app.register_blueprint(adminprofesor)
    app.register_blueprint(agregarprofesor)
    app.register_blueprint(agregaralumno)
    app.register_blueprint(asignargrupo)
    app.register_blueprint(asignarmateria)
    app.register_blueprint(iniciousuario)
    app.register_blueprint(evaluacion)
    app.register_blueprint(informacion)
    app.register_blueprint(lista)
    app.register_blueprint(avance)
    app.register_blueprint(promedio)
    app.register_blueprint(relacion)


    return app