
<img align="left" width="64" height="64" src="https://github.com/frostworx/repo-assets/blob/master/pics/steamtinkerlaunch-logo_64px.png" alt="**SteamTinkerLaunch** (short **stl**) is a Linux wrapper tool for use with the Steam client">

**Steam Tinker Launch** (short **stl**) is a Linux wrapper tool for use with the Steam client
which allows customizing and start tools and options for games quickly on the fly *(see [Features](#Features))*

By using a versatile configuration structure it is both easy to set up and flexible.

## How to use

### General usage
**stl works with linux native games and with games using proton!**
*(Some features (f.e. [ReShade](https://github.com/frostworx/steamtinkerlaunch/wiki/ReShade)) are only available for games using proton)*
*(Non-Steam games added to Steam are supported as well)*

There are two ways to use **stl** with steam.
Either as [Launch Option](#Steam-Launch-Option) or as [Steam Compatibility Tool](https://github.com/frostworx/steamtinkerlaunch/wiki/Steam-Compatibility-Tool)
*(simply enabling it as global default [Steam Compatibility Tool](https://github.com/frostworx/steamtinkerlaunch/wiki/Steam-Compatibility-Tool) seems to work fine as well)*

*(of course you're using this tool at your own risk and you're responsible which 3rd party programs you launch with it)*

#### Steam Launch Option
To use **stl** as Steam Launch Option just add it to your Steam Game Launch Option command line like this:

`stl %command%`

![stl starter](https://github.com/frostworx/repo-assets/blob/master/gifs/stl-command.gif)

*A little script which automatically does this for every game in the Steam library can be found [here](https://gist.github.com/frostworx/36bd76e705a0c87af523fa57cfeebaf8)*

**To use stl with a linux native game this option needs to be selected, as Steam automatically downloads the windows build, when using a "Steam Compatibility Tool"!** 

### Game specific use
When starting a game a small [Wait requester](#Wait-Requester) will pop up.
If within a short waiting period *(default 2 seconds)* the spacebar is pressed the [Settings Menu](https://github.com/frostworx/steamtinkerlaunch/wiki/Settings-Menu) will open where everything can be configured comfortably.
When done with configuring (or when the requester timeouts) the game will be started regularly with all tools and options configured.

## Installation
### Installation via Package Management
If you are on Arch Linux you can install stl from [AUR](https://aur.archlinux.org/packages/steamtinkerlaunch) *(f.e. using yay)*:
`yay -S steamtinkerlaunch`

[![Packaging status](https://repology.org/badge/vertical-allrepos/steamtinkerlaunch.svg)](https://repology.org/project/steamtinkerlaunch/versions)

### Manual Installation:
If **stl** is not in your package management yet, just `make install`
*(or copy everything manually if you date)*

## Community
Feel free to contribute to the project - there are many possibilities to do so:
- implement new features
- make good bug reports
- suggest new features
- maintain a package for your distribution
- add translations
- add your tinkered tweaks
- find out how cool it is and tell others :)

Got and idea or suggestions, but don't want to open an issue?
Visit [/r/SteamTinkerLaunch/](https://www.reddit.com/r/SteamTinkerLaunch)

## Quick start
When **stl** is started for the first time it will create its default [configuration](#Configuration) structure.
Almost everything can be configured with the built-in [Settings Menu](https://github.com/frostworx/steamtinkerlaunch/wiki/Settings-Menu), but optionally also with a graphical text editor.
It might be a good idea to start with configuring everything in the [Settings Menu](https://github.com/frostworx/steamtinkerlaunch/wiki/Settings-Menu) to your needs

## Features

**For a complete list of features, please see [the wiki](https://github.com/frostworx/steamtinkerlaunch/wiki). For the most recent changes, see [the release page](https://github.com/frostworx/steamtinkerlaunch/releases)
For current development changes, you can also check [this Changelog issue](https://github.com/frostworx/steamtinkerlaunch/issues/177)**


*(main categories)*

* [External Tools](https://github.com/frostworx/steamtinkerlaunch/wiki#external-tools): All external 3rd party programs (like [Boxtron](https://github.com/frostworx/steamtinkerlaunch/wiki/Boxtron), [Luxtorpeda](https://github.com/frostworx/steamtinkerlaunch/wiki/Luxtorpeda), [MangoHud](https://github.com/frostworx/steamtinkerlaunch/wiki/MangoHud), [vkBasalt](https://github.com/frostworx/steamtinkerlaunch/wiki/vkBasalt), etc.) which can be enabled for game launch can be found here, including their corresponding options.
* [GUI Options](https://github.com/frostworx/steamtinkerlaunch/wiki/Settings-Menu#GUI-Options)
* [Misc](https://github.com/frostworx/steamtinkerlaunch/wiki#misc): All configuration options which can't be put into a generic category usually can be found here.
* [Proton](https://github.com/frostworx/steamtinkerlaunch/wiki/Proton-Selection): switch between Proton-Versions, automatically download custom Proton builds...
* [Shader Management](https://github.com/frostworx/steamtinkerlaunch/wiki/Shader-Management): Download/Update/Install/Enable/Disable Shaders with support for [ReShade](https://github.com/frostworx/steamtinkerlaunch/wiki/ReShade) and [Depth3D](https://github.com/frostworx/steamtinkerlaunch/wiki/Depth3D)
* [Stl](https://github.com/frostworx/steamtinkerlaunch/wiki#stl): Stl has multiple [configuration](https://github.com/frostworx/steamtinkerlaunch/wiki/Configuration-Locations) options.
* [Tweaks](https://github.com/frostworx/steamtinkerlaunch/wiki/Tweaks): community mini configfiles (so-called [Tweakfiles](https://github.com/frostworx/steamtinkerlaunch/wiki/Tweaks#Tweakfiles)) to automatically start problematic games OOTB - can also start custom [Tweak Commands](https://github.com/frostworx/steamtinkerlaunch/wiki/Tweaks#Tweak-Commands)
* [Vortex](https://github.com/frostworx/steamtinkerlaunch/wiki/Vortex)
* [VR](https://github.com/frostworx/steamtinkerlaunch/wiki#vr): [Side by Side VR](https://github.com/frostworx/steamtinkerlaunch/wiki/Side-by-Side-VR): automatically play regular games in side-by-side mode in VR!
* [Wine](https://github.com/frostworx/steamtinkerlaunch/wiki/Wine-Support): Download and use custom Wine archives instead of Proton

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
- [Yad](https://github.com/v1cont/yad) All GUI elements like [Settings Menu](https://github.com/frostworx/steamtinkerlaunch/wiki/Settings-Menu), [Tray Icon](https://github.com/frostworx/steamtinkerlaunch/wiki/Tray-Icon), the [Editor Dialog](https://github.com/frostworx/steamtinkerlaunch/wiki/Settings-Menu#editor-dialog)
  and all other windows use yad. **A new enough version *(>=7.2; see [here](https://github.com/frostworx/steamtinkerlaunch/issues/98))* is required**
  **Instead of a global/system wide installation, stl also supports easy to use [custom solutions](https://github.com/frostworx/steamtinkerlaunch/wiki/Custom-Yad)**
   
Programs needed for optional external features *(no special order)*:
- [strace](https://github.com/frostworx/steamtinkerlaunch/wiki/Strace)
- [Gamemode](https://github.com/frostworx/steamtinkerlaunch/wiki/GameMode)
- [MangoHud](https://github.com/frostworx/steamtinkerlaunch/wiki/MangoHud)
- [winetricks](https://github.com/frostworx/steamtinkerlaunch/wiki/Winetricks)
- vr-video-player for playing regular games side-by-side in VR ([SBS-VR](https://github.com/frostworx/steamtinkerlaunch/wiki/Side-by-Side-VR))
- a graphical text editor and optionally an internet browser see [Global Config](https://github.com/frostworx/steamtinkerlaunch/wiki/Configuration-Locations#global-config)
- [vkBasalt](https://github.com/frostworx/steamtinkerlaunch/wiki/vkBasalt)
- [Nyrna](https://github.com/frostworx/steamtinkerlaunch/wiki/Nyrna)
- [ReplaySorcery](https://github.com/frostworx/steamtinkerlaunch/wiki/ReplaySorcery)
- netstat from net-tools for basic network monitoring
- [Boxtron](https://github.com/frostworx/steamtinkerlaunch/wiki/Boxtron) and dosbox to optionally start dos games with linux native dosbox
- ScummVM to optionally start compatible games natively using [Roberta](https://github.com/dreamer/roberta)
- [luxtorpeda-dev](https://github.com/luxtorpeda-dev/luxtorpeda) or [Luxtorpeda](https://github.com/dreamer/luxtorpeda) to optionally start supported games with a linux native binary
- [GameConqueror/scanmem](https://github.com/frostworx/steamtinkerlaunch/wiki/GameConqueror) to optionally cheat
- [GameScope](https://github.com/frostworx/steamtinkerlaunch/wiki/GameScope)
- cabextract *(currently only used to extract the [WMP10](https://github.com/frostworx/steamtinkerlaunch/wiki/WMP10) setup exe)*
- innoextract *(currently only used to extract the [Cheat Engine](https://github.com/frostworx/steamtinkerlaunch/wiki/Cheat-Engine) setup exe - with wine as fallback)*
- lsusb *(for an optional [SBS-VR](https://github.com/frostworx/steamtinkerlaunch/wiki/Side-by-Side-VR) check if a VR HMD was found)*
- jq *(used to extract game names from the steam api and for receiving the Lutris wine list)*
- convert from imagemagick *(currently only used to scale a custom installed game header picture)*
- rsync *(for backup support)*
- openssl *(currently only used to generate a random hex string for [Non-Steam Game](https://github.com/frostworx/steamtinkerlaunch/wiki/Add-Non-Steam-Game) `appid`)*

## Configuration
All configuration files are self-contained documented and always growing, so not every option is documented in here.
For a general overview what can be configured, just check the [wiki](https://github.com/frostworx/steamtinkerlaunch/wiki) or simply browse through the 
[Settings Menu](https://github.com/frostworx/steamtinkerlaunch/wiki/Settings-Menu), which covers almost everything available.

### Wait requester
The initial Requester which acts as gate to the [Settings Menu](https://github.com/frostworx/steamtinkerlaunch/wiki/Settings-Menu).
If selected within a [timeout](#Wait-requester-duration) the [Start Menu](#Start-Menu) will open,
else the game starts seamlessly with all configurations set.
It also shows how many game-related config files *(or tweakfiles)* are found.

![stl requester](https://github.com/frostworx/repo-assets/blob/master/pics/stl-requester.jpg)

### Wait requester duration
The [Wait requester](#Wait-requester) will wait `WAITEDITOR` seconds for User input *(either Space or press `OK`)*

When `WAITEDITOR` is set to 0 *(in [Game Menu](https://github.com/frostworx/steamtinkerlaunch/wiki/Settings-Menu#game-menu))* **stl** will directly start the game with the current configuration.
If `MAXASK` in the [Global Config](https://github.com/frostworx/steamtinkerlaunch/wiki/Configuration-Locations#global-config) *(f.e. via [Global Menu](https://github.com/frostworx/steamtinkerlaunch/wiki/))* is defined, the requester can be cancelled maximal `MAXASK` times
before `WAITEDITOR` is automatically set to 0 for the selected game.
Letting the requester timeout does not count as cancelled.
The "Cancelled counter" is stored directly in the [Game Config](https://github.com/frostworx/steamtinkerlaunch/wiki/Configuration-Locations#game-config) as `ASKCNT`
and is resetted to 0 when `MAXASK` was reached and `WAITEDITOR` was set to 0.

#### Start Menu
The menu which should open as initial Menu when accepting the [Wait requester](#Wait-Requester).
Can for example be configured in the [GUI Options](https://github.com/frostworx/steamtinkerlaunch/wiki/Settings-Menu#GUI-Options)
Options are
- [Selection Menu](https://github.com/frostworx/steamtinkerlaunch/wiki/Settings-Menu#Selection-Menu) *(default)*
- [Favorites Menu](https://github.com/frostworx/steamtinkerlaunch/wiki/Settings-Menu#Favorites-Menu)
- [Game Menu](https://github.com/frostworx/steamtinkerlaunch/wiki/Settings-Menu#Game-Menu)
- [Editor Dialog](https://github.com/frostworx/steamtinkerlaunch/wiki/Settings-Menu#Editor-Dialog)

### [Configuration Locations](https://github.com/frostworx/steamtinkerlaunch/wiki/Configuration-Locations)

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
Logs are written into the `LOGDIR` defined in the [Global Menu](https://github.com/frostworx/steamtinkerlaunch/wiki/Settings-Menu#global-menu) / [Global Config](https://github.com/frostworx/steamtinkerlaunch/wiki/Configuration-Locations#global-config).
The verbosity of the logfile depends on `WRITELOG` *(write logfile if not 0, increase verbosity from 1-2 (1:less, 2:all))*
in the same location.
There are several logfiles, those which are written mostly are the game specific ones *($SteamAppId.log)*

## Command Line
**stl** also has several command line options which are useful outside steam.
For available options please check `stl help
