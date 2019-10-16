#!/usr/bin/python3
class BaseGeometry():
    """ Base Geometry class """
    def __init__(self):
        """ Init method """
        pass
    def area(self):
        """ area method """
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """ Integer validator method """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """ A rectangle object. """
    def __init__(self, width, height):
        self.__width = Rectangle.integer_validator(self, "width", width)
        self.__height = Rectangle.integer_validator(self, "height", height)


    # def __str__(self):
    #     """ Print a recangle of width x height '#'s """
    #     if self.__width == 0 or self.__height == 0:
    #         return None
    #     else:
    #         for row in range(self.__height):
    #             return ("#" * self.__width)

    # def area(self):
    #     """ Calculate area of the rectangle"""
    #     return (self.__width * self.__height)

    # @property
    # def width(self):
    #     """ Get private width variable """
    #     return self.__width

    # @width.setter
    # def width(self, width):
    #     """ Set private width variable """
    #     if not isinstance(width, int):
    #         raise TypeError("width must be an integer")
    #     if (width < 0):
    #         raise ValueError("width must be >= 0")
    #     self.__width = (width)

    # @property
    # def height(self):
    #     """ Get private height variable """
    #     return self.__height

    # @height.setter
    # def height(self, height):
    #     """ Set private height variable """
    #     if not isinstance(height, int):
    #         raise TypeError("height must be an integer")
    #     if (height < 0):
    #         raise ValueError("height must be >= 0")
    #     self.__height = (height)

    # def area(self):
    #     """ public instance attribute area """
    #     return self.__width * self.__height

    # def perimeter(self):
    #     """ public instance attribute perimeter """
    #     if (self.__width == 0 or self.__height == 0):
    #         return 0
    #     else:
    #         return 2 * self.__width + 2 * self.__height

    # def my_print(self):
    #     """ Print a recangle of width x height '#'s """
    #     if self.__width == 0 or self.__height == 0:
    #         return ""
    #     else:
    #         for row in range(self.__height):
    #             print("#" * self.__width)
