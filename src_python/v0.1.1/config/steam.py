from pathlib import Path

from . import env, project

def get_steam_path(filename: str) -> Path | None:

    dirs = [
        Path.home() / '.steam/root',
        Path.home() / '.steam/steam',
    ]

    for d in dirs:
        target = d / filename

        if target.exists():
            return target.resolve()
    
    else:
        # writelog "WARN" "${FUNCNAME[0]} - '$2' not found for variable '$1' in '$HSR' or '$HSS'!"
        return None
    
def get_user_id(user_data: Path):
    user_id = project.STL_GLOBAL_CONFIG.get('STEAMUSERID', None)

    if not user_id:

        if not user_data.exists():
            raise FileNotFoundError(f'Steam \'{user_data}\' directory not found, other variables depend on it')

        # this works for 99% of all users, because most do have 1 steamuser on their system
        uid_dir = list(user_data.iterdir())[0]

        return uid_dir.name

# TODO: cash this in steampaths.txt?

SHARE_ROOT          = get_steam_path('')
USER_DATA           = get_steam_path('userdata')
STEAM_APPS          = get_steam_path('steamapps')
STEAM_APPS_COMMON   = get_steam_path('steamapps/common')
CONFIG_VDF          = get_steam_path('config/config.vdf')
LIBRARY_FOLDERS_VDF = get_steam_path('steamapps/libraryfolders.vdf')
APP_INFO_VDF        = get_steam_path('appcache/appinfo.vdf')
PACKAGE_INFO_VDF    = get_steam_path('appcache/packageinfo.vdf')
COMPAT_TOOLS        = get_steam_path('compatibilitytools.d')
GAMES               = get_steam_path('steam/games')

STEAM_COMPAT_CLIENT_INSTALL_PATH = env.read_env_var('STEAM_COMPAT_CLIENT_INSTALL_PATH', SHARE_ROOT)

STEAM_USER_ID     = get_user_id(USER_DATA)
STEAM_USER_CONFIG = USER_DATA / STEAM_USER_ID / 'config'
LOCAL_CONFIG_VDF  = STEAM_USER_CONFIG / 'localconfig.vdf'

# old variable names
_SROOT           = SHARE_ROOT
_SUSDA           = USER_DATA
_DEFSTEAMAPPS    = STEAM_APPS
_DEFSTEAMAPPS    = STEAM_APPS
_CFGVDF          = CONFIG_VDF
_LFVDF           = LIBRARY_FOLDERS_VDF
_FAIVDF          = APP_INFO_VDF
_PIVDF           = PACKAGE_INFO_VDF
_STEAMCOMPATOOLS = COMPAT_TOOLS
_ICODIR          = GAMES
_SUIC            = STEAM_USER_CONFIG
_FLCV            = LOCAL_CONFIG_VDF