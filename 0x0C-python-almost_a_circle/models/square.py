#!/usr/bin/python3
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square subclass of Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        # super().__init__(id=id, x=x, y=y, width= size, height=size)
        super().__init__(size, size, x, y, id)
        # self.__size = size
        self.size = size
        self.x = x
        self.y = y


    def __str__(self):
        """ Print super class name, dimensions """
        # print(self.x, self.y, self.size, self.id)
        return ("[{}] ({}) {}/{} - {}".format((self.__class__.__name__),
                                self.id, self.x, self.y, self.size))

    @property
    def size(self):
        """ Get private size variable """
        return self.__width

    @size.setter
    def size(self, width):
        """ Set private width variable """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if (width <= 0):
            raise ValueError("width must be > 0")
        self.__width = width
        self.__height = width

    def update(self, *args, **kwargs):
        if len(args) > 0:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.width = arg
                if i == 2:
                    self.x = arg
                if i == 3:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        d = {}
        d["id"] = self.id
        d["size"] = self.width
        d["x"] = self.x
        d["y"] = self.y
        return d

