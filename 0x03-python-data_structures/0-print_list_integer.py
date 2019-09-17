#!/usr/bin/python3


def print_list_integer(my_list=[]):

    """My print list function

    Args:
        my_list: the list

    Returns:
        Nothing.
    """

    for item in my_list:
        print('{}'.format(my_list[item - 1]))
