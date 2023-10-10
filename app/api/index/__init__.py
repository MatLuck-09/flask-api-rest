from flask import Blueprint


index = Blueprint("index", __name__)


from app.api.index import routes
