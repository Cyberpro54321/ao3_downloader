
let sendObject = {"name":"test1","css":"test2"};

/*
On startup, connect to the "ping_pong" app.
*/
let port = browser.runtime.connectNative("ao3_downloader");

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
  console.log(`Received ${response}`);
}

function onError(error) {
  console.log(`Error: ${error}`);
}

/*
When the extension's action icon is clicked, send the app a message.
*/
browser.browserAction.onClicked.addListener(() => {
  console.log("Sending:  ping");
  // port.postMessage("ping");
  let sending = browser.runtime.sendNativeMessage("ao3_downloader", JSON.stringify(sendObject));
  sending.then(onResponse, onError);
});
// background-script.js
function handleMessage(request, sender, sendResponse) {
  console.log(`A content script sent a message: ${request.name}`);
  console.log(`A content script sent a message: ${request.css}`);
  sendResponse({ response: "Response from background script" });
}

browser.runtime.onMessage.addListener(handleMessage);

