# steamtinkerlaunch

steamtinkerlaunch or short stl - is a linux wrapper bashscript for steam
with its help every proton game creates/reads its own custom launch settings like
* every env variable, like PROTON* , DXVK*, MANGOHUD, RADV_PERFTEST, WINE*

usage: add this program to your steam game command line like 'stl %command%'
-----------------------------------
stl will check if a config file exists in $STLCFGDIR for the game exename and will source it if available
if it is not available it is created from a default config file $STLDEFCFG (which is created from the createDefaultCfg function if not available)

most options shipped with the (autowritten) default config are commented out.
described are only the variables which come from stl, for all others please check their upstream project:
* JUSTWRITECFG=1 # set JUSTWRITECFG to 1 to exit after writing the default config for the selected game without starting the game - useful for quickly creating a configuration
* USEGAMEMODERUN=1 # start game with gamemoderun
* NOTY=notify-send # the notifier used
* RADV_PERFTEST=aco # radv mode - default is aco
