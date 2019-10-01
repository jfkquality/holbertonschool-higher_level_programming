#!/usr/bin/python3
def safe_print_list(mylist=[], x=0):
        y = 0
        try:
                for i in range(x):
                        print(mylist[i], end='')
                        y += 1
        except IndexError:
                pass
        print()
        return y
