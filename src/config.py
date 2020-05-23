from os import environ


class Config:
    def __init__(self):
        self.data = {
            'weather': self.__get_weather()
        }

    def __get_weather(self):
        server_address = self.__read_env_var_with_default('WEATHER_SERVER_ADDRESS', 'http://localhost')
        api_key = self.__read_env_var_with_default('WEATHER_API_KEY', 'apiKey')
        return {
            'server_address': server_address,
            'api_key': api_key
        }

    @staticmethod
    def __read_env_var_with_default(key, default_value):
        env_var_value = environ.get(key)
        if env_var_value is None:
            env_var_value = default_value

        return env_var_value

    def get(self):
        return self.data
