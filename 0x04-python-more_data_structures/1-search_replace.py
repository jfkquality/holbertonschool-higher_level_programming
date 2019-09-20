#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newlist = []
    for i, val in enumerate(my_list):
            if val == search:
                newlist.append(replace)
            else:
                newlist.append(my_list[i])
    return newlist
