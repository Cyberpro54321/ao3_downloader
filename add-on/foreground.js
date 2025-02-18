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

var name1 = document.querySelector("html body div div div div ul li.download ul");
var name2 = name1.lastElementChild.firstChild;
for (let i = 0; i < name1.children.length; i++) {
  if (name1.children[i].innerText == "HTML") {
    name2 = name1.children[i].firstChild;
  }
}
var dlLink = name2.getAttribute("href");
var filename = dlLink.split('/')[3].split('?')[0].slice(0, -5)
console.log(dlLink);
console.log(filename);


// content-script.js

function handleResponse(message) {
  console.log(`Message from the background script: ${message.response}`);
}

function handleError(error) {
  console.log(`Error: ${error}`);
}

const sending = browser.runtime.sendMessage({
  origin: "foreground",
  payload: {
    name: filename,
    css: y,
    download: dlLink
  }
});
sending.then(handleResponse, handleError);


