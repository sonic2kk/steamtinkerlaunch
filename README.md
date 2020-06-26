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
to initially create a default config template "$HOME/.stl/default_template.conf"
and a default global config "$HOME/.stl/global.conf"
just call the script without any arguments
you might want to change the created config to your needs before use


usage: add this program to your steam game command line like 'stl %command%'
-----------------------------------
stl will check if a config file exists in "$HOME/.stl/$GAMENAME.conf" for the game and will source it if available
if it is not available it is created from the default config file (which is created from the stl script if not found)

most options shipped with the (autowritten) default config are commented out.
described are only the variables which come from stl, for all others please check their upstream project:

global settings:

* JUSTWRITECFG=1 							# set to 1 to exit after writing the default config for the selected game without starting the game - useful for quickly creating a configuration
* CREATESTLDXVKCFGTMPL						# create an empty $STLDXVKCFG_tmpl for easier editing when required
* STRACEDIR=/tmp/ 							# the base strace path used to optionally dump strace logs
* STLLOG=/tmp/$(basename "$0").log			# the stl logfile
* WRITELOG=0								# write logfile if enabled


per game settings:

* USEGAMEMODERUN=1							# start game with gamemoderun
* NOTY=notify-send							# the notifier used
* RADV_PERFTEST=aco							# radv mode - default is aco
* STRACERUN=0 								# if set to one stl will write a strace log of the launched game
* STRACEOPTS=-f -t -e trace=file			# the strace options used for strace


strace:
when STRACERUN is enabled make sure
/proc/sys/kernel/yama/ptrace_scope is set to 0
else your user will get access denied when trying to attach a process
either "echo 0 > /proc/sys/kernel/yama/ptrace_scope" as root or enable it persistent in sysctl
