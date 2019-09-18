#!/usr/bin/python3
def no_c(my_string):
    newstring = []
    for char in range(len(my_string)):
        # print(newstring)
        if my_string[char] == "c" or my_string[char] == "C":
            # print (len(newstring), char)
            newstring = my_string[len(newstring):char] + my_string[char + 1:]
    # print(newstring)
    return (newstring)
