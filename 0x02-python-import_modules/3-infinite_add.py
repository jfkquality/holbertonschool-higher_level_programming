#!/usr/bin/python3
import sys

argslen = len(sys.argv)
if argslen == 1:
    print("0")
else:
    sum = 0
    for i, arg in enumerate(sys.argv):
        if i == 0:
            continue
        sum += int(arg)
    print(sum)
