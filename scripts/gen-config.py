# TODO: add assertions

from utils import get_config
from constants import CUSTOM_CONFIG_OUTPUT_PATH, SERVER_CONFIG_HEADER

config = get_config()
config_string = SERVER_CONFIG_HEADER + "\nOptionSettings=("

for key, value in config.items():
    if value == None:
      config_string += f"{key}=null,"
    elif isinstance(value, bool):
      config_string += f"{key}={str(value)},"
    elif isinstance(value, str):
      config_string += f"{key}=\"{value}\","
    elif isinstance(value, int):
      config_string += f"{key}={value},"
    elif isinstance(value, float):
      config_string += f"{key}={value:.6f},"
    else:
      config_string += f"{key}={value},"
    
config_string = config_string[:-1] + ")"

if CUSTOM_CONFIG_OUTPUT_PATH != None:
  open(CUSTOM_CONFIG_OUTPUT_PATH, 'a').close()
  with open(CUSTOM_CONFIG_OUTPUT_PATH, "w") as file:
    file.write(config_string)