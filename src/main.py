from flask import Flask, request, redirect, url_for
from src import create_app
from flask import render_template

from src.models import Profesor

app = create_app()

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
        print(profesor)
        if profesor["status"] == True:
            if usuario == "gowoncita":
                return redirect(url_for("inicio.inicioprincipal"))
            else:
                return redirect(url_for("iniciousuario.iniciousuario"))

        else:
            return 'datos incorrectos'


        #if profesor = True:
            #(usuario)
    return 'ok'

if __name__ == '__main__':

    app.run() #debug=True, port=5000