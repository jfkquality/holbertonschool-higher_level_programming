#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ A rectangle object. """
    def __init__(self, width, height):
        Rectangle.integer_validator(self, "width", width)
        self.__width = width
        Rectangle.integer_validator(self, "height", height)
        self.__height = height

        # try:
        #      Rectangle.integer_validator(self, "width", width)
        #      self.__width = width
        # except Exception as e:
        #     print(e)
        # try:
        #    Rectangle.integer_validator(self, "height", height)
        #    self.__height = height
        # except Exception as e:
        #     print(e)
