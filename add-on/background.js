
let defaultName = "placeholder1";
let workName = defaultName;
let workCSS = [];
let downloadLink = "";
let installDir = "";

/*
On startup, connect to the "ping_pong" app.
*/
let port = browser.runtime.connectNative("ao3_downloader");

async function restoreOptions() {
  let res = await browser.storage.local.get('installDir');
  installDir = res.installDir;
  console.log(res.installDir);
}

document.addEventListener('DOMContentLoaded', restoreOptions);
/*
Listen for messages from the app and log them to the console.
*/
port.onMessage.addListener((response) => {
  console.log("Received: " + response);
});

/*
Listen for the native messaging port closing.
*/
port.onDisconnect.addListener((port) => {
  if (port.error) {
    console.log(`Disconnected due to an error: ${port.error.message}`);
  } else {
    // The port closed for an unspecified reason. If this occurred right after
    // calling `browser.runtime.connectNative()` there may have been a problem
    // starting the the native messaging client in the first place.
    // https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/Native_messaging#troubleshooting
    console.log(`Disconnected`, port);
  }
});


function onResponse(response) {
  console.log(`Received message: ${response.payload.notification}`);
}

function onError(error) {
  console.log(`Error: ${error}`);
}
function onStartedDownload(id) {
  console.log(`Started downloading: ${id}`);
}

function onFailed(error) {
  console.log(`Download failed: ${error}`);
}

function handleChanged(delta) {
  if (delta.state && delta.state.current === "complete") {
    console.log(`Download ${delta.id} has completed.`);
    let sendingDLComplete = browser.runtime.sendNativeMessage("ao3_downloader", JSON.stringify({
      "type": "notification",
      "payload": {
        "notification": "HTML Download Complete",
        "installDir": installDir,
        "name": workName
      }
    }));
    sendingDLComplete.then(onResponse, onError);
  }
}

/*
When the extension's action icon is clicked, send the app a message.
*/
browser.browserAction.onClicked.addListener(() => {
  if (workName != defaultName) {
    let downloadUrl = "https://archiveofourown.org" + downloadLink;
    let downloading = browser.downloads.download({
      url: downloadUrl,
      // filename: "my-image-again.png",
      // conflictAction: "uniquify",
    });
    downloading.then(onStartedDownload, onFailed);
    browser.downloads.onChanged.addListener(handleChanged);

    let sendingCSS = browser.runtime.sendNativeMessage("ao3_downloader", JSON.stringify({
      "type": "workskinInfo",
      "payload": {
        "name": workName,
        "css": workCSS,
        "installDir": installDir
      }
    }));
    sendingCSS.then(onResponse, onError);
  } else {
    console.log("Button was clicked without foreground.js having sucessfully sent a message");
  }
});
// background-script.js
function handleMessage(request, sender, sendResponse) {
  console.log(`A content script sent a message: ${request.payload.name}`);
  if (request.type == "foreground") {
    workName = request.payload.name;
    workCSS = request.payload.css;
    downloadLink = request.payload.download;
  }
  sendResponse({ response: "Response from background script" });
}

browser.runtime.onMessage.addListener(handleMessage);

