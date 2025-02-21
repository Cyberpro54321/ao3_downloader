#!/bin/python3

import argparse  # https://docs.python.org/3/library/argparse.html

parser = argparse.ArgumentParser()
parser.add_argument(
    "fileName", help="Targeted Filename (without extension)", metavar="<filename>"
)
parser.add_argument("-d", "--directory", help="Install Directory")
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
input = open(args.directory + "Raws/" + args.fileName + ".html", "r")
output = open(args.directory + "Complete/" + args.fileName + ".html", "w")
buffer = []
for i in input:
    buffer.append(i.strip() + "\n")

for i in range(len(buffer) - 1, 0, -1):
    if buffer[i] == "\n":
        buffer.pop(i)

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
    buffer.insert(indexPreface, '<div class="wrapper">\n')
    buffer.insert(indexPreface, '<div id="main" class="works-show-region">\n')
    buffer.insert(indexPreface, '<div id="inner" class="wrapper">\n')
    buffer.insert(indexPreface, '<div id="outer" class="wrapper">\n')
    del indexPreface
    try:
        indexEndBody = buffer.index("</body>\n")
    except ValueError:
        for i in range(len(buffer)):
            if buffer[i].find("</body>") != -1:
                indexEndBody = i
    for i in range(3):
        buffer.insert(indexEndBody, "</div>\n")
    del indexEndBody
    buffer[buffer.index('<div id="afterword">\n')] = (
        '<div class="afterword preface group">\n'
    )
    buffer[buffer.index('<dl class="tags">\n')] = '<dl class="tags work meta group">\n'
    for i in range(len(buffer)):
        place = buffer[i].find("<h1")
        if place != -1:
            h1location = i
    h1content = buffer[h1location][buffer[h1location].find(">"):]
    buffer[h1location] = '<h1 class="title heading"' + h1content
    h1contentRaw = h1content[1:-6]
    print(h1contentRaw)
    buffer.insert(h1location, '<div class="preface group">\n')
    buffer.insert(h1location, '<div id="workskin">\n')
    buffer.insert(h1location, "</div>\n")
    buffer.insert(h1location, "</div>\n")

    try:
        h2location = buffer.index('<h2 class="toc-heading">' + h1contentRaw + "</h2>\n")
        buffer[h2location] = (
            '<h2 class="toc-heading title heading">' + h1contentRaw + "</h2>\n"
        )
    except:
        h2location = buffer.index('<div id="chapters" class="userstuff">\n')
    buffer.pop(h2location - 2)

buffer.append("<!-- This file written by AO3 Downloader version 1.0.5.2 -->")


for line in buffer:
    if line.find("</head>") != -1 or line.find("</div>") != -1:
        indentLevel -= 1
    output.write(indent(indentLevel) + line)
    if line.find("<head") != -1 or line.find("<div") != -1:
        indentLevel += 1
