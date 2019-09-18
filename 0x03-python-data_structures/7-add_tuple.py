#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuplista = list(tuple_a)
    tuplistb = list(tuple_b)
    newlist = []
    if len(tuplista) < 2:
        if len(tuplista) == 0:
            tuplista.append(0)
        tuplista.append(0)
    if len(tuplistb) < 2:
        if len(tuplistb) == 0:
            tuplistb.append(0)
        tuplistb.append(0)

    for val in range(0, 2):
        newlist.append(tuplista[val] + tuplistb[val])
    newtuple = tuple(newlist)

    # tuple(map(lambda x, y: x + y, tuple_a, tuple_b))

    return (newtuple)
