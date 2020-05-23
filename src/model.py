from requests import get
from urllib import parse


class WeatherSpecificLocation:
    def __init__(self, server_address, api_key, lat, lon):
        self.server_address = server_address
        self.api_key = api_key
        self.lat = lat
        self.lon = lon

    def get_current(self):
        self.__fetch_data()
        current_data = self.data['current']
        data_dict = dict()
        data_dict['temp'] = current_data['temp']
        data_dict['pressure'] = current_data['pressure']
        data_dict['humidity'] = current_data['humidity']
        data_dict['dew_point'] = current_data['dew_point']
        data_dict['uvi'] = current_data['uvi']
        data_dict['clouds'] = current_data['clouds']
        data_dict['visibility'] = current_data['visibility']
        data_dict['wind_speed'] = current_data['wind_speed']
        data_dict['wind_deg'] = current_data['wind_deg']
        data_dict['weather'] = current_data['weather'][0]['main']
        return data_dict

    def __fetch_data(self):
        path = 'data/2.5/onecall?lat={}&lon={}&appid={}'.format(self.lat, self.lon, self.api_key)
        endpoint = parse.urljoin(self.server_address, path)
        result = get(endpoint)
        self.data = result.json()
        return self.data
