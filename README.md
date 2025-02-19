# AO3 Downloader
This is a set of python scripts and browser extension designed to streamline the process of downloading works from the website [archiveofourown.org](https://archiveofourown.org/) - coloquially "AO3" - while maintaining the CSS theming one would see on the original page.

Currently this project is only compatible with Firefox and only tested on Linux. If any volunteers would like to test how this project works on Windows, MacOS, Android, or IOS, or would like to work on porting the browser-side parts of this project to Chromium, I would apreciate the help.

## Installation
1. Download the contents of the 'app' folder and the browser extension (.xpi file) from this repository.
   - In my experience, Firefox will attempt to install the browser extension immediately at this step, rather than saving it like a normal file. If that doesn't happen for you, install it now.
2. Mark `ao3_downloader.py`, `process_fic.py`, and `install.py` as executable if they aren't already. Your file browser program may or may not be able to do this graphically depending on what distro you're using, but the following command should work on any variant of linux:
```
chmod +x ao3_downloader.py process_fic.py install.py
```
3. Run `install.py`
4. Go to the Firefox addons management page (about:addons), then navigate to ao3_downloader's Preferences menu (Extensions -> ao3_downloader -> Preferences) and type in the directory you chose to store your downloaded files during step 3. Be sure to click the "Save" button afterwards.
5. (Optional): Download copies of archiveofourown's official CSS stylesheets and put them in the `ao3css` folder that was created in step 3.
> [!NOTE]
> Sometimes when I access AO3, the official stylesheets are served as 27 different stylesheets, numbered 01-22 plus 25-28, plus a non-numbered 'sandbox.css'. Some other times, however, there will be only 6 stylesheets, with 'sandbox.css' and numbered sheets 1 + 4-7.
> The current version of this tool was made for use with the 27 different stylesheets. If the 6 stylesheets are put in `ao3css` instead, the only one that will be used by files made with the current version of this program is 'sandbox.css'

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
- [install.py](app/install.py): Original
