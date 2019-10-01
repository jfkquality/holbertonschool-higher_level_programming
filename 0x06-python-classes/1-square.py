#!/usr/bin/python3

cls = type('Square', (object,), {'__doc__': 'class created by type'})

class Square:
    """ A square object. """
    # __size = None
    def __init__(self, size):
        self.__size = size
