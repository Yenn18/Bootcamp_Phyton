from flask import Flask, render_template

# Crear una instancia en el flask
app = Flask(__name__)

#Crear una ruta 
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return f"hola {name} esto es una pagina con flask y junto html"
#Definir la segunda ruta
@app.route('/about')
def abour ():
    return " Esta es una pagina normal"

#Ejecutar la aplicacion 
if __name__ == '__main__':
    app.run(debug=True)