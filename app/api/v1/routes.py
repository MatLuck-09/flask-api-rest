"""
Module providing clima-api-v1 endpoints.
"""
from flask import jsonify
from app.api.v1 import clima_api_v1


@clima_api_v1.route("/clima", methods=["GET"])
def get_clima():
    response = {
        "message": "Evaluando el clima.....",
        "clima": "soleado"
    }

    return jsonify(response), 200
