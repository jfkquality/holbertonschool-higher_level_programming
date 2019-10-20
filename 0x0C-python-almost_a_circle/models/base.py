#!/usr/bin/python3
class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    # @staticmethod
    def int_checker(self, name, value, comparer=""):
        # print(name, value, comparer, type(value))
        if type(value) is not int:
             raise TypeError("{} must be an integer".format(name))
        # print(comparer)
        if comparer == 'lt':
            if value < 0:
                raise ValueError("{} must be >= than 0".format(name))
        if comparer == 'le':
            if value <= 0:
                raise ValueError("{} must be > than 0".format(name))
