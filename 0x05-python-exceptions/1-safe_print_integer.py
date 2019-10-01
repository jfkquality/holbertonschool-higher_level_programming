#!/usr/bin/python3
def safe_print_integer(value):
        y = 0
        try:
                print("{:d}".format(value))
        except:
                return False
        return True
