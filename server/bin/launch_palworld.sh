#!/bin/bash

echo -e "\e[1;32m [2] Installing Palworld Dedicated Server \e[0m"

for i in "$@"; do
  case $i in
    --os=*)
      OS="${i#*=}"
      shift
      ;;
  esac
done

if [ -z "$OS" ] && [ "$OS" != "windows" ] && [ "$OS" != "linux" ]; then
  echo -e "\e[1;31m [ERROR] --os is required and must be either 'windows' or 'linux' \e[0m"
  exit 1
fi

is_first_run=false
latest_version_response=$(curl -s https://api.steamcmd.net/v1/info/2394010)
# https://api.steamcmd.net/v1/info/2394010 STATUS CODE 200 (without jq)
echo -e "\e[1;32m [INFO] GET https://api.steamcmd.net/v1/info/2394010 \e[0m"
latest_version=$(echo $latest_version_response | jq '.["data"]["2394010"]["depots"]["branches"]["public"]["buildid"]')
if [ -e /palworld/version.txt ]; then
  current_version=$(head -n 1 /palworld/version.txt)
fi

echo -e "\e[1;32m [INFO] Latest version: $latest_version \e[0m"
echo -e "\e[1;32m [INFO] Current version: $current_version \e[0m"

if [ "$latest_version" = "null" ]; then
  echo -e "\e[1;31m [ERROR] Unable to get latest version from SteamCMD API \e[0m"
  exit 1
fi

echo -e "\e[1;32m [2.1] Check SteamCMD installation \e[0m"
if [ -f /home/steam/steamcmd/steamcmd.sh ]; then
  echo -e "\e[1;32m [INFO] SteamCMD is correctly installed \e[0m"
else
  echo -e "\e[1;31m [ERROR] Steamcmd is not installed. Please contact the maintainer of this image. \e[0m"
  exit 1
fi

echo -e "\e[1;32m [2.2] Create /palworld directory and give permissions... \e[0m"
usermod -o -u $PUID steam
groupmod -o -g $PGID steam
mkdir -p /palworld
chown -R steam:steam /palworld

echo -e "\e[1;32m [2.3] Download and install Palworld Dedicated Server... \e[0m"
if [ -f /palworld/PalServer.sh ] && [ -e /palworld/version.txt ]; then
  echo -e "\e[1;32m [INFO] Installation found. Version : $current_version \e[0m"
else
  echo -e "\e[1;32m [INFO] No installation found. \e[0m"
  is_first_run=true
fi

if [ "$current_version" = "$latest_version" ] && [ "$is_first_run" = "false" ]; then
  echo -e "\e[1;32m [INFO] Palworld Dedicated Server is up to date \e[0m"
elif [ "$PALWORD_AUTOMATIC_UPDATE" == "false" ]; then
  echo -e "\e[1;32m [INFO] Automatic update is disabled. Skipping... \e[0m"
else
  if [ "$is_first_run" = "true" ]; then
    echo -e "\e[1;32m [INFO] First run detected. Installing Palworld Dedicated Server version $latest_version for $OS... \e[0m"
  else
    echo -e "\e[1;32m [INFO] New version detected. Updating Palworld Dedicated Server to version $latest_version for $OS... \e[0m"
  fi
  
  # TODO: Use $OS
  /home/steam/steamcmd/steamcmd.sh +@sSteamCmdForcePlatformType linux +@sSteamCmdForcePlatformBitness 64 +force_install_dir "/palworld" +login anonymous +app_update 2394010 validate +quit

  if [ -f /palworld/PalServer.sh ]; then
    echo -e "\e[1;32m [INFO] Palworld Dedicated Server has been updated to version $latest_version \e[0m"
    echo $latest_version > /palworld/version.txt
  else
    echo -e "\e[1;31m [ERROR] Palworld Dedicated Server installation failed \e[0m"
    exit 1
  fi
fi

echo -e "\e[1;32m [3] Launching Palworld Dedicated Server \e[0m"
# Check if config file exists
if [ ! -e $PALWORLD_CONFIG_FILE_PATH ]; then
  echo -e "\e[1;32m [INFO] Configuration file not found. Generating Default... \e[0m"
  su steam -c "timeout --preserve-status 15s /palworld/PalServer.sh 1> /dev/null"
  sleep 5
fi

echo -e "\e[1;32m [3.1] Applying Configuration... \e[0m"
python /home/steam/server/core/update-config.py

command=$(python /home/steam/server/core/start-command.py)
echo -e "\e[1;32m [3.2] Starting Palworld Server... \e[0m"
echo -e "\e[1;32m [COMMAND] ${command[@]} \e[0m"
su steam -c "${command[@]}" >> /palworld/logs/server.log 2>&1 &
sleep 5

if [ "$PALWORLD_WHITELIST_ENABLED" == "true" ]; then
  echo -e "\e[1;32m [3.3] Starting Players Listener with Whitelist Enabled... \e[0m"
  python /home/steam/server/core/players-listener.py --whitelist & 
  # PLAYERS_LISTENER_PID=$!
  # echo -e "\e[1;32m [INFO] Players Listener PID: $PLAYERS_LISTENER_PID \e[0m"
# TODO: Add headers to players-listener requests for listen other servers
# else
#   echo -e "\e[1;32m [3.3] Starting Players Listener with Whitelist Disabled... \e[0m"
#   python /home/steam/server/core/players-listener.py
fi