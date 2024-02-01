import os
import yaml
import subprocess
import re
import json
from logger import log

APP_ID                    = 2394010
SERVER_CONFIG_FILE_PATH   = "/palworld/Pal/Saved/Config/LinuxServer/PalWorldSettings.ini"
SERVER_CONFIG_HEADER      = "[/Script/Pal.PalGameWorldSettings]"
CUSTOM_CONFIG_FILE_PATH   = "../config.yml"
SERVER_START_COMMAND      = "./PalServer.sh"

def get_env(key):
    try:
        return os.environ[key]
    except:
        log.critical(f'Environment variable {key} is not set.')
        exit(0)
        
def execute_command(command, error_message):
    try:
        if type(command) == str:
            command = command.split(' ')
        subprocess.run(command, check = True)
    except Exception as e:
        log.critical(e)
        log.critical(error_message)
        log.critical(f'Command: {command}')
        exit(0)

def give_permissions_and_create_directory():
    puid = get_env('PUID')
    pgid = get_env('PGID')
    
    execute_command(
        f'usermod -o -u {puid} steam',
        'Failed to give permissions.'
    )
    
    execute_command(
        f'groupmod -o -g {pgid} steam',
        'Failed to give permissions.'
    )
    
    execute_command(
        f'mkdir -p /palworld',
        'Failed to create directory.'
    )
    
    execute_command(
        f'chown -R steam:steam /palworld',
        'Failed to give permissions.'
    )

def check_steamcmd():
    execute_command(
        '/home/steam/steamcmd/steamcmd.sh +quit',
        'Steamcmd is not installed. Please install it first.'
    )
    
def download_server():
    first_run = False
    current_version = 0
    latest_version = 0
    
    if os.path.isfile('/palworld/version.txt'):
        with open('/palworld/version.txt', 'r') as file:
            current_version = int(file.read())
    else:
        first_run = True
            
    try:
        response = json.loads(subprocess.check_output(["curl", "-s", f"https://api.steamcmd.net/v1/info/{APP_ID}"]))
        latest_version = int(response['data'][f'{APP_ID}']['depots']['branches']['public']['buildid'])
    except Exception as e:
        log.error(e)
        log.error('Failed to get latest version from steamcmd.')
        return

    log.info(f'Current version: {current_version} (auto-update: {get_env("AUTOMATIC_UPDATE")})')
    log.info(f'Latest version: {latest_version}')
    log.info(f'First run: {first_run}')
            
    if first_run == False and current_version == latest_version:
        log.info('Server binaries already up to date.')
        return
    elif first_run == False and get_env('AUTOMATIC_UPDATE') == False:
        log.info('AUTOMATIC_UPDATE is set to false, skipping update.')
        return
    else:
        log.info('Updating server binaries...')
        execute_command(
            ['su', 'steam', '-c', '"/home/steam/steamcmd/steamcmd.sh +force_install_dir \"/palworld\" +login anonymous +app_update 2394010 validate +quit"'],
            'Failed to download server binaries.'
        )
        
        with open('/palworld/version.txt', 'w') as file:
            file.write(str(latest_version))
    

def get_config():
    config = {}
    path = os.path.join(os.path.dirname(__file__), CUSTOM_CONFIG_FILE_PATH)
    with open(path, 'r') as file:
        config = yaml.load(file, Loader=yaml.FullLoader)
    return config

def setup_server():
    if not os.path.isfile(SERVER_CONFIG_FILE_PATH):
        execute_command(
            ['su', 'steam', '-c', 'timeout --preserve-status 15s /palworld/PalServer.sh 1> /dev/null'],
            'Failed to create default configuration.'
        )
    
    config = get_config()  
    config_string = SERVER_CONFIG_HEADER + "\nOptionSettings=("
    
    for key, value in config.items():
        if value == None:
            config_string += f"{key}=null,"
        elif re.match(r'^\{\{(.*)\}\}$', str(value)):
            env_key = re.search(r'^\{\{(.*)\}\}$', str(value)).group(1)
            if '@' in env_key:
                cast = env_key.split('@')[1]
                env_key = env_key.split('@')[0]
                config_string += f"{key}={cast}({get_env(env_key)}),"
            else:
                config_string += f"{key}={get_env(env_key)},"
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
    
    if SERVER_CONFIG_FILE_PATH != None:
        open(SERVER_CONFIG_FILE_PATH, 'a').close()
        with open(SERVER_CONFIG_FILE_PATH, "w") as file:
            file.write(config_string)
            
def launch_server():
    command = SERVER_START_COMMAND
    
    if get_env('USE_COMMUNITY').lower() == 'true':
        command += " EpicApp=PalServer"

    if get_env('SERVER_QUERY_ACTIVE').lower() == 'true':
        command += f" -queryport={get_env('SERVER_QUERY_PORT')}"

    if get_env('USE_MULTITHREADING').lower() == 'true':
        command += " -useperfthreads -NoAsyncLoadingThread -UseMultithreadForDS"
    
    if get_env('RCON_ENABLED').lower() == 'true':
        command += " -rcon"
    
    log.info(f'Starting server with command: {command}')