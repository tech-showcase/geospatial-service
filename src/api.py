from flask import Blueprint, jsonify
import model
import controller
import global_var

api = Blueprint('api', __name__)


@api.route('/api/weather/current')
def fetch_current_weather(*args, **kwargs):
    config = global_var.config.get()['weather']
    weather_model = model.WeatherSpecificLocation(config['server_address'],
                                                  config['api_key'],
                                                  "-6.200000",
                                                  "106.816666")
    result_dict = controller.fetch_current_weather(weather_model)
    return jsonify(result_dict)
