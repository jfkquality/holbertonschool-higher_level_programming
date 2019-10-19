#!/usr/bin/python3
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Square subclass of Rectangle"""
    def __init__(self, size):
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """ Print super class name, dimensions """
        return ("[{}] {}/{}".format(Rectangle.__name__, self.__size, self.__size))
