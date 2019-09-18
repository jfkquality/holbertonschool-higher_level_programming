#!/usr/bin/python3
def max_integer(my_list=[]):
    myMax = my_list[0]
    for num in my_list:
        if myMax < num:
            myMax = num
    return myMax
