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

