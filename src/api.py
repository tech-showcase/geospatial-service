from flask import Blueprint

api = Blueprint('api', __name__)


@api.route('/api/weather/current')
def fetch_current_weather(*args, **kwargs):
    return "dummy"
