# Steam Tinker Launch
[![GitHub stars](https://img.shields.io/github/stars/frostworx/steamtinkerlaunch.svg?style=flat-square)](https://github.com/frostworx/steamtinkerlaunch/stargazers)
[![GitHub contributors](https://img.shields.io/github/contributors/frostworx/steamtinkerlaunch.svg?style=flat-square)](https://github.com/frostworx/steamtinkerlaunch/graphs/contributors)
[![GitHub issues](https://img.shields.io/github/issues/frostworx/steamtinkerlaunch.svg?style=flat-square)](https://github.com/frostworx/steamtinkerlaunch/issues)
[![GitHub license](https://img.shields.io/github/license/frostworx/steamtinkerlaunch.svg?style=flat-square)](https://github.com/frostworx/steamtinkerlaunch/blob/dev/LICENSE)
[![reddit](https://img.shields.io/reddit/subreddit-subscribers/SteamTinkerLaunch?style=flat-square&label=Reddit)](https://www.reddit.com/r/SteamTinkerLaunch)

## What is SteamTinkerLaunch?

<img align="left" width="64" height="64" src="https://github.com/frostworx/repo-assets/blob/master/pics/steamtinkerlaunch-logo_64px.png" alt="**SteamTinkerLaunch** is a Linux wrapper tool for use with the Steam client">

**Steam Tinker Launch** is a versatile Linux wrapper tool for use with the Steam client which allows for easy graphical configuration of game tools, such as [GameScope](https://github.com/frostworx/steamtinkerlaunch/wiki/GameScope), [MangoHud](https://github.com/frostworx/steamtinkerlaunch/wiki/MangoHud), [modding tools](https://github.com/frostworx/steamtinkerlaunch/wiki/Modding) and a bunch more. It supports both games using Proton and native Linux games, and works on both X11 and Wayland.
 
As described by _/u/TaylorRoyal23_ on [r/linux_gaming](https://www.reddit.com/r/linux_gaming/comments/ud58i2/comment/i6i3yf9/?utm_source=share&utm_medium=web2x&context=3):

> _"An incredible wrapper with a menu that lets you easily toggle and modify various settings for games on Linux.
Anything from proton versions, to startup and exit scripts, proton/dxvk/etc. settings, FSR, reshade,
and even options for various tools like gamemode, replay-sorcery, gamescope, etc. Tons more too.
I just set my default proton version to "steam tinker launcher" and then every game launches
with a 2 second menu that allows you to easily change any of the settings.
If you don't press any buttons it just goes with the defaults and launches the game.
The menus can get a little confusing but it consolidates it all in one place and is way more simple
than trying to remember dozens of commands for various settings that one might need."_

![image](https://user-images.githubusercontent.com/7917345/186237765-8803c246-a025-413b-be8c-f2c13243291d.png)

## What Does It Do?
SteamTinkerLaunch offers a huge variety of features, too many to list in this Readme. Please see the [Features List](https://github.com/frostworx/steamtinkerlaunch/wiki#features) and their associated wiki pages for a full breakdown. However, here are some of the key features offered by SteamTinkerLaunch. Note that some of these features may not work with Flatpak Steam!

| Feature | Description |
| ------- | ----------- |
| Custom Per-Game Environment Variables | Set custom environment variables on a per-game basis. Useful for adding command-line tweaks for various games. |
| Custom Game Executable | Change the executable that Steam launches. Useful for custom game launchers/mod launchers.<br /><br />This option is extremely flexible, allowing for launching a custom executable with a game, instead of the game, before the game or after the game. See the [Custom Program wiki page](https://github.com/frostworx/steamtinkerlaunch/wiki/Custom-Program) for usage. |
| Easy installation of Winetricks verbs | SteamTinkerLaunch can apply the necessary steps to install, for example, `dotnet48` or later in a Proton prefix, which can fix common issues with GUI tools running through Proton. |
| [ModOrganizer 2](https://github.com/ModOrganizer2/modorganizer) Support | Installs and sets up mod installation and organization tool ModOrganizer 2. Includes browser integration for handling NXM links.<br /><br />See our [ModOrganizer 2 wiki page](https://github.com/frostworx/steamtinkerlaunch/wiki/Mod-Organizer-2) and [modding wiki page](https://github.com/frostworx/steamtinkerlaunch/wiki/Modding) for more details. |
| [Vortex Mod Manager](https://www.nexusmods.com/about/vortex/) Support | Installs and sets up Nexus Mods' mod management tool Vortex Mod Manager. Includes browser integration for handling NXM links.<br /><br />See our [Vortex wiki page](https://github.com/frostworx/steamtinkerlaunch/wiki/Vortex) and [modding wiki page](https://github.com/frostworx/steamtinkerlaunch/wiki/Modding) for more details. |
| [SpecialK](https://github.com/SpecialKO) support | Utility for enhancing and fixing common problems with Windows games.<br /><br />See our [SpecialK wiki page](https://github.com/frostworx/steamtinkerlaunch/wiki/SpecialK) for usage. May require additional [Optional Dependencies](https://github.com/frostworx/steamtinkerlaunch/wiki/Installation#optional-dependencies). |
| [ReShade](https://reshade.me/) Support (Proton/Wine Only) | Supports the use of ReShade shaders to enhance the visual quality of games.<br /><br />See our [ReShade wiki page](https://github.com/frostworx/steamtinkerlaunch/wiki/ReShade) for usage and information on using **ReShade** and **SpecialK** together. |
| Custom Proton/Wine Download | Manages downloading custom Proton and Wine releases, such as GloriousEggroll's popular Proton flavour [GEProton](https://github.com/GloriousEggroll/proton-ge-custom). These versions are installed and managed by SteamTinkerLaunch.<br /><br />See our wiki pages on [Custom Proton Versions](https://github.com/frostworx/steamtinkerlaunch/wiki/Download-Custom-Proton) and [Custom Wine Versions](https://github.com/frostworx/steamtinkerlaunch/wiki/Download-Custom-Wine) for more details. |

To find out about the latest release, check out the [stable release changelog](https://github.com/frostworx/steamtinkerlaunch/releases/latest). To find out about the latest bleeding-edge development changes not yet in a stable build, check out the [full changelog](https://github.com/frostworx/steamtinkerlaunch/wiki/Changelog).

## How Do I Use It?
### General usage
Steam Tinker Launch works with Linux native games and games using Proton, however some Windows-only utilities (such as [ReShade](https://github.com/frostworx/steamtinkerlaunch/wiki/ReShade)) are only available for Proton games. SteamTinkerLaunch also supports Non-Steam Games so long as they are launched through the Steam client.

There are two ways to use SteamTinkerLaunch through Steam:

#### Steam Compatability Tool (Proton Games)
Using SteamTinkerLaunch as a [compatability tool](https://github.com/frostworx/steamtinkerlaunch/wiki/Steam-Compatibility-Tool) is the preferred way of using it with Proton games. Once SteamTinkerLaunch is installed, force it as a compatability tool for your chosen game from the list of compatability tools. You can also set SteamTinkerLaunch as the default compatability tool for all applications from the Steam Play settings of the Steam client.

Please note that some platforms such as [Steam Flatpak](https://github.com/frostworx/steamtinkerlaunch/wiki/Steam-Flatpak) only allow you to use SteamTinkerLaunch as a compatibility tool. When forcing a game to use a compatability tool, Steam will always download the Windows release of a game, so as a result your mileage may vary. Please report any issues using SteamTinkerLaunch as a compatability tool with Steam Flatpak on the [SteamTinkerLaunch Flatpak issue](https://github.com/frostworx/steamtinkerlaunch/issues/27).

#### Steam Launch Option (Native Linux Games)
To use SteamTinkerLaunch with native Linux games, you can simply add the following to your native game's launch option:

```sh
steamtinkerlaunch %command%
```

On some platforms such as [Steam Deck](https://github.com/frostworx/steamtinkerlaunch/wiki/Steam-Deck), using SteamTinkerLaunch as a launch option may require you to add it to your path. Refer to your distributions documentation on how to add the script to your path, as this can vary between distributions and shells. 

### Game-Specific Use
When starting a game, a small [Wait Requester](#Wait-Requester) dialog will pop up. This will allow you to access the Main Menu either by pressing the button or pressing the spacebar, or skip to launching the game. By default, the dialog will only stay for two seconds before it times out and launches the game, but this can be configured in the SteamTinkerLaunch settings.

![Wait Requester](https://github.com/frostworx/repo-assets/blob/master/pics/Wait-Requester.jpg)

The Main Menu is the springboard to tinkering with your game options. See the [wiki page](https://github.com/frostworx/steamtinkerlaunch/wiki/Main-Menu) for more information on the options it provides. 

### Command Line
SteamTinkerLaunch has several [command line options](https://github.com/frostworx/steamtinkerlaunch/wiki/Command-Line) which can be useful outside Steam, such as for installing modding tools. You can run `steamtinkerlaunch help` for a full list of available commands.

## How Do I Install It?
SteamTinkerLaunch can be installed in a few different ways depending on your platform and needs. Please refer to the [Installation wiki page](https://github.com/frostworx/steamtinkerlaunch/wiki/Installation) for detailed installation instructions.

| Platform | Notes |
| -------- | ----- |
| Package Manager | Preferred installation method. See distribution package status below.<br />Many thanks to all package maintainers!<br /><br />[![Packaging status](https://repology.org/badge/vertical-allrepos/steamtinkerlaunch.svg)](https://repology.org/project/steamtinkerlaunch/versions)<br /><br />See also [Installation Wiki](https://github.com/frostworx/steamtinkerlaunch/wiki/Installation#package-manager). |
| Manual Installation | [See Installation Wiki notes](https://github.com/frostworx/steamtinkerlaunch/wiki/Installation#manual-installation) for dependency information and post-installation setup. |
| [Steam Deck](https://github.com/frostworx/steamtinkerlaunch/wiki/Steam-Deck) | See [Installation Wiki](https://github.com/frostworx/steamtinkerlaunch/wiki/Installation#steam-deck) for Steam Deck specific installation instructions. |
| [Steam Flatpak](https://github.com/frostworx/steamtinkerlaunch/wiki/Steam-Flatpak) | See [Installation Wiki](https://github.com/frostworx/steamtinkerlaunch/wiki/Installation#steam-flatpak) for setup instructions on using Steam Flatpak and SteamTinkerLaunch. |
| Other | See [Installation Wiki](https://github.com/frostworx/steamtinkerlaunch/wiki/Installation#distro-specific) for any distro-specific installation instructions. |

## Press
Several great people have mentioned SteamTinkerLaunch on their platforms/channels. Many thanks to all who have covered SteamTinkerLaunch!

| Name | Press |
| ---- | ----- |
| **[podiki](https://boilingsteam.com/author/podiki/)** (also a SteamTinkerLaunch contributor) | [Wrote a huge article about SteamTinkerLaunch on BoilingSteam](https://boilingsteam.com/supercharge-steam-with-steamtinkerlaunch-stl)! |
| **[ekianjo](https://boilingsteam.com/author/ekianjo/)** | [Wrote up a Q&A on BoilingSteam](https://boilingsteam.com/steam-tinker-launcher-making-tinkering-much-easier) with SteamTinkerLaunch creator Frostworx! |
| **[Hex DSL](https://www.youtube.com/c/HexDSL)** | Made a [YouTube video](https://www.youtube.com/watch?v=rdXQRMwMfPE) showcasing SteamTinkerLaunch |
| **[tuxfoo](https://www.youtube.com/channel/UCWpoyqSBIXtylRLFgP3PFfg)** | Made a [YouTube video](https://www.youtube.com/watch?v=l1KjIANTIKs) showcasing SteamTinkerLaunch
| **[Linux Game Cast](https://linuxgamecast.com/)** | Mentioned SteamTinkerLaunch on their [casts](https://www.youtube.com/watch?v=djuZdnE83fE&t=436s) [several](https://www.youtube.com/watch?v=yVsTMhx8E7c&t=983s) [times](https://www.youtube.com/watch?v=qhybhTGV3mA&t=1279s), and [counting]((https://linuxgamecast.com/2021/11/linux-game-cast-484-yami-pedro))! |
| [Mark Dougherty](https://linuxgamingcentral.com/) | Has written [several](https://linuxgamingcentral.com/posts/news-stl-v10-released/) [articles](https://linuxgamingcentral.com/posts/stl-v11-released/) about SteamTinkerLaunch |

 
## Configuration
When SteamTinkerLaunch is started for the first time, it will create its default [configuration](#Configuration) structure (usually in `~/.config/steamtinkerlaunch`). All [Configuration Files](https://github.com/frostworx/steamtinkerlaunch/wiki/Configuration-Files) are self-contained documents and are always growing, and as a result some options may be missing. If you find a configuration option that is not documented, please request it on the [issue tracker](https://github.com/frostworx/steamtinkerlaunch/issues). You may even write the documentation yourself and a collaborator can add it.

For a general overview what can be configured, you check the [wiki](https://github.com/frostworx/steamtinkerlaunch/wiki), or simply browse through the 
[Main Menu](https://github.com/frostworx/steamtinkerlaunch/wiki/Main-Menu), which covers almost everything available. If you want to get an overview of SteamTinkerLaunch's features, and you find the huge [wiki](https://github.com/frostworx/steamtinkerlaunch/wiki) too overwhelming,
you might want to check out the [articles and videos](#Press) created by members of the community.

### Configuration with Text Editors
As mentioned, almost everything can be configured from the [Main Menu](https://github.com/frostworx/steamtinkerlaunch/wiki/Main-Menu), but optionally you can edit SteamTinkerLaunch's global and per-game configuration files with a graphical text editor for a more granular approach. Before diving into editing with a text editor, it might be a good idea to start by exploring the configuration options in the [Main Menu](https://github.com/frostworx/steamtinkerlaunch/wiki/Main-Menu), and then diving in and tweaking with a text editor.

For more information on SteamTinkerLaunch's specific configuration files, see the [Configuration Files wiki page](https://github.com/frostworx/steamtinkerlaunch/wiki/Configuration-Files).

For information on where SteamTinkerLaunch stores downloaded files, see the [Downloads wiki page](https://github.com/frostworx/steamtinkerlaunch/wiki/Downloads).

## Troubleshooting
### Logs
Logs are written into the `LOGDIR` as defined in the [Global Menu](https://github.com/frostworx/steamtinkerlaunch/wiki/Global-Menu) or [Global Config](https://github.com/frostworx/steamtinkerlaunch/wiki/Configuration-Files#Global-Config) (by default, this is usually `~/.config/steamtinkerlaunch/logs/`). The verbosity of the logfile depends on the `WRITELOG` variable, where `0` is no logging, `1` is less verbosity and `2` is most verbosity.

SteamTinkerLaunch produces a number of logs, including game-specific log files. For logs that have a Steam AppID in them (such as Proton logs), there is usually a symlink for the log file with the game's name to make it easier to identify logs. 

SteamTinkerLaunch may also store additional logging information in `/dev/shm/steamtinkerlaunch`.

## Disclaimer
Keep in mind that you are using SteamTinkerLaunch at your own risk and that you are responsible for the 3rd party programs that you launch with it.

## License
SteamTinkerLaunch is licensed under the GNU General Public License v3.0. See [LICENSE](https://github.com/frostworx/steamtinkerlaunch/blob/master/LICENSE) for more information.
