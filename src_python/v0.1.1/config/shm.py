
from pathlib import Path

# i assume this means "shared memory"
SHM = Path('/dev/shm')

STL_SHM     = SHM / 'steamtinkerlaunch'
STL_SHM_BAK = SHM / 'steamtinkerlaunch.bak'

MENU_TEMP    = STL_SHM / 'menutemp'
VERSION_FILE = STL_SHM / 'version'

STEAM_PATH_FILE = STL_SHM / 'steampaths.txt'

# old variable names
_MTEMP   = MENU_TEMP
_SHMVERS = VERSION_FILE