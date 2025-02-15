#!/bin/python3

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("fileName", help="Targeted Filename (without extension)", metavar="<filename>")
args = parser.parse_args()

class Stylesheet:
    def __init__(self, file, folder, media):
        self.file = file
        self.folder = folder
        self.media = media
    def __str__(self):
        return f'  <link rel="stylesheet" type="text/css" media="{self.media}" href="../{self.folder}/{self.file}.css">\n'
def indent(level):
    temp = ""
    for i in range(level):
        temp = temp+"  "
    return temp

# variables
stripStyleTag = True
insertStylesheets = True
a = 0
styleStartFound = False
styleEndFound = False
headEndFound = False
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
    Stylesheet("25-media-midsize", "ao3css", "only screen and (max-width: 62em), handheld"),
    Stylesheet("26-media-narrow", "ao3css", "only screen and (max-width: 62em), handheld"),
    Stylesheet("27-media-aural", "ao3css", "speech"),
    Stylesheet("28-media-print", "ao3css", "print"),
    Stylesheet("sandbox", "ao3css", "screen"),
    Stylesheet(args.fileName, "Workskins", "screen")
)
buffer1 = []
buffer2 = []
indentLevel = 0

# code
input = open("../Raws/"+args.fileName+".html", "r")
output = open("../Complete/"+args.fileName+".html", "w")
buffer1.clear()
for i in input:
    buffer1.append(i.strip()+"\n")

#for i in input:
#    writeLine = True;
#    buffer = str(i)
#    if stripStyleTag:
#        if not styleStartFound:
#            if i.find('type="text/css">') != -1:
#                styleStartFound = True
#        if styleStartFound and not styleEndFound:
#            writeLine = False
#            if i.find('</style>') != -1:
#                styleEndFound = True
#    if insertStylesheets and not headEndFound:
#        if i.find('</head>') != -1:
#            headEndFound = True
#            for j in stylesheets:
#                output.write(str(j))
#
#    if writeLine == True:
#        output.write(buffer)
#    a += 1
print(a)
for i in buffer1:
    if i.find("</head>") != -1 or i.find("</body>") != -1 or i.find("</div>") != -1:
        indentLevel -= 1
    buffer2.append(indent(indentLevel)+i)
    if i.find("<head") != -1 or i.find("<body") != -1 or i.find("<div") != -1:
        indentLevel += 1

for i in buffer2:
    output.write(i)

#print(f.readline())
#print(f.readline())
#print(type(f.readline()))
#print(type(f))
#print(args.fileName)
