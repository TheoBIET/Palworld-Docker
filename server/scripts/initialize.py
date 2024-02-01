import sys
import functions
import time
from logger import log

print("""
\x1b[32;20m______     _                    _     _                       \x1b[0m
\x1b[32;20m| ___ \   | |                  | |   | |                      \x1b[0m
\x1b[32;20m| |_/ /_ _| |_      _____  _ __| | __| |                      \x1b[0m
\x1b[32;20m|  __/ _` | \ \ /\ / / _ \| '__| |/ _` |                      \x1b[0m
\x1b[32;20m| | | (_| | |\ V  V / (_) | |  | | (_| |                      \x1b[0m
\x1b[32;20m\_|  \__,_|_| \_/\_/ \___/|_|  |_|\__,_|                      \x1b[0m
\x1b[32;20m                                                              \x1b[0m
\x1b[32;20m                                                              \x1b[0m
\x1b[32;20mUnofficial Palworld Dedicated Server Image                    \x1b[0m
\x1b[32;20mRepository: https://github.com/TheoBIET/Palworld-Docker       \x1b[0m
\x1b[32;20mVersion: 0.2.0                                                \x1b[0m
\x1b[32;20mAuthor: TheoBIET                                              \x1b[0m
""", file=sys.stderr)

log.step('Server is initializing...')

log.step('Create /palworld directory and give permissions...')
functions.give_permissions_and_create_directory()

log.step('Check if steamcmd is installed...')
functions.check_steamcmd()

log.step('Install/Update Palworld server binaries...')
functions.download_server()

log.step(f'Setting up Palworld server...')
functions.setup_server()

log.step(f'Launching Palworld server...')
functions.launch_server()