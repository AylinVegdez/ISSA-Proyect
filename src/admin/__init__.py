from flask import Blueprint

inicio = Blueprint('inicio', __name__, url_prefix='/admin', template_folder='templates')

adminalumno = Blueprint('adminalumno', __name__, url_prefix='/admin', template_folder='templates')

admincalificacion = Blueprint('admincalificacion', __name__, url_prefix='/admin', template_folder='templates')

admingrupo = Blueprint('admingrupo', __name__, url_prefix='/admin', template_folder='templates')

adminmateria = Blueprint('adminmateria', __name__, url_prefix='/admin', template_folder='templates')

adminprofesor = Blueprint('adminprofesor', __name__, url_prefix='/admin', template_folder='templates')

agregarprofesor = Blueprint('agregarprofesor', __name__, url_prefix='/admin', template_folder='templates')

agregaralumno = Blueprint('agregaralumno', __name__, url_prefix='/admin', template_folder='templates')

asignargrupo = Blueprint('asignargrupo', __name__, url_prefix='/admin', template_folder='templates')

asignarmateria = Blueprint('asignarmateria', __name__, url_prefix='/admin', template_folder='templates')



from . import routes