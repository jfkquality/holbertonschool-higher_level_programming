#!/usr/bin/python3
def list_division(list1, list2, listlen):
        newlist = [None] * listlen
        try:
                for i in range(listlen):
                        try:
                                newlist[i] = (list1[i]) / (list2[i])
                        except ZeroDivisionError:
                                newlist[i] = 0
                                print("division by 0")
                        except TypeError:
                                newlist[i] = 0
                                print("wrong type")
                        except IndexError:
                                newlist[i] = 0
                                print("out of range")
        finally:
                return newlist
