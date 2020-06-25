# steamtinkerlaunch

steamtinkerlaunch or short stl - is a linux wrapper bashscript for steam.
With its help every proton game creates/reads a config file with its own custom launch settings like
* every env variable, like all PROTON* , DXVK* variables, MANGOHUD, RADV_PERFTEST, WINE* and so on
* radv mode, use gamemoderun, notifier, write config and exit, maybe more to come...

the idea is that you just have to edit the steam command line once (imho the editor is not very usable)
and every thing else can be changed easily with the parsed per-game config.
also a gui editor could be created (or even prelaunched - maybe depending on a boolean set) later for editing the custom settings.

# installation: 
this is one single bash script. just copy it wherever you want, f.e. /usr/local/bin/
to initially create a default config template "$HOME/.stl/default_template"
just call the script without any arguments
you might want to change the created config to your needs before use


usage: add this program to your steam game command line like 'stl %command%'
-----------------------------------
stl will check if a config file exists in "$HOME/.stl/" for the game exename and will source it if available
if it is not available it is created from a default config file "$HOME/.stl/default_template" (which is created from the stl script if not found)

most options shipped with the (autowritten) default config are commented out.
described are only the variables which come from stl, for all others please check their upstream project:
* JUSTWRITECFG=1 # set JUSTWRITECFG to 1 to exit after writing the default config for the selected game without starting the game - useful for quickly creating a configuration
* USEGAMEMODERUN=1 # start game with gamemoderun
* NOTY=notify-send # the notifier used
* RADV_PERFTEST=aco # radv mode - default is aco
