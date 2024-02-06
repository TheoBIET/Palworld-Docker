import os
import yaml

def get_env(key):
  var = os.environ.get(key)
  if var == None:
      raise Exception(f"Environment variable {key} not found")
  return var

def parse_config():
  config = {}
  file_path = get_env('PALWORLD_CUSTOM_CONFIG_PATH')
  with open(file_path, 'r') as file:
      config = yaml.load(file, Loader=yaml.FullLoader)
  return config
