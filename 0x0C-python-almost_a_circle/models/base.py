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
        """ JSON strong to file:
        writes the JSON string representation of list_objs to a file:
        """
        # Why doesn't this work for Squares? Get Rectangle AND Square attrs!
        import json

        dictlist = []
        filename = cls.__name__ + ".json"

        if not list_objs:
            with open(filename, mode='w') as myfile:
                dictlist = (Base.to_json_string(dictlist))
                myfile.write(dictlist)
        else:
            for i, obj in enumerate(list_objs):
                dictlist.append(vars(obj))
            with open(filename, mode='w') as myfile:
                filestring = (Base.to_json_string(dictlist))
                filestring = (filestring.replace("_Rectangle__", ''))
                filestring = (filestring.replace("_Square__", ''))
                # filestring = (filestring.replace("_"+cls.__name__+"__", ''))
                myfile.write(filestring)
                # json.dump(filestring, myfile)

    @staticmethod
    def from_json_string(json_string):
        """ JSON string list of dicts. return to list of json strings. """
        import json

        if not json_string:
            return ([])
        else:
            return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set:"""
        if cls.__name__ == "Rectangle":
            dummy = cls(width=1, height=1, x=0, y=0)
        else:
            dummy = cls(size=1, x=0, y=0)
            dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """File to instances: returns a list of instances"""

        import json

        dictlist = []
        instlist = []
        filename = cls.__name__ + ".json"
        with open(filename, mode='r', encoding="utf-8") as f:
            jsondict = json.load(f)

        for obj in jsondict:
            instlist.append(cls.create(**obj))

        return instlist

        #     for jsonstr in f:
        #         print(type(jsonstr), jsonstr)
        #         dictlist.append(Base.from_json_string(jsonstr))
        # for d in dictlist:
        #     print(type(d), d)
        #     instlist.append(Base.create(**d))
        # return dictlist

        # @classmethod
        # def save_to_file_csv(cls, list_objs):

        # @classmethod
        # def load_from_file_csv(cls):
