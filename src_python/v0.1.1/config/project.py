import configparser
import sys

from pathlib import Path

from . import env

def _read_config(file: Path):
    parser = configparser.ConfigParser()

    # configparser hack: https://stackoverflow.com/a/26859985
    parser.read_string('[config]\n' + file.read_text())

    return parser['config']

NAME         = 'SteamTinkerLaunch'
DISPLAY_NAME = 'Steam Tinker Launch'
VERSION      = 'v11.12.20221211-1-py'
SCRIPT_NAME  = Path(sys.argv[0]).name
SCRIPT_DIR   = Path(__file__).resolve().parent.parent
STL_NAME     = 'stl'

GITHUB_URL     = 'https://github.com'
GITHUB_API_URL = 'https://api.github.com'
GITHUB_AUTHOR  = 'sonic2kk'
PROJECT_PAGE   = f'{GITHUB_URL}/{GITHUB_AUTHOR}/{NAME.lower()}'
PROJECT_WIKI   = f'{PROJECT_PAGE}/wiki'

START_DEBUG = True

HOME_CONFIG_DIR        = env.read_env_var('XDG_CONFIG_HOME', Path.home() / '.config')
STL_CONFIG_DIR         = HOME_CONFIG_DIR / NAME.lower()
STL_GLOBAL_CONFIG_FILE = STL_CONFIG_DIR / 'global.conf'
STL_GLOBAL_CONFIG      = _read_config(STL_GLOBAL_CONFIG_FILE)

WAIT_FOR_EXIT_AND_RUN = 'waitforexitandrun'

# old variable names
_PROGNAME     = NAME
_NICEPROGNAME = DISPLAY_NAME
_PROGVERS     = VERSION
_PROGCMD      = SCRIPT_NAME
_SHOSTL       = STL_NAME
_GHURL        = GITHUB_URL
_AGHURL       = GITHUB_API_URL
_PROJECTPAGE  = PROJECT_PAGE
_PPW          = PROJECT_WIKI
_CURWIKI      = _PPW
_STARTDEBUG   = START_DEBUG
_ONSTEAMDECK  = False

_STLCFGDIR       = STL_CONFIG_DIR
_STLDEFGLOBALCFG = STL_GLOBAL_CONFIG

_WFEAR = WAIT_FOR_EXIT_AND_RUN
