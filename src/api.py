from flask import Blueprint, jsonify, request
from src import model
from src import controller
from src import config as global_config

api = Blueprint('api', __name__)


@api.route('/api/weather/current', methods=['GET'])
def fetch_current_weather(*args, **kwargs):
    config = global_config.config.get()['weather']

    lat = request.args.get('lat', default='0')
    lon = request.args.get('lon', default='0')

    weather_model = model.WeatherSpecificLocation(config['server_address'],
                                                  config['api_key'],
                                                  lat,
                                                  lon)
    result_dict = controller.fetch_current_weather(weather_model)

    return jsonify(result_dict)
