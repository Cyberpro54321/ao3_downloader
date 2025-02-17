var x = document.getElementsByTagName("STYLE");
var y = [];
for (let i = 0; i < x.length; i++) {
	y[i] = x[i].innerHTML;
}

console.log("Hello World!");
if (y.length > 0) {
  window.alert(y.length+" Workskin(s) Detected");
} else {
	y[0] = "";
}

for (let i = 0; i < y.length; i++) {
  console.log(y[i]);
}
// content-script.js

function handleResponse(message) {
  console.log(`Message from the background script: ${message.response}`);
}

function handleError(error) {
  console.log(`Error: ${error}`);
}

const sending = browser.runtime.sendMessage({
  name: "Greeting from the content script",
  css: y
});
sending.then(handleResponse, handleError);


