from pathlib import Path

USR_DIR     = Path('/usr')
USR_BIN_DIR = USR_DIR / 'bin'
FLATPAK_BIN = Path('/app/utils/bin')

# old variable names
_FPBIN  = FLATPAK_BIN
_PREFIX = USR_DIR