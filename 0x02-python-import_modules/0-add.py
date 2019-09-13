#!/usr/bin/python3

from add_0 import add
# add = __import__('add-0').add

a = 1
b = 2
# print(add(a, b))
print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))
