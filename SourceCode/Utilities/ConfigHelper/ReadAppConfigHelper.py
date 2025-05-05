import yaml
import os

config_relative_path = "../../AppConfigFiles/AppConfiguration.yaml"
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)
os.chdir('..')
config_path = os.path.join(os.getcwd(), config_relative_path)

with open(config_relative_path) as f:
    data = yaml.load(f, Loader=yaml.FullLoader)


def get_config(key):
    value = data.get(key)
    return value
