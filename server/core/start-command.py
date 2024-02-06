from functions import get_env

def get_start_command():
    command = get_env('PALWORLD_START_COMMAND')
    
    if get_env('PALWORLD_COMMUNITY_ENABLED').lower() == 'true':
        command += " EpicApp=PalServer"

    if get_env('PALWORLD_QUERY_ENABLED').lower() == 'true':
        command += f" -queryport={get_env('PALWORLD_QUERY_PORT')}"

    if get_env('PALWORLD_MULTITHREADING_ENABLED').lower() == 'true':
        command += " -useperfthreads -NoAsyncLoadingThread -UseMultithreadForDS"
    
    if get_env('PALWORLD_RCON_ENABLED').lower() == 'true':
        command += " -rcon"

    return command
  
if __name__ == '__main__':
    print(get_start_command())