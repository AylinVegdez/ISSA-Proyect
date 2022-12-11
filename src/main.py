from flask import Flask
from src import create_app
from flask import render_template

app = create_app()

@app.route('/', methods=['GET'])
def index():
    return render_template('Login.html')

if __name__ == '__main__':

    app.run() #debug=True, port=5000