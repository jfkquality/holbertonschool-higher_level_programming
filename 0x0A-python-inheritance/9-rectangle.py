#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """A rectangle sublcass of BaseGeometry."""
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def __str__(self):
        """ Print class name, dimensions """
        return ("[{}] {}/{}".format((self.__class__.__name__),
                self.__width, self.__height))

    def area(self):
        """ Calculate area of the rectangle"""
        return (self.__width * self.__height)
