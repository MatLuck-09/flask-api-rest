from flask import Flask
from app.api.index import index
from app.api.v1 import clima_api_v1
from .ext import init_error_handler

## INICIALIZO LA APP CON LO QUE SE NECESITE PARA EJECUTAR UNA ARQUITECTURA SOLIDA.

def create_app():

    # Create flask app
    app = Flask(__name__)

    # Register blueprints
    app.register_blueprint(blueprint=index)
    app.register_blueprint(blueprint=clima_api_v1)

    init_error_handler(app)

    return app
