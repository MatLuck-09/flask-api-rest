from flask import jsonify

# Aca funcionalidades que van de la mano de la arquitectura:
# ej: seguridad, implementacion, integracion.


def init_error_handler(app):
    @app.errorhandler(404)
    def not_found(error=None):
        response: dict = {
            "message": f"{error}"
        }
        return jsonify(response), 404
