#!/bin/bash

echo -e "\e[1;32m ______     _                    _     _                      \e[0m"
echo -e "\e[1;32m | ___ \   | |                  | |   | |                     \e[0m"
echo -e "\e[1;32m | |_/ /_ _| |_      _____  _ __| | __| |                     \e[0m"
echo -e "\e[1;32m |  __/ _\` | \\ \\ /\\ / / _ \| '__| |/ _\` |                \e[0m"
echo -e "\e[1;32m | | | (_| | |\ V  V / (_) | |  | | (_| |                     \e[0m"
echo -e "\e[1;32m \_|  \__,_|_| \_/\_/ \___/|_|  |_|\__,_|                     \e[0m"
echo -e "\e[1;32m                                                              \e[0m"
echo -e "\e[1;32mUnofficial Palworld Dedicated Server Image                    \e[0m"
echo -e "\e[1;32mRepository: https://github.com/TheoBIET/Palworld-Docker       \e[0m"
echo -e "\e[1;32mVersion: Preview 0.3.0                                        \e[0m"
echo -e "\e[1;32m                                                              \e[0m"

DEBUG=true
if [ "$DEBUG" = "true" ]; then
  echo -e "\e[1;32m [INFO] Debugging mode is enabled \e[0m"
fi

/usr/bin/launch_palworld.sh --os=linux

if [ "$DEBUG" = "true" ]; then
  sleep infinity
fi