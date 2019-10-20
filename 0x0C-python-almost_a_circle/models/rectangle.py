#!/usr/bin/python3
from models.base import Base

class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        # self.int_checker("width", width, "le")
        # self.int_checker("height", height, "le")
        # self.int_checker("x", x, "lt")
        # self.int_checker("y", y, "lt")
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Get private width variable """
        return self.__width

    @width.setter
    def width(self, width):
        """ Set private width variable """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if (width <= 0):
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """ Get private height variable """
        return self.__height

    @height.setter
    def height(self, height):
        """ Set private height variable """
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if (height <= 0):
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, x):
        """ Set private x variable """
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if (x < 0):
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, y):
        """ Set private y variable """
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if (y < 0):
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        """ Calculate area of the rectangle"""
        return (self.__width * self.__height)

    def display(self):
        """ Print a recangle of width x height '#'s """
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            print('\n' * self.__y, end='')
            for row in range(self.__height):
                print(" " * self.__x, end='')
                print("#" * self.__width)

    def __str__(self):
        """ Print class name, dimensions """
        return ("[{}] ({}) {}/{} - {}/{}".format((self.__class__.__name__),
                self.id, self.__x, self.__y, self.__width, self.__height))
