#!/usr/bin/python3
""" 0-main """
from models.base import Base

if __name__ == "__main__":

    b1 = Base('abc')
    # print(type(b1.id))
    print(b1.id)

    b2 = Base()
    # print(type(b2.id))
    print(b2.id)

    b3 = Base()
    # print(type(b3.id))
    print(b3.id)

    b4 = Base(12)
    # print(type(b4.id))
    print(b4.id)

    b5 = Base()
    # print(type(b5.id))
    print(b5.id)
