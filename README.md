# Steam Tinker Launch
[![GitHub stars](https://img.shields.io/github/stars/frostworx/steamtinkerlaunch.svg?style=flat-square)](https://github.com/frostworx/steamtinkerlaunch/stargazers)
[![GitHub contributors](https://img.shields.io/github/contributors/frostworx/steamtinkerlaunch.svg?style=flat-square)](https://github.com/frostworx/steamtinkerlaunch/graphs/contributors)
[![GitHub issues](https://img.shields.io/github/issues/frostworx/steamtinkerlaunch.svg?style=flat-square)](https://github.com/frostworx/steamtinkerlaunch/issues)
[![GitHub license](https://img.shields.io/github/license/frostworx/steamtinkerlaunch.svg?style=flat-square)](https://github.com/frostworx/steamtinkerlaunch/blob/dev/LICENSE)
[![reddit](https://img.shields.io/reddit/subreddit-subscribers/SteamTinkerLaunch?style=flat-square&label=Reddit)](https://www.reddit.com/r/SteamTinkerLaunch)

# Summary

<img align="left" width="64" height="64" src="https://github.com/frostworx/repo-assets/blob/master/pics/steamtinkerlaunch-logo_64px.png" alt="**SteamTinkerLaunch** is a Linux wrapper tool for use with the Steam client">

**Steam Tinker Launch** is a Linux wrapper tool for use with the Steam client
which allows customizing and start tools and options for games quickly on the fly *(see [Features](#Features))*

By using a versatile configuration structure it is both easy to set up and flexible.

## How to use

### General usage
**steamtinkerlaunch works with Linux native games and with games using Proton!**
*(Some features (f.e. [ReShade](https://github.com/frostworx/steamtinkerlaunch/wiki/ReShade)) are only available for games using Proton)*
*(Non-Steam games added to Steam are supported as well)*

There are two ways to use **steamtinkerlaunch** with Steam.
Either as [Steam Launch Option](https://github.com/frostworx/steamtinkerlaunch/wiki/Steam-Launch-Option) or as [Steam Compatibility Tool](https://github.com/frostworx/steamtinkerlaunch/wiki/Steam-Compatibility-Tool)
*(simply enabling it as global default [Steam Compatibility Tool](https://github.com/frostworx/steamtinkerlaunch/wiki/Steam-Compatibility-Tool) works fine as well)*

**I recommend the [Steam Compatibility Tool](https://github.com/frostworx/steamtinkerlaunch/wiki/Steam-Compatibility-Tool) for all Proton games and
the [Steam Launch Option](https://github.com/frostworx/steamtinkerlaunch/wiki/Steam-Launch-Option) only for native Linux games.**

*(of course you're using this tool at your own risk and you're responsible which 3rd party programs you launch with it)*

### Game specific use
When starting a game a small [Wait requester](#Wait-Requester) will pop up.
If within a short waiting period *(default 2 seconds)* the spacebar is pressed the [Main Menu](https://github.com/frostworx/steamtinkerlaunch/wiki/Main-Menu) will open where everything can be configured comfortably.
When done with configuring (or when the requester timeouts) the game will be started regularly with all tools and options configured.

## Installation
### Installation via Package Management
**Thanks to all package maintainers!** 👍

**Arch Linux** [via AUR](https://aur.archlinux.org/packages/steamtinkerlaunch) *(f.e. using yay)*:
`yay -S steamtinkerlaunch`

**Solus** has an official package:
`sudo eopkg install steamtinkerlaunch`

Fedora: **[unoffical package](https://copr.fedorainfracloud.org/coprs/capucho/steamtinkerlaunch/)**

Ansible: **[playbook](https://github.com/tofu114/ansible_playbooks)**

[![Packaging status](https://repology.org/badge/vertical-allrepos/steamtinkerlaunch.svg)](https://repology.org/project/steamtinkerlaunch/versions)

### Manual Installation:
If **steamtinkerlaunch** is not in your package management yet, just `sudo make install`

**steamtinkerlaunch** depends on several other programs which need to be installed as well.
Check the [Installation wiki](https://github.com/frostworx/steamtinkerlaunch/wiki/Installation)

## Press
Several great people already mentioned **steamtinkerlaunch** on their platforms/channels.

**Thanks a lot to you all!** 👍

*(no specific order, list might be incomplete)*

- **podiki** *(who also contributed to **stl**)* wrote a huge [Boiling Steam article](https://boilingsteam.com/supercharge-steam-with-steamtinkerlaunch-stl)
- **ekianjo** made a [Q&A](https://boilingsteam.com/steam-tinker-launcher-making-tinkering-much-easier)
- **Hex DSL** made a [youtube video](https://www.youtube.com/watch?v=rdXQRMwMfPE)
- **tuxfoo**  made a [youtube video](https://www.youtube.com/watch?v=l1KjIANTIKs)
- **Linux Game Cast** already mentioned **stl** in their [casts](https://www.youtube.com/watch?v=djuZdnE83fE&t=436s) [several](https://www.youtube.com/watch?v=yVsTMhx8E7c&t=983s) [times](https://www.youtube.com/watch?v=qhybhTGV3mA&t=1279s)
  and still [counting](https://linuxgamecast.com/2021/11/linux-game-cast-484-yami-pedro)

## Quick start
When **steamtinkerlaunch** is started for the first time it will create its default [configuration](#Configuration) structure.
Almost everything can be configured with the built-in [Main Menu](https://github.com/frostworx/steamtinkerlaunch/wiki/Main-Menu), but optionally also with a graphical text editor.
It might be a good idea to start with configuring everything in the [Main Menu](https://github.com/frostworx/steamtinkerlaunch/wiki/Main-Menu) to your needs

**If you want to get an overview over the Steam Tinker Launch features, but the huge [wiki](https://github.com/frostworx/steamtinkerlaunch/wiki) is too overwhelming,
you might want to check the [articles and videos](#Press) of many cool people!**


## Features
- [Feature list](https://github.com/frostworx/steamtinkerlaunch/wiki#features)
- [Changes in the latest release](https://github.com/frostworx/steamtinkerlaunch/releases/latest)
- [Changelog](https://github.com/frostworx/steamtinkerlaunch/wiki/Changelog)


## Requirements
See [Installation](https://github.com/frostworx/steamtinkerlaunch/wiki/Installation)
 
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
Besides some other (possibly relevant) log files, the log file of the last run can also be found here:
`/dev/shm/steamtinkerlaunch/steamtinkerlaunch.log`

## Command Line
**steamtinkerlaunch** also has several [command line](https://github.com/frostworx/steamtinkerlaunch/wiki/Command-Line) which can also be useful outside steam.
For available options please check `steamtinkerlaunch help`
