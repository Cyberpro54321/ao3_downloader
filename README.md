# AO3 Downloader
This is a set of python scripts and browser extension designed to streamline the process of downloading works from the website [archiveofourown.org](https://archiveofourown.org/) - coloquially "AO3" - while maintaining the CSS theming one would see on the original page.

Currently this project is only compatible with Firefox and only tested on Linux. If any volunteers would like to test how this project works on Windows, MacOS, Android, or IOS, or would like to work on porting the browser-side parts of this project to Chromium, I would apreciate the help.

## Alternatives / Why Bother Using A Browser Extension
### Official Download Links
AO3 has official download links for every work on the website in a variety of formats, including HTML. However, none of these official downloads come with any of the CSS theming from the archiveofourown.org website, or the theming from the "Workskins" that authors can put on their creations, which is annoying for most works and downright calamitous for those that heavily rely on that theming.

### Control + S In Browser
Modern Browsers have the ability to save a web page and all its required files to local storage. However, attempting to save AO3 works this way results in several issues, including:
- The preservation of several buttons that interact with the AO3 servers that don't make sense to be kept in a downloaded version (including the "Bookmark", "Subscribe/Unsubscribe", and "Download" buttons near the top of the page and the comments section at the bottom of the page.)
- If you were logged in to AO3 at the time, your username and whether or not you're subscribed to the work will be baked into the saved version
- A seperate copy of the following, totaling aproximately 530 kilobytes, will be saved to your local storage for every single work you download this way.
  - The AO3 logo
  - All of AO3's default CSS stylesheets
  - And every JavaScript file called upon by the website

### Download the raw web pages with Curl and then process them locally
While the curl command line utility for Linux does seem to be able to download publicly-available AO3 works with little issue, every time I've tried calling it from within a python script, including using the subprocess.run() command, has resulted in a page from Cloudflare saying that AO3 is having connection issues, likely as part of some sort of anti-bot or anti-DDOS protocol. Even if I could find a way around that, AO3 authors have the option to make their works visible only to those currently signed in to their own AO3 accounts, and getting around *that* would require having the user input their AO3 credentials and then figuring out how to send them to AO3's servers as part of the download request.

## Copyright & Licensing
Most of this project's core files were created by copying and modifying those found in [the Mozilla Add-ons team's webextension-examples repository](https://github.com/mdn/webextensions-examples), particularly the [Favorite Colour](https://github.com/mdn/webextensions-examples/tree/main/favourite-colour) and [Native Messaging](https://github.com/mdn/webextensions-examples/tree/main/native-messaging) plugins.

- [foreground.js](add-on/foreground.js): Largely original, with certain functions copied from [the MDN Web documentation](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/Content_scripts#communicating_with_background_scripts)
- [background.js](add-on/background.js): Original form copied from [native-messaging/add-on/background.js](https://github.com/mdn/webextensions-examples/blob/main/native-messaging/add-on/background.js), then significantly modified.
- [ao3_downloader.py](app/ao3_downloader.py): Original form copied from [native-messaging/app/ping-pong.py](https://github.com/mdn/webextensions-examples/blob/main/native-messaging/app/ping_pong.py), then significantly modified.
- [process_fic.py](app/process_fic.py): Original
- [manifest.json](add-on/manifest.json): Original form copied from [native-messaging/add-on/manifest.json](https://github.com/mdn/webextensions-examples/blob/main/native-messaging/add-on/manifest.json), then lightly modified.
- [options.html](add-on/options.html): Copied from [MDN Web documentation](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/user_interface/Options_pages)
- [options.js](add-on/options.js): Original form copied from [favourite-colour/options.js](https://github.com/mdn/webextensions-examples/blob/main/favourite-colour/options.js), then lightly modified.
- [ao3_downloader.json](app/ao3_downloader.json): Original form copied from [native-messaging/app/ping_pong.json](https://github.com/mdn/webextensions-examples/blob/main/native-messaging/app/ping_pong.json), then lightly modified
