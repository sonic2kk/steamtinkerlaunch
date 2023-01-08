# Steam Tinker Launch
[![GitHub version](https://img.shields.io/github/v/tag/sonic2kk/steamtinkerlaunch?label=version&style=flat-square)](https://github.com/sonic2kk/steamtinkerlaunch/releases/latest)
[![GitHub stars](https://img.shields.io/github/stars/sonic2kk/steamtinkerlaunch.svg?style=flat-square)](https://github.com/sonic2kk/steamtinkerlaunch/stargazers)
![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/sonic2kk/steamtinkerlaunch?style=flat-square)
[![GitHub contributors](https://img.shields.io/github/contributors/sonic2kk/steamtinkerlaunch.svg?style=flat-square)](https://github.com/sonic2kk/steamtinkerlaunch/graphs/contributors)
[![aur votes](https://img.shields.io/aur/votes/steamtinkerlaunch?label=aur%20votes&style=flat-square)](https://aur.archlinux.org/packages/steamtinkerlaunch)
[![GitHub issues](https://img.shields.io/github/issues/sonic2kk/steamtinkerlaunch.svg?style=flat-square)](https://github.com/sonic2kk/steamtinkerlaunch/issues)
[![GitHub license](https://img.shields.io/github/license/sonic2kk/steamtinkerlaunch.svg?style=flat-square)](https://github.com/sonic2kk/steamtinkerlaunch/blob/dev/LICENSE)

## What is SteamTinkerLaunch?

<img align="left" width="64" height="64" src="https://github.com/frostworx/repo-assets/blob/master/pics/steamtinkerlaunch-logo_64px.png" alt="**SteamTinkerLaunch** is a Linux wrapper tool for use with the Steam client">

**Steam Tinker Launch** is a versatile Linux wrapper tool for use with the Steam client which allows for easy graphical configuration of game tools, such as [GameScope](https://github.com/sonic2kk/steamtinkerlaunch/wiki/GameScope), [MangoHud](https://github.com/sonic2kk/steamtinkerlaunch/wiki/MangoHud), [modding tools](https://github.com/sonic2kk/steamtinkerlaunch/wiki/Modding) and a bunch more. It supports both games using Proton and native Linux games, and works on both X11 and Wayland.
 
As described by _/u/TaylorRoyal23_ on [r/linux_gaming](https://www.reddit.com/r/linux_gaming/comments/ud58i2/comment/i6i3yf9/?utm_source=share&utm_medium=web2x&context=3):

> _"An incredible wrapper with a menu that lets you easily toggle and modify various settings for games on Linux.
Anything from proton versions, to startup and exit scripts, proton/dxvk/etc. settings, FSR, reshade,
and even options for various tools like gamemode, replay-sorcery, gamescope, etc. Tons more too.
I just set my default proton version to "steam tinker launcher" and then every game launches
with a 2 second menu that allows you to easily change any of the settings.
If you don't press any buttons it just goes with the defaults and launches the game.
The menus can get a little confusing but it consolidates it all in one place and is way more simple
than trying to remember dozens of commands for various settings that one might need."_

![image](https://user-images.githubusercontent.com/7917345/209706023-40eefb0d-b115-48a5-aa6f-c6509863811b.png)

## What Does It Do?
SteamTinkerLaunch offers a huge variety of features, too many to list in this Readme. Please see the [Features List](https://github.com/sonic2kk/steamtinkerlaunch/wiki#features) and their associated wiki pages for a full breakdown. However, here are some of the key features offered by SteamTinkerLaunch. Note that some of these features may not work with Flatpak Steam!

| Feature | Description |
| ------- | ----------- |
| Custom Per-Game Environment Variables | Set custom environment variables on a per-game basis. Useful for adding command-line tweaks for various games. |
| Custom Game Executable | Change the executable that Steam launches. Useful for custom game launchers/mod launchers.<br /><br />This option is extremely flexible, allowing for launching a custom executable with a game, instead of the game, before the game or after the game. See the [Custom Program wiki page](https://github.com/sonic2kk/steamtinkerlaunch/wiki/Custom-Command) for usage. |
| Easy installation of Winetricks verbs | SteamTinkerLaunch can apply the necessary steps to install, for example, `dotnet48` or later in a Proton prefix, which can fix common issues with GUI tools running through Proton.<br /><br />It is **highly recommended** to install `dotnet48` using a community flavour of Proton such as GE-Proton or Proton 5.0. You will also want to ensure your Winetricks version is up-to-date. |
| [ModOrganizer 2](https://github.com/ModOrganizer2/modorganizer) Support | Installs and sets up mod installation and organization tool ModOrganizer 2. Includes browser and command line integration for handling NXM links with `xdg-open`.<br /><br />See our [ModOrganizer 2 wiki page](https://github.com/sonic2kk/steamtinkerlaunch/wiki/Mod-Organizer-2) and [modding wiki page](https://github.com/sonic2kk/steamtinkerlaunch/wiki/Modding) for more details. |
| [Vortex Mod Manager](https://www.nexusmods.com/about/vortex/) Support | Installs and sets up Nexus Mods' mod management tool Vortex Mod Manager. Includes browser and command line integration for handling NXM links with `xdg-open`.<br /><br />See our [Vortex wiki page](https://github.com/sonic2kk/steamtinkerlaunch/wiki/Vortex) and [modding wiki page](https://github.com/sonic2kk/steamtinkerlaunch/wiki/Modding) for more details. |
| [SpecialK](https://github.com/SpecialKO) Support | Utility for enhancing and fixing common problems with Windows games.<br /><br />See our [SpecialK wiki page](https://github.com/sonic2kk/steamtinkerlaunch/wiki/SpecialK) for usage. May require additional [Optional Dependencies](https://github.com/sonic2kk/steamtinkerlaunch/wiki/Installation#optional-dependencies). |
| [ReShade](https://reshade.me/) Support (Proton/Wine Only) | Supports the use of ReShade shaders to enhance the visual quality of Windows games. Note that ReShade does not support native Linux games.<br /><br />See our [ReShade wiki page](https://github.com/sonic2kk/steamtinkerlaunch/wiki/ReShade) for usage and information on using **ReShade** and **SpecialK** together. |
| [Hedge Mod Manager](https://github.com/thesupersonic16/HedgeModManager) support | Supports automatic installation of the Open-Source Modern Sonic game mod manager as well as attempting to install workarounds for various games that require it.<br/><br/>Due to the nature of this tweaks relying on Winetricks some manual intervention may be required in some instances. Please see the [SteamTinkerLaunch Hedge Mod Manager wiki page](https://github.com/sonic2kk/steamtinkerlaunch/wiki/Hedge-Mod-Manager) for details. |
| Custom Wine/Proton Download | Manages downloading custom Proton and Wine releases, such as GloriousEggroll's popular Proton flavour [GEProton](https://github.com/GloriousEggroll/proton-ge-custom). These versions are installed and managed by SteamTinkerLaunch. (**Requires `jq` to be installed!**)<br /><br />See our wiki pages on [Custom Proton Versions](https://github.com/sonic2kk/steamtinkerlaunch/wiki/Download-Custom-Proton) and [Custom Wine Versions](https://github.com/sonic2kk/steamtinkerlaunch/wiki/Download-Custom-Wine) for more details. |

To find out about the latest release, check out the [stable release changelog](https://github.com/sonic2kk/steamtinkerlaunch/releases/latest). To find out about the latest bleeding-edge development changes not yet in a stable build, check out the [full changelog](https://github.com/sonic2kk/steamtinkerlaunch/wiki/Changelog).

## How Do I Use It?
### General usage
Steam Tinker Launch works with Linux native games and games using Proton, however some Windows-only utilities (such as [ReShade](https://github.com/sonic2kk/steamtinkerlaunch/wiki/ReShade)) are only available for Proton games. SteamTinkerLaunch also supports Non-Steam Games so long as they are launched through the Steam client.

There are two ways to use SteamTinkerLaunch through Steam, either as a Compatibility Tool (intended for Proton games) or as a Launch Option (intended for native Linux games). Only **one** of these options should be used per game.

#### Steam Compatibility Tool (**Proton Games**)
Using SteamTinkerLaunch as a [compatibility tool](https://github.com/sonic2kk/steamtinkerlaunch/wiki/Steam-Compatibility-Tool) is the intended way of using it with Proton games. Once SteamTinkerLaunch is installed, force it as a compatibility tool for your chosen game from the list of compatibility tools. You can also set SteamTinkerLaunch as the default compatibility tool for all applications from the Steam Play settings of the Steam client. Keep in mind that if you force SteamTinkerLaunch as a compatibility tool, Steam will always download the Windows release of the game.

#### Steam Launch Option (**Native Linux Games**)
Using SteamTinkerLaunch as a [Launch Option](https://github.com/sonic2kk/steamtinkerlaunch/wiki/Steam-Launch-Option) is the intended way of using it with native Linux games. You can enable SteamTinkerLaunch as a launch option

```sh
steamtinkerlaunch %command%
```

On some platforms such as [Steam Deck](https://github.com/sonic2kk/steamtinkerlaunch/wiki/Steam-Deck), using SteamTinkerLaunch as a launch option may require you to add it to your path. Refer to your distributions documentation on how to add the script to your path, as this can vary between distributions and shells. If you installed SteamTinkerLaunch via [ProtonUp-Qt](https://github.com/sonic2kk/steamtinkerlaunch/wiki/ProtonUp-Qt) it will added to your path for you, though you may still have to set the path to `$HOME/stl/prefix/steamtinkerlaunch` as described on the [Launch Option wiki page](https://github.com/sonic2kk/steamtinkerlaunch/wiki/Steam-Launch-Option).

It is possible to use SteamTinkerLaunch as a launch option for Proton games, but this is **not** the intended use-case.

### Game-Specific Use
When starting a game, a small [Wait Requester](#Wait-Requester) dialog will pop up. This will allow you to access the Main Menu either by pressing the button or pressing the spacebar, or skip to launching the game. By default, the dialog will only stay for two seconds before it times out and launches the game, but this can be configured in the SteamTinkerLaunch settings.

![Wait Requester](https://github.com/frostworx/repo-assets/blob/master/pics/Wait-Requester.jpg)

The Main Menu is the springboard to tinkering with your game options. See the [wiki page](https://github.com/sonic2kk/steamtinkerlaunch/wiki/Main-Menu) for more information on the options it provides. 

### Command Line
SteamTinkerLaunch has several [command line options](https://github.com/sonic2kk/steamtinkerlaunch/wiki/Command-Line) which can be useful outside Steam, such as for installing modding tools. You can run `steamtinkerlaunch help` for a full list of available commands, or if SteamTinkerLaunch is not in your path you can run `sh steamtinkerlaunch help` from the folder where you downloaded SteamTinkerLaunch. 

## How Do I Install It?
SteamTinkerLaunch can be installed in a few different ways depending on your platform and needs. Please refer to the [Installation wiki page](https://github.com/sonic2kk/steamtinkerlaunch/wiki/Installation) for detailed installation instructions.

| Platform | Notes |
| -------- | ----- |
| Package Manager | Preferred installation method. See distribution package status below, though this list may not be exhaustive.<br />Many thanks to all package maintainers!<br /><br />[![Packaging status](https://repology.org/badge/vertical-allrepos/steamtinkerlaunch.svg)](https://repology.org/project/steamtinkerlaunch/versions)<br /><br />Refer to the [Installation Wiki](https://github.com/sonic2kk/steamtinkerlaunch/wiki/Installation#package-manager) for more information on available packages. |
| [ProtonUp-Qt](https://github.com/sonic2kk/steamtinkerlaunch/wiki/ProtonUp-Qt) | As of v2.7.3, [ProtonUp-Qt](https://github.com/DavidoTek/ProtonUp-Qt) has support for SteamTinkerLaunch. This should allow you to intall SteamTinkerLaunch regardless which distribution you are using **including Steam Deck**. See the [Installation wiki](https://github.com/sonic2kk/steamtinkerlaunch/wiki/Installation#protonup-qt) and our [ProtonUp-Qt wiki page](https://github.com/sonic2kk/steamtinkerlaunch/wiki/ProtonUp-Qt) for more details.<br /><br />Outside of Steam Deck, ensure you have met the relevant SteamTinkerLaunch [hard dependencies](https://github.com/sonic2kk/steamtinkerlaunch/wiki/Installation#hard-dependencies). |
| Manual Installation | SteamTinkerLaunch supports **system-wide** (root) and **local** (non-root) manual installation. [See Installation Wiki notes](https://github.com/sonic2kk/steamtinkerlaunch/wiki/Installation#manual-installation) for setup and details. |
| [Steam Deck](https://github.com/sonic2kk/steamtinkerlaunch/wiki/Steam-Deck) | See [Installation Wiki](https://github.com/sonic2kk/steamtinkerlaunch/wiki/Installation#steam-deck) for Steam Deck specific installation instructions. |
| [Steam Flatpak](https://github.com/sonic2kk/steamtinkerlaunch/wiki/Steam-Flatpak) | See [Installation Wiki](https://github.com/sonic2kk/steamtinkerlaunch/wiki/Installation#steam-flatpak) for setup instructions on using Steam Flatpak and SteamTinkerLaunch.<br><br>**NOTE:** This is **only** for Flatpak Steam. |
| Other | See [Installation Wiki](https://github.com/sonic2kk/steamtinkerlaunch/wiki/Installation#distro-specific) for any distro-specific installation instructions. |

## Press
Several great people have mentioned SteamTinkerLaunch on their platforms/channels. Many thanks to all who have covered SteamTinkerLaunch!

| Name | Press |
| ---- | ----- |
| **[podiki](https://boilingsteam.com/author/podiki/)** (also a SteamTinkerLaunch contributor) | [Wrote a huge article about SteamTinkerLaunch on BoilingSteam](https://boilingsteam.com/supercharge-steam-with-steamtinkerlaunch-stl)! |
| **[ekianjo](https://boilingsteam.com/author/ekianjo/)** | [Wrote up a Q&A on BoilingSteam](https://boilingsteam.com/steam-tinker-launcher-making-tinkering-much-easier) with SteamTinkerLaunch creator Frostworx! |
| **[Hex DSL](https://www.youtube.com/c/HexDSL)** | Made a [YouTube video](https://www.youtube.com/watch?v=rdXQRMwMfPE) showcasing SteamTinkerLaunch |
| **[tuxfoo](https://www.youtube.com/channel/UCWpoyqSBIXtylRLFgP3PFfg)** | Made a [YouTube video](https://www.youtube.com/watch?v=l1KjIANTIKs) showcasing SteamTinkerLaunch
| **[Linux Game Cast](https://linuxgamecast.com/)** | Mentioned SteamTinkerLaunch on their [casts](https://www.youtube.com/watch?v=djuZdnE83fE&t=436s) [several](https://www.youtube.com/watch?v=yVsTMhx8E7c&t=983s) [times](https://www.youtube.com/watch?v=qhybhTGV3mA&t=1279s), and [counting]((https://linuxgamecast.com/2021/11/linux-game-cast-484-yami-pedro))! |
| **[Mark Dougherty](https://linuxgamingcentral.com/)** | Has written [several](https://linuxgamingcentral.com/posts/news-stl-v10-released/) [articles](https://linuxgamingcentral.com/posts/stl-v11-released/) about SteamTinkerLaunch |
| **[Kevin Wammer](https://overkill.wtf/author/kevin/)** | Wrote [this article](https://overkill.wtf/steam-deck-steam-tinker-launch-stl/) |
| **[Starlogical from HiTechLoLife](https://www.youtube.com/c/HiTechLoLife)** | Created [this video](https://www.youtube.com/watch?v=4FRU2fuvLlw) describing SteamTinkerLaunch |
| **[joker1007](https://joker1007.hatenablog.com)** (Japanese) | Wrote a [huge article](https://joker1007.hatenablog.com/entry/2022/11/28/014825) on SteamTinkerLaunch for Japanese users |

 
## Configuration
When SteamTinkerLaunch is started for the first time, it will create its default [configuration](#Configuration) structure (usually in `~/.config/steamtinkerlaunch`). All [Configuration Files](https://github.com/sonic2kk/steamtinkerlaunch/wiki/Configuration-Files) are self-contained documents and are always growing, and as a result some options may be missing. If you find a configuration option that is not documented, please request it on the [issue tracker](https://github.com/sonic2kk/steamtinkerlaunch/issues). You may even write the documentation yourself and a collaborator can add it.

For a general overview what can be configured, you check the [wiki](https://github.com/sonic2kk/steamtinkerlaunch/wiki), or simply browse through the 
[Main Menu](https://github.com/sonic2kk/steamtinkerlaunch/wiki/Main-Menu), which covers almost everything available. If you want to get an overview of SteamTinkerLaunch's features, and you find the huge [wiki](https://github.com/sonic2kk/steamtinkerlaunch/wiki) too overwhelming,
you might want to check out the [articles and videos](#Press) created by members of the community.

### Configuration with Text Editors
As mentioned, almost everything can be configured from the [Main Menu](https://github.com/sonic2kk/steamtinkerlaunch/wiki/Main-Menu), but optionally you can edit SteamTinkerLaunch's global and per-game configuration files with a graphical text editor for a more granular approach. Before diving into editing with a text editor, it might be a good idea to start by exploring the configuration options in the [Main Menu](https://github.com/sonic2kk/steamtinkerlaunch/wiki/Main-Menu), and then diving in and tweaking with a text editor.

For more information on SteamTinkerLaunch's specific configuration files, see the [Configuration Files wiki page](https://github.com/sonic2kk/steamtinkerlaunch/wiki/Configuration-Files).

For information on where SteamTinkerLaunch stores downloaded files, see the [Downloads wiki page](https://github.com/sonic2kk/steamtinkerlaunch/wiki/Downloads).

## Troubleshooting
### Logs
Logs are written into the `LOGDIR` as defined in the [Global Menu](https://github.com/sonic2kk/steamtinkerlaunch/wiki/Global-Menu) or [Global Config](https://github.com/sonic2kk/steamtinkerlaunch/wiki/Configuration-Files#Global-Config) (by default, this is usually `~/.config/steamtinkerlaunch/logs/`). The verbosity of the logfile depends on the `WRITELOG` variable, where `0` is no logging, `1` is less verbosity and `2` is most verbosity.

SteamTinkerLaunch produces a number of logs, including game-specific log files. For logs that have a Steam AppID in them (such as Proton logs), there is usually a symlink for the log file with the game's name to make it easier to identify logs. 

SteamTinkerLaunch may also store additional logging information in `/dev/shm/steamtinkerlaunch`.

As well as logs, there is a wiki page for [troubleshooting](https://github.com/sonic2kk/steamtinkerlaunch/wiki/Troubleshooting) which lists some problems a few users have faced and some known issues.

## Disclaimer
Keep in mind that you are using SteamTinkerLaunch at your own risk and that you are responsible for the third party programs that you launch with it. SteamTinkerLaunch is not affiliated with Valve Corporation or Steam.

## Contributing
SteamTinkerLaunch is always looking for new contributors. See [CONTRIBUTING.md](https://github.com/sonic2kk/steamtinkerlaunch/blob/master/CONTRIBUTING.md) for some more information on how to contribute to the project.

## License
SteamTinkerLaunch is licensed under the GNU General Public License v3.0. See [LICENSE](https://github.com/sonic2kk/steamtinkerlaunch/blob/master/LICENSE) for more information.
