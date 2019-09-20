#!/usr/bin/python3
def uniq_add(my_list=[]):
    sumlist = []
    sum = 0
    for i, val1 in enumerate(my_list):
        if val1 not in sumlist:
            sumlist.append(val1)
    for val2 in sumlist:
        sum += int(val2)
    return sum
