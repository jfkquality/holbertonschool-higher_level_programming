#!/usr/bin/python3
""" Base class
"""


class Base:
    """ Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ init method
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    # @staticmethod
    def int_checker(self, name, value, comparer=""):
        """ Unused int checker
        """
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

    @classmethod
    def _clear_inits(cls):
        """ clear nb objects
        """
        # for testing only, hook to clear the class-level cache.
        # print("****", cls, "*****")
        cls.__nb_objects = 0
        # cls.__nb_objects.clear

    @staticmethod
    def to_json_string(list_dictionaries):
        """ convert to jsaon string
        """
        import json
        if not list_dictionaries:
            return ("[]")
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """ Save to file
        """
        import json

        emptylist = []
        filename = cls.__name__ + ".json"

        if not list_objs:
            with open(filename, mode='w', encoding="utf-8") as myfile:
                emptylist = (Base.to_json_string(emptylist))
                myfile.write(emptylist)
        else:
            dictlist = []
            for i, obj in enumerate(list_objs):
                dictlist.append(vars(obj))
                with open(filename, mode='w', encoding="utf-8") as myfile:
                    filestring = (Base.to_json_string(dictlist))
                    filestring = (filestring.replace('_Rectangle__', ''))
                    myfile.write(filestring)
