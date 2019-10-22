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

    @classmethod
    def _clear_inits(cls):
        # for testing only, hook to clear the class-level cache.
        # print("****", cls, "*****")
        cls.__nb_objects = 0
        # cls.__nb_objects.clear

    @staticmethod
    def to_json_string(list_dictionaries):
        import json
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        import json
        # filename = self.__class__.__name__ + ".json"
        filename = "file.json"
        # print(list_objs)
        for i, obj in enumerate(list_objs):
            # print(obj.__dict__.keys())
            # print(vars(obj))
            # print(vars(obj))
            # print(val)

        # with open(filename, mode='w', encoding="utf-8") as myfile:
            for obj in list_objs:
                for i, attr in vars(obj):
                    print(attr)
                # lststr = cls.to_json_string(obj)
                # lststr = (cls.to_json_string((obj)))
                # print(json.JSONEncoder.default(cls, lststr))
                # lstdict = cls.to_dictionary()
                # print(lststr)
                # for obj in list_objs:
                # json.dump(obj, myfile)


        # for obj in list_objs:
            # print(obj)
            # print(json.dumps(obj))
            # print(list_str)
            # print(type(list_str))
            # print(json.loads(list_str))

        # return (json.loads(list_objs))
