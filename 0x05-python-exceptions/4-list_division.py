#!/usr/bin/python3
def list_division(list1, list2, listlen):
        newlist = [None] * listlen
        try:
                for i in range(listlen):
                        newlist[i] = (list1[i]) / (list2[i])
        except ZeroDivisionError:
                newlist[i] = 0
                print("division by 0")
        except ValueError:
                newlist[i] = 0
                print("wrong type")
        except TypeError:
                newlist[i] = 0
                print("wrong type")
        # finally:
        return newlist
