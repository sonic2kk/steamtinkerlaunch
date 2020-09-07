#!/bin/bash

function DoesNotHelp {
GPFX="$STEAM_COMPAT_DATA_PATH/pfx"
GCFGDIR="$GPFX/drive_c/users/steamuser/Local Settings/Application Data/Strange Brigade"
GCFG="$GCFGDIR/GraphicsOptions.ini"

if [ ! -d "$GCFGDIR" ]; then
	mkdir -p "$GCFGDIR"
fi

if [ ! -f "$GCFG" ]; then
	echo "D3D12 = 0" > "$GCFG"
else
	sed "s:D3D12 = 1:D3D12 = 0:g" -i "$GCFG"
fi

}


if [ ! -f "bin/StrangeBrigade_ORG.exe" ]; then
	mv "bin/StrangeBrigade.exe" "bin/StrangeBrigade_ORG.exe"
	cp "bin/StrangeBrigade_Vulkan.exe" "bin/StrangeBrigade.exe" 
fi
 
 
