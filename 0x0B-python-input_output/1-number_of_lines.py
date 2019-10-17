#!/usr/bin/python3
def number_of_lines(filename=""):
    with open(filename, encoding="utf-8") as myfile:
        lines = len([i for i, line in enumerate(myfile)])
        return (lines)
