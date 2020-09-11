#!/bin/bash
# Crysis 2 enable SBS in game config

function writelog {
# dummy writelog
	echo "$*"
}

GPFX="$STEAM_COMPAT_DATA_PATH/pfx"
CRY2CFG="$GPFX/drive_c/users/steamuser/Saved Games/Crysis2/game.cfg"

if [ -f "$CRY2CFG" ]; then
	writelog "HACK" "${FUNCNAME[0]} - SteamID $AID Crysis 2 found - editing game config $CRY2CFG to enable Stereo Support"
	echo "r_StereoSupportAMD=1" >> "$CRY2CFG"
	awk -i inplace '!visited[$0]++' "$CRY2CFG"
else
	writelog "SKIP" "${FUNCNAME[0]} -HACK failed - SteamID $AID Crysis 2 found but game config $CRY2CFG not found to insert Stereo Support - restarting the game should fix this"
fi
