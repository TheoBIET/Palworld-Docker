import os
from datetime import datetime

def local_backup():
    date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_name = f'palworld-{date}.tar.gz'
    os.system(f'tar -zcf {backup_name} ./server/palworld/Pal/Saved')
    print(f'Backup created at ./server/backups/{backup_name}')

def backup():
    from logger import log
    date = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_name = f'palworld-{date}.tar.gz'
    os.system(f'tar -zcf {backup_name} /palworld/Pal/Saved')
    os.system(f'mv {backup_name} /home/steam/server/backups/')
    log.info(f'Backup created at /home/steam/server/backups/{backup_name}')
  
if __name__ == "__main__":
  import argparse
  parser = argparse.ArgumentParser()
  parser.add_argument('--local', action='store_true')
  args = parser.parse_args()
    
  if args.local:
    local_backup()
  else:
    backup()