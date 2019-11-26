#!/usr/bin/python3
def read_lines(filename="", nblines=0):
    with open(filename, encoding="utf-8") as myfile:
        lines = len([i for i, line in enumerate(myfile)])
        myfile.seek(0) # set file position to beginning b/c lines moves it to end
        if nblines <= 0 or nblines >= lines:
            print(myfile.read(), end='')
        else:
            while nblines > 0:
                print(myfile.readline(), end='')
                nblines -= 1
