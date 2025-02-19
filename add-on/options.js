async function saveOptions(e) {
  e.preventDefault();
  // console.log(document.querySelector("#installDir").value);
  await browser.storage.local.set({
    installDir: document.querySelector("#installDir").value
  });
}

async function restoreOptions() {
  let res = await browser.storage.local.get('installDir');
  document.querySelector("#installDir").value = res.installDir || '/home/XXXX/Documents/AO3_Downloader/';
}

document.addEventListener('DOMContentLoaded', restoreOptions);
document.querySelector("form").addEventListener("submit", saveOptions);
