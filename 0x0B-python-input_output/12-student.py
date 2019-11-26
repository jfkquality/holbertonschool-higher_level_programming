#!/usr/bin/python3
class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        # print(type(attrs), self)
        # print(dir(self))
        # print()
        if type(attrs) == list:
            attrdict = {}
            # for i, attr in enumerate(attrs):
            for i in attrs:
                print(self.first_name)
                # print(self.__getattribute__.i)
            # return(attrdict)
            # if all(type(i) ==  str for i in attrs ):
            #     return(self.i)
        else:
            # print(type(attrs))
            return(self.__dict__)
