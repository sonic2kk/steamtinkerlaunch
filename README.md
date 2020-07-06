# SteamTinkerLaunch

SteamTinkerLaunch or short **stl** - is a linux wrapper script for steam.
It creates/reads game config files on the fly, making it very easy to setup and use,
but still giving you the possibility to fully customize game configurations live on game start. 
The idea is that you just have to edit the steam command line once (imho the editor is not very usable)
and everything else can be changed and controlled easily using **stl**

## How to use

### general usage:
Just add this program to your steam game command line like:
'stl %command%'

### game specific use:

The base gamedirectory `STLCFGDIR` will be either `XDG_CONFIG_HOME/stl` or `$HOME/.config/stl` if `XDG_CONFIG_HOME` not set.

When starting a game with **stl** it will check if a config file exists in `$STLCFGDIR/gamecfgs/$SteamAppId.conf` for the game
if it is not available it is created from the default config file (which is automatically created if not found).

When starting the game a small requester will popup (default 2 seconds).
When you want to change settings for that game press space to open the game configuration and adjust it to your needs.
The game start will wait until you're done and your changes are used on the fly.


## Installation: 
This is one single bash script. Just copy it whereever you want, f.e. /usr/local/bin/

When you call the script without any arguments from commandline
it will initially create the default config structure
`$STLCFGDIR/default_template.conf`
and a default global config
`$STLCFGDIR/global.conf`

As `$STLCFGDIR/default_template.conf` is the template for creating the game configs 
you might want to adjust its options to your needs before use.


## Quickstart:
In the shipped default configs almost everything is disabled.
* at least make sure that STLEDITOR is a valid text editor (per default set to "geany") in `$STLCFGDIR/global.conf`
Also enable everything you want in the freshly created
`$STLCFGDIR/default_template.conf`

## Features:

