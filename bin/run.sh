#!/bin/bash

printf "\033[32m______     _                    _     _ \e[0m\n"
printf "\033[32m| ___ \   | |                  | |   | |\e[0m\n"
printf "\033[32m| |_/ /_ _| |_      _____  _ __| | __| |\e[0m\n"
printf "\033[32m|  __/ _\` | \ \ /\ / / _ \| '__| |/ _\` |\e[0m\n"
printf "\033[32m| | | (_| | |\ V  V / (_) | |  | | (_| |\e[0m\n"
printf "\033[32m\_|  \__,_|_| \_/\_/ \___/|_|  |_|\__,_|\e[0m\n"
printf "\n"
printf "\033[32mUnofficial Palworld Server Docker Image\e[0m\n"
printf "\033[32mhttps://github.com/TheoBIET/palworld-docker\e[0m\n"
printf "\033[32mVersion : 0.1.0\e[0m\n"
printf "\033[32mAuthor : TheoBIET (from thijsvanloef/palworld-server-docker)\e[0m\n"
printf "\n"

printf "\e[0;32m#### CREATE BACKUP\e[0m\n"
if [ -d "backups" ]; then
  ./home/steam/server/bin/backup.sh
fi

printf "\e[0;32m#### VERIFY USER PERMISSIONS\e[0m\n"
if [[ ! "${PUID}" -eq 0 ]] && [[ ! "${PGID}" -eq 0 ]]; then
    usermod -o -u "${PUID}" steam
    groupmod -o -g "${PGID}" steam
else
    printf "\033[31mERROR: Running as root is not supported, please fix your PUID and PGID !\n"
    exit 1
fi

printf "\e[0;32m#### INSTALL/UPDATE PALWORD SERVER BINARIES\e[0m\n"
mkdir -p /palworld
chown -R steam:steam /palworld

if [ "${UPDATE_ON_BOOT}" = true ] || [ ! -f /palworld/steamapps ]; then
    su steam -c '/home/steam/steamcmd/steamcmd.sh +force_install_dir "/palworld" +login anonymous +app_update 2394010 validate +quit'
fi

printf "\e[0;32m#### SYNCING CONFIGURATION FILES\e[0m\n"
if [ ! -f /palworld/Pal/Saved/Config/LinuxServer/PalWorldSettings.ini ]; then
    printf "\e[0;32m#### MISSING CONFIGURATION FILES, CREATING...\e[0m\n"
    cd /palworld || exit
    su steam -c "timeout --preserve-status 15s ./PalServer.sh 1> /dev/null "
    sleep 5
    cd /home/steam || exit
fi

rm -rf  GeneratedConfig.ini
python scripts/gen-config.py

while [ ! -f GeneratedConfig.ini ]; do
    sleep 1
done

cp GeneratedConfig.ini /palworld/Pal/Saved/Config/LinuxServer/PalWorldSettings.ini

printf "\e[0;32m#### RCON CONFIGURATION\e[0m\n"
cat >~/.rcon-cli.yaml  <<EOL
host: localhost
port: ${RCON_PORT}
password: ${RCON_PASSWORD}
EOL

printf "\e[0;32m#### STARTING SERVER\e[0m\n"
START_COMMAND=$(python scripts/gen-command.py)
echo "${START_COMMAND}"
cd /palworld || exit
su steam -c "${START_COMMAND}"