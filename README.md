
<img align="left" width="64" height="64" src="https://github.com/frostworx/repo-assets/blob/master/pics/steamtinkerlaunch-logo_64px.png" alt="**SteamTinkerLaunch** (short **stl**) is a Linux wrapper tool for use with the Steam client">

**SteamTinkerLaunch** (short **stl**) is a Linux wrapper tool for use with the Steam client
which allows to customize and start tools and options for games quickly on the fly *(see [Features](#Features))*

By using a versatile configuration structure it is both easy to setup and flexible.

<li><a href="https://liberapay.com/frostworx"><img alt="Liberapay receives" src="http://img.shields.io/liberapay/receives/frostworx.svg?logo=liberapay"></a></li>

## How to use

### General usage
**stl works with linux native games and with games using proton!**
*(Some features (f.e. [ReShade](#ReShade)) are only available for games using proton)*
*(Non-Steam games added to Steam are supported as well)*

There are two ways to use **stl** with steam.
Either as [Launch Option](#Launch-Option) or as [Steam Compatibility Tool](#Steam-Compatibility-Tool)

#### Steam Launch Option
To use **stl** as Steam Launch Option just add it to your Steam Game Launch Option command line like this:

`stl %command%`

![stl starter](https://github.com/frostworx/repo-assets/blob/master/gifs/stl-command.gif)

*A little script which automatically does this for every game in the Steam library can be found [here](https://gist.github.com/frostworx/36bd76e705a0c87af523fa57cfeebaf8)*

#### Steam Compatibility Tool
**stl** can also be used as Steam Compatibility Tool, simply by using the **stl** builtin [Command Line](#Command-Line) options:

- `stl compat add` *(adds stl under compatibilitytools.d/SteamTinkerLaunch)*
- `stl compat del` *(deletes compatibilitytools.d/SteamTinkerLaunch)*
- `stl compat (get)` *(checks the state of compatibilitytools.d/SteamTinkerLaunch)*

If `add` is selected and stl is started from a different path than before, the symlink will be automatically updated.

*(as usual, when a Steam Compatibility Tool was added, Steam needs to be restarted to make the added Tool available)*

All programs used as custom Compatibility Tool *(of course including **stl**)* are started without the [Steam Linux Runtime](#Steam-Linux-Runtime)!

![stl steam compat](https://github.com/frostworx/repo-assets/blob/master/gifs/stl-steam-compat.gif)

*(It doesn't make any sense, but a game also works, when stl is set both as Launch Option and as Steam Compatibility Tool)*

### Game specific use
When starting a game a small [Wait requester](#Wait-Requester) will popup.
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
Feel free to contribute to the project - there are many possibilites to do so:
- implement new features
- make good bugreports
- suggest new features
- maintain a package for your distribution
- add translations
- add your tinkered tweaks
- find out how cool it is and tell others :)
- help to improve/shorten this monstrous README *(especially if english is your mother language)*
- sponsor this project


Got and idea or suggestions, but don't want to open an issue?
Visit [/r/SteamTinkerLaunch/](https://www.reddit.com/r/SteamTinkerLaunch)

## Quickstart
When **stl** is started for the first time it will create its default [configuration](#Configuration) structure.
Almost everything can be configured with the built-in [Settings Menu](#Settings-Menu), but optionally also with a graphical text editor.
It might be a good idea to start with configuring everything in the [Settings Menu](#Settings-Menu) to your needs

## Features

**This README might not always be up2date, because with English not being my mother tounge
formulating it takes more time than I want to spend on it additionally to the programming
so it could be also a good idea to check the [Changes on the release page](https://github.com/frostworx/steamtinkerlaunch/releases)
or just to browse through the latest version**

*(no special order)*

* **[ENV Variables](#ENV-Variables)** can be easily set for every single game (f.e `PROTON`* , `DXVK`* , `MANGOHUD`, `RADV_PERFTEST`, `WINE`...)
* **[Custom Program](#Custom-Program)** launch custom programs before or instead the game itself *(also windows exes)*
* **[winetricks](#Winetricks)** start winetricks before game launch *(gui or silent)*
* **[winecfg](#Winecfg)** start winecfg before game launch
* **[GameMode](#GameMode)** start/stop gamemoderun per game
* **[Notifier](#Notifier)** start/stop notify message per game
* **[Strace](#Strace)** for easily debugging a game
* **[Editor Hotkey](#Editor)** for editing the gameconfig
* **[Editor URL](#Editor)** automatically open a defined URL for the launched game with the editor
* **[ReShade](#ReShade)** automatic installation and configuration
* **[Depth3D](#Depth3D)** automatic shader installation
* **[vkBasalt](#vkBasalt)** basic vkBasalt configuration
* **[SBS-VR](#Side-by-Side-VR)** automatically play regular games in side-by-side mode in VR!
* **[Tweaks](#Tweaks)** community mini configfiles (so-called [Tweakfiles](#Tweakfiles)) to automatically start problematic games ootb - can also start custom [Tweak Commands](#Tweak-Commands)
* **[Auto Tweaks](#Auto-Tweaks)** support for automatic import of game configs from several other platforms
* **[Nyrna](#Nyrna)** start/stop ReplaySorcery per game
* **[ReplaySorcery](#ReplaySorcery)** start/stop ReplaySorcery per game
* **[NetMon](#Network-Monitoring)** basic network monitoring
* **[Boxtron](#Boxtron)** support via steam `DOSBox` category
* **[Roberta](#Roberta)** support via steam `ScummVM` category
* **[Luxtorpeda](#Luxtorpeda)** support via steam `Luxtorpeda` category
* **[Vortex Mod Manager](#Vortex)** via steam `Vortex` category see [Video of usage](#stl-Vortex-gif)
* **[GFWL/xlive](#GFWL)** automatic support for games using GFWL
* **[WMP10](#WMP10)** automatic support for WMP10 installation
* **[self maintaining configs](#self-maintaining-configs)** optional automatic cloning of this repo as replacemement for missing system wide installation
* **[GameConqueror](#GameConqueror)** automatically open gameconqueror (scanmem gui) with the game exe on game launch
* **[Custom User Start/Stop scripts](#Start-Stop-Scripts)** optional start custom scripts when game starts/ends
* **[GameScope](#GameScope)** start/stop gamescope per game
* **[Settings Menu](#Settings-Menu)** easy configuration for almost all settings with the builtin modular Settings Menu
* **[native Support](#Native-Games)** support native Linux games
* **[Steam Compatibility Tool](#Steam-Compatibility-Tool)** can be used as [Steam Launch Option](#Steam-Launch-Option) and as [Steam Compatibility Tool](#Steam-Compatibility-Tool)
* **[Proton Selection](#Proton-Selection)** switch between Proton-Versions, automatically download custom Proton builds...
* **[Multi Language](#Multi-Language-Support)** Multi-Language Support
* **[Steam Linux Runtime](#Steam-Linux-Runtime)** the Steam Linux Runtime can be disabled optionally
* **[Game Launcher](#Game-Launcher)** built in game launcher mode
* **[Game Pictures](#Game-Pictures)** uses Game Pictures
* **[Desktop Files](#Desktop-Files)** automatic creation of *(stl-internal)* desktop files
* **[Shader Management](#Shader-Management)** Download/Update/Install/Enable/Disable Shaders
* **[Custom Proton Autoupdate](#Custom-Proton-Autoupdate)** optionally Download/Install/Enable version bumps of Custom Proton version per game
* **[ReShade Presets](#ReShade-Presets)** Select ReShade Presets
* **[Cheat Engine](#Cheat-Engine)** automatic CheatEngine download, install, autostart per game and autostop on game exit
* **[Pressure Vessel](#Pressure-Vessel)** Some Pressure Vessel options
* **[Wine Support](#Wine-Support)** Download and use custom Wine archives instead of Proton
* **[Backup Support](#Backup-Support)** optionally automatic backup of 'steamuser' files of the 'steamuser' files per Proton game
* **[Metadata Support](#Metadata-Support)** Collect as much as possible gamedata to make further automations easier and faster

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
- a graphical text editor and optionally a internetbrowser see [Global Config](#Global-Config)
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

### Settings Menu
The Settings Menu consists of multiple separate submenus, where most be be reached via [Selection Menu](#Selection-Menu).
Tooltips give a basic description for every entry in all submenus.
When **stl** was launched "standalone" via [Command Line](#Command-Line) the corresponding game will be started using the steam `-applaunch` parameter.

#### Selection Menu
There central menu is the Selection Menu
from where all other submenus can be reached directly or indirectly.
*(Currently)* it has following options:

- **Exit** - Exit the program. If started from Steam game launch will be canceled as well
- **GUI SETS** - Opens the submenu [Gui Settings Menu](#Gui-Settings-Menu) for several Gui related Settings 
- **CATEGORY** - Opens the dropdown [Category Menu](#Category-Menu)
- **GAME MENU** - Opens the [Game Menu](#Game-Menu)
- **DEFAULT** - Opens the [Default Menu](#Default-Menu)
- **GLOBAL** - Opens the 1st part of the [Global Menu](#Global-Menu)
- **GLOBAL** - Opens the 2nd part of the [Global Menu](#Global-Menu)
- **FAVORITES** - Opens the [Favorites Menu](#Favorites-Menu)
- **EDITOR** - Opens the [Editor Dialog](#Editor-Dialog)
- **PLAY** - Starts the current game

![gui selection](https://github.com/frostworx/repo-assets/blob/master/pics/gui-selection.jpg)

#### Gui Settings Menu
 - **BACK** - Go back to previous menu
 - **FAVORITES SELECTION** - Opens the [Favorites Selection](#Favorites-Selection) where the [Favorites Menu](#Favorites-Menu) entries can be selected
 - **BLOCK CATEGORIES** - Opens the [Block Categories Selection](#Block-Categories-Selection) where whole Categories can be disabled
 - **SORT CATEGORIES** -see [Sort Categories](#Sort-Categories)
 - **GUI OPTIONS** - Opens the [GUI Options](#GUI-Options)
 - **EXTRA BUTTONS** - Opens the [Extra Buttons Menu](#Extra-Buttons)

![gui settings](https://github.com/frostworx/repo-assets/blob/master/pics/gui-settings.jpg)

#### Category Menu
A small dropdown Menu where a Sub Category Menu to open can be selected.
The Menus are all autogenerated from the code.
![category selection](https://github.com/frostworx/repo-assets/blob/master/pics/category-selection.jpg)

The [GUI Options](#GUI-Options) option from the [Gui Settings Menu](#Gui-Settings-Menu) is simply one of those Menus.

##### GUI Options
An autogenerated Menu which offers all GUI related configuration options.

![gui menu](https://github.com/frostworx/repo-assets/blob/master/pics/gui-menu.jpg)

#### Game Menu
The Game Menu is the Menu for the selected game *(either started from steam or via [Command Line](#Command-Line)/last started one)*
All options in here are stored in the [Game Config](#Game-Config).

#### Default Menu
In the Default Menu the template [Default Config](#Default-Config) for all newly created gameconfigs
for the [Game Menu](#Game-Menu) can be configured.

#### Global Menu
Here are all global configurations which are valid for all games. As these are pretty many Menu is split into two parts.

#### Favorites Menu
This is the user customizable Favorites Menu, which shows only the entries the user is interested in.
It can be opened 
- as [Start Menu](#Start-Menu) for the wait requester
- via 
- via [Selection Menu](#Selection-Menu)

![favorites menu](https://github.com/frostworx/repo-assets/blob/master/pics/favorites-menu.jpg)

It can be configured with the [Favorites Selection](#Favorites-Selection), which is opened automatically with a basic preset if nothing was selected yet.
 
##### Favorites Selection
Here the [Favorites Menu](#Favorites-Menu) entries can be selected.
Every available Menu option can be selected via checkbox and is listed with description, tooltip and variablename.
This Menu optionally also shows up, when the [Favorites Menu](#Favorites-Menu) is opened and no custom [Favorites Config](#Favorites-Config) exists (yet).
For a quickstart, when started for the first time some entries are preselected. 

![favorites selection](https://github.com/frostworx/repo-assets/blob/master/pics/favorites-selection.jpg)
 
#### Block Categories Selection
Here categories can be selected via checkbox, which should not show up in the Settings Menus at all.

![block selection](https://github.com/frostworx/repo-assets/blob/master/pics/block-selection.jpg)

#### Sort Categories
An optionally preconfigured "menusort.conf" is opened with the [Editor](#Editor) where the default category sort order can be configured.
Duplicate entries will be removed automatically.

#### Extra Buttons
A little Menu with some functions behind buttons, which do not find good into other locations.
*(you have to export lots of variables and functions for 'vertical buttons' in yad, therefore this solution)*
Currently only constist of

- **BACK** - Go back to previous menu
- **DOWNLOAD CUSTOM PROTON** - Opens the [Download Custom Proton](#Download-Custom-Proton) Menu
- **DOWNLOAD WINE** - Opens the [Wine Download](#Wine-Download) Menu
- **UPDATE SHADERS** - Opens the [Shader Management](#Shader-Management) for the current game

![extra buttons](https://github.com/frostworx/repo-assets/blob/master/pics/extra-buttons.jpg)

#### Editor Dialog
A little File selection requester allowing to choose which config files to open with the [Editor](#Editor).
The [Editor Dialog](#Editor-Dialog) can be opened either via [Settings Menu](#Settings-Menu) or [via Command Line](#via-Command-Line).

#### Gui Window Size
When `SAVESETSIZE` is enabled in the [Global Config](#Global-Config) *(f.e. via [Global Menu](#Global-Menu))* *(by default it is)* resolution changes of every **stl** window are automatically saved
when the corresponding window is closed. This function requires xwininfo to work.
All resolutions will be stored in the [Gui Config](#Gui-Config).
If you prefer window decoration to resize windows, you can enable it in the [Global Menu](#Global-Menu) or directly in the [Global Config](#Global-Config)
*(else hold Left-Alt while resizing the window while holding the right mouse button)*.

### Tray Icon
**stl** also offers a Tray Icon, which automatically starts and is available until **stl** *(or the started game)* exits.
Can be disabled *(by default enabled)* with disabling `USETRAYICON` in the [Global Config](#Global-Config) *(f.e. via [Global Menu](#Global-Menu))* .
Right Click opens The Menu.
Middle Click Closes The Menu

#### Tray Icon Buttons
- "Kill Proton Game" *(kills the currently running Proton game by killing its wineserver)*
- "Pause/Unpause active window" *(waits 5 seconds and un-/pauses the process of the window which is currently active)*
- "Shader Menu" *(opens [Shader Management](#Shader-Management) for the currently running Game - Shaders can be added/removed on the fly here)*
- "Open running game in VR" *(opens the running game in [SBS-VR](#Side-by-Side-VR))*

### Configuration Locations

#### User Configuration

The main user configuration directory `STLCFGDIR` can be found under
`$HOME/.config/stl` (or `XDG_CONFIG_HOME/stl` if `XDG_CONFIG_HOME` is set).

When started for the first time **stl** will initially create a default configuration structure in its configdir `STLCFGDIR`

#### Systemwide Configuration
The systemwide configuration directory `SYSTEMSTLCFGDIR` can be found under `/usr/share/$PROGCMD` *(/usr/share/stl/)*

All configs used here are read first, so user configs override them if required.
System-wide configs help to keep configuration easy and get things to work ootb.
f.e. there are preconfigured [Steam Category](#Steam-Categories),
custom per-game [registry](#Registry) files, which are autodetected and applied *(when `REGEDIT` is 1)*,
*community contributed* [tweaks](#Tweaks) which make sure specific games work ootb using the provided configuration options,
*community contributed* [sbs tweaks](#SBS-Tweaks) which make sure specific games work ootb in [SBS-VR](#Side-by-Side-VR) mode using the provided configuration options

##### self maintaining configs
With the variable `DLGLOBAL` being set to 1 *(it is by default)* **stl**
uses systemwide configurations from the directory `STLDLDIR/stl` and also git pulls this repo into there (max once per day).
This **only** is used when the systemwide configuration directory `SYSTEMSTLCFGDIR` does not exist at all!
As almost no distro provides a stl package, the idea is that the user only has to copy stl into `$PATH`
and still can make use of the bundled config files without having to install them manually.
No executable files will be used from here!

Auto-generated [auto tweaks](#Auto Tweaks) imported from other platform will be loaded before global configs, so global configs override them by default.

### Global Config
`STLDEFGLOBALCFG` *(`$STLCFGDIR/global.conf`)*

Contains universal configuration options used all games, f.e.
file paths, command line options for supported 3rd party programs, but also general "behavior" settings
*(f.e. [Logs](#Logs) mode or timeout for the [Settings Menu](#Settings-Menu) and [Editor](#Editor)WAITEDITOR)*
All available options can be configured in the [Settings Menu](#Settings-Menu) with [Global Menu](#Global-Menu) being the central location.


### Gui Config
`STLGUICFG` *(`$STLCFGDIR/gui.conf`)*
All [window sizes](#Gui-Window-Size) will be stored in this config when `SAVESETSIZE` is enabled *(by default it is)* - see [Gui Window Size](#Gui-Window-Size).
The initial resolution of all windows is calculated based on the screen-resolution.

### Url Config
`STLURLCFG` *(`$STLCFGDIR/url.conf`)*
For a transparent and easy overview all URLs available in **stl** are stored in here.
The file can always be selected in the [Editor Dialog](#Editor-Dialog), but Url is also a usable Category available in the [Category Menu](#Category-Menu)

### Game Configurations

#### Game Config
`STLGAMECFG` *(`$STLCFGDIR/gamecfgs/$SteamAppId.conf`)*

When starting a game using **stl** the game specific config file `STLGAMECFG` is searched in `STLGAMEDIR`
and created if not available from the [Default config](#Default-Config) file *(which in turn is automatically created as well if not found)*.
All available options can be configured in the [Settings Menu](#Settings-Menu) with [Game Menu](#Game-Menu) being the central location.

#### Default Config
`STLDEFGAMECFG` *(`$STLCFGDIR/default_template.conf`)*

Contains the default configurations options used as template for every new [Game Config](#Game-Config).
Most options are disabled by default. To deploy appropriate global options early this file should be adjusted early.
All available options can be configured in the [Settings Menu](#Settings-Menu) with [Default Menu](#Default-Menu) being the central location.

#### Favorites Config
`STLFAVMENUCFG` *(`$STLCFGDIR/favorites.conf`)*
Basically a plain list with all user selected configuration options variables which should be available in the
[Favorites Menu](#Favorites-Menu). The config can be configured with the [Favorites Selection](#Favorites-Selection).


### Steam Categories
**stl** parses the Steam categories of the started game and examines if a associated **stl** configuration file exists
under the same name (case-sensitive, but written uppercase in Steam **!**)

If a configuration file is found it is initialized as additional config file.

This makes it easy to create "Configuration categories" by
- simply creating a Steam Category
- creating a categories configfile under the same name and defining settings in it
- adding a game to the category to use those settings automatically

Category Configuration Files are searched in the [User Configurations](#User-Configuration) `STLCATEGORYDIR` *(`STLCFGDIR`/categories)*
or in the [system-wide](#Systemwide-Configuration) dir `GLOBALCATEGORYDIR` *(`SYSTEMSTLCFGDIR/categories)`*
where some category files are already preconfigured:

a game in the corresponding category
- **CheatEngine.conf** [Cheat Engine](#Cheat-Engine) is automatically started with the game.
- **DOSBox.conf** is started automatically with linux native dosbox provided by [Boxtron](#Boxtron)
- **GameConqueror.conf** [GameConqueror](#GameConqueror) is automatically started with the game.
- **Luxtorpeda.conf** is started automatically with linux native binary provided by [Luxtorpeda](#Luxtorpeda)
- **ReShadeVR.conf** is started automatically in [SBS-VR](#Side-by-Side-VR) mode using [ReShade](#ReShade)
- **SBS-VR.conf** is started automatically in [SBS-VR](#Side-by-Side-VR) mode without Shader (for games with builtin Stereoscopic3D support)
- **ScummVM.conf** is started automatically with linux native scummvm provided by [Roberta](#Roberta)
- **Vortex.conf** is started automatically with the [Vortex](#Vortex) Mod Manager
- **vkVR.conf** is started automatically in [SBS-VR](#Side-by-Side-VR) mode using [vkBasalt](#vkBasalt) and 

Multiple Category Configuration Files are possible, they are loaded one after another, with the last one overriding settings also found in the previous files.
All settings which are also configured in `$STLGAMECFG` are overridden (but not overwritten).

The function can be diabled per game with the option `CHECKCATEGORIES` 

The same function also checks if a script with the same name  *(".sh" suffix expected)* as the Steam category is in the global `GLOBALTWEAKCMDDIR` and in the user `TWEAKCMDDIR`.
When found it is executed before the game with following 3 commandline parameters
 1) SteamAppID
 2) Game directory
 3) Game wineprefix

*(of course the script should not block the actual game start, and it is up to the user what is actually executed in the script)*

### Tweaks

All different user writable tweakfiles live in their own subdirectory under `TWEAKDIR` *("$STLCFGDIR/tweaks")*

If a tweak config `TWEAKCFG` ( `SteamAppID.conf` ) in `GLOBALTWEAKDIR` or `USERTWEAKDIR` *(overrides global)* is found its settings
overrides the settings in the [Game Config](#Game-Config).
By means of this function it is be possible to contribute tweak configs required to get games to work hazzlefree out of the box to the community.
With `CREATETWEAKS` a default template tweak file is autogenerated on game launch, to make creating one a bit easier.

Some systemwide tweaks can already be used (see [Installation](#Installation)).

If you use/create tweaks make sure to retest your game with later proton versions without the tweak and report upstream if the bug is fixed!
The used proton Version is automatically written into the tweak file when created with `CREATETWEAKS`.
User tweak-files in `USERTWEAKDIR` override global tweaks in `GLOBALTWEAKDIR`, [Autotweaks](#Auto Tweaks)

#### Tweakfiles
An example tweakfile looks like this:

`stl/tweaks/user/8080.conf:`

```
#########
#GAMENAME=Kane and Lynch Dead Men
#GAMEEXE=Launcher
#GAMEID=8080
#PROTONVERSION=proton-5.0-10-rc4
#########
WINETRICKSPAKS=d3dx9_31 d3dx9_34
PROTON_NO_ESYNC=1
PROTON_NO_FSYNC=1
NOGFWL=1
```

Explained in detail:
When the game "Kane and Lynch Dead Men" is started **stl** will find its tweakfile *(8080.conf = SteamAppId.conf)*
and apply following configurations:

- d3dx9_31 d3dx9_34 will be installed via wintricks
- PROTON_NO_ESYNC and PROTON_NO_FSYNC will both be set to 1
- gfwl will be removed

This works completely automatically and transparent without any user interaction.
*(of course the first start will need some time when aditional packages are installed)*

### Tweak Commands

It is also possible to define a script under `TWEAKCMD` *(f.e. in `TWEAKCFG`)* which should be started before the game launch.
This is especially useful when it is necessary to move or rename game files to get a game working.
When a `TWEAKCMD` is defined **stl** will check if it finds the file
- as absolute path
- in the system tweak directory
- in the user tweak directory
- in the gamedir

In case the file was found **stl** checks if a `TWEAKFILE` is defined in the `TWEAKCMD` file.
This comes in handy when the script requires a specific file (f.e. a custom game exe) which is not available for everybody.
With this little "dependency check" the tweak file is simply skipped if the file was not found and the tweak can still be shared in the community.
Not exported variables are not available in the script, but usually none should be required (yay might want to check `env` for available vars)

- `GPFX="$STEAM_COMPAT_DATA_PATH/pfx"` :can be used as variable for the games `WINEPREFIX`
- `GFD="$(awk -F 'common' '{print $1}' <<< "$PWD")common/$(awk -F 'common' '{print $NF}' <<< "$PWD" | cut -d'/' -f2)"`: can be used for the base game dir

### SBS Tweaks

Game specific config files `SteamAppID.conf` both in and [system-wide](#Systemwide-Configuration) *(`GLOBALSBSTWEAKDIR`)* and [User Configurations](#User-Configuration) *(`SBSTWEAKDIR`)*
with optimal settings for [SBS-VR](#Side-by-Side-VR) *(f.e. launcher skips using the game exe as custom command)*.

Here's an example config for trine 2 `STLCFGDIR/sbs/35720.conf`

```
#########
#GAMENAME=Trine 2
#GAMEEXE=trine2_launcher
#GAMEID=35720
CUSTOMCMDMODE="always"
CUSTOMCMD=trine2_32bit.exe
ONLY_CUSTOMCMD=1
GAMEWINDOW=Trine 2
```

Means, when `RUNSBSVR` is not 0 in the main Trine2 config file it will autodetect above sbs tweak config and use the defined variables:
Trine 2 won't start it's original launcher (`ONLY_CUSTOMCMD=1`), but only the custom command `trine2_32bit.exe` and will wait for a `Trine 2` window to open in **VR**

So in general sbs configs are automatically loaded when found and override settings in the main config
so you just have to enable `RUNSBSVR` in `STLCFGDIR/gamecfgs/35720.conf` and everything else is configured automatically.

### Auto Tweaks

**stl** allows to import required game config files from several other platforms.
The path to those autogenerated tweaks is
`AUTOTWEAKDIR` *("$TWEAKDIR/auto")* with "$platform" as subdirectory.

All platforms from where configurations shall be imported need to be listed in the
global `AUTOTWEAKS` variable.
All enabled autotweak platform tweak files are loaded before all other configs, so it is always possible to override them later.
This is necessary, as aparrently not all autogenerated configs can be tested.

When `ATVALIDATE=0` the order in `AUTOTWEAKS` decides in which order they are loaded.
The later a config is found the more important it is, as it discards the configs found from previous platforms.
With `ATVALIDATE` being disabled there is apparently no control over what will be actually loaded.

When the variable `ATVALIDATE` is >0 a requester will pop up
asking the user if he wants to open the autocreated config with the editor
*(also her in the same order as the platforms are listed in `AUTOTWEAKS`)*
Afterwards another requester asks if the config should be loaded or skipped.
When multiple Auto Tweak Configs are found the requesters are opened for all of them,
but only the last accepted config is actually loaded!

If `IGNOREAUTOTWEAKS=1` is set in the current gameconfig `$STLGAMECFG` all autotweaks are skipped automatically.
If `ATADOPT=1` is set in the current gameconfig a requester will pop up when th game exited
asking if the used AutoTweak config should be converted into a regular tweakconfig.
Autotweaks will be disabled in this new config then.


#### Creating Auto Tweaks

Auto Tweaks are either autocreated on game launch automatically (if the chosen `AUTOTWEAKS` support the game)
or can be .


**stl** will download an active repo on the first run and prepare the datafiles for better searching if required.
To keep downloads as low as possible, on later runs the already downloaded data will be re-used where possible.

When started directly from Steam **stl** searches for a gamefix for the current SteamAppID.
If one is found the gamefix will be converted into a **stl** autotweakfile under `AUTOTWEAKDIR/protonfixes`.
This config is then applied like described in [Auto Tweaks](#Auto Tweaks) above.

Creating Auto Tweaks via **stl** [Command Line](#Command-Line):

`stl autotweaks|at ('dl') PLAFTORM (optional steamid)`

Will autogenerate all tweak files for every parsible game of platform PLATFORM or just for the optional SteamAppID
Example:

`stl autotweaks|at lutris`
Creates for all supported Games Autotweak files in `AUTOTWEAKDIR/lutris`

`stl autotweaks|at lutris 883710`

Creates only for game 883710 an Autotweak file.

Using the option 'dl' the corresponding platform source is updated before the actual process starts - f.e:
`stl at dl lutris`


**Depending on the platform stl filters several original configuration options.
If you think something important is missing please open an issue!**

#### ProtonFixes
Some [protonfixes](https://github.com/simons-public/protonfixes) gamefixes are marked as deprecated inside protonfixes.
Those and a handful more (mostly those copying/changing files) are skipped automatically.
When run from terminal those skipped will be listed.
To see how Auto Tweak files are created read general describtion from above [here](# Creating Auto Tweaks)

Currently following options are imported into the Auto Tweak file:

- winetricks packages
- alternative executables
- env variables
- dll overrides
- game command line arguments

#### Lutris
[Lutris](https://github.com/lutris/lutris) is pretty huge and supports many different platforms.
**stl** uses multiple filters to extract the following options into the Auto Tweak file:

- winetricks packages
- commandline arguments
- env variables
- dll overrides
- pulseaudio latency
- xlive
- mfplat
- basic script creation *(`TWEAKCMD`)*
- downloads and their extraction will be added commented out in the autotweak file

To see how Auto Tweak files are created read general describtion from above [here](# Creating Auto Tweaks)


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

### Logs
Logs are written into the `LOGDIR` defined in the [Global Menu](#Global-Menu) / [Global Config](#Global-Config).
The verbosity of the logfile depends on `WRITELOG` *(write logfile if not 0, increase verbosity from 1-2 (1:less, 2:all))*
in the same location.
There are several logfiles, those which are written mostly are the game specific ones *($SteamAppId.log)*

## Features in detail:

#### Proton Selection
**stl** provides the option to easily choose a specific Proton Version per game, by simply selecting one from an autogenerated dropdown Menu in
the [Game Menu](#Game-Menu).

The function can also be en-/disabled in the [Game Menu](#Game-Menu) *(by default disabled!)*, but if **stl** is used as [Steam Compatibility Tool](#Steam-Compatibility-Tool) with a Proton game,
a force override flag disables the set flag, as it obviously requires any Proton version to start. In this case the latest official Proton Version is set by default.

The List of available Proton Versions is generated on the first **stl** launch *(in `/dev/shm`)* and recreated when a new Proton Version was added on the fly.

**stl** searches in the following sources for Proton Versions to generate the list:
- user installed compatibility tools *(~/.steam/steam/compatibilitytools.d/)*
- system-wide compatibility tools *(/usr/share/steam/compatibilitytools.d)*
- official proton versions installed via Steam in default SteamLibrary *(~/.steam/steam/steamapps/common/)*
- official proton versions installed via Steam in additional SteamLibrary Paths *(the additional Paths are extraced from ~/.steam/steam/config/config.vdf)*
- a [custom Proton List](#Custom-Proton-List)

##### Custom Proton List
The optional custom Proton List `CUSTOMPROTONLIST` in [`STLCFGDIR`](#User-Configuration)
is used as additional source for custom Proton Versions for inclusion into the autogenerated Proton Version (dropdown) List.

###### Adding Entries to the Custom Proton List

There are several methods to add new entries to the list
*(besides editing it manually / via [Editor Dialog](#Editor-Dialog))*:

###### Adding local Custom Proton
a locally installed Custom Proton can be added
- via [Command Line](#Command-Line): `stl addcustomproton` or just `stl acp` 
  *(accepting an absolute path to a proton executable as optional argument)*

A `proton` file can be selected via file-requester
and an optional "proton version name" can be entered in a separate field.

###### Download Custom Proton
Custom Proton packages can also be downloaded and added by
- using the button `Download Custom Proton` in the [Extra Buttons Menu](#Extra-Buttons)
- via [Command Line](#Command-Line): `stl dlcustomproton|dcp <url>`
  *(accepting direct download URL  as optional argument)*

With either method a download requester with a dropdown menu is opened.

![stl download custom proton gui with german translation](https://github.com/frostworx/repo-assets/blob/master/pics/stl-dcp.jpg)

The menu is autogenerated, by parsing all `CP_*` *(Custom Proton)* URLs from the [Url Config](#Url-Config)
for proton packages. Currently following Custom builds are parsed *(feel free to recommend one if you think something is missing)*

- [GloriousEggroll](/https://github.com/GloriousEggroll/proton-ge-custom)
- [Proton TKG](https://github.com/Frogging-Family/wine-tkg-git)
- [Protola](https://github.com/Patola/wine)

Packages *(`tar.*`, `zip`)* containing a `proton` file will be extracted and added to the List of available Proton Builds.

###### Automatic Proton version
Using the variable `WANTPROTON` in configs and tweaks it is possible to automatically request a specific proton version to be used with the corresponding game.
If `AUTOPULLPROTON` is enabled *(it is by default)* **stl** will automatically download the specific proton version and install it.

#### Custom Proton Autoupdate
**stl** can optionally check if a newer version of the currently (per game) configured custom *(only!)* proton exists
and automatically reacts depending on the user configuration.

The variable `PROTONCHECK` can be set per game to one of the following:
- `disabled`              : the whole check is skipped
- `ask_before_menu`       : call checkProtonBump only when the settings menu is opened and open a [Custom Proton Autoupdate Requester](#Custom-Proton-Autoupdate-Requester)
- `ask_before_game`       : call the function only before the game is launched and open a [Custom Proton Autoupdate Requester](#Custom-Proton-Autoupdate-Requester)
- `auto_download`         : automatically download and extract  but don't replace the currently used custom proton version
- `auto_download_and_use` : automatically download, extract and replace the active custom proton version of the current game
- `only_notify`           : only pop up notifier

##### Custom Proton Autoupdate Requester
If a newer minor version for the currently used custom Proton is available and 
`PROTONCHECK` is either `ask_before_menu` or `ask_before_game` (see [Custom Proton Autoupdate](#Custom-Proton-Autoupdate)
a Requester will pop up, giving the option to either
- skip the update
- only download and extract the new custom proton version
- download, extract and immediately use the new custom proton version for the current game


#### Multi-Language Support
**stl** Multi-Language Support *(currently with [these languages](https://github.com/frostworx/steamtinkerlaunch/tree/master/lang))*.

At least the default language file (english) needs to be found, else **stl** will exit with an error.
**stl** searches both in the [Systemwide Configuration](#Systemwide-Configuration) and in the [User Configuration](#User-Configuration) for language files,
where those in the latter have a higher priority *(so copying a systemwide file to improve it is possible)*

Every language found can be selected from the Language Dropdown Menu in the [GUI Options](#GUI-Options).
*(a change requires a restart to take effect)*.

To give also the option to get a translated description in freshly created **stl** configfiles
it is also possible to define an available language or an absolute path to a valid language file with the `lang=` [Command Line](#Command-Line) option.

When no language file was found as a last resort **stl** will download its own projectpage and use the language file from there.

*(every language file simply consists of multiple variables defining a text, so to contribute a translation,
simply duplicate one of the existing ones and translate all variables inside)*

#### Steam Linux Runtime
Introduced with proton 5.13-1 the Steam Linux Runtime is autostarted and part of the game command line parameters.

When **stl** is used as [Launch Option](#Launch-Option)
both the Steam Linux Runtime and the [Proton Version](#Proton Selection) show up in the Steam Game launch command and therefore can be read by **stl**.
In that case the Steam Linux Runtime can be disabled per game in the [Game Config](#Menu-Config) *(f.e. via [Game Menu](#Game-Menu))*
and if one *(or more)* of above confliciting tools are enabled **stl** warns that it is incompatible with the Steam Linux Runtime *(for now)*.

When starting **stl** as [Steam Compatibility Tool](#Steam-Compatibility-Tool) there are no Steam Linux Runtime parameters in the Steam Game launch command and therefore cannot be disabled
*(maybe comparable to the [Proton Version](#Proton Selection) which doesn't show up as command line parameter as well and is used 'under the hood')*.

#### Game Launcher

**stl** comes with a small Game Launcher, which starts selected games using the steam `-applaunch` parameter.
The Launcher has several modes, which can be selected via [Command Line](#Command-Line):
- Without additional command line parameters:
  `stl launcher` *(will start the Game Launcher with all installed games)*
- Optional arguments for launcher are:

 - `stl launcher $CATEGORY` *(will show only the installed games in the steam category `$CATEGORY`)*
 - `stl launcher menu` 		*(will open a small menu with all available steam categories)*
 - `stl launcher last` 		*(will open the last played game as 'menu')*
 - `stl launcher auto` 		*(automatically creates/downloads required data for all installed games before opening the launcher with all installed games)*
 - `stl launcher update` 	*(recreates the already autogenerated category menus - can be combined with auto')*
 - `stl launcher $INVALID` 	*(with any invalid parameter all faound valid Steam Categories will be listed)*

The contents of the corresponding categories are autogenerated on the fly *(in `/dev/shm/`)* using [Game Pictures](#Game-Pictures) and [Desktop Files](#Desktop-Files).
With above `auto` both [Game Pictures](#Game-Pictures) and [Desktop Files](#Desktop-Files) are autogenerated/downloaded if missing.

![stl Game Launcher](https://github.com/frostworx/repo-assets/blob/master/pics/stl-gamelauncher.jpg)

#### Game Pictures

By default **stl** downloads automatically the main `header.jpg` picture from *(configurable `STASSURL`)* if not found and saves it under the `SteamAppID` name.
Those pictures are for example used in the [Game Launcher](#Game-Launcher) *(via [Desktop File](#Desktop-Files))* and also in the [Wait requester](#Wait-Requester),
in the [Editor Dialog](#Editor-Dialog) and in the [Settings Menu](#Settings-Menu).

Downloading of the Game Pictures can be disabled with `DLGAMEDATA` in the **GLOBAL SETTINGS** of the [Settings Menu](#Settings-Menu).
Displaying the Game Pictures can be disabled in the **GLOBAL SETTINGS** of the [Settings Menu](#Settings-Menu) as well or directly by disabling `USEGAMEPICS`.
Displaying the Game Pictures only  can be disabled  in the [Settings Menu](#Settings-Menu) or directly by disabling `USEGAMEPICINMENU`.

#### Desktop-Files
The [Game Launcher](#Game-Launcher) *(yad)* takes a directory containing desktopfiles as argument and lists all of them.
Those Desktop-Files are [autogenerated](#Game-Data) using the *(big)* [Game Pictures](#Game-Pictures) in the `STLCFGDIR` and therefore are of no use for generic usage.

#### Game Data

Both [Game Pictures](#Game-Pictures) and [Desktop Files](#Desktop-Files) *(for the [Game Launcher](#Game-Launcher))* are autogenerated/downloaded
per game start by default but also can be batch created via [Command Line](#Command-Line):

- `stl update gamedata` *(updates missing desktopfiles and pictures of installed games and exits - depending on the missing files this might need some time)*
- `stl update gamedata $APPID` *(updates missing desktopfiles and picture for game `$APPID`)*
- `stl update allgamedata` *(updates missing desktopfiles and pictures of **all** games in 'sharedconfig.vdf' and exit - depending on the missing files this might need some time)*


#### Custom Program
*(in [Game Menu](#Game-Menu) and [Game Config](#Game-Config))*

When enabled you can start custom programs easily with the following per-game config options:

- `CUSTOMCMDMODE`: set to 1 or 2 *(see below)* to start the custom command `CUSTOMCMD`
- `CUSTOMCMD`: start this custom command
- `CUSTOMCMD_ARGS`: start `CUSTOMCMD` command with those args
- `ONLY_CUSTOMCMD`: set to 1 to only start `CUSTOMCMD` and not the game command itself
- `FORK_CUSTOMCMD`: set to 1 to fork the custom `CUSTOMCMD` into the background and continue with starting `%command%`

If only `CUSTOMCMDMODE` is enabled, but `CUSTOMCMD` is empty, a requester will open where a executable file can be selected.
When `CUSTOMCMDMODE` is `"always"` this selected file is automatically written into the [Game Config](#Game-Config).
When `CUSTOMCMDMODE` is `"once"` this selected file is only started this time without saving the exe into the config.
This is especially useful for installers *(see provided [Steam Category](#Steam-Categories) 'Installer')*

If string `CUSTOMCMD` can't be found as file in either `PATH`, in game dir or as absolute filepath the requester will open as well.

#### Start Stop Scripts
If commands are defined in `USERSTART` `USERSTOP` they will be executed when a game starts/ends.
*(in [Game Menu](#Game-Menu) and [Game Config](#Game-Config))*

Of course the user is responsbile for what is executed here and needs take care that it both works and exits correctly!

Both scripts make use of following commandline arguments:
- SteamAppID as argument1
- the absolute path to the game exe as argument2
- and the WINEPREFIX of the game as argument 3

#### Winetricks
[Winetricks](https://wiki.winehq.org/Winetricks)
*(in [Game Menu](#Game-Menu) and [Game Config](#Game-Config))*
GUI:
Set `RUN_WINETRICKS` to 1 to start winetricks gui before game launch

Silent winetricks installation:
- `WINETRICKSPAKS`: install all packages in WINETRICKSPAKS silently with winetricks

Set `DLWINETRICKS` to 1 download/and automatically update winetricks instead of using/depending on the systemwide installation

dotnet installation might be problematic because of this [wine bug](https://bugs.winehq.org/show_bug.cgi?id=49897)
**stl** opens a *(non-blocking)* warn requester if a incompatible wine version was found until the bug is fixed.

#### Winecfg
*(in [Game Menu](#Game-Menu) and [Game Config](#Game-Config))*
- `RUN_WINECFG`: set to 1 to start winecfg before game launch

#### Boxtron

[Boxtron](https://github.com/dreamer/boxtron):

The global configs `BOXTRONCMD` and `BOXTRONARGS` in the [Global Config](#Global-Config) *(f.e. via [Global Menu](#Global-Menu))*  need to be set correcty initially.
It should not be necessary to change the default `ROBERTAARGS`.
Defaults are:
**
BOXTRONCMD=/usr/share/boxtron/run-dosbox
BOXTRONARGS=--wait-before-run
**
which is at least valid if you are on Arch Linux and installed boxtron from AUR.

To start a game with boxtron either set `USEBOXTRON` in the [Game Config](#Menu-Config) *(f.e. via [Game Menu](#Game-Menu))* or put the game into the [steam category](#Steam-Categories) "DOSBox"
Alternatively duplicate the file to a different name which you want to use as category name, ideally into [`STLCATEGORYDIR`.](#Steam-Categories).

#### Roberta

[Roberta](https://github.com/dreamer/roberta):

The global configs `ROBERTACMD` and `ROBERTAARGS` in the [Global Config](#Global-Config) *(f.e. via [Global Menu](#Global-Menu))* need to be set correcty initially.
It should not be necessary to change the default `ROBERTAARGS`.
Defaults are:
**
ROBERTACMD=$HOME/.local/share/Steam/compatibilitytools.d/roberta/run-vm
ROBERTAARGS=--wait-before-run
**
which is at least valid if you installed roberta manually.

To start a game with roberta either set `USEROBERTA` in the [Game Config](#Menu-Config) *(f.e. via [Game Menu](#Game-Menu))* or put the game into the [steam category](#Steam-Categories) "ScummVM"
Alternatively duplicate the file to a different name which you want to use as category name, ideally into [`STLCATEGORYDIR`.](#Steam-Categories-dir).

#### Luxtorpeda
[Luxtorpeda-dev](https://github.com/luxtorpeda-dev/luxtorpeda) or *(untested)* the [main branch](https://github.com/dreamer/luxtorpeda)

The global configs `LUXTORPEDACMD` and `LUXTORPEDAARGS` in the [Global Config](#Global-Config) *(f.e. via [Global Menu](#Global-Menu))*  need to be set correctly initially.
It should not be necessary to change the default `LUXTORPEDAARGS`.

Defaults are:
**
LUXTORPEDACMD=$HOME/.local/share/Steam/compatibilitytools.d/luxtorpeda/luxtorpeda
LUXTORPEDAARGS=wait-before-run
**
which is at least valid if you installed roberta manually.

To start a game with luxtorpeda either set `USELUXTORPEDA` in the [Game Config](#Menu-Config) *(f.e. via [Game Menu](#Game-Menu))* or put the game into the [steam category](#Steam-Categories) **"Luxtorpeda"**
Alternatively duplicate the file to a different name which you want to use as category name, ideally into [`STLCATEGORYDIR`.](#Steam-Categories-dir).
The luxtorpeda-dev dev was so kind to add a manual-download option in v20, so if native game files are missing they are downloaded before the actual game launch now.
Therefore it is recommended to use the lastest luxtorpeda-dev version.

#### Native Games
**stl** also works with native linux games.
Currently the first distinction is if "waitforexitandrun" appears in the game %command%.
If yes, **stl** assumes we have a proton game. Now, when another check finds "steamapps/common" (without "waitforexitandrun") a linux game is assumed, and the *(now generic)* launchSteamGame function is started.
Looks like only proton games have the Variable `STEAM_COMPAT_DATA_PATH`, so if it is missing several features are disabled in the setLinGameVals function,
as they do not work with native linux games (f.e. [ReShade](#ReShade)). The Game and Exe Path Variables are differently extracted as well when `STEAM_COMPAT_DATA_PATH` is missing.


#### GFWL
Some games still depend on GFWL which is discountinued and doesn't work under wine.
With the variable `NOGFWL` set to 1 for a game **stl** takes care that
everything is configured automatically to start the game ootb.
*(in [Game Menu](#Game-Menu) and [Game Config](#Game-Config))*
If the dependant xlive.dll is missing it will be downloaded automatically
( [from Ultimate-ASI-Loader](https://github.com/ThirteenAG/Ultimate-ASI-Loader/releases) )
into `$STLDLDIR/xlive/` and installed into the gamedir.
**stl** ships already several tweak files, which enable `NOGFWL` for some games (f.e.: "Fable 3 (105400)", "Resident Evil 5 (21690)", "Kane and Lynch Dead Men (8080)", "FlatOut Ultimate Carnage (12360)"

#### WMP10
Games which depend on WMP10 can be played by setting the variable `HACKWMP10` to 1.
*(in [Game Menu](#Game-Menu) and [Game Config](#Game-Config))*

[Tweak](#Tweaks) with automatic support already implemented for

**
Giana Sisters Twisted Dreams (223220)
Giana Sisters - Rise of the Owlverlord (246960)	
**

#### Vortex
[Vortex Mod Manager](https://github.com/Nexus-Mods/Vortex)

##### Starting Vortex:
Vortex can be used without any **stl** configuration and will work ootb without zero configuration.

There are 3 different ways to start Vortex:

###### Start Vortex using Steam Category
Just create a "Vortex" [Steam Category](#Steam-Categories) and add your (Vortex compatible) game to it and start the game regularly.
Vortex will start, with the selected game preconfigured and ready to mod
and when you exit Vortex the selected game will start normally (with your mods).

###### Start Vortex using commandline:
see [Command Line](#Command-Line)

###### Start Vortex by enabling it in the Settings Menu:
The `VORTEXMODE` option in the [Game Config](#Menu-Config) *(f.e. via [Game Menu](#Game-Menu))* has the following modes:
- "disabled": Vortex won't be used
- "normal": Vortex will be started regularly
- "quickstart": Vortex will be started but some checks are skipped
- "editormode": Vortex will be started in quickstart mode, but the selected game won't start after Vortex is closed

##### stl Vortex gif
![stl Vortex in action](https://github.com/frostworx/repo-assets/blob/master/gifs/stl-vortex.gif)

**Installation**
If Vortex is not yet installed, it will be installed on the first launch, so the first launch will need some time
*(mostly depends on dotnets mind of its own... maybe 5 minutes - see [Additional Vortex Notes](#Additional-Vortex-Notes))*.

Alternatively you can also install it via [Command Line](#Command-Line) *(see below)*.
If using proton-wine for `VORTEXWINE` (which is default if it is not configured) the `WINEPREFIX` user is "steamuser" *(as always with proton wine)*.
When you switch to a wine version which doesn't patch the username to "steamuser" your user-settings are empty of course *(not recommended)*
**stl** will not symlink in between those two users!

**Currently it [is recommended](#Additional-Vortex-Notes) to use an older wine/proton version with Vortex.**
**When the default wine for Vortex is unconfigured stl tries to autodetect an old Proton4 wine and use that (when found)**

**Functionality**:
Some settings are preconfigured, to make this working without any user configuration, but of course all of the settings can be as well configured if you want.

##### Vortex Configuration

**stl** uses an extra vortex directory inside `STLCFGDIR` defined under `STLVORTEXDIR`
Vortex is one of the **stl** Categories so it has an own Vortex Menu available in the [Category Menu](#Category-Menu)
Most available options are stored in the [Global Config](#Global-Config)

##### Vortex Stages

Vortex uses 2 main [Deployment_Methods](https://wiki.nexusmods.com/index.php/Deployment_Methods) to enable Mods for the managed games.
"Hardlink Deployment" and "Symlink Deployment". Symlink Deployment doesn't work under wine, so Hardlink is required (and automatically set for every game from **stl**, although it is default anyway)
Those "Hardlinks" only work if the "Staging directory" is on the same partition as the game (yes the same physical partition, not the same "windows drive in wine).
As Steam Library directories can be on multiple partitions a "Staging directory" is required for every one of them.

###### Automated (zeroconf) `VORTEXSTAGELIST` configuration
When you start a game **stl** will parse on which mount point it actually lies.
Then it tests if it can create/write a "Vortex" directory in the root directory of the partition.
If it fails to create a directory in the previous step, it tests next if it can create/write a "Vortex" directory
directly in the "Steam Library" directory of the started game besides the "steamapps" directory.

The first succeeding directory will be added automatically to the `VORTEXSTAGELIST` list
and will be used from now on as "Staging directory" automatically for all games lying on the same partition.
So after you have started one "Vortex" game from each of your "Steam Library" partitions the `VORTEXSTAGELIST` variable is ready for all of your games.
The only exception is the partition where your steam is installed ("/" or "/home" if you have an extra /home/partition).
Here the default "Vortex Staging directory" is `STLVORTEXDIR/staging` instead.

Other additional paths can be added easily, just make suggestions.
If you don't want that automation just set `DISABLE_AUTOSTAGES` to 1 and set them manually instead:

##### Script Extender
Several games *(Skyrim, Fallout flavours)* have many mods which depends on a special "Script Extender" program ("SE").
Unfortunately those "SE" programs don't [work with default proton since some time](https://github.com/ValveSoftware/Proton/issues/170).
When **stl** detects one of those "SE exe" files in the game dir, a requester will pop up with following options:
- start the regular game exe
- start the regular game exe and save the decision (so don't ask again)
- start the found "SE exe"
- start the found "SE exe" and save the decision (so don't ask again)

When choosing "SE exe" make sure the [selected Proton Version](#Proton-Selection) is can actually run the exe!

*(The "don't ask again" option `SELAUNCH` can't be set in the [Settings Menu](#Settings-Menu)
and must be removed manually from the [Game Config](#Game-Config) -f.e. via [Editor Dialog](#Editor-Dialog)*

##### Additional Vortex Notes

- On the first start Vortex warns that it is started with admin privileges. Very likely wine related, just click it away, it won't pop up again
- I tested ~25 games and they worked ootb, feel free to open an issue for a not *(automatically)* working game if you think this is a **stl** bug. *(Nehrim doesn't seem to work (yet))*
- It was pretty much work to get this into the current state, but although I tested a lot there still might be glitches and problems.
  Also Vortex can stop working under linux/wine anytime after an update *(as it already did before)*.
  Don't complain and rant when it doesn't work as expected *(anymore)* *(as it happened already before with other Vortex-linux solutions)*,
  but try to help fixing the issue instead then *(no offense, but imho linux already had better times regarding this!)* **!**
- Vortex depends on dotnet48. See [Winetricks](#Winetricks) for initial installation & check your winetricks.log
  *(Vortex installs and works fine with wine from Proton 4.11)*

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
- start the game (game settings required to enable sbs are not automatically enabled! added a tweakcmd for **Crysis 2** though )
- start [vr-video-player](https://git.dec05eba.com/vr-video-player)
- when exiting the game, vr-video-player wil be closed as well.

There are also two quickstart options to choose from to directly start regular games in SBS mode without any further configuration
by auto-enabling side-by-side with the shader [Depth3D](#Depth3D):

 - `SBSVRVK`: set to 1 as shortcut to enable all required flags for SBSVR with [vkBasalt](#vkBasalt)
 - `SBSVRRS`: set to 1 as shortcut to enable all required flags for SBSVR with [ReShade](#Reshade)

Where Reshade has more features and vkBasalt is probably more stable, because it works natively.

Before Starting SteamVR **stl** checks if a HMD is present *(using lsusb)*.
If none was found the SBS VR mode is cancelled and if `SBSVRRS` was supposed to start ReShade is disabled as well.
The game starts regularly in pancake mode subsequently.

**stl** goes through several functions to automatically find the current window id
*(and for later use also the game window name, to make starting SBS VR for the game faster)*
This works mostly very good, but some games start own launchers before the actual game.
Then autodetecting the correct window is almost impossible, and the window name has to be set manually as `GAMEWINDOW`.
If autodetecting failed for whatever reason, it is still possible to pick the game window name again, by using the [Tray Icon](#Tray-Icon)

The vr-video-player author was so kind to accept a little patch, to work better with **stl**.
It is possible to live zoom in and out and the zoom state is written into a temporary file, which **stl** picks up.
The value is stored in the internal [SBS Tweak](#SBS-Tweaks) config (also when changed) and read from there from now on.

To make switching between game- and vr-video-player window easier (with hmd) there is also the option [Toggle Open Windows](#Toggle-Open-Windows)
So switching between the windows is easily possible with *Alt+Tab*.
It is also enabled by default in the **VR** [Steam Categories](#Steam-Categories) *(ReShadeVR,SBS-VR,vkVR.conf)*

![Cyberpunk 2077 VR category German](https://github.com/frostworx/repo-assets/blob/master/pics/stl-vr-gui.jpg)


#### GameMode
[gamemode](https://github.com/FeralInteractive/gamemode)
*(in [Game Menu](#Game-Menu) and [Game Config](#Game-Config))*
`USEGAMEMODERUN`: set to 1 to start game with gamemoderun

#### Notifier
Set `NOTY` to your notifier to draw some start/stop **stl** messages

#### MangoHud
[MangoHud](https://github.com/flightlessmango/MangoHud)
*(in [Game Menu](#Game-Menu) and [Game Config](#Game-Config))*
Set `MANGOHUD` to 1 to enable mangohud *(does nothing in stl itself, but just exports the upstream variable)*

#### Nyrna
[Nyrna](https://github.com/Merrit/nyrna)
*(in [Game Menu](#Game-Menu) and [Game Config](#Game-Config))*
Set `RUN_NYRNA` to 1 to enable nyrna while game is running 

#### ReplaySorcery
[ReplaySorcery](https://github.com/matanui159/ReplaySorcery)
*(in [Game Menu](#Game-Menu) and [Game Config](#Game-Config))*
Set `RUN_REPLAY` to 1 to enable replay-sorcery while game is running 

#### GameConqueror
[GameConqueror](https://github.com/scanmem/scanmem)
*(in [Game Menu](#Game-Menu) and [Game Config](#Game-Config))*

Set `RUN_GAMCON` to 1 to automatically start GameConqueror when the game starts.
The game exe will be loaded into GC automatically,
but also can be overridden with `GAMCONWAITEXE` *(f.e. for games starting a launcher)*.
When the game exits GameConqueror will be closed automatically as well.

As the gameconqueror startscript uses pkexec and asks for more permissions, the default
executable is set to `GAMCON=/usr/share/gameconqueror/GameConqueror.py` in the global config.
Enabling GameConqueror is also possible by simply adding the game to the "Cheat" [[Steam Category](#Steam-Categories).

Some games *(afaik mostly multiplayer)* are not cheat-safe and could lead to a ban, so **be careful with cheating**!

#### Cheat Engine
[CheatEngine](https://github.com/cheat-engine/cheat-engine)
*(in [Game Menu](#Game-Menu) and [Game Config](#Game-Config))*
Set `RUN_CHEATENGINE` to 1 to automatically start CheatEngine when the game starts.
When the game exits CheatEngine will be closed automatically as well.

When the CheatEngine installation can't be found, it will be installed automatically,
using innoextract if available or with wine as fallback.
For the latter an own temporary `WINEPREFIX` is created and removed after succesful extraction of the CheatEngine directory.
In both cases the productive directory is inside the `STLCEDIR` and is used from there without any active installation into the corresponding game `WINEPREFIX`.

If the CheatEngine Installer Setup can't be found, it will be downloaded automatically.
The CheatEngine Version `CHEATENGINEVERSION` can be found in the [global.conf](#Global-Config).

Enabling CheatEngine is also possible by simply adding the game to the "CheatEngine" [Steam Category](#Steam-Categories).

Some games *(afaik mostly multiplayer)* are not cheat-safe and could lead to a ban, so **be careful with cheating**!

#### GameScope
[GameScope](https://github.com/Plagman/gamescope)
*(in [Game Menu](#Game-Menu) and [Game Config](#Game-Config))*
Set `USEGAMESCOPE` to 1 to automatically start GameScope when the game starts, either per game or globally.
The commandline arguments used *(`GAMESCOPE_ARGS`)* can be configured both per game and globally as well.

#### Toggle Open Windows
*(in [Global Menu](#Global-Menu) and [Global Config](#Global-Config))*
minimize all open windows on game start and maximize them when game exited using xprop
- `TOGGLEWINDOWS`: toggle visibility of all open windows on start/stop

#### Strace
*(in [Game Menu](#Game-Menu) and [Game Config](#Game-Config))*
If `STRACERUN` is set to 1 **stl** will write a strace log of the launched game
strace is launched with the commandline arguments found in `STRACEOPTS`.

When `STRACERUN` is enabled make sure
`/proc/sys/kernel/yama/ptrace_scope` is set to 0.
else your user will get access denied when trying to attach a process.
Either 
`echo 0 > /proc/sys/kernel/yama/ptrace_scope`
as root or enable it persistent in sysctl.

#### Network Monitoring
*(in [Game Menu](#Game-Menu) and [Game Config](#Game-Config))*
Basic Network Traffic Monitor
- `NETMON`: program to record game network-traffic with arguments `NETOPTS` - used when enabled

If `NETMON` is set the basic network traffic of the selected game is monitored and written into `NETMONDIR`.
duplicate lines are unique sorted at the end.

#### ReShade
[ReShade](https://reshade.me)
*(in [Game Menu](#Game-Menu) and [Game Config](#Game-Config))*
Set `INSTALL_RESHADE` to 1 to automatically install reshade into the selected game dir.
Set `USERESHADE` to 1 to start game with ReShade enabled

If `DOWNLOAD_RESHADE` is set to 1 all required files for ReShade are [downloaded](#Downloads) once into `RESHADESRCDIR`
of course you can install all files manually as well. make sure to rename all files correctly:

**64bit** `d3dcompiler_47.dll`: -> d3dcompiler_47_64.dll
**32bit** `d3dcompiler_47.dll`: -> d3dcompiler_47_32.dll
`ReShade64.dll`, `ReShade32.dll`: renaming not required as they will be placed in the gamedir under the required name

The required architecture is autodetected from the game.exe and the matching files are copied from `RESHADESRCDIR` into the selected game dir
both downloadfiles and basic configuration were taken from [r/linux_gaming](https://www.reddit.com/r/linux_gaming/comments/b2hi3g/reshade_working_in_wine_43) 

If `USERESHADE` is disabled and the corresponding game is started, the previously installed ReShade dll will be renamed, so ReShade is disabled when the game starts.
When `USERESHADE` is re-enabled the renamed dll will be re-activated.

##### ReShade-Presets
Available ReShade Presets can be selected via Dropdown Menu in the [Settings Menu](#Settings-Menu) per game,
to automatically create a default ReShade configuration on the first launch.

The bundled minimal SuperDepth3D_VR ReShade Preset is automatically used when [SBSVRRS](#Side-by-Side-VR) *(f.e. via [Steam Category](#Steam-Categories))* is enabled

##### ReShade-Auto-Update
With `RESHADEUPDATE` being enabled *(per game)* in the [Settings Menu](#Settings-Menu)
- new ReShade Setups are downloaded/extracted automatically *(every Setup is also stored versioned from now on)*
- ReShade dlls are automatically updated in every game directory
  
#### vkBasalt
[vkBasalt](https://github.com/DadSchoorse/vkBasalt)
- `ENABLE_VKBASALT`: set `ENABLE_VKBASALT` to 1 to start the game with vkbasalt *(does nothing in stl itself, but just exports the upstream variable)*
- `VKBASALT_CONFIG_FILE`: the vkbasalt source config file - it points per default to `STLCFGDIR/vkBasalt.conf` and is autogenerated if not found
The autogenerated `VKBASALT_CONFIG_FILE` points to the files from `RESHADE_DEPTH3D` so it should have been at least checked out once with `CLONE_DEPTH3D`

#### Depth3D
[Depth3D](https://github.com/BlueSkyDefender/Depth3D)
Mostly useful in combination with [SBS-VR](#Side-by-Side-VR).
Set `RESHADE_DEPTH3D` to 1 to install ReShade Depth3D Shader into gamedir
If `CLONE_DEPTH3D` is set to 1 the git repository will be automatically cloned/pulled (only when `RESHADE_DEPTH3D=1`) to `DEPTH3DSRCDIR` in [Downloads](#Downloads)

With `RESHADE_DEPTH3D` enabled `Overwatch.fxh`, `SuperDepth3D.fx`, `SuperDepth3D_VR.fx` from Depth3D are copied to the gamedir.
When the game started just create a initial profile by selecting the autodetected `SuperDepth3D_VR.fx`
The Depth3D Shader is automatically deactivated if HMD wasn't detected or VR mode was stopped otherwise and re-enabled on success.

Also see [Shader Management](#Shader-Management)

#### Shader-Management
**stl** has a built in shader management with following features:
- Downloader/Updater of several Shader repositories *(if important/good repos are missing feel free to open an issue)*
- Shader Selection Menu
  - all available Shaders are automatically listed
  - all Shaders already installed in the current game directory are checked
  - all checked Shaders will be installed into the current game directory
  - all unchecked Shaders will be removed from the current game directory
  - The Shader Selection Menu can be started
    - via [Command Line](#Command-Line) _(with any directory as destination path)_
    - directly from the [Extra Buttons Menu](#Extra-Buttons)
    - automatically before game start
    - via [Tray-Icon](https://github.com/frostworx/steamtinkerlaunch#Tray-Icon) _(so Shaders could be installed while the game is already running)_
- for games with launchers not being in the same path as the actual game exe the destination path can be overridden _(used for both Shaders and [ReShade](#ReShade))_
- added ShaderMenu Steam Category which installs [ReShade](#ReShade) into the game directory and opens the Shader Selection Menu
- additional files required by installed Shaders (f.e. textures) are automatically installed as well into the game directory

![shader dialog](https://github.com/frostworx/repo-assets/blob/master/pics/shader-dialog.jpg)

#### Editor
Config files can optionally be opened with the texteditor `STLEDITOR` if desired, either by accepting a requester *(for editing Tweakfiles)* or by opening
Configfiles within the [Editor Dialog](#Editor-Dialog) started directly or as submenu of the [Settings Menu](#Settings-Menu).

If xdg-open is configured as `STLEDITOR` or if the configured editor is not found, **stl** tries to autoconfigure an installed texteditor.
*(first trying to find it through 'xdg-mime query', then check binary availability in this order: geany, gedit, leafpad, kwrite)*

Set `OPENEDITORURL` to 1 to additionally open the `EDITORURL` url for the game in your `BROWSER` when starting the editor from the [Editor Dialog](#Editor-Dialog).
*(by default the url `$OPENEDITORURL/$SteamAppID` is opened, if this doesn't work with the url you want to open just open an issue)*
If `EDITORURL` contains "AID" it will be replaced by the current SteamAppID.


#### ENV Variables
Literally every env variable can be set for example in [Game Config](#Game-Config) or [Global Config](#Global-Config),
making it pretty easy to tinker with important ones *(f.e `PROTON`* , `DXVK`* , `MANGOHUD`, `RADV_PERFTEST`, `WINE`...)*
The Possibilities Are Endless...

#### Pressure Vessel
Pressure Vessel is *(currently)* only active when not using a [Steam Compatibility Tool](#Steam-Compatibility-Tool).
So if you want to use any of the variables via **stl**, it must be set as [Launch Option](#Launch-Option) and not as [Steam Compatibility Tool](#Steam-Compatibility-Tool).

All Pressure Vessel *(PV)* options are in a separate PressureVessel category and therefore available in the [Category Menu](#Category-Menu).
*(Currently)* Only one of the available options can be used *(until there are enough to know which can be combined)* in order of below appearance *(first wins)*

- `PRESSURE_VESSEL_VERBOSE`
  With `STL_PV_VERBOSE` enabled, the PV variable `PRESSURE_VESSEL_VERBOSE` enabled and the output is written to `"$STLPVLOGDIR/pressure-vessel-${AID}.log"`

- `PRESSURE_VESSEL_SHELL`
  With `STL_PV_SHELL` enabled, the PV variable `PRESSURE_VESSEL_SHELL` is set to `STL_PV_SHELL`
  can be
  - none  *(disabled - `PRESSURE_VESSEL_SHELL` won't be even set)*
  - after *(shell starts after the game)*
  - fail  *(shell starts only after the game crashed)*
  - instead *(shell starts and game start is skipped)*

- `PRESSURE_VESSEL_TERMINAL`
  With `STL_PV_TERMINAL` enabled, the PV variable `PRESSURE_VESSEL_TERMINAL` is set to `STL_PV_TERMINAL`

#### Wine Support
With enabling `USEWINE` *(either directly in the [Game Config](#Game-Config) or by adding the game to the `Wine` [Steam Category](#Steam-Categories))*
a Windows game is started with pure Wine instead of a Proton version.
Both the currently used Wine Version and the Wine version which should be used as default can be comfortably chosen with drop down menus in the [Game Config](#Game-Config),
where the dropdown menus list all wine directories found in the "Wine extract directory" `WINEEXTDIR`.

As source wine archives from [Lutris](#Lutris) are used, additional sources could be easily added later.
Instead of using an own **stl** default wine version, it is also possible to simply use the default wine version from Lutris,
either as "default, when no game specific wine verion has been set" or generally as default wine version for all games.

When no Wine version for the current game was set or could be determined with above settings, a requester opens automatically where
either an available Wine Version can be picked or the [Wine Download Requester](#Wine-Download) can be opened.

The selected Wine version will not only be used for the game itself, but also for all other wine-related programs like
[winetricks](#Winetricks), [winecfg](#Winecfg), [custom Programs](#Custom-Program) and so on.


##### Wine Download
It is possible to automatically download and extract a Wine Archive with the Wine Download Requester,
where an Archive can easily picked from an autogenerated Drop-Down Menu.
The selected archive will be downloaded to `WINEDLDIR` and extracted to the productive directory `WINEEXTDIR`.

The Requester can either be opened via the [Extra Buttons Menu](#Extra-Buttons), automatically when no Wine version could be determined using the [Wine Support](#Wine-Support)
or via [Command Line](#Command-Line): `stl dlwine|dw <url>` *(accepting direct download URL as optional argument)*.

#### Backup Support
With enabling `BACKUPSTEAMUSER` *(either directly in the [Game Config](#Game-Config) or by adding the game to the `Backup` [Steam Category](#Steam-Categories))*
all directories with files from the `steamuser` inside the Proton pfx will be backed *(using `rsync`)* when closing the game.
The destination directory is `STLCFGDIR/backup/steamuser/id/$AID`. 
A `STLCFGDIR/backup/steamuser/title/$GAMETITLE` symlink pointing to it will be created as well.
Files and directories can be excluded from the backup, by either adding them into the per game
`STLCFGDIR/backup/exclude/exclude-$AID.txt`
or into the globally parsed 
`STLCFGDIR/backup/exclude/exclude-global.txt`
exclude file.
For easier editing both files are also available via the [Editor Dialog](#Editor-Dialog).

#### Metadata Support
To improve and speedup existing and further automations and functions **stl** collects as many useful metadata as possible.

The base storage directory for all metadata is `STLCFGDIR/meta` with subdirectories 
- id
  - custom
  - general
- title
  - custom
  - general

All metadata files are created/updated in the id subdirectories and symlinks with the game titles are created in the corresponding title subdirectory.
*(might make sense to use a sqlite3 db here, but having a transparent easily simple filestructure also has its benefits)*

Metadata are separated into `custom` and `general` to make sharing of `general` metadata in the community possible.

##### Custom Metadata
Currently `custom` metadata are only the `WINEPREFIX` and the `GAMEDIR` of the game.

##### General Metadata
The very basic `general` metadata currently stored are `GAMEID` and `GAMENAME`, depending on the detection function `GAMEEXE` will be stored as well.
The `GAMEWINDOWNAME` will be one of the next useful data to be added.

##### Storing Metadata
When metadata is created via [Command Line](#Command-Line) *(either directly using the `meta` or indirectly the `menu` command line argument)*
only the `GAMEID`, `GAMENAME`, `WINEPREFIX` and the `GAMEDIR` are created/updated,
as `GAMEEXE`, `GAMEWINDOWNAME` and probably any other value are simply not available outside steam.
When launching a game via steam using **stl** *(here it doesn't matter if the game is actually started, or the user exists the launch via stl)*
the additional values are stored as well when entering the `closeSTL` function *(so usually after the game has exited)*

##### Backup using commandline:
see [Command Line](#Command-Line)

## Game Launch Speed
**stl** has pretty much to check, but when everything is configured, several option-checks can be disabled (per game)
to speed up the actual game start process.
Here are some examples which improve the start notably *(all settings can be configured in the [Settings Menu](#Settings-Menu))*
- set `WAITEDITOR` to `0` [Wait requester](#Wait-Requester)
- set `CHECKCATEGORIES` to `0` if the Game has no [Steam Category](#Steam-Categories) Tweak anyway
- set `SAVESETSIZE` to `0` when all windows have their optimal [size](#Gui-Window-Size)
- *(IMHO)* games start much faster when **stl** is configured as [Steam Compatibility Tool](#Steam-Compatibility-Tool) instead of [Launch Option](#Launch-Option).
  The reason is probably simply that the Steam Linux Runtime isn't loaded when using a [Steam Compatibility Tool](#Steam-Compatibility-Tool).

## Command Line
**stl** also has several command line options which are useful outside steam.
For available options please check `stl help
