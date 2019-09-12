#!/usr/bin/python3
def remove_char_at(str, n):
    i = 0
    str2 = ''
    for let in str:
        if i == n:
            i += 1
            continue
        str2 += let
        i += 1
    return (str2)
