#!/usr/bin/python3
def print_sorted_dictionary(adict):
    for i in sorted(adict.keys()):
        print("{}: {}".format(i, adict[i]))
