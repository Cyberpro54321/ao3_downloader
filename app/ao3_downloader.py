#!/usr/bin/env python3

import sys  # https://docs.python.org/3/library/sys.html
import json  # https://docs.python.org/3/library/json.html
import struct  # https://docs.python.org/3/library/struct.html


# Read a message from stdin and decode it.
def getMessage():
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
    # sendMessage(encodeMessage(receivedMessage))
    file = open("/home/no1/Documents/AO3_Downloader/scripts/log.log", "w")
    file.write("receivedMessage is: " + receivedMessage + "\n")
    file.write("receivedMessage is type: " + str(type(receivedMessage)) + "\n")
    test = json.loads(receivedMessage)
    file.write("test is: " + str(test) + "\n")
    file.write("test is type: " + str(type(test)) + "\n")
    name = str(test["name"])
    file.write("test.name is: " + name + "\n")
    css = str(test["css"])
    file.write("test.css is: " + css + "\n")
    file.close()
    # sendMessage(encodeMessage(name))
    sendMessage(encodeMessage(css))
