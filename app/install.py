#!/bin/python3

from getpass import getuser
import os  # https://docs.python.org/3/library/os.html
import os.path  # https://docs.python.org/3/library/os.path.html


# functions
# t = selectOption([
#     ["a", "1", "alpha"],
#     ["b", "2", "beta"]
# ])
# t == 0 if user types a, 1, or alpha
# t == 1 if user types b, 2, or beta
def selectOption(options: list, prompt="", caseSensitive=False):
    rawInput = ""
    while True:
        rawInput = input(prompt)
        for i in range(len(options)):
            for j in options[i]:
                if caseSensitive:
                    if j == rawInput:
                        return i
                else:
                    if j.lower() == rawInput.lower():
                        return i


def getYesNo(prompt="Yes or No? "):
    return selectOption(
        [
            ["0", "no", "n", "false", "f", "stop", "s"],
            ["1", "yes", "y", "true", "t", "go", "g"],
        ],
        prompt,
        False,
    )


# variables
dry_run = True
scriptNameInstall = "install.py"
scriptNameWorkskin = "ao3_downloader.py"
scriptNameHTML = "process_fic.py"

if os.path.exists(os.getcwd() + "/" + scriptNameInstall):
    currentScriptDir = os.getcwd() + "/"
elif os.path.exists(os.getcwd() + "/app/" + scriptNameInstall):
    currentScriptDir = os.getcwd() + "/app/"
else:  # TODO: figure out where install.py will be if the github-created .zip / .tar.gz archives are put in ~/Downloads and then extracted
    currentScriptDir = ""

# safety checks
if getuser() == "root":
    raise Exception("DON'T RUN THIS AS ROOT. NO.")

# main code
if not bool(currentScriptDir):
    promptFindScript = (
        "What folder / directory are the script files ("
        + scriptNameInstall
        + ", "
        + scriptNameWorkskin
        + ", and "
        + scriptNameHTML
        + ") currently in?"
        + "\n"
    )
    while not bool(currentScriptDir):
        rawInput = os.path.abspath(os.path.expanduser(input(promptFindScript)))
        if os.path.exists(rawInput + scriptNameInstall):
            currentScriptDir = rawInput
        elif os.path.exists(rawInput + "/" + scriptNameInstall):
            currentScriptDir = rawInput + "/"
        elif os.path.exists(rawInput + "/app/" + scriptNameInstall):
            currentScriptDir = rawInput + "/app/"

promptDoChangeScriptDir = (
    "Do you want to keep these files in their current location, or move them?"
    + "\n"
    + "Current location: "
    + currentScriptDir
    + "\n"
)
doChangeScriptDir = getYesNo(promptDoChangeScriptDir)

if doChangeScriptDir:
    promptChangeScriptDir = (
        "What folder / directory should the script files be moved to?\n"
    )
    scriptDir = os.path.abspath(os.path.expanduser(input(promptChangeScriptDir)))
    if scriptDir[-1:] != "/":
        scriptDir = scriptDir + "/"
    if not os.path.exists(scriptDir):
        print(scriptDir + " doesn't exist. Create it?")
        if bool(getYesNo()):
            try:
                os.makedirs(scriptDir)
            except PermissionError:
                print("You don't have the permissions needed to create " + scriptDir)
    while not os.access(scriptDir, os.W_OK):
        print(
            scriptDir + " isn't writable. Maybe you don't have the right permissions?"
        )
        scriptDir = os.path.abspath(os.path.expanduser(input(promptChangeScriptDir)))
        if not os.path.exists(scriptDir):
            print(scriptDir + " doesn't exist. Create it?")
            if bool(getYesNo()):
                try:
                    os.makedirs(scriptDir)
                except PermissionError:
                    print(
                        "You don't have the permissions needed to create " + scriptDir
                    )
    if os.access(scriptDir, os.W_OK) and not dry_run:
        os.rename(currentScriptDir + scriptNameInstall, scriptDir + scriptNameInstall)
        os.rename(currentScriptDir + scriptNameWorkskin, scriptDir + scriptNameWorkskin)
        os.rename(currentScriptDir + scriptNameHTML, scriptDir + scriptNameHTML)
else:
    scriptDir = currentScriptDir
