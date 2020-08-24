#!/bin/bash
#########
#GAMENAME=Divinity Original Sin 2
#GAMEEXE=SupportTool
#GAMEID=435150
#PROTONVERSION=proton-5.0-10-rc4
#########

#GPFX="$STEAM_COMPAT_DATA_PATH/pfx"
GFD="$(awk -F 'common' '{print $1}' <<< "$PWD")common/$(awk -F 'common' '{print $NF}' <<< "$PWD" | cut -d'/' -f2)"

OPWD="$PWD"

if [ ! -d "$GFD/bin.bak" ]; then
	cd "$GFD" || die
	mv bin bin.bak
	ln -s DefEd/bin bin 
	cd bin || die
	mv SupportTool.exe SupportTool.exe.bak
	ln -s EoCApp.exe SupportTool.exe
	cd "$OPWD" || die
fi
