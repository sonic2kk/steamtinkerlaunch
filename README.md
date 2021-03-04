
<img align="left" width="64" height="64" src="https://github.com/frostworx/repo-assets/blob/master/pics/steamtinkerlaunch-logo_64px.png" alt="**SteamTinkerLaunch** (short **stl**) is a Linux wrapper tool for use with the Steam client">

**Steam Tinker Launch** (short **stl**) is a Linux wrapper tool for use with the Steam client
which allows customizing and start tools and options for games quickly on the fly *(see [Features](#Features))*

By using a versatile configuration structure it is both easy to set up and flexible.

<li><a href="https://liberapay.com/frostworx"><img alt="Liberapay receives" src="http://img.shields.io/liberapay/receives/frostworx.svg?logo=liberapay"></a></li>

## How to use

### General usage
**stl works with linux native games and with games using proton!**
*(Some features (f.e. [ReShade](#ReShade)) are only available for games using proton)*
*(Non-Steam games added to Steam are supported as well)*

There are two ways to use **stl** with steam.
Either as [Launch Option](#Steam-Launch-Option) or as [Steam Compatibility Tool](#Steam-Compatibility-Tool)

#### Steam Launch Option
To use **stl** as Steam Launch Option just add it to your Steam Game Launch Option command line like this:

`stl %command%`

![stl starter](https://github.com/frostworx/repo-assets/blob/master/gifs/stl-command.gif)

*A little script which automatically does this for every game in the Steam library can be found [here](https://gist.github.com/frostworx/36bd76e705a0c87af523fa57cfeebaf8)*

**To use stl with a linux native game this option needs to be selected, as Steam automatically downloads the windows build, when using a "Steam Compatibility Tool"!** 

### Game specific use
When starting a game a small [Wait requester](#Wait-Requester) will pop up.
If within a short waiting period *(default 2 seconds)* the spacebar is pressed the [Settings Menu](#Settings-Menu) will open where everything can be configured comfortably.
When done with configuring (or when the requester timeouts) the game will be started regularly with all tools and options configured.

## Installation
### Installation via Package Management
If you are on Arch Linux you can install stl from [AUR](https://aur.archlinux.org/packages/steamtinkerlaunch) *(f.e. using yay)*:
`yay -S steamtinkerlaunch`

[![Packaging status](https://repology.org/badge/vertical-allrepos/steamtinkerlaunch.svg)](https://repology.org/project/steamtinkerlaunch/versions)

### Manual Installation:
If **stl** is not in your package management yet, just `make install`

Alternatively copy `stl` wherever you want (f.e. `/usr/local/bin/`) and make it executable:
`chmod +x stl`

When copying manually the enclosed directories *(containing optional configuration files)*
should be dropped into `/usr/share/stl/` *(preferred location)*.
Else they are automatically pulled from git *(default if `/usr/share/stl/` does not exist)*.

## Community
Feel free to contribute to the project - there are many possibilities to do so:
- implement new features
- make good bug reports
- suggest new features
- maintain a package for your distribution
- add translations
- add your tinkered tweaks
- find out how cool it is and tell others :)
- help to improve/shorten this monstrous README *(especially if English is your mother language)*
- sponsor this project


Got and idea or suggestions, but don't want to open an issue?
Visit [/r/SteamTinkerLaunch/](https://www.reddit.com/r/SteamTinkerLaunch)

## Quick start
When **stl** is started for the first time it will create its default [configuration](#Configuration) structure.
Almost everything can be configured with the built-in [Settings Menu](#Settings-Menu), but optionally also with a graphical text editor.
It might be a good idea to start with configuring everything in the [Settings Menu](#Settings-Menu) to your needs

## Features

**This README might not always be up2date, because with English not being my mother tongue
formulating it takes more time than I want to spend on it additionally to the programming
so it could be also a good idea to check the [Changes on the release page](https://github.com/frostworx/steamtinkerlaunch/releases)
or just to browse through the latest version**

*(no special order)*

* **[[ENV Variables]]** can be easily set for every single game (f.e `PROTON`* , `DXVK`* , `MANGOHUD`, `RADV_PERFTEST`, `WINE`...)
* **[[Custom Program]]** launch custom programs before or instead of the game itself *(also windows exes)*
* **[[winetricks]]** start winetricks before game launch *(gui or silent)*
* **[[Winecfg]]** start winecfg before game launch
* **[[GameMode]]** start/stop gamemoderun per game
* **[[Notifier]]** start/stop notify message per game
* **[[Strace]]** for easily debugging a game
* **[[Editor Hotkey|Editor]]** for editing the gameconfig
* **[[Editor URL|Editor]]** automatically open a defined URL for the launched game with the editor
* **[[ReShade]]** automatic installation and configuration
* **[[Depth3D]]** automatic shader installation
* **[[vkBasalt]]** basic vkBasalt configuration
* **[[Side by Side VR]]** automatically play regular games in side-by-side mode in VR!
* **[[Tweaks]]** community mini configfiles (so-called [Tweakfiles](#Tweakfiles)) to automatically start problematic games ootb - can also start custom [Tweak Commands](#Tweak-Commands)
* **[[Auto Tweaks]]** support for automatic import of game configs from several other platforms
* **[[Nyrna]]** start/stop ReplaySorcery per game
* **[[ReplaySorcery]]** start/stop ReplaySorcery per game
* **[[NetMon]]** basic network monitoring
* **[[Boxtron]]** support via steam `DOSBox` category
* **[[Roberta]]** support via steam `ScummVM` category
* **[[Luxtorpeda]]** support via steam `Luxtorpeda` category
* **[[Vortex Mod Manager|Vortex]]** via steam `Vortex` category see [Video of usage](#stl-Vortex-gif)
* **[[GFWL/xlive|GFWL]]** automatic support for games using GFWL
* **[[WMP10]]** automatic support for WMP10 installation
* **[[self maintaining configs|Configuration Locations]]** optional automatic cloning of this repo as replacement for missing system wide installation
* **[[GameConqueror]]** automatically open gameconqueror (scanmem gui) with the game exe on game launch
* **[[Custom User Start/Stop scripts|Start Stop Scripts]]** optional start custom scripts when game starts/ends
* **[[GameScope]]** start/stop gamescope per game
* **[[Settings Menu]]** easy configuration for almost all settings with the built-in modular Settings Menu
* **[[Native Games]]** support native Linux games
* **[[Steam Compatibility Tool]]** can be used as [Steam Launch Option](#Steam-Launch-Option) and as [Steam Compatibility Tool](#Steam-Compatibility-Tool)
* **[[Proton Selection]]** switch between Proton-Versions, automatically download custom Proton builds...
* **[[Multi Language Support]]** Multi-Language Support
* **[[Steam Linux Runtime]]** the Steam Linux Runtime can be disabled optionally
* **[[Game Launcher]]** built in game launcher mode
* **[[Game Pictures|Game Launcher]]** uses Game Pictures
* **[[Desktop Files|Game Launcher]]** automatic creation of *(stl-internal)* desktop files
* **[[Shader Management]]** Download/Update/Install/Enable/Disable Shaders
* **[[Custom Proton Autoupdate]]** optionally Download/Install/Enable version bumps of Custom Proton version per game
* **[[ReShade Presets|ReShade]]** Select ReShade Presets
* **[[Cheat Engine]]** automatic CheatEngine download, install, autostart per game and autostop on game exit
* **[[Pressure Vessel]]** Some Pressure Vessel options
* **[[Wine Support]]** Download and use custom Wine archives instead of Proton
* **[[Backup Support]]** optionally automatic backup of 'steamuser' files of the 'steamuser' files per Proton game
* **[[Metadata Support]]** Collect as much as possible gamedata to make further automations easier and faster
* **[[X64dbg Support]]** optionally start the selected game automatically with the *(auto-installed)* debugger x64dbg
* **[[Add Non Steam Game]]** Add Non-Steam games either via command line or via Gui

## Requirements
*(no special order)*

Programs required for a full internal functionality:
- awk *(gawk)*
- bash *(only shell tested)*
- bc
- git
- pgrep
- unzip
- wget
- which
- xdotool
- xprop
- xrandr
- xwininfo
- [Yad](https://github.com/v1cont/yad) All GUI elements like [Settings Menu](#Settings-Menu), [Tray Icon](#Tray-Icon), the [Editor Dialog](#Editor-Dialog)
  and all other windows use yad. **A new enough version *(>=7.2; see [here](https://github.com/frostworx/steamtinkerlaunch/issues/98))* is required**
   
Programs needed for optional external features *(no special order)*:
- [strace](#Strace)
- [Gamemode](#GameMode)
- [MangoHud](#MangoHud)
- [winetricks](#Winetricks)
- vr-video-player for playing regular games side-by-side in VR ([SBS-VR](#Side-by-Side-VR))
- a graphical text editor and optionally an internet browser see [Global Config](#Global-Config)
- [vkBasalt](#vkBasalt)
- [Nyrna](#Nyrna)
- [ReplaySorcery](#ReplaySorcery)
- netstat from net-tools for basic network monitoring
- [Boxtron](#Boxtron) and dosbox to optionally start dos games with linux native dosbox
- ScummVM to optionally start compatible games natively using [Roberta](https://github.com/dreamer/roberta)
- [luxtorpeda-dev](https://github.com/luxtorpeda-dev/luxtorpeda) or [Luxtorpeda](https://github.com/dreamer/luxtorpeda) to optionally start supported games with a linux native binary
- [GameConqueror/scanmem](#GameConqueror) to optionally cheat
- [GameScope](#GameScope)
- cabextract *(currently only used to extract the [WMP10](#WMP10) setup exe)*
- innoextract *(currently only used to extract the [Cheat Engine](#Cheat-Engine) setup exe - with wine as fallback)*
- lsusb *(for an optional [SBS-VR](#Side-by-Side-VR) check if a VR HMD was found)*
- jq *(used to extract game names from the steam api and for receiving the Lutris wine list)*
- convert from imagemagick *(currently only used to scale a custom installed game header picture)*
- rsync *(for backup support)*
- openssl *(currently only used to generate a random hex string for [Non-Steam Game](#Add-Non-Steam-Game) `appid`)*

## Configuration
All configuration files are self-contained documented and always growing, so not every option is documented in here.
For a general overview what can be configured, just check the [Features](#Features) or simply browse through the 
[Settings Menu](#Settings-Menu), which covers almost everything available.

### Wait requester
The initial Requester which acts as gate to the [Settings Menu](#Settings-Menu).
If selected within a [timeout](#Wait-requester-duration) the [Start Menu](#Start-Menu) will open,
else the game starts seamlessly with all configurations set.
It also shows how many game-related config files *(or tweakfiles)* are found.

![stl requester](https://github.com/frostworx/repo-assets/blob/master/pics/stl-requester.jpg)

### Wait requester duration
The [Wait requester](#Wait-requester) will wait `WAITEDITOR` seconds for User input *(either Space or press `OK`)*

When `WAITEDITOR` is set to 0 *(in [Game Menu](#Game-Menu))* **stl** will directly start the game with the current configuration.
If `MAXASK` in the [Global Config](#Global-Config) *(f.e. via [Global Menu](#Global-Menu))* is defined, the requester can be cancelled maximal `MAXASK` times
before `WAITEDITOR` is automatically set to 0 for the selected game.
Letting the requester timeout does not count as cancelled.
The "Cancelled counter" is stored directly in the [Game Config](#Game-Config) as `ASKCNT`
and is resetted to 0 when `MAXASK` was reached and `WAITEDITOR` was set to 0.

#### Start Menu
The menu which should open as initial Menu when accepting the [Wait requester](#Wait-Requester).
Can for example be configured in the [GUI Options](#GUI-Options)
Options are
- [Selection Menu](#Selection-Menu) *(default)*
- [Favorites Menu](#Favorites-Menu)
- [Game Menu](#Game-Menu)
- [Editor Dialog](#Editor-Dialog)

### [[Tray Icon]]

#
### [[Configuration Locations]]

### Downloads
The `STLDLDIR` directory stores all downloads started through **stl**
To name a few those are
[Depth3D](#Depth3D) shader files
[Vortex](#Vortex) the installation setup exe
[ReShade](#ReShade) ReShade itself and required d3dcompiler dlls
[Auto Tweaks](#Auto-Tweaks) downloads for all enabled Auto Tweaks are stored in here
[GFWL/xlive](#GFWL) xlive replacement
[self maintaining configs](#self-maintaining-configs) stl itself will be downloaded here when self-maintaining-configs are used
[Proton packages](#Proton) Proton packages
[Shaders](#Shaders) all Shader repositories
[X64dbg](#X64dbg-Support) debugger

### Logs
Logs are written into the `LOGDIR` defined in the [Global Menu](#Global-Menu) / [Global Config](#Global-Config).
The verbosity of the logfile depends on `WRITELOG` *(write logfile if not 0, increase verbosity from 1-2 (1:less, 2:all))*
in the same location.
There are several logfiles, those which are written mostly are the game specific ones *($SteamAppId.log)*

## Features in detail:

#### [[Registry]]

#### [[MangoHud]]

#### [[Toggle Open Windows]]

#### [[SteamAppID.txt]]

## [[Game Launch Speed]]

## Command Line
**stl** also has several command line options which are useful outside steam.
For available options please check `stl help
