#!/usr/bin/python3
""" 15-main """
from models.rectangle import Rectangle
from models.square import Square

if __name__ == "__main__":
    # r1 = []

    r1 = Rectangle(10, 7, 2, 8)
    r2 = Rectangle(2, 4)
    Rectangle.save_to_file([r1, r2])
    # Rectangle.save_to_file(None)

    with open("Rectangle.json", "r") as f:
        print(f.read())


    s1 = Square(10, 7, 2)
    s2 = Square(2)
    Square.save_to_file([s1, s2])
    # Rectangle.save_to_file(None)

    with open("Square.json", "r") as f:
        print(f.read())

        # newfile = (f.read().split("_Rectangle__"))
        # print(f.read().split("_Rectangle__"))
        # print(newfile)
        # for key in newfile:
        #     print(key)
        # newfile = f.read().replace('_Rectangle__', '')
        # print(newfile)
