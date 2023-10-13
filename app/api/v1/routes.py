"""
Module providing clima-api-v1 endpoints.
"""
from flask import jsonify, request
from app.api.v1 import clima_api_v1
from .services import ClimaClient


@clima_api_v1.route("/clima", methods=["GET", "POST"])
def get_clima():
    try:
        if request.method == 'POST':
            city = request.form.get('city')
            response = ClimaClient().get_clima_info(city)

            if response is None:
                return jsonify({"error": "Bad Request"}), 400

            else:
                data = response
                temp_celsius = data['main']['temp'] - 273.15
                temp_max_celsius = data['main']['temp_max'] - 273.15
                temp_min_celsius = data['main']['temp_min'] - 273.15
                feels_like_celsius = data['main']['feels_like'] - 273.15
                traducciones_clima = {
                    'Thunderstorm': 'Tormenta',
                    'Drizzle': 'Llovizna',
                    'Rain': 'Lluvia',
                    'Snow': 'Nieve',
                    'Mist': 'Niebla',
                    'Clear': 'Despejado',
                    'Clouds': 'Nublado',
                }
                clima_en_ingles = data['weather'][0]['main']
                clima_en_espanol = traducciones_clima.get(clima_en_ingles, clima_en_ingles)

                # Crear un diccionario con los datos y devolverlo en formato JSON
                result = {
                    'city': data['name'],
                    'main': clima_en_espanol,
                    'temp': temp_celsius,
                    'max': temp_max_celsius,
                    'min': temp_min_celsius,
                    'feels': feels_like_celsius,
                }
                return jsonify(result)

        return jsonify({})

    except Exception as error:
        return jsonify({"error": "Error en la solicitud"}), 400
