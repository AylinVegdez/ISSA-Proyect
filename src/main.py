from flask import Flask, request, redirect, url_for, g
from src import create_app
from flask import render_template

from src.Globales import Globales
from src.models import Profesor

app = create_app()
@app.after_request
def after_request(response):

    return response
@app.before_request
def before_request():
    g.usuario = "hola mundo"
    g.id = "sin id"


@app.route('/', methods=['GET'])
def index():
    return render_template('Login.html')

@app.route('/login', methods=['POST'])
def login():

    if request.method == 'POST':
        usuario = request.form["usuario"]
        contraseña = request.form["contrasena"]
        prof = Profesor()
        profesor = prof.validar_cliente(usuario, contraseña)
        print(usuario)
        if profesor["status"] == True:

            if usuario == "gowoncita":

                #return render_template("/admin/adminMenuP.html", usuario = usuario)
                return redirect(url_for("inicio.inicioprincipal", usu = usuario))
            else:
                return redirect(url_for("iniciousuario.iniciousuario", usu = usuario))
        else:
            return 'datos incorrectos'
        #if profesor = True:
            #(usuario)
    return 'ok'



if __name__ == '__main__':

    app.run() #debug=True, port=5000