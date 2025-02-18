#!/usr/bin/env python3

import sys  # https://docs.python.org/3/library/sys.html
import json  # https://docs.python.org/3/library/json.html
import struct  # https://docs.python.org/3/library/struct.html
import subprocess  # https://docs.python.org/3/library/subprocess.html

# config
installDir = ""


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
    sendMessage(encodeMessage(receivedMessage))
    # logfile = open("log.log", "w")
    # logfile.write("Message Received\n")
    parsedMessage = json.loads(receivedMessage)
    installDir = parsedMessage["installDir"]
    # logfile.write("installDir is " + installDir + "\n")
    if parsedMessage["notification"] == "CSS":
        file = open(
            installDir + "Workskins/" + parsedMessage["name"] + ".css",
            "w",
        )
        for i in parsedMessage["css"]:
            file.write(i)
    if parsedMessage["notification"] == "DownloadComplete":
        args = ["./process_fic.py", "--directory", installDir, parsedMessage["name"]]
        subprocess.run(args)
    # logfile.close()
