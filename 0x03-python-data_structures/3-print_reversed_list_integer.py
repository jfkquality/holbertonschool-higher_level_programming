#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return
    for item in range(len(my_list), 0, -1):
        print('{:d}'.format(my_list[item - 1]))
