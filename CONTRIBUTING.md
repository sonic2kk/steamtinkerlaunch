# Contributing
We are always looking for new contributors! SteamTinkerLaunch has a lot of parts and a lot of features, so there's always something to contribute. 

## How to Contribute
SteamTinkerLaunch is basically a huge Bash script. If you know any Bash, feel free to jump in and look around the code. It might seem a little daunting at first but just play around and you'll get the hang of it. I also recommend reading through the `steamtinkerlaunch.log` file. The log for the most recent launch can be found in `/dev/shm/steamtinkerlaunch`. This can give you a sense for the flow of the script and how all the functions connect together.

Given that SteamTinkerLaunch is a Linux utility, you will probably have a smoother time developing on Linux. This includes on Steam Deck.

## Where to Contribute
You don't have to be a developer to get involed with SteamTinkerLaunch! Here are some ideas on where contributions would be welcome:
- Reporting bugs and suggesting issues on the [issue tracker](https://github.com/sonic2kk/steamtinkerlaunch/issues).
- Fixing bugs you encounter or bugs listed on the issue tracker.
- Helping improve existing features, especially with ModOrganizer 2 and Vortex Mod Manager integration.
- Optimisation improvements
- Suggest improvements to the wiki's documentation.
- Update any existing translations or submit a new translation.

## Submitting Pull Requests
So you've made a feature and you're ready to submit a PR - Awesome! Where applicable please outline your changes and rationale to help with the review process, please don't open blank PRs.

### Standards
A good PR will target a specific area or specific feature, and have a clear improvement on that area. If your PR addresses a specific ticket on the issue tracker, feel free to mention it so that the issue can be automatically closed upon merge.

Reviewing PRs may take time, and to help with this please consider the size and scope of your PRs before submission. There is no hard and fast rule on how to scope your PRs, but it would be slightly preferable to submit several small PRs for easier review rather than one large PR.

You are free to open draft PRs as well if your feature is still in the works but not quite ready for a full review yet. Feel free to ask for advice or review on specific elements in a draft PR.

### Naming
There are no strict rules on how to name or format your pull requests. Just try to make it descriptive, informative and keep it clean :-)

### Commit History
It is totally fine to open a pull request with several commits, however before merging it is much preferable to have your commit history squashed at least a bit. This is in the interest of keeping the commit history relatively clean for contributions. Ideally, one PR will be merged as one commit, but if you feel your changes are better separated across a few commits, please feel free to note that in your PR.

If you don't know how to squash commits, don't let that scare you off from contributing too much. You can do it at the end before merging, and there are plenty of helpful resources online to guide you through the process of squashing commits.

### Translations
If you edit any of the language files when contributing, add the string to **all** the other language files *or* update the string in other language files too if it is untranslated. For example, if you add a string to `english.txt`, and that same string is untranslated in `dutch.txt`, just copy the English string into `dutch.txt`.

The placement of the strings does not matter but try to keep related strings grouped together where possible. 

You are also free to translate the string, if you speak the language. But if not, the English string will be fine.

## Development Tips
This section has some tips and guidance to help with writing code for SteamTinkerLaunch.

