from os import environ
from json import load


class Config:
    def __init__(self):
        environment = environ.get("ENVIRONMENT")
        if environment is None:
            environment = "DEV"

        config_path = environ.get("{}_CONFIG_PATH".format(environment))
        if config_path is None:
            config_path = "config/config-dev.json"

        with open(config_path, 'r') as file:
            self.data = load(file)

    def get(self):
        return self.data
