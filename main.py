#!/bin/python3

import argparse
parser = argparse.ArgumentParser()
parser.add_argument("fileName", help="Targeted Filename (without extension)", metavar="<filename>")
args = parser.parse_args()

# variables
stripStyleTag = True;
insertStylesheets = True;

# code
file = open("../Raws/"+args.fileName+".html", "r")
a = 0
for i in file:
    if i.find('type="text/css">') != -1:
        print("lol")
    else:
        print(i.replace(" ", ""))
    a += 1
print(a)


#print(f.readline())
#print(f.readline())
#print(type(f.readline()))
#print(type(f))
#print(args.fileName)
