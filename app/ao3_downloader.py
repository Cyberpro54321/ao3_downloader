#!/usr/bin/env python3

import sys  # https://docs.python.org/3/library/sys.html
import json  # https://docs.python.org/3/library/json.html
import struct  # https://docs.python.org/3/library/struct.html
import subprocess  # https://docs.python.org/3/library/subprocess.html
import os.path  # https://docs.python.org/3/library/os.path.html
from os import rename

# config
installDir = ""
logfile = "ao3dl.log"


def getMessage():  # Read a message from stdin and decode it.
    rawLength = sys.stdin.buffer.read(4)
    if len(rawLength) == 0:
        sys.exit(0)
    messageLength = struct.unpack("@I", rawLength)[0]
    message = sys.stdin.buffer.read(messageLength).decode("utf-8")
    return json.loads(message)


# Encode a message for transmission, given its content.
def encodeMessage(messageContent):
    # https://docs.python.org/3/library/json.html#basic-usage
    # To get the most compact JSON representation, you should specify
    # (',', ':') to eliminate whitespace.
    # We want the most compact representation because the browser rejects
    # messages that exceed 1 MB.
    encodedContent = json.dumps(messageContent, separators=(",", ":")).encode("utf-8")
    encodedLength = struct.pack("@I", len(encodedContent))
    return {"length": encodedLength, "content": encodedContent}


# Send an encoded message to stdout
def sendMessage(encodedMessage):
    sys.stdout.buffer.write(encodedMessage["length"])
    sys.stdout.buffer.write(encodedMessage["content"])
    sys.stdout.buffer.flush()


while True:
    receivedMessage = getMessage()
    response = {}
    response = {
        "type": "notification",
        "payload": {"notification": "placeholder"},
    }
    log = open(logfile, "w")
    log.write("Message Received\n")
    parsedMessage = json.loads(receivedMessage)
    installDir = os.path.expanduser(parsedMessage["payload"]["installDir"])
    if installDir[-1:] != "/":
        installDir = installDir + "/"
    log.write("installDir is " + installDir + "\n")
    log.write("Beginning sanitization of work name. Starting name is:\n")
    log.write(parsedMessage["payload"]["workName"] + "\n")
    workName = ""  # whitelist is a-z, A-Z, 0-9, space, comma, _, -, `, (, ), and +.
    for i in parsedMessage["payload"]["workName"]:
        if i.isascii() and i.isprintable():
            workName = workName + i
    workName.replace(" ", "_")
    workName.replace("~", "-")
    workName.replace('"', "`")
    workName.replace("'", "`")
    workName.replace(".", ",")
    workName.replace("[", "(")
    workName.replace("]", ")")
    workName.replace("{", "(")
    workName.replace("}", ")")
    workName = workName.strip("/\\!#$%^*|;:<>?")
    while workName.find("&") != -1 and len(workName) < (255 - 5 - 2):
        workName.replace("&", "and", 1)
    while workName.find("@") != -1 and len(workName) < (255 - 5 - 1):
        workName.replace("@", "at", 1)
    workName = workName.strip("@&")
    log.write("Ending work name is:\n")
    log.write(workName + "\n")
    if parsedMessage["type"] == "workskinInfo":
        fullFileName = (
            installDir + "Workskins/" + parsedMessage["payload"]["workName"] + ".css"
        )
        file = open(
            fullFileName,
            "w",
        )
        log.write("Sucessfully opened " + fullFileName + "\n")

        for i in parsedMessage["payload"]["css"]:
            file.write(i)
        response["payload"]["notification"] = "Workscript Sucessfully Written"
        log.write("Finished writing " + fullFileName + "\n")
    if (
        parsedMessage["type"] == "notification"
        and parsedMessage["payload"]["notification"] == "HTML Download Complete"
    ):
        rename(
            installDir + "Raws/" + parsedMessage["payload"]["fileName"] + ".html",
            installDir + "Raws/" + workName + ".html",
        )
        log.write("background.js says the download of the HTML file is complete.\n")
        args = [
            "./process_fic.py",
            "--directory",
            installDir,
            workName,
        ]
        log.write("About to launch process_fic.py.\n")
        subprocess.run(args)
        response["payload"]["notification"] = "HTML Sucessfully Parsed"
        log.write("process_fic.py has completed sucessfully\n")
    log.write(str(response) + "\n")
    log.write(str(encodeMessage(response)) + "\n")
    log.close()
    sendMessage(encodeMessage(response))
