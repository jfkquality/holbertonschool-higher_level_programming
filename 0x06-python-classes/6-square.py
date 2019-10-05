#!/usr/bin/python3
class Square:
    """ A square object. """
    def __init__(self, size=0, position=(0, 0)):
        self.size = int(size)
        self.__position = position

    def area(self):
        """ Calculate area of the square"""
        return (self.__size * self.__size)

    def get_size(self):
        """ Get private size variable """
        return self.__size

    def set_size(self, size):
        """ Set private size variable """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = (size)

    def get_position(self):
        """ Get private position tuple variable """
        return self.__position

    def set_position(self, value):
        """ Set private position tuple variable """
        if not (isinstance(position, tuple) or len(position) != 2 or
                all(i > 0 for i in position)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position(value, value)

    def my_print(self):
        """ Print a square of size x size '#'s """
        # if self.__size == 0:
        #     print()
        # else:
        print("\n" * self.__position[1], end='')
        for row in range(self.__size):
            print(" " * self.__position[0], end='')
            print("#" * self.__size, end='')
            print()

    size = property(get_size, set_size)
    position = property(get_position, set_position)
