#!/usr/bin/python3
from sys import  argv
savejson = __import__('7-save_to_json_file').save_to_json_file
loadjson = __import__('8-load_from_json_file').load_from_json_file

filename = "add_item.json"

f  = loadjson(filename)

newlist = list(f)

for i, arg in enumerate(argv):
    if i == 0:
        continue
    newlist.append(arg)

savejson(newlist, filename)
