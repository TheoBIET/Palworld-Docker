import re
from functions import parse_config, get_env

config = parse_config()
config_header = get_env('PALWORLD_CONFIG_HEADER')
config_file_path = get_env('PALWORLD_CONFIG_FILE_PATH')
config_string = config_header + "\nOptionSettings=("

for key, value in config.items():
    if re.match(r'^\{\{(.*)\}\}$', str(value)):
        env_key = re.search(r'^\{\{(.*)\}\}$', str(value)).group(1)
        if '@' in env_key:
            cast = env_key.split('@')[1]
            env_key = env_key.split('@')[0]
            if cast == 'int':
                config_string += f"{key}={int(get_env(env_key))},"
            elif cast == 'float':
                config_string += f"{key}={float(get_env(env_key))},"
            elif cast == 'bool':
                config_string += f"{key}={get_env(env_key).lower() == 'true'},"
            elif cast == 'str':
                config_string += f"{key}=\"{get_env(env_key)}\","
    elif value == None:
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

if config_file_path != None:
    open(config_file_path, 'a').close()
    with open(config_file_path, "w") as file:
        file.write(config_string)