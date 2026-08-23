# Importacion de librerias necesarias junto con las rutas que se usaran.
from flask import Flask
from flask_cors import CORS
from carro_compras.routes.rutas import carrito_compras


# Construccion de la aplicacion flask con la ruta iniciada "url/cart/rutas". 
app = Flask(__name__)
app.register_blueprint(carrito_compras,url_prefix = '/cart')
CORS(app,origins='https://1138-190-24-70-29.ngrok-free.app ',supports_credentials=True, methods=['GET', 'POST', 'OPTIONS'],allow_headers=['Content-Type', 'ngrok-skip-browser-warning'])