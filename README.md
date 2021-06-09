<img align="left" width="64" height="64" src="https://github.com/frostworx/repo-assets/blob/master/pics/steamtinkerlaunch-logo_64px.png" alt="**SteamTinkerLaunch** (short **stl**) is a Linux wrapper tool for use with the Steam client">

**Steam Tinker Launch** (short **stl**) is a Linux wrapper tool for use with the Steam client
which allows customizing and start tools and options for games quickly on the fly *(see [Features](#Features))*

By using a versatile configuration structure it is both easy to set up and flexible.

## How to use

### General usage
**stl works with Linux native games and with games using Proton!**
*(Some features (f.e. [ReShade](https://github.com/frostworx/steamtinkerlaunch/wiki/ReShade)) are only available for games using Proton)*
*(Non-Steam games added to Steam are supported as well)*

There are two ways to use **stl** with Steam.
Either as [Steam Launch Option](https://github.com/frostworx/steamtinkerlaunch/wiki/Steam-Launch-Option) or as [Steam Compatibility Tool](https://github.com/frostworx/steamtinkerlaunch/wiki/Steam-Compatibility-Tool)
*(simply enabling it as global default [Steam Compatibility Tool](https://github.com/frostworx/steamtinkerlaunch/wiki/Steam-Compatibility-Tool) works fine as well)*

*(of course you're using this tool at your own risk and you're responsible which 3rd party programs you launch with it)*

### Game specific use
When starting a game a small [Wait requester](#Wait-Requester) will pop up.
If within a short waiting period *(default 2 seconds)* the spacebar is pressed the [Main Menu](https://github.com/frostworx/steamtinkerlaunch/wiki/Main-Menu) will open where everything can be configured comfortably.
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
- contribute your tinkered tweaks to [steamtinkerlaunch-tweaks](https://github.com/frostworx/steamtinkerlaunch-tweaks)
- find out how cool it is and tell others :)

Got and idea or suggestions, but don't want to open an issue?
Visit [/r/SteamTinkerLaunch/](https://www.reddit.com/r/SteamTinkerLaunch)

## Quick start
When **stl** is started for the first time it will create its default [configuration](#Configuration) structure.
Almost everything can be configured with the built-in [Main Menu](https://github.com/frostworx/steamtinkerlaunch/wiki/Main-Menu), but optionally also with a graphical text editor.
It might be a good idea to start with configuring everything in the [Main Menu](https://github.com/frostworx/steamtinkerlaunch/wiki/Main-Menu) to your needs

**If you want to get an overview over the Steam Tinker Launch features, but the huge [wiki](https://github.com/frostworx/steamtinkerlaunch/wiki) is too overwhelming,
you might want to read this excellent [Boiling Steam article](https://boilingsteam.com/supercharge-steam-with-steamtinkerlaunch-stl) by @podiki**


## Features
**For a complete list of features, please see [the wiki](https://github.com/frostworx/steamtinkerlaunch/wiki). For the most recent changes, see [the release page](https://github.com/frostworx/steamtinkerlaunch/releases)
For current development changes, you can also check [this Changelog issue](https://github.com/frostworx/steamtinkerlaunch/issues/177)**

* Support for multiple [External Tools](https://github.com/frostworx/steamtinkerlaunch/wiki/Tools) like
	* [Boxtron](https://github.com/frostworx/steamtinkerlaunch/wiki/Boxtron)
	* [Cheat Engine](https://github.com/frostworx/steamtinkerlaunch/wiki/Cheat-Engine)
	* [Conty](https://github.com/frostworx/steamtinkerlaunch/wiki/Conty)
	* [GameConqueror](https://github.com/frostworx/steamtinkerlaunch/wiki/GameConqueror)
	* [GameMode](https://github.com/frostworx/steamtinkerlaunch/wiki/GameMode)
	* [GameScope](https://github.com/frostworx/steamtinkerlaunch/wiki/GameScope)
	* [Luxtorpeda](https://github.com/frostworx/steamtinkerlaunch/wiki/Luxtorpeda)
	* [MangoHud](https://github.com/frostworx/steamtinkerlaunch/wiki/MangoHud)
	* [Nyrna](https://github.com/frostworx/steamtinkerlaunch/wiki/Nyrna)
	* [ReplaySorcery](https://github.com/frostworx/steamtinkerlaunch/wiki/ReplaySorcery)
	* [Roberta](https://github.com/frostworx/steamtinkerlaunch/wiki/Roberta)
	* [Strace](https://github.com/frostworx/steamtinkerlaunch/wiki/Strace)
	* [X64dbg](https://github.com/frostworx/steamtinkerlaunch/wiki/X64dbg-Support)

* Highly customizable [Gui System](https://github.com/frostworx/steamtinkerlaunch/wiki/Gui)

* [Misc](https://github.com/frostworx/steamtinkerlaunch/wiki/Misc) features like support for various methods to launch custom programs

* Multiple [Proton](https://github.com/frostworx/steamtinkerlaunch/wiki/Proton) options like
	* [Backup Support](https://github.com/frostworx/steamtinkerlaunch/wiki/Backup-Support)
	* [Download](https://github.com/frostworx/steamtinkerlaunch/wiki/Download-Custom-Proton) and [manage](https://github.com/frostworx/steamtinkerlaunch/wiki/Proton-Versions) [Custom Proton Builds](https://github.com/frostworx/steamtinkerlaunch/wiki/Custom-Proton-Autoupdate)
	* [DXVK Hud Options](https://github.com/frostworx/steamtinkerlaunch/wiki/Dxvk-Hud-Options)
	* [ProtonDB-Rating](https://github.com/frostworx/steamtinkerlaunch/wiki/ProtonDB-Rating)
	* [(Re-)Create Proton compatdata and WINEPREFIX](https://github.com/frostworx/steamtinkerlaunch/wiki/Steam-First-Time-Setup#re-create-compatdata-and-wineprefix)
	* [Steam First Time Setup packages](https://github.com/frostworx/steamtinkerlaunch/wiki/Steam-First-Time-Setup): install [Regular](https://github.com/frostworx/steamtinkerlaunch/wiki/Steam-First-Time-Setup#Regular-First-Time-Setup) or [Custom](https://github.com/frostworx/steamtinkerlaunch/wiki/Steam-First-Time-Setup#Custom-First-Time-Setup) First-Time-Setups on the fly

* [Shader](https://github.com/frostworx/steamtinkerlaunch/wiki/Shader) [ReShade](https://github.com/frostworx/steamtinkerlaunch/wiki/ReShade) [Management](https://github.com/frostworx/steamtinkerlaunch/wiki/Shader-Management)

* Multiple [Steam](https://github.com/frostworx/steamtinkerlaunch/wiki/Steam) related options like
	* [SteamGridDB Support](https://github.com/frostworx/steamtinkerlaunch/wiki/SteamGridDB)
	* [Add Non Steam Game](https://github.com/frostworx/steamtinkerlaunch/wiki/Add-Non-Steam-Game) easily
	* use [Steam Categories](https://github.com/frostworx/steamtinkerlaunch/wiki/Steam-Categories) to enable functions for games on the fly
	* quickly open [Help-Urls](https://github.com/frostworx/steamtinkerlaunch/wiki/Help-Url) like steam github, pcgamingwiki protondb

* [Vortex](https://github.com/frostworx/steamtinkerlaunch/wiki/Vortex)

* Support for [Stereoscopic3D](https://github.com/frostworx/steamtinkerlaunch/wiki/Side-by-Side-VR) [VR](https://github.com/frostworx/steamtinkerlaunch/wiki/VR)

* Use [Wine](https://github.com/frostworx/steamtinkerlaunch/wiki/Wine) instead of [Proton](https://github.com/frostworx/steamtinkerlaunch/wiki/Proton) with support for
	* [Download Custom Wine](https://github.com/frostworx/steamtinkerlaunch/wiki/Download-Custom-Wine)
	* [Winetricks](https://github.com/frostworx/steamtinkerlaunch/wiki/Winetricks)
	* [Winecfg](https://github.com/frostworx/steamtinkerlaunch/wiki/Winecfg)
	* [Wineconsole](https://github.com/frostworx/steamtinkerlaunch/wiki/Wineconsole)
	* [Wine Debug](https://github.com/frostworx/steamtinkerlaunch/wiki/Wine-Debug)
	* [Registry](https://github.com/frostworx/steamtinkerlaunch/wiki/Registry)

## Requirements
*(no special order)*

Programs required for a full internal functionality:
- awk *(gawk)*
- bash *(only shell tested)*
- git
- pgrep
- unzip
- wget
- which
- xdotool
- xprop
- xrandr
- xwininfo
- [Yad](https://github.com/v1cont/yad) All GUI elements like [Main Menu](https://github.com/frostworx/steamtinkerlaunch/wiki/Main-Menu), [Tray Icon](https://github.com/frostworx/steamtinkerlaunch/wiki/Tray-Icon), the [Editor Menu](https://github.com/frostworx/steamtinkerlaunch/wiki/Editor-Menu)
  and all other windows use yad. **A new enough version *(>=7.2; see [here](https://github.com/frostworx/steamtinkerlaunch/issues/98))* is required**
  **Instead of a global/system wide installation, stl also supports easy to use [custom solutions](https://github.com/frostworx/steamtinkerlaunch/wiki/Custom-Yad)**
   
Programs needed for optional external features *(no special order)*:
- [strace](https://github.com/frostworx/steamtinkerlaunch/wiki/Strace)
- [Gamemode](https://github.com/frostworx/steamtinkerlaunch/wiki/GameMode)
- [MangoHud](https://github.com/frostworx/steamtinkerlaunch/wiki/MangoHud)
- [winetricks](https://github.com/frostworx/steamtinkerlaunch/wiki/Winetricks)
- vr-video-player for playing regular games side-by-side in VR ([SBS-VR](https://github.com/frostworx/steamtinkerlaunch/wiki/Side-by-Side-VR))
- a graphical text editor and optionally an internet browser see [Global Config](https://github.com/frostworx/steamtinkerlaunch/wiki/Configuration-Files#Global-Config)
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
All [Configuration Files](https://github.com/frostworx/steamtinkerlaunch/wiki/Configuration-Files) are self-contained documented and always growing, so not every option is documented in here.
For a general overview what can be configured, just check the [wiki](https://github.com/frostworx/steamtinkerlaunch/wiki) or simply browse through the 
[Main Menu](https://github.com/frostworx/steamtinkerlaunch/wiki/Main-Menu), which covers almost everything available.

### Wait requester
The initial [Wait Requester](https://github.com/frostworx/steamtinkerlaunch/wiki/Wait-Requester) acts as gate to the [Main Menu](https://github.com/frostworx/steamtinkerlaunch/wiki/Main-Menu).
If selected within a [timeout](https://github.com/frostworx/steamtinkerlaunch/wiki/Wait-Requester#timeout) the [Start Menu](https://github.com/frostworx/steamtinkerlaunch/wiki/Start-Menu) will open,
else the game starts seamlessly with all configurations set.

![Wait Requester](https://github.com/frostworx/repo-assets/blob/master/pics/WaitRequester.jpg)

### [Configuration Files](https://github.com/frostworx/steamtinkerlaunch/wiki/Configuration-Files)

### [Downloads](https://github.com/frostworx/steamtinkerlaunch/wiki/Downloads)

### Logs
Logs are written into the `LOGDIR` defined in the [Global Menu](https://github.com/frostworx/steamtinkerlaunch/wiki/Global-Menu) / [Global Config](https://github.com/frostworx/steamtinkerlaunch/wiki/Configuration-Files#Global-Config).
The verbosity of the logfile depends on `WRITELOG` *(write logfile if not 0, increase verbosity from 1-2 (1:less, 2:all))*
in the same location.
There are several logfiles, those which are written mostly are the game specific ones *($SteamAppId.log)*

## Command Line
**stl** also has several [command line](https://github.com/frostworx/steamtinkerlaunch/wiki/Command-Line) which can also be useful outside steam.
For available options please check `stl help`
