from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        try:
            # Recoge los datos del formulario
            nota1 = float(request.form['nota1'])
            nota2 = float(request.form['nota2'])
            nota3 = float(request.form['nota3'])
            asistencia = float(request.form['asistencia'])

            # Calcula el promedio de las notas
            promedio = (nota1 + nota2 + nota3) / 3

            # Verifica si la asistencia es suficiente (al menos 75%)
            asistencia_suficiente = asistencia >= 75

            # Verifica si el promedio es suficiente (al menos 40)
            promedio_suficiente = promedio >= 40

            # Determina el estado (aprobado/reprobado)
            estado = 'APROBADO' if promedio_suficiente and asistencia_suficiente else 'REPROBADO'

            return render_template('resultado.html', promedio=promedio, estado=estado)
        except ValueError:
            return "Por favor, ingrese valores numéricos válidos."
    return render_template('ejercicio1.html')

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        dato2 = request.form['dato2']
        # Procesa el dato2 aquí
        return f'Dato 2 recibido: {dato2}'
    return render_template('ejercicio2.html')

if __name__ == '__main__':
    app.run(debug=True)