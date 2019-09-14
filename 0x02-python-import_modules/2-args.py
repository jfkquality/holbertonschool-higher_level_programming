#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argslen = len(sys.argv)
    if argslen == 1:
        print("0 arguments.")
    elif argslen == 2:
        print("1 argument:")
    else:
        print("{:d} arguments:".format(argslen-1))

    if argslen > 1:
        for i, arg in enumerate(sys.argv):
            if i == 0:
                continue
            print("{:d}: {}".format(i, arg))
