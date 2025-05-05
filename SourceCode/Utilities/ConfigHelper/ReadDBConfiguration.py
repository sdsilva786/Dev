import json
import os

config_relative_path = "../../AppConfigFiles/DBConfiguration.json"
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)
os.chdir('..')
config_path = os.path.join(os.getcwd(), config_relative_path)


def get_config_data():
    with open(config_path, "r") as config_file:
        config_data = json.load(config_file)
        return config_data
