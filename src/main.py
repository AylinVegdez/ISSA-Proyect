from flask import Flask, request, redirect, url_for, g, session
from src import create_app
from flask import render_template

from src.Globales import Globales
from src.models import Profesor

app = create_app()



@app.route('/', methods=['GET'])
def index():
    return render_template('Login.html')

@app.before_request
def before_request():
    if "username" in session:
        g.user = session["username"]
    else:
        g.user = "Nombre_usuario"

@app.route('/login', methods=['POST'])
def login():

    if request.method == 'POST':
        usuario = request.form["usuario"]
        contraseña = request.form["contrasena"]
        prof = Profesor()
        profesor = prof.validar_cliente(usuario, contraseña)
        print(usuario)
        if profesor["status"] == True:
            session["username"] = usuario
            if usuario == "gowoncita":


                #return render_template("/admin/adminMenuP.html", usuario = usuario)
                return redirect(url_for("inicio.inicioprincipal"))
            else:
                return redirect(url_for("iniciousuario.iniciousuario"))
        else:
            return 'datos incorrectos'
        #if profesor = True:
            #(usuario)
    return 'ok'


@app.context_processor
def context_processor():
    return dict(usuario=g.user)


if __name__ == '__main__':

    app.run() #debug=True, port=5000