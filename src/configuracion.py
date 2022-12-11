

class BaseConfig:
    # Variables de configuración base
    SQLALCHEMY_DATABASE_URI = "mysql://uf1jdrizixlxu3wc:xHjtSkkAFNUiS0ORkS1O@bd8pr1wfvf1uzzbgmloc-mysql.services" \
                              ".clever-cloud.com/bd8pr1wfvf1uzzbgmloc"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    TESTING = True
    DEBUG = True
    SECRET_KEY = "Palabra_Secreta"
    TESTING = True

class DevConfig(BaseConfig):
    # Variables de la clase Padre
    pass

class ProdConfig(BaseConfig):
    DEBUG = False
    TESTING = False