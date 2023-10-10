from flask import Blueprint


clima_api_v1 = Blueprint("clima_api_v1", __name__)


from app.api.v1 import routes
