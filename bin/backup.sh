#!/bin/bash

DATE=$(date +"%Y-%m-%d_%H-%M-%S")

if [ ! -d "backups" ]; then
  mkdir backups
fi

FILE_PATH="backups/palworld-${DATE}.tar.gz"
tar -zcf "$FILE_PATH" "palworld/Pal/Saved/"
echo "Backup created at $FILE_PATH"
