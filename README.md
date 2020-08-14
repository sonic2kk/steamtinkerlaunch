**SteamTinkerLaunch** (short **stl**) is a Linux wrapper tool for use with the Steam client
which allows to customize and start tools and options for games quickly on the fly.

By using a versatile configuration structure it is both easy to setup and flexible.

The steam command line has to be edited once and for all (imho the editor is not very usable)
and everything else can be changed and controlled easily subsequently using **stl**

## How to use

### General usage
Just add this program to your steam game command line like:
'stl %command%'

![stl starter](https://media.giphy.com/media/gghbOGB41ggEsrq3KM/giphy.gif)

*A little script which automatically does this for every game in the Steam library can be found [here](https://gist.github.com/frostworx/36bd76e705a0c87af523fa57cfeebaf8)*

### Game specific use
When starting a game a small requester will popup.
If within a short waiting period (default 2 seconds) the spacebar is pressed it will open an editor with the games individual config file.
When done with configuring (or when the requester timeouts) the game will be started regularly with all tools and options configured.

## Installation
This is one single bash script. Just copy it wherever you want (f.e. '/usr/local/bin/') and make it executable:
`chmod +x stl`
The enclosed directories containing optional configuration files should be dropped into '/usr/share/stl/'

If you are on Arch Linux you can install **stl** from **AUR**
`yay -S steamtinkerlaunch`

## Quickstart
When **stl** is started for the first time it will create its default [configuration](#Configuration) structure.
At least make sure that `STLEDITOR` points to an installed graphical text editor in [`$STLCFGDIR/global.conf`](#global.conf)
(set to "xdg-open" by default, which should just work in most cases)
Also enable everything you want to use generally for your games in [`$STLCFGDIR/default_template.conf`](#default_template.conf)

## Features

*(no special order)*

* **[ENV Variables](#ENV Variables)** can be easily set for every single game (f.e `PROTON`* , `DXVK`* , `MANGOHUD`, `RADV_PERFTEST`, `WINE`...)
* **[Custom Program](#Custom Program)** launch custom programs before or instead the game itself (also windows exes)
* **[winetricks](#Winetricks)** start winetricks before game launch *(gui or silent)*
* **[winecfg](#Winecfg)** start winecfg before game launch
* **[GameMode](#GameMode)** start/stop gamemoderun per game
* **[Notifier](#Notifier)** start/stop notify message per game
* **[Strace](#Strace)** for easily debugging a game
* **[Editor Hotkey](#Editor)** for editing the gameconfig
* **[ProtonDB](#Editor)** automatically open page for the launched game with the editor
* **[ReShade](#ReShade)** automatic installation and configuration
* **[Depth3D](#Depth3D)** automatic shader installation
* **[vkBasalt](#vkBasalt)** basic vkBasalt configuration
* **[SBS-VR](#Side-by-Side VR)** automatically play regular games in side-by-side mode in VR!
* **[Tweaks](#Tweaks)** community mini configfiles to automatically start problematic games ootb
* **[32bit wineprefix](#32bit Wineprefix)** force 32bit `WINEPREFIX`
* **[Nyrna](#Nyrna)** start/stop ReplaySorcery per game
* **[ReplaySorcery](#ReplaySorcery)** start/stop ReplaySorcery per game
* **[Custom Game Launch](#Custom Game Launch)** easy simple custom game launch
* **[NetMon](#Network Monitoring)** basic network monitoring
* **[Boxtron](#Boxtron)** support via steam `DOSBox` category
* **[Roberta](#Roberta)** support via steam `ScummVM` category
* **[Luxtorpeda](#Luxtorpeda)** support via steam `Luxtorpeda` category
* **[Vortex Mod Manager](#Vortex)** via steam `Vortex` category

## Requirements
*(no special order)*

The script itself doesn't have any special dependencies.

For the optional features you need:
- [strace](#Strace)
- [Gamemode](#GameMode)
- [MangoHud](#MangoHud)
- [winetricks](#Winetricks)
- wget, unzip for optional [Reshade](#ReShade) download, git for pulling optional shaders ([Depth3D](#Depth3D))
- xdotool, xwininfo, vr-video-player for playing regular games side-by-side in VR ([SBS-VR](#Side-by-Side VR))
- a graphical text editor and optionally a internetbrowser see [global.conf](#global.conf)
- [vkBasalt](#vkBasalt)
- [Nyrna](#Nyrna)
- [ReplaySorcery](#ReplaySorcery)
- wmctrl to optionally minimize/maximize all open windows on game start/stop
- netstat from net-tools for basic network monitoring
- [Boxtron](#Boxtron) and dosbox to optionally start dos games with linux native dosbox
- ScummVM to optionally start compatible games natively using [Roberta](https://github.com/dreamer/roberta)
- [luxtorpeda-dev](https://github.com/luxtorpeda-dev/luxtorpeda) or [Luxtorpeda](https://github.com/dreamer/luxtorpeda) to optionally start supported games with a linux native binary
- wine for optional [Vortex](#Vortex) support


## Configuration
All configuration files are self-contained documented and always growing, so not every option is documented in here.
For a general overview what can be configured, just check the [Features](#Features)

### Configuration Locations

#### User Configuration

The main user configuration directory `STLCFGDIR` can be found under
`$HOME/.config/stl` (or `XDG_CONFIG_HOME/stl` if `XDG_CONFIG_HOME` is set).

When started for the first time **stl** will initially create this default configuration structure:

        `STLCFGDIR`/
        ├── [categories](#Steam Categories)
        ├── [default_template.conf](#default_template.conf)
        ├── [downloads](#Downloads)
        ├── [downloads](#Downloads)/[Depth3D](#Depth3D)
        ├── [gamecfgs](#Game Configurations)
        ├── [global.conf](#global.conf)
        ├── [logs](#Logs)
        ├── [logs](#Logs)/[stl.log](#Logs)
        ├── [tweaks](#Tweaks)
        ├── [vortex](#Vortex)      
        └── [vortex](#Vortex)/[vortex.conf](#vortex.conf)

#### Systemwide Configuration
The systemwide configuration directory `SYSTEMSTLCFGDIR` can be found under `/usr/share/$PROGCMD` *(/usr/share/stl/)*

All configs used here are read first, so user configs override them if required.
System-wide configs help to keep configuration easy and get things to work ootb.
f.e. there are preconfigured [Steam Category](#Steam Categories),
custom per-game [registry](#Registry) files, which are autodetected and applied *(when `REGEDIT` is 1)*,
*community contributed* [tweaks](#Tweaks) which make sure specific games work ootb using the provided configuration options,
*community contributed* [sbs tweaks](#SBS Tweaks) which make sure specific games work ootb in [SBS-VR](#Side-by-Side VR) mode using the provided configuration options


### default_template.conf

`STLDEFGAMECFG` *(`$STLCFGDIR/default_template.conf`)*

Contains the default configurations options used as template for every new game specific configfile.
Most options are disabled by default. To deploy appropriate global options early this file should be adjusted early.

### global.conf
`STLDEFGLOBALCFG` *(`$STLCFGDIR/global.conf`)*

Contains universal configuration options used all games, f.e.
file paths, command line options for supported 3rd party programs, but also general "behavior" settings
*(f.e. [Logs](#Logs) mode or timeout for the [Editor](#Editor))*
or which default programs to use
*(f.e. which `BROWSER` to use for opening [ProtonDB](#Editor) together with the `STLEDITOR` (default 'xdg-open') [Editor](#Editor))*

### Game Configurations

`$STLGAMECFG` *(`$STLCFGDIR/gamecfgs/$SteamAppId.conf`)*

When starting a game using **stl** the game specific config file is searched in `STLGAMEDIR`
and created if not available from the default config file *(which in turn is automatically created as well if not found)*.
Additional individual configs can be loaded via [Tweaks](#Tweaks) and [SBS Tweaks](#SBS Tweaks)
Any option configured in here and also in [global.conf](#global.conf) is overridden by this config.


### Steam Categories
**stl** parses the Steam categories of the started game and examines if a associated **stl** configuration file exists
under the same name (case-sensitive, but written uppercase in Steam **!**)

If a configuration file is found it is initialized as additional config file.

This makes it easy to create "Confifuration categories" by
- simply creating a Steam Category
- creating a categories configfile under the same name and defining settings in it
- adding a game to the category to use those settings automatically

Category Configuration Files are searched in the [User Configurations](#User Configuration) `STLCATEGORYDIR` *(`STLCFGDIR`/categories)*
or in the [system-wide](#Systemwide Configuration) dir `GLOBALCATEGORYDIR` *(`SYSTEMSTLCFGDIR/categories)`*
where some category files are already preconfigured:

a game in the corresponding category
- **DOSBox.conf** is started automatically with linux native dosbox provided by [Boxtron](#Boxtron)
- **Luxtorpeda.conf** is started automatically with linux native binary provided by [Luxtorpeda](#Luxtorpeda)
- **ReShadeVR.conf** is started automatically in [SBS-VR](#Side-by-Side VR) mode using [ReShade](#ReShade)
- **SBS-VR.conf** is started automatically in [SBS-VR](#Side-by-Side VR) mode without Shader (for games with builtin Stereoscopic3D support)
- **ScummVM.conf** is started automatically with linux native scummvm provided by [Roberta](#Roberta)
- **Vortex.conf** is started automatically with the [Vortex](#Vortex) Mod Manager
- **vkVR.conf** is started automatically in [SBS-VR](#Side-by-Side VR) mode using [vkBasalt](#vkBasalt) and 

Multiple Category Configuration Files are possible, they are loaded one after another, with the last one overriding settings also found in the previous files.
All settings which are also configured in `$STLGAMECFG` are overridden (but not overwritten).

### Tweaks

- `USETWEAKS`: set to 1 to override settings with tweaks when found
When enabled *([User Configurations](#User Configuration) overrides [system-wide](#Systemwide Configuration)* an existing tweak config `TWEAKCFG` in `TWEAKDIR`
overrides the settings in the [`$STLGAMECFG`](#Game Configurations).
Using this it would be possible to contribute tweak configs required to get games to work hazzlefree out of the box to the community.
With `CREATETWEAKS` a default template tweak file is autogenerated on game launch, to make creating one a bit easier.

Depending on general contribution of community tweak configs `USETWEAKS` could be also expanded with a game specific `TWEAKCMD` -
community contributed scripts with commands required to get a game working *(f.e. move or rename files)*

Some systemwide tweaks can already be used (see [Installation](#Installation)).

If you use/create tweaks make sure to retest your game with later proton versions without the tweak (`USETWEAKS=0`) and report upstream if the bug is fixed!
The used proton Version is automatically written into the tweak file when created with `CREATETWEAKS`
user tweak-files in `TWEAKDIR` override global ones in `GLOBALTWEAKDIR`


### SBS Tweaks

Game specific config files `SteamAppID.conf` both in and [system-wide](#Systemwide Configuration) *(`GLOBALSBSTWEAKDIR`)* and [User Configurations](#User Configuration) *(`SBSTWEAKDIR`)*
with optimal settings for [SBS-VR](#Side-by-Side VR) (f.e. launcher skips using the game exe as custom command).

Here's an example config for trine 2 `STLCFGDIR/sbs/35720.conf`

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

Means, when `RUNSBSVR` is not 0 in the main Trine2 config file it will autodetect above sbs tweak config and use the defined variables:
Trine 2 won't start it's original launcher (`ONLY_CUSTOMCMD=1`), but only the custom command `trine2_32bit.exe` and will wait for a `Trine 2` window to open in **VR**

So in general sbs configs are automatically loaded when found and override settings in the mainconfig
so you just have to enable `RUNSBSVR` in `STLCFGDIR/gamecfgs/35720.conf` and everything else is configured automatically.


### vortex.conf
See [Vortex Configuration](#Vortex Configuration)


### Downloads
The `STLDLDIR` directory stores all downloads started through **stl**
As of writing those are
[Depth3D](#Depth3D) shader files
[Vortex](#Vortex) the installation setup exe
[ReShade](#ReShade) ReShade itself and required d3dcompiler dlls

### Logs
Logs are written into the `LOGDIR` defined in the [global.conf](#global.conf).
The verbosity of the logfile depends on `WRITELOG` *(write logfile if not 0, increase verbosity from 1-2 (1:less, 2:all))*
also defined in the [global.conf](#global.conf).
There are several logfiles, those which are written mostly are the game specific ones *($SteamAppId.log)*

## Features in detail:

#### Custom Program

When enabled you can start custom programs easily with the following per-game config options:

- `RUN_CUSTOMCMD`: set to 1 to start the custom command `CUSTOMCMD`
- `CUSTOMCMD`: start this custom command
- `CUSTOMCMD_ARGS`: start `CUSTOMCMD` command with those args
- `ONLY_CUSTOMCMD`: set to 1 to only start `CUSTOMCMD` and not the game command itself
- `FORK_CUSTOMCMD`: set to 1 to fork the custom `CUSTOMCMD` into the background and continue with starting `%command%`

If only `RUN_CUSTOMCMD` is enabled, but `CUSTOMCMD` is empty, a requester will open where a executable file can be selected.
This selected file is automatically written into the [in game configfile `$STLGAMECFG`](#Game Specific Configuration).

If string `CUSTOMCMD` can't be found as file in either `PATH`, in game dir or as absolute filepath the requester will open as well.


#### Winetricks
[Winetricks](https://wiki.winehq.org/Winetricks)
GUI:
Set `RUN_WINETRICKS` to 1 to start winetricks gui before game launch

Silent winetricks installation:
- `WINETRICKSPAKS`: install all packages in WINETRICKSPAKS silently with winetricks

#### Winecfg
- `RUN_WINECFG`: set to 1 to start winecfg before game launch


#### Boxtron

[Boxtron](https://github.com/dreamer/boxtron):

The global configs `BOXTRONCMD` and `BOXTRONARGS` in the [global.conf](#global.conf) need to be set correcty initially.
It should not be necessary to change the default `ROBERTAARGS`.
Defaults are:
**
BOXTRONCMD=/usr/share/boxtron/run-dosbox
BOXTRONARGS=--wait-before-run
**
which is at least valid if you are on Arch Linux and installed boxtron from AUR.

To start a game with boxtron either set `USEBOXTRON` in the [gameconfig `$STLGAMECFG`](#Game Configurations) or put the game into the [steam category](#Steam Categories) "DOSBox"
Alternatively duplicate the file to a different name which you want to use as category name, ideally into [`STLCATEGORYDIR`.](#Steam Categories).

#### Roberta

[Roberta](https://github.com/dreamer/roberta):

The global configs `ROBERTACMD` and `ROBERTAARGS` in the [global.conf](#global.conf) need to be set correcty initially.
It should not be necessary to change the default `ROBERTAARGS`.
Defaults are:
**
ROBERTACMD=$HOME/.local/share/Steam/compatibilitytools.d/roberta/run-vm
ROBERTAARGS=--wait-before-run
**
which is at least valid if you installed roberta manually.

To start a game with roberta either set `USEROBERTA` in the [gameconfig `$STLGAMECFG`](#Game Configurations) or put the game into the [steam category](#Steam Categories) "ScummVM"
Alternatively duplicate the file to a different name which you want to use as category name, ideally into [`STLCATEGORYDIR`.](#Steam Categories-dir).

#### Luxtorpeda
[Luxtorpeda-dev](https://github.com/luxtorpeda-dev/luxtorpeda) or (untested) the [main branch](https://github.com/dreamer/luxtorpeda)

The global configs `LUXTORPEDACMD` and `LUXTORPEDAARGS` in the [global.conf](#global.conf) need to be set correctly initially.
It should not be necessary to change the default `LUXTORPEDAARGS`.

Defaults are:
**
LUXTORPEDACMD=$HOME/.local/share/Steam/compatibilitytools.d/luxtorpeda/luxtorpeda
LUXTORPEDAARGS=wait-before-run
**
which is at least valid if you installed roberta manually.

To start a game with luxtorpeda either set `USELUXTORPEDA` in the [gameconfig `$STLGAMECFG`](#Game Configurations) or put the game into the [steam category](#Steam Categories) "Luxtorpeda"
Alternatively duplicate the file to a different name which you want to use as category name, ideally into [`STLCATEGORYDIR`.](#Steam Categories-dir).
The luxtorpeda-dev dev was so kind to add a manual-download option in v20, so if native game files are missing they are downloaded before the actual game launch now.
Therefore it is recommended to use the lastest luxtorpeda-dev version.


#### Vortex
[Vortex Mod Manager](https://github.com/Nexus-Mods/Vortex)

**Usage**:

Vortex can be used without any **stl** configuration and will work ootb without zero configuration.
Just create a "Vortex" [Steam Category](#Steam Categories) and add your (Vortex compatible) game to it and start the game regularly.
Vortex will start, with the selected game preconfigured and ready to mod
and when you exit Vortex the selected game will start normally (with your mods).


**Installation?**
If Vortex is not yet installed, it will be installed on the first launch, so the first launch will need some time (mostly depends on dotnets mind of its own... maybe 5 minutes).
Alternatively you can also install it via command line (see below).

**Functionality**:
Some settings are preconfigured, to make this working without any user configuration, but of course all of the settings can be as well configured if you want.

##### Vortex Configuration

**stl** uses an extra vortex directory inside `STLCFGDIR` defined under `STLVORTEXDIR`
This directory contains the Vortex configfile `STLVORTEXCFG` *(`STLCFGDIR`/vortex/vortex.conf`)*

Here are the main configuration options:
- `VORTEXWINE`: the wine binary used for Vortex - **default commented out, but internally searches for system-wide wine if not configured**
- `VORTEXPREFIX`:the `WINEPREFIX` path used for Vortex - **default is `STLVORTEXDIR/wineprefix`**
- `VORTEXDOWNLOADPATH`: the path where all Vortex downloads should be stored - **default is `STLVORTEXDIR/downloads`**
- `VORTEXINSTALL`: download and install Vortex automatically if set to 1 **default enabled**
- [`VORTEXSTAGES`](#Vortex Stages): comma-seperated list of "Vortex Staging directories - one for each of your "Steam Library" partitions - **default commented out and empty**
- `DISABLE_AUTOSTAGES`: set to 1 if you don't want **stl** to try to auto set/create `VORTEXSTAGE` directories **default 0**

##### Vortex Stages
**Explanation `VORTEXSTAGES`:**

Vortex uses 2 main [Deployment_Methods]:(https://wiki.nexusmods.com/index.php/Deployment_Methods) to enable Mods for the managed games.
"Hardlink Deployment" and "Symlink Deployment". Symlink Deployment doesn't work under wine, so Hardlink is required (and automatically set for every game from **stl**, although it is default anyway)
Those "Hardlinks" only work if the "Staging directory" is on the same partition as the game (yes the same physical partition, not the same "windows drive in wine).
As Steam Library directories can be on multiple paritions a "Staging directory" is required for every one of them.

###### Automated (zeroconf) `VORTEXSTAGES` configuration
When you start a game **stl** will parse on which mount point it actually lies.
Then it tests if it can create/write a "Vortex" directory in the root directory of the partition.
If it fails to create a directory in the previous step, it tests next if it can create/write a "Vortex" directory
directly in the "Steam Library" directory of the started game besides the "steamapps" directory.

The first succeeding directory will be added automatically to the `VORTEXSTAGES` variable
and will be used from now on as "Staging directory" automatically for all games lying on the same partition.
So after you have started one "Vortex" game from each of your "Steam Library" partitions the `VORTEXSTAGES` variable is ready for all of your games.
The only exception is the partition where your steam is installed ("/" or "/home" if you have an extra /home/partition).
Here the default "Vortex Staging directory" is `STLVORTEXDIR/staging` instead.

Other additional paths can be added easily, just make suggestions.
If you don't want that automation just set `DISABLE_AUTOSTAGES` to 1 and set them manually instead:

###### Manual `VORTEXSTAGES` configuration
This can be manually configured in the `VORTEXSTAGES` simply by adding one writeable directory per partition you want to use.
This `VORTEXSTAGES` is currently not very stable without any sanity checks so make sure to:
Seperate the paths with a "," and do not use quotes or spaces in between!
**working example:**
`VORTEXSTAGES=/media/games1/Vortex,/media/games2/Vortex,/home/blah/blubb/Vortex`
**not working example:**
`VORTEXSTAGES=/media/games1/Vortex, /media/games2/Vortex, "/home/blah/blubb/Vortex"`

#####  Vortex Commandline
**stl Vortex commandline options:**
`stl vortex install`: starts a full Vortex installation with all dependencies
`stl vortex start`: starts Vortex
`stl vortex getset`: lists all configured Vortex settings

#####  Some additional Notes

- On the first start Vortex warns that it is started with admin priviledges. Very likely wine related, just click it away, it won't pop up again
- I tested ~25 games and they worked ootb, feel free to open an issue for a not (automatically) working game if you think this is a **stl** bug. (Nehrim doesn't seem to work (yet))
- It was pretty much work to get this into the current state, but although I tested a lot there still might be glitches and problems.
  Also Vortex can stop working under linux/wine anytime after an update (as it already did before).
  Don't complain and rant when it doesn't work as expected (anymore) (as it happened already before with other Vortex-linux solutions),
  but try to help fixing the issue instead then (no offense, but imho linux already had better times regarding this).
- The `VORTEX` variable is mostly used as boolean. Vortex is not used when 0 or undefined, and Vortex starts regularly with set to 1 (the "Vortex" steam category does nothing else)
  You can also set it to 2+3 though (ideally in the gameconfig `$STLGAMECFG`), where 2 "quickstarts" Vortex leaving out some checks, and 3 doing the same, but doesn't start the game afterwards.
- unfortunately Skyrim/Fallout (flavours) Script Extender doesn't [work with default proton since some time](https://github.com/ValveSoftware/Proton/issues/170).
  As many mods depend on "SE" I added a function which renames the "SE" exe when found in the gamedir, to ensure that Vortex knows it is uninstalled and would complain if a mod depends on it.
  To enable that function just set `BUG170=170` somewhere (f.e. [global.conf](#global.conf)

#### Registry

Auto-applying registry files:
If `REGEDIT` is
- set to 0 it will be skipped completely
- set to 1 a registry file `$SteamAppId.reg` will be searched and used in `GLOBALREGDIR` and `STLREGDIR`
- set to anything else the file `$REGEDIT` will be searched and used in `GLOBALREGDIR` and `STLREGDIR`

when a registry file from above was applied `REGEDIT` will be set to "0" in the game config, to skip regedit on the following game starts


#### Side-by-Side VR

SBS-VR (regular games side-by-side in **VR**):
--------------------------------------------

To play games with **built in** side-by-side you just have to set `RUNSBSVR` to 1 (or greater to delay the VR start for `RUNSBSVR` seconds) in the game specific config,
everything else is done (almost) automatically:

- start SteamVR
- start the game (game settings required to enable sbs are not automatically enabled! added an auto config setting for **Crysis 2** though )
- start [vr-video-player](https://git.dec05eba.com/vr-video-player)
- when exiting the game, vr-video-player wil be closed as well.

There are also two quickstart options to choose from to directly start regular games in SBS mode without any further configuration
by auto-enabling side-by-side with the shader [Depth3D](#Depth3D):

 - `SBSVRVK`: set to 1 as shortcut to enable all required flags for SBSVR with [vkBasalt](#vkBasalt)
 - `SBSVRRS`: set to 1 as shortcut to enable all required flags for SBSVR with [ReShade](#Reshade)

Where Reshade has more features and vkBasalt is probably more stable, because it works natively.

Some games start own launchers before the actual game and autodetecting the correct window is not easy
*(searching for the biggest window from the game process, which may not be always the correct one)*
That's why you can configure the exact window name to look for, which makes the whole process much more straighter.

Setting the [global.conf](#global.conf) option `SAVESBSWINNAME` to 1 enabled saving the game window name into a freshly created [SBS Tweak](#SBS Tweaks) config (so this is only done once and used from now on automatically).
With the game window name available SBS-VR starting works much better and faster than without, so you should enable that option.

Setting SAVESBSWINNAME to 1 allows you to pick the game window name, which is the fastest method to get the window name. It usually works very good, but when f.e. the game has a launcher which you have to click this won't work of course.
If `SAVESBSWINNAME` is greater than 1 the program will wait `SAVESBSWINNAME` seconds long to get the name of the currently active window and save that into the [SBS Tweak](#SBS Tweaks) config.
So setting this f.e. to 60 seconds and playing the game for 2 minutes is enough.
In rare cases a game doesn't have a valid window name, which makes detecting the correct window pretty complicated.

The author [vr-video-player](https://git.dec05eba.com/vr-video-player) was so kind to accept a little patch, to work better with **stl**.
It is possible to live zoom in and out and the zoom state is written into a temporar file, which **stl** picks up.
The value is stored in the internal [SBS Tweak](#SBS Tweaks) config (also when changed) and read from there from now on.

To make switching between game- and vr-video-player window easier (with hmd) there is also the option `TOGGLEWINDOWS`:
When enabled, all visible windows will minimize on game start, and will maximize back when game finishes *(might glitch sometimes)*
So switching between the windows is easily possible with *Alt+Tab*.
`TOGGLEWINDOWS` is also enabled by default in the **VR** [Steam Categories](#Steam Categories) *(ReShadeVR,SBS-VR,vkVR.conf)*

#### GameMode
[gamemode](https://github.com/FeralInteractive/gamemode)
- `USEGAMEMODERUN`: set to 1 to start game with gamemoderun
*([User Configuration](#User Configuration) overrides [system-wide configuration](#Systemwide Configuration))*

#### Notifier
Set `NOTY` to your notifier to draw some start/stop **stl** messages

#### 32bit Wineprefix
Set `FORCE32BITPFX` to 1 to force 32bit pfx *(experimental)*
Used by the	246960 [Tweak](#Tweaks) *(Giana Sisters - Rise of the Owlverlord)*
	
#### MangoHud
[MangoHud](https://github.com/flightlessmango/MangoHud)
Set `MANGOHUD` to 1 to enable mangohud *(does nothing in stl itself, but just exports the upstream variable)*

#### Nyrna
[Nyrna](https://github.com/Merrit/nyrna)
Set `RUN_NYRNA` to 1 to enable nyrna while game is running 
*([User Configuration](#User Configuration) overrides [system-wide configuration](#Systemwide Configuration))*

#### ReplaySorcery
[ReplaySorcery](https://github.com/matanui159/ReplaySorcery)
Set `RUN_REPLAY` to 1 to enable replay-sorcery while game is running 
*([User Configuration](#User Configuration) overrides [system-wide configuration](#Systemwide Configuration))*

#### Toggle Open Windows
minimize all open windows on game start and maximize them when game exited using wmctrl
- `TOGGLEWINDOWS`: toggle visibility of all open windows on start/stop

#### Custom Game Launch
Meant for a simple custom game launch using proton/steamruntime
and not as a fully fledged custom game launch option!
If `RUN_CUSTOMCMD` is set for the SteamAppId defined in the global `CUSTOMLAUNCHID`
a requester will ask for a exe you want to start inside the `CUSTOMLAUNCHID`
The selected exe will be started inplace of the regular game.
If no exe is selected the game `CUSTOMLAUNCHID` will exit
If `RUN_CUSTOMCMD` is disabled, the regular game is started normally
If `CUSTOMCMD` is configured for the game `CUSTOMLAUNCHID` the requester will be skipped and `CUSTOMCMD` will be started directly
defaults `CUSTOMLAUNCHID` is SteamAppId `15520` ("Aaaa...") because it is small and always on top of the library
**stl** of course won't install dependencies for the selected exe, so you're on your own.

#### Strace
If `STRACERUN` is set to 1 **stl** will write a strace log of the launched game
strace is launched with the commandline arguments found in `STRACEOPTS`.

When `STRACERUN` is enabled make sure
`/proc/sys/kernel/yama/ptrace_scope` is set to 0.
else your user will get access denied when trying to attach a process.
Either 
`echo 0 > /proc/sys/kernel/yama/ptrace_scope`
as root or enable it persistent in sysctl.

#### Block Internet
If `NOINET` is set to 1 this command is used to block the internet for the selected game. game might fail to start!
To use this option you need to configure this little [howto](https://serverfault.com/questions/550276/how-to-block-internet-access-to-certain-programs-on-linux)
Feel free to send pull requests. Depending on the game, it might reject to start at all without internet!

#### Network Monitoring
Basic Network Traffic Monitor
- `NETMON`: program to record game network-traffic with arguments `NETOPTS` - used when enabled

If `NETMON` is set the basic network traffic of the selected game is monitored and written into `NETMONDIR`.
duplicate lines are unique sorted at the end.

#### ReShade
[ReShade](https://reshade.me)
Set `INSTALL_RESHADE` to 1 to automatically install reshade into the selected game dir.
Set `USERESHADE` to 1 to start game with ReShade enabled
	
The required `$STLCFGDIR/reshade.conf` is autogenerated on the first run with `INSTALL_RESHADE` enabled.
If `DOWNLOAD_RESHADE` is set to 1 all required files for ReShade are [downloaded](#Downloads) once into `RESHADESRCDIR`
of course you can install all files manually as well. make sure to rename all files correctly:

**64bit** `d3dcompiler_47.dll`: -> d3dcompiler_47_64.dll
**32bit** `d3dcompiler_47.dll`: -> d3dcompiler_47_32.dll
`ReShade64.dll`, `ReShade32.dll`: renaming not required as they will be placed in the gamedir under the required name

The required architecture is autodetected from the game.exe and the matching files are copied from `RESHADESRCDIR` into the selected game dir
both downloadfiles and basic configuration were taken from [r/linux_gaming](https://www.reddit.com/r/linux_gaming/comments/b2hi3g/reshade_working_in_wine_43) 

#### vkBasalt
[vkBasalt](https://github.com/DadSchoorse/vkBasalt)
- `ENABLE_VKBASALT`: set `ENABLE_VKBASALT` to 1 to start the game with vkbasalt *(does nothing in stl itself, but just exports the upstream variable)*
- `VKBASALT_CONFIG_FILE`: the vkbasalt source config file - it points per default to `STLCFGDIR/vkBasalt.conf` and is autogenerated if not found
The autogenerated `VKBASALT_CONFIG_FILE` points to the files from `RESHADE_DEPTH3D` so it should have been at least checked out once with `CLONE_DEPTH3D`

#### Depth3D
[Depth3D](https://github.com/BlueSkyDefender/Depth3D)
Mostly useful in combination with [SBS-VR](#Side-by-Side VR).
Set `RESHADE_DEPTH3D` to 1 to install ReShade Depth3D Shader into gamedir
If `CLONE_DEPTH3D` is set to 1 the git repository will be automatically cloned/pulled (only when `RESHADE_DEPTH3D=1`) to `DEPTH3DSRCDIR` in [Downloads](#Downloads)

With `RESHADE_DEPTH3D` enabled `Overwatch.fxh`, `SuperDepth3D.fx`, `SuperDepth3D_VR.fx` from Depth3D are copied to the gamedir.
When the game started just create a initial profile by selecting the autodetected `SuperDepth3D_VR.fx`

#### Editor
When `WAITEDITOR` is greater 0 a zenity requester will pop up on game launch and wait `WAITEDITOR` seconds for a keypress
forediting the [Game specific configuration file](#User Configurations) with your `STLEDITOR` if desired.
set PROTONDB to 1 to additionally open the protondb.com url for the game `PDBURL` in your `BROWSER` when starting the editor

#### ENV Variables
Literally every env variable can be set in [gameconfig `$STLGAMECFG`](#Game Configurations) and [system-wide configuration](#global.conf),
making it pretty easy to tinker with important ones *(f.e `PROTON`* , `DXVK`* , `MANGOHUD`, `RADV_PERFTEST`, `WINE`...)*
The Possibilities Are Endless...
