from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


class Nombre_Mas_largo:
    pass

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1(longitud=None):
    if request.method == 'POST':
       
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']
       
        return render_template('ejercicio1.html', Nombre_Mas_Largo=Nombre_Mas_largo, longitud=longitud)

    return render_template('ejercicio1.html')

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2(longitud=None, nombre_mas_largo=None):
    if request.method == 'POST':

        return render_template('ejercicio2.html', nombre_mas_largo=nombre_mas_largo, longitud=longitud)

    return render_template('ejercicio2.html')

if __name__ == '__main__':
    app.run(debug=True)