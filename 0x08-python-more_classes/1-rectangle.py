#!/usr/bin/python3
class Rectangle:
    """ A rectangle object. """
    def __init__(self, width=0, height=0):
        self.width = int(width)
        self.height = int(height)

    def area(self):
        """ Calculate area of the rectangle"""
        return (self.__width * self.__height)

    # @property
    def width(self):
        """ Get private width variable """
        return self.__width

    def width(self, width):
        """ Set private width variable """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if (width < 0):
            raise ValueError("width must be >= 0")
        self.__width = (width)

    # @property
    def height(self):
        """ Get private height variable """
        return self.__height

    def height(self, height):
        """ Set private height variable """
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if (height < 0):
            raise ValueError("height must be >= 0")
        self.__height = (height)

    def my_print(self):
        """ Print a recangle of width x height '#'s """
        if self.__size == 0:
            print()
        else:
            for row in range(self.__size):
                print("#" * self.__size)

    width = property(width, width)
    height = property(height, height)
