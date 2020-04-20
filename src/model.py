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
        data_dict = dict()
        data_dict['temp'] = self.data['temp']
        data_dict['pressure'] = self.data['pressure']
        data_dict['humidity'] = self.data['humidity']
        data_dict['dew_point'] = self.data['dew_point']
        data_dict['uvi'] = self.data['uvi']
        data_dict['clouds'] = self.data['clouds']
        data_dict['visibility'] = self.data['visibility']
        data_dict['wind_speed'] = self.data['wind_speed']
        data_dict['wind_deg'] = self.data['wind_deg']
        data_dict['weather'] = self.data['weather'][0]['main']

    def __fetch_data(self):
        path = "data/2.5/onecall?lat={}&lon={}&appid={}".format(self.lat, self.lon, self.api_key)
        endpoint = parse.urljoin(self.server_address, path)
        result = get(endpoint)
        self.data = result.json()
        return self.data
