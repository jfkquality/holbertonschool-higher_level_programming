#!/usr/bin/python3
def safe_print_list_integers(mylist=[], x=0):
        y = 0
        for i in range(x):
                try:
                        print("{:d}".format(mylist[i]), end="")
                        y += 1
                except ValueError:
                        pass
                except TypeError:
                        pass
        print()
        return y
