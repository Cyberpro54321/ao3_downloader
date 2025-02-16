#!/bin/python3

import argparse  # https://docs.python.org/3/library/argparse.html

parser = argparse.ArgumentParser()
parser.add_argument(
    "fileName", help="Targeted Filename (without extension)", metavar="<filename>"
)
args = parser.parse_args()


class Stylesheet:
    def __init__(self, file, folder, media):
        self.file = file
        self.folder = folder
        self.media = media

    def __str__(self):
        return f'<link rel="stylesheet" type="text/css" media="{self.media}" href="../{self.folder}/{self.file}.css">\n'


def indent(level):
    temp = ""
    for i in range(level):
        temp = temp + "  "
    return temp


# variables
stripStyleTag = True
insertStylesheets = True
doHtmlTagChanges = True
stylesheets = (
    Stylesheet("01-core", "ao3css", "screen"),
    Stylesheet("02-elements", "ao3css", "screen"),
    Stylesheet("03-region-header", "ao3css", "screen"),
    Stylesheet("04-region-dashboard", "ao3css", "screen"),
    Stylesheet("05-region-main", "ao3css", "screen"),
    Stylesheet("06-region-footer", "ao3css", "screen"),
    Stylesheet("07-interactions", "ao3css", "screen"),
    Stylesheet("08-actions", "ao3css", "screen"),
    Stylesheet("09-roles-states", "ao3css", "screen"),
    Stylesheet("10-types-groups", "ao3css", "screen"),
    Stylesheet("11-group-listbox", "ao3css", "screen"),
    Stylesheet("12-group-meta", "ao3css", "screen"),
    Stylesheet("13-group-blurb", "ao3css", "screen"),
    Stylesheet("14-group-preface", "ao3css", "screen"),
    Stylesheet("15-group-comments", "ao3css", "screen"),
    Stylesheet("16-zone-system", "ao3css", "screen"),
    Stylesheet("17-zone-home", "ao3css", "screen"),
    Stylesheet("18-zone-searchbrowse", "ao3css", "screen"),
    Stylesheet("19-zone-tags", "ao3css", "screen"),
    Stylesheet("20-zone-translation", "ao3css", "screen"),
    Stylesheet("21-userstuff", "ao3css", "screen"),
    Stylesheet("22-system-messages", "ao3css", "screen"),
    Stylesheet(
        "25-media-midsize", "ao3css", "only screen and (max-width: 62em), handheld"
    ),
    Stylesheet(
        "26-media-narrow", "ao3css", "only screen and (max-width: 62em), handheld"
    ),
    Stylesheet("27-media-aural", "ao3css", "speech"),
    Stylesheet("28-media-print", "ao3css", "print"),
    Stylesheet("sandbox", "ao3css", "screen"),
    Stylesheet(args.fileName, "Workskins", "screen"),
)
indentLevel = 0

# code
input = open("../Raws/" + args.fileName + ".html", "r")
output = open("../Complete/" + args.fileName + ".html", "w")
buffer = []
for i in input:
    buffer.append(i.strip() + "\n")

if stripStyleTag:
    for i in range(
        buffer.index("</style>\n"), buffer.index('<style type="text/css">\n') - 1, -1
    ):
        buffer.pop(i)

if insertStylesheets:
    headEndIndex = buffer.index("</head>\n")
    for i in stylesheets:
        buffer.insert(headEndIndex, str(i))
        headEndIndex += 1
    del headEndIndex

if doHtmlTagChanges:
    indexPreface = buffer.index('<div id="preface">\n')
    buffer.pop(indexPreface)
    buffer.insert(indexPreface, '<div id="outer" class="wrapper">\n')
    buffer.insert(indexPreface, '<div id="inner" class="wrapper">\n')
    buffer.insert(indexPreface, '<div id="main" class="works-show-region">\n')
    buffer.insert(indexPreface, '<div class="wrapper">\n')
    del indexPreface
    indexEndBody = buffer.index("</body>\n")
    for i in range(3):
        buffer.insert(indexEndBody, "</div>\n")
    del indexEndBody


for line in buffer:
    if line.find("</head>") != -1 or line.find("</div>") != -1:
        indentLevel -= 1
    output.write(indent(indentLevel) + line)
    if line.find("<head") != -1 or line.find("<div") != -1:
        indentLevel += 1
