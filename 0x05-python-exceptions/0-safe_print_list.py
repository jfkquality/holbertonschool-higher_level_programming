#!/usr/bin/python3
def safe_print_list(mylist=[], x=0):
        try:
                for i in range(x):
                        print(mylist[i], end='')
                i += 1
        except IndexError:
                pass
        print()
        return i
