"""
Module providing index endpoints.
"""
from flask import jsonify
from app.api.index import index


@index.route("/status", methods=["GET"])
def get_status():
    """
    The function returns a JSON response with a message and API version.
    """
    response = {
        "message": "API FLASK ESTRUCTURA GENERAL funciona!"
    }
    return jsonify(response), 200
