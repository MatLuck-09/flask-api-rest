import os

# ACA SOLO SETEO ENV VARS EXTERIORES

API_VERSION = "1.0.0"
ENVIRONMENT = "local"
APP_PORT = 5000

# Add the OpenWeatherMap API key to settings.py
OPENWEATHERMAP_API_KEY = os.environ.get('OPENWEATHERMAP_API_KEY')