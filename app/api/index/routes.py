from flask import jsonify
from app.api.index import index


@index.route("/status", methods=["GET"])
def get_status():
    response = {
        "message": "API FLASK ESTRUCTURA GENERAL funciona!"
    }
    return jsonify(response), 200
