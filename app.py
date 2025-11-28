from flask import Flask

# Crear la aplicacion Flask
app = Flask(__name__)

# Definir una ruta
@app.route('/')
def hello_world():
    return "¡Hola Mundo desde Flask!"

# Ejecutar la aplicacion
if __name__ == '__main__':
    app.run(debug=True)