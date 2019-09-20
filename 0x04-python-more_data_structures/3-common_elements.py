#!/usr/bin/python3
def common_elements(set_1, set_2):
    newset = []
    for i, val1 in enumerate(set_1):
        for j, val2 in enumerate(set_2):
            if val1 == val2:
                newset.append(val1)
    return newset
