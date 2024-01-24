from constants import CUSTOM_CONFIG_FILE_PATH
import os
import yaml

def get_config():
    config = {}
    path = os.path.join(os.path.dirname(__file__), CUSTOM_CONFIG_FILE_PATH)
    with open(path, 'r') as file:
        config = yaml.load(file, Loader=yaml.FullLoader)
    return config