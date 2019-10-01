#!/usr/bin/python3
import sys
def safe_print_integer(value):
        except Exception as ex:
                print("Exception: {}".format(ex), file=sys.stderr)
