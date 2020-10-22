from flask import Flask
from flask import render_template 
from flask import request
import os

uploads_dir = os.path.join('static')
app = Flask(__name__)

@app.route('/')
def index():
    print(uploads_dir )
    return render_template("home.html")

@app.route('/cv')
def Curriculum():
    if(request.args.get('integrante')=='kevin'):
        return render_template('kevin.html')
    if(request.args.get('integrante')=='ignacio'):
        return render_template('ignacio.html')
    else:
        return ("Petición erronéa o integrante no existente")
    


@app.route('/nuevo-integrante', methods=['POST'])
def NuevoIntegrante():
    nombreCompleto = request.form['nombreCompleto']
    Carrera = request.form['Carrera']
    Facebook = request.form['Facebook']
    Twitter = request.form['Twitter']
    GitHub = request.form['GitHub']
    CV =request.files['SubirCurriculum']
    CV.save(os.path.join(uploads_dir, 'CVNuevo.pdf'))

    return render_template('NuevoIntegrante.html', nombreCompleto = nombreCompleto, Carrera = Carrera, Facebook = Facebook , Twitter = Twitter, GitHub = GitHub)

@app.route('/CVNuevo')
def CVNuevo():
    return render_template('CVNuevo.html')

@app.errorhandler(404)
def handle_bad_request(e):
    return 'Petición erronea'


if __name__ == '__main__':
    
    app.run(debug=True)
    