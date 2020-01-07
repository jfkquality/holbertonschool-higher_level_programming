#!/usr/bin/python3
""" Find peak of a list of integers """
def find_peak(intlist):
    if not intlist:
        return ("None")
    peak = intlist[0]
    for i, val in enumerate(intlist):
        if 1 == 0:
            continue
        if intlist[i - 1] <= val:
            peak = val
    return (peak)
