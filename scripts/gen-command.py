# TODO: add assertions

from utils import get_config
from constants import SERVER_START_COMMAND, SERVER_QUERY_PORT, SERVER_QUERY_PORT_ACTIVE, SERVER_USE_MULTITHREADING

config = get_config()
command = SERVER_START_COMMAND

if config['PublicPort'] != None:
    command += f" -publicport={config['PublicPort']}"
    
if config['ServerPlayerMaxNum'] != None:
    command += f" -players={config['ServerPlayerMaxNum']}"
    
if config['bIsMultiplay'] == True:
    command += " -EpicApp=PalServer"
    
if config['PublicIP'] != None:
    command += f" -publicip={config['PublicIP']}"
    
if config['PublicPort'] != None:
    command += f" -publicport={config['PublicPort']}"

if config['ServerName'] != "":
    command += f" -servername={config['ServerName']}"

if config['ServerPassword'] != "":
    command += f" -serverpassword={config['ServerPassword']}"

if config['AdminPassword'] != "":
    command += f" -adminpassword={config['AdminPassword']}"

if SERVER_QUERY_PORT_ACTIVE == True:
    command += f" -queryport={SERVER_QUERY_PORT}"

if SERVER_USE_MULTITHREADING == True:
    command += " -useperfthreads -NoAsyncLoadingThread -UseMultithreadForDS"

print(command)