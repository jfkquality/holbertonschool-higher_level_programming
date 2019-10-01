#!/usr/bin/python3
def safe_print_list(mylist=[], x=0):
        try:
                for i in range(x):
                        print(mylist[i], end='')
                print()
                i += 1
        except:
                print()
                pass
        return i
