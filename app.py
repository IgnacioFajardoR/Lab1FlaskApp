from flask import Flask
from flask import render_template 
from flask import request
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/kevin')
def kevin():
    return render_template('kevin.html')

@app.route('/ignacio')
def ignacio():
    return render_template('ignacio.html')

@app.route('/nuevo-integrante', methods=['POST'])
def NuevoIntegrante():
    nombreCompleto = request.form['nombreCompleto']
    Carrera = request.form['Carrera']
    Facebook = request.form['Facebook']
    Twitter = request.form['Twitter']
    GitHub = request.form['GitHub']

    return render_template('NuevoIntegrante.html', nombreCompleto = nombreCompleto, Carrera = Carrera, Facebook = Facebook , Twitter = Twitter, GitHub = GitHub)

if __name__ == '__main__':
    
    app.run(debug=True)