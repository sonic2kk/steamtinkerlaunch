import os

from pathlib import Path


def read_env_var(name: str, default=None):
    return os.environ.get(name, default)

# I can't decipher how STL bash detects steam deck, so I'm using this instead
# https://www.reddit.com/r/SteamDeck/comments/telfda/comment/i6pfkpz/?utm_source=share&utm_medium=web2x&context=3
def check_on_steam_deck():
    dir = Path('/sys/devices/virtual/dmi/id/')

    if not dir.exists():
        return False
    
    vendor = dir / 'board_vendor'
    name   = dir / 'board_name'

    if not vendor.exists() and name.exists():
        return False
    
    if 'Valve' in vendor.read_text() and 'Jupiter' in name.read_text():
        return True
    else:
        return False
    

def check_flatpak():
    return read_env_var('FLATPAK_ID') == 'com.valvesoftware.Steam'
        