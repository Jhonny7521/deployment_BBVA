#1° Inicializamos el proyecto
from flask import Flask
from flask_cors import CORS, cross_origin

app = Flask(__name__)
app.secret_key = "Mi llave secreta"

# CORS(app)
CORS(app, resources={r"/api/*": {"origins": "*"}})