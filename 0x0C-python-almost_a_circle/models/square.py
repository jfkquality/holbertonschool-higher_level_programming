#!/usr/bin/python3
"""Square subclass of Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square subclass of Rectangle"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(id=id, x=x, y=y, width=size, height=size)
        # super().__init__(width, height, x, y, id)
        # self.__size = size
        self.size = size
        self.x = x
        self.y = y

    def __str__(self):
        """ Print super class name, dimensions """
        return ("[{}] ({}) {}/{} - {}".
                format((self.__class__.__name__),
                       self.id, self.x, self.y, self.size))

    @property
    def size(self):
        """ Get private size variable """
        return self.__width

    @size.setter
    def size(self, v):
        """ Set private width variable """
        if type(v) is not int:
            raise TypeError("width must be an integer")
        if (v <= 0):
            raise ValueError("width must be > 0")
        self.__width = v
        self.__height = v

    def update(self, *args, **kwargs):
        """ Update attributes """
        if len(args) > 0:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.size = arg
                if i == 2:
                    self.x = arg
                if i == 3:
                    self.y = arg
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """Convert attr's to dict"""
        d = {}
        d["id"] = self.id
        d["size"] = self.width
        d["x"] = self.x
        d["y"] = self.y
        return d