### Use ShellCheck
**Note**: You may have to use [ShellCheck v0.8.0](https://github.com/koalaman/shellcheck/releases/tag/v0.8.0) with SteamTinkerLaunch, due to an issue with memory consumption with newer versions of ShellCheck ([koalaman/shellcheck#2652](https://github.com/koalaman/shellcheck/issues/2652)).

There is an awesome utility called [ShellCheck](http://shellcheck.net/) which helps ensure shell code is bug-free. It is strongly recommended to use this when developing for SteamTinkerLaunch, it's a good way to catch bugs and write well structured code.

There may be rare instances where ShellCheck is a bit *too* helpful. In cases like that, you can add a `shellcheck disable` check to your code. In Pull Requests and/or in a comment near that section, please note the reason for disabling that ShellCheck warning.

### Clearing Temp Files
Before running development builds, it can be a good idea to clear out the `/dev/shm/steamtinkerlaunch` folder. Before each execution you can run `rm -rf /dev/shm/steamtinkerlaunch`.

### Testing Development Builds
There are a few ways to test development builds of SteamTinkerLaunch. One of the first things you should do is change the `PROGVERS` at the top of the script. For development purposes you can set this to anything you like, as this will help you ensure you are definitely running the development version of SteamTinkerLaunch. You could append `-dev` to the end of the `PROGVERS`, for example.

To run your development build of SteamTinkerLaunch, you can simply run `./steamtinkerlaunch` to execute the script. You can check the version with `./steamtinkerlaunch version`.

To run your development build of SteamTinkerLaunch through Steam, you can run `./steamtinkerlaunch compat add` and then launch your game through Steam. You shouldn't need to restart Steam for this change to take effect, as it should just change the symlink in Steam's `compatibilitytools.d` folder to point to your development script.

Once you're done with development, you can go back to using your regular SteamTinkerLaunch version in one of the following ways depending on how you installed SteamTinkerLaunch:
- For package manager installations, root installs (with `sudo make install`), or if SteamTinkerLaunch is otherwise on your `PATH` (like on Steam Deck with ProtonUp-Qt), you can run `steamtinkerlaunch compat add` from **outside** of your SteamTinkerLaunch development folder. This will point the symlink in Steam's `compatibilitytools.d` folder back to the original script and not your development script.
- For non-root installs, locale the folder where your original SteamTinkerLaunch script is stored and run `./steamtinkerlaunch compat add`. This will point the symlink in Steam's `compatibilitytools.d` folder to the script you are currently executing instead of the development script.
  
You can then verify that you are using the correct version again by running SteamTinkerLaunch through Steam and checking the version on the Main Menu.

### Text Editors
You can use any text editor you like to develop SteamTinkerLaunch, since it is just a Bash script and ShellCheck will do the linting work for you. If you need some recommendations, [Kate](https://apps.kde.org/kate/), [KWrite](https://apps.kde.org/kwrite/) and [Geany](https://www.geany.org/) have been tested and work very well. [VSCodium](https://vscodium.com/) has also been tested, however note that VSCodium's default Bash language server and syntax highlighting often breaks. This has not been observed in other text editors.

### Navigation and Logging
SteamTinkerLaunch is a big script. Like, **really** big. To help you navigate around, you should search the language files for a string and copy the string's key (e.g., `GUI_MO2MODE`) and use your text editor's "Find" function to locate that string. It might happen that the string appears in multiple places, but this can help serve as a good starting point for finding the area of the code that you're wanting to work on.

As mentioned, using the `steamtinkerlaunch.log` file in `/dev/shm/steamtinkerlaunch` can be really useful when getting started. Each log statement is in the format `DATETIME STATEMENT_TYPE - FUNCNAME - LOG_STATEMENT`. Each log starts with the current date and time from your system (e.g. `Mon 31 Oct 00:00:00 UTC 2022`). After this is the type of statement, denoting whether it's a `WARN`ing, or `INFO`rming, or an `ERROR`. Then the last part of each log is the actual log message itself, such as `started SteamTinkerLaunch from /path/to/script`. An example log message might look like this: `Mon 31 Oct 00:00:00 UTC 2022 initAID - Set AID from STEAM_COMPAT_APP_ID to '1454400'`.

If you want to help trace how your code is executing, you can add your own logging statements with the `WRITELOG` function. For example: `writelog "INFO" "${FUNCNAME[0]} - This is a log message"`. This will log an `INFO` that says `This is a log message`. Using `${FUNCNAME[0]}` is what puts the function name your code is executing from into the logging message. 

## Translations
Any contributions related to translations are always welcome, whether it's an update for untranslated strings in an existing language, an overhaul to improve an existing translation, or a brand new translation! The current maintainer of SteamTinkerLaunch only speaks English, so you are more than welcome to contribute a PR to add a translation.

To update a translation, open the translation file and start updating the strings. If you need a reference, the `english.txt` translation file is probably the most correct and up-to-date so it could be a good reference point on how to translate a given string.

To start writing a new translation, it is recommended to use `english.txt` as your base as this is the most up-to-date translation available. Duplicate this file and start translating the strings. As there are hundreds of strings you don't have to update all of them, but **don't** remove the strings you cannot or have not translated. If you run into this, just leave the string untranslated.

In future, you are always welcome to come back and improve your translation. More and more strings will be added as SteamTinkerLaunch grows, and translations can quickly become outdated. Don't be afraid to keep an eye on the repository and submit PRs to update the translation strings, even if it's only one or two lines each time.