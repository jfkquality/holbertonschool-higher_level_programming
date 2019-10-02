#!/usr/bin/python3
class Square:
    """ A square object. """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = int(size)

    def area(self):
        """ Calculate area of the square"""
        return (self.__size * self.__size)

    def get_size(self):
        """ Get private size variable """
        return self.__size

    def set_size(self, size):
        """ Set private size variable """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = (size)

    size = property(get_size, set_size)
