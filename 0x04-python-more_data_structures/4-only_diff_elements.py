#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    set1list = list(set_1)
    set2list = list(set_2)
    bothsets = set1list + set2list
    newset = []
    for i, val1 in enumerate(bothsets):
        if val1 not in newset:
            newset.append(val1)
    return set(newset)
