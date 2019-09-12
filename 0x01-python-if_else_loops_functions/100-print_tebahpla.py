#!/usr/bin/python3
for let in range(ord('z'), ord('a'), -2):
    print("{}".format(chr(let) + chr(let-33)), end='')
