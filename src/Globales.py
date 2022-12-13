

class Globales():

    variables = {
        "usuario": "",
        "id": ""
    }
    def __init__(self, usuario, id):
        self.variables["usuario"] = usuario
        self.variables["id"] = id

    def regresar_variables(self):

        return self.variables