* **env variables** can be easily set for every single game (f.e `PROTON`* , `DXVK`* variables, `MANGOHUD`, `RADV_PERFTEST`, `WINE`...)
* **custom program** launch before or instead the game itself (also windows exes)
* **winetricks**
* **winecfg**
* **gamemoderun**
* **notifier**
* **strace**
* **editor hotkey** for editing the gameconfig
* **open protondb** page for the launched game with the editor
* **automatic ReShade installation and configuration** for launched game
* **automatic Depth3D shader installation
* **basic vkBasalt configuration using Depth3D 
* **automatically play regular games in side-by-side mode in VR! (including "sbs tweaks"**
* **tweaks**

# Requirements:

The script itself doesn't have any special dependencies 

For the optional features you need:
- strace
- zenity (optional, `STEAM_ZENITY` is used)
- gamemoderun
- mangohud
- winetricks
- wget, unzip for optional reshade download, git for pulling optional shaders
- xdotool, xwininfo, vr-video-player for playing regular games side-by-side in VR
- your favourite editor for editor mode and otionally xdg-open for opening the protondb url of started game
- vkbasalt

## Configuration:

Most options shipped with the (autowritten) default config are commented out.
Described are only the variables which come from **stl**, for all others please check their upstream project:

### Global Settings:

`$STLCFGDIR/global.conf`
- `LOGDIR`: default logfile dir
- `WRITELOG`: write logfile if enabled
- `STLEDITOR`: the texteditor to use for opening the gameconfig
- `WAITEDITOR`: wait `WAITEDITOR` seconds for a keypress to open the texteditor `STLEDITOR` with the game config; **can be overridden in the gameconfig**
- `PROTONDB`: set `PROTONDB` to 1 to also directly xdg-open the protondb page](https://www.protondb.com/) for the game when starting the editor `STLEDITOR`
- `PDBURL`: protondb base url - for optional `PROTONDB`
- `VRVIDEOPLAYER`: vr-video-player - the program used to play regular games in **VR**
- `CREATESTLDXVKCFGTMPL`: create an empty `STLDXVKCFG`_tmpl for easier editing when required
- `STRACEDIR`: the base strace path used to optionally dump strace logs
- `STLLOG=/tmp/$(basename "$0").log`: the stl logfile
- `USETWEAKS`: set to 1 to override settings with tweaks when found
- `CREATETWEAKS`: set to 1 create tweak config templates (just the header) for the launched game if not found
- `DEPTH3DURL`:Depth3D git project
- `CLONE_DEPTH3D`: allow git clone of Depth3D shaderfiles
- `DEPTH3DSRCDIR`: Depth3D sourcefiles
		
If you do not want to start the editor requester on game launch generally just set `WAITEDITOR=0` - it will be skipped then for all games

### Functions in detail:

#### Custom Game Launch:
When enabled you can start custom programs easily with the following per-game config options:

- `RUN_CUSTOMCMD`: set to 1 to start the custom command `CUSTOMCMD`
- `CUSTOMCMD`: start this custom command
- `CUSTOMCMD_ARGS`: start `CUSTOMCMD` command with those args
- `ONLY_CUSTOMCMD`: set to 1 to only start `CUSTOMCMD` and not the game command itself
- `FORK_CUSTOMCMD`: set to 1 to fork the custom `CUSTOMCMD` into the background and continue with starting `%command%`

#### additional game arguments:
- `GAMEARGS`: additional command line args for the game itself

#### winetricks
- `RUN_WINETRICKS`: set to 1 to start winetricks gui before game launch

#### winecfg
- `RUN_WINECFG`: set to 1 to start winecfg before game launch

#### [gamemode](https://github.com/FeralInteractive/gamemode)
- `USEGAMEMODERUN`: set to 1 to start game with gamemoderun

#### notifier
- `NOTY`: the notifier used

#### [MangoHud](https://github.com/flightlessmango/MangoHud)
* - `MANGOHUD`: set to 1 to enable mangohud - does nothing in stl itself, but just exports the upstream variable

#### radv [Mesa](https://www.mesa3d.org/)
- `#RADV_PERFTEST=aco`: aco is default starting with mesa 20.2 

#### strace
- `STRACERUN`: if set to 1 stl will write a strace log of the launched game
- `STRACEOPTS`: the strace options used for strace

When `STRACERUN` is enabled make sure
`/proc/sys/kernel/yama/ptrace_scope` is set to 0.
else your user will get access denied when trying to attach a process.
Either 
`echo 0 > /proc/sys/kernel/yama/ptrace_scope`
as root or enable it persistent in sysctl

#### [ReShade](https://reshade.me)
- `INSTALL_RESHADE`: set to 1 to automatically install reshade into the selected game dir.
- `USERESHADE`: set to 1 to start game with ReShade enabled

	
The required `$STLCFGDIR/reshade.conf` is autogenerated on the first run with `INSTALL_RESHADE` enabled.
If `DOWNLOAD_RESHADE` is set to 1 all required files for ReShade are downloaded once into `RESHADESRCDIR`
of course you can install all files manually as well. make sure to rename all files correctly:

**64bit** `d3dcompiler_47.dll`: -> d3dcompiler_47_64.dll
**32bit** `d3dcompiler_47.dll`: -> d3dcompiler_47_32.dll
`ReShade64.dll`, `ReShade32.dll`: renaming not required as they will be placed in the gamedir under the required name


The required architecture is autodetected from the game.exe and the matching files are copied from RESHADESRCDIR into the selected game dir
both downloadfiles and basic configuration were taken from [r/linux_gaming](https://www.reddit.com/r/linux_gaming/comments/b2hi3g/reshade_working_in_wine_43) 

#### [vkBasalt](https://github.com/DadSchoorse/vkBasalt)
- `ENABLE_VKBASALT`: set to 1 to start the game with vkbasalt
- `VKBASALT_CONFIG_FILE`: the vkbasalt source config file - it points per default to `STLCFGDIR/vkBasalt.conf` and is autogenerated if not found
The autogenerated `VKBASALT_CONFIG_FILE` points to the files from `RESHADE_DEPTH3D` so it should have been at least checked out once with `CLONE_DEPTH3D`

#### [Depth3D](https://github.com/BlueSkyDefender/Depth3D)
 - `RESHADE_DEPTH3D`: set to 1 to install ReShade Depth3D Shader into gamedir

If `CLONE_DEPTH3D` is set to 1 the git repository will be automatically cloned/pulled (only when `RESHADE_DEPTH3D=1`) to `DEPTH3DSRCDIR`.

With `RESHADE_DEPTH3D` enabled `Overwatch.fxh`, `SuperDepth3D.fx`, `SuperDepth3D_VR.fx` from Depth3D are copied to the gamedir.
when the game started just create a initial profile by selecting the autodetected `SuperDepth3D_VR.fx`

SBS-VR (regular games side-by-side in **VR**):
--------------------------------------------

Currently experimental - it often works very good and sometimes not.
For me it works good enough to have much fun with it.
- sometimes setting the focus back to the main window or adjusting the direction of the vr view automatically fails (timing)
- sometimes steamvr doesn't start correctly (probably related to the ancient upstream bug, where games fail to start steamvr if not running yet)
- in rare cases even amdgpu fails, but that is very likely a steamvr bug as well (timing?)

To use it you just have to enable `RUNSBSVR=1` in the game specific config, with some luck everything else is done (almost) automatically:

- start SteamVR
- start the game (game settings required to enable sbs are not automatically enabled! added an auto config setting for **Crysis 2** though )
- start [vr-video-player](https://git.dec05eba.com/vr-video-player)
- when exiting the game, vr-video-player wil be closed as well.

**
to start SBS-VR with a complete new configuration with vkBasalt you need to do the following:
- ( allow cloning the Depth3D shader repo `DEPTH3DSRCDIR` by setting `CLONE_DEPTH3D` in the global config `$STLCFGDIR/global.conf` at least once )
- start the game, enter the editor and comment in `ENABLE_VKBASALT=1` and `RUNSBSVR=1`
- exit the editor and if everything goes well the game should start in SBS-VR now
**


Some games start own launchers before the actual game and autodetecting the correct window is not easy
(searching for the biggest window from the game process, which may not be always the correct one)
That's why you can configure the exact window name to look for, which makes the whole process much more straighter.

There are also specific sbs game config overrides, which have optimal settings for **VR** (f.e. predefined game window, or launcher skips).

here's an example config for trine 2 `STLCFGDIR/sbs/35720.conf`

```
#########
#GAMENAME=Trine 2
#GAMEEXE=trine2_launcher
#GAMEID=35720
RUN_CUSTOMCMD=1
CUSTOMCMD=trine2_32bit.exe
ONLY_CUSTOMCMD=1
VRGAMEWINDOW=Trine 2
```

Means, when `RUNSBSVR=1` is set in the main Trine2 config file it will autodetect above sbs tweak config and use the defined variables:
Trine 2 won't start it's original launcher (`ONLY_CUSTOMCMD=1`), but only the custom command `trine2_32bit.exe` and will wait for a `Trine 2` window to open in **VR**

So in general sbs configs are automatically loaded when found and override settings in the mainconfig
so you just have to enable `RUNSBSVR=1` in `STLCFGDIR/gamecfgs/35720.conf` and everything else is configured automatically.

I added some initial preconfigured sbs tweak configs into this project.
For now just copy them into your `STLCFGDIR/sbs/` directory if you want to use them.

some gamewindows are causing trouble with vr-video-player (f.e. reproducable with `Giana Sisters 2D (350770)`).
I try to exit the SBSVR routines as graceful as possible, keeping the game open.

To play regular games in VR which do not have builtin SBS, you can either enable ReShade or vkBasalt,
where Reshade probably has more features and vkBasalt is probably more stable

#### Tweaks
function similar to above sbs override.
- `USETWEAKS`: set to 1 to override settings with tweaks when found
When enabled (gameconfig overrides global config) an existing tweak config in `STLCFGDIR/sbs/$SteamAppId.conf`
overrides the settings in the main gameconfig. Using this it would be possible to contribute tweak configs required to get games to work hazzlefree out of the box to the community.
Only useful if some people contribute gamespecific tweaks, else this will vanish:
global settings are `USETWEAKS` and `CREATETWEAKS` (see above).
Depending on general contribution of community tweak configs `USETWEAKS` could be also expanded with a game specific `TWEAKCMD` -
community contributed scripts with commands required to get a game working (install deps via winetricks, create configs and so on)

I added a preconfigured tweak config for 'SonicGenerations (71340)' into this project, which disables ESYNC and FSYNC required to play the game.
For now just copy tweak configs into your `STLCFGDIR/tweaks/` directory if you want to use them.
If you use/create tweaks make sure to retest your game with later proton versions without the tweak (`USETWEAKS=0`) and report upstream if the bug is fixed!
The used proton Version is automatically written into the tweak file when created with `CREATETWEAKS`
