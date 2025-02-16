// ==UserScript==
// @name     Workscript Detector
// @version  1
// @match    https://*.archiveofourown.org/works/*
// @require  http://ajax.googleapis.com/ajax/libs/jquery/2.1.0/jquery.min.js
// @grant    GM.setClipboard
// ==/UserScript==

var x = document.getElementsByTagName("STYLE");
var y = [];
for (let i = 0; i < x.length; i++) {
	y[i] = x[i].innerHTML;
}

console.log("Hello World!");
if (y.length > 0) {
  window.alert(y.length+" Workskin(s) Detected");
} else {
	y[0] = "No Workskin";
}

// for (let i = 0; i < x.length; i++) {
//   console.log(x[i].innerHTML);
//   GM.setClipboard(x[i].innerHTML);
// }
for (let i = 0; i < y.length; i++) {
  console.log(y[i]);
  GM.setClipboard(y[i]);
}

// console.log(x[0].innerHTML);
