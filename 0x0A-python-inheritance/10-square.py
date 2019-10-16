#!/usr/bin/python3
# class BaseGeometry():
#     """Base Geometry class"""
#     def __init__(self):
#         """ Init method """
#         pass

#     def area(self):
#         """ area method """
#         raise Exception("area() is not implemented")

#     def integer_validator(self, name, value):
#         """ Integer validator method """
#         if type(value) is not int:
#             raise TypeError("{} must be an integer".format(name))
#         if value <= 0:
#             raise ValueError("{} must be greater than 0".format(name))


# class Rectangle(BaseGeometry):
#     """A rectangle sublcass of BaseGeometry."""
#     def __init__(self, width, height):
#         self.__width = self.integer_validator("width", width)
#         self.__height = self.integer_validator("height", height)

#     def __str__(self):
#         """ Print class name, dimensions """
#         return ("[{}] {}/{}".format((self.__class__.__name__),
#                 self.__width, self.__height))

#     def area(self):
#         """ Calculate area of the rectangle"""
#         return (self.__width * self.__height)

Rectangle = __import__("9-rectangle").Rectangle
class Square(Rectangle):
    """Square subclass of Rectangle"""
    def __init__(self, size):
        super().__init__(size, size)
        Square.integer_validator(self, "size", size)
        self.__size = size

    def area(self):
        """Calculate area of a square"""
        return (self.__size * self.__size)
