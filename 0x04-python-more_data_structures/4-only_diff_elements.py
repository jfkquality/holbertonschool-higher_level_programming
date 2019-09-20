#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    set1list = list(set_1)
    set2list = list(set_2)
    bothsets = set1list + set2list
    print ("BOTH SETS", format(bothsets))
    newset = []
    # for h in set_2:
    #     bothsets.append(set_2[h])
    for i, val1 in enumerate(bothsets):
        # for ((i, val2 in enumerate(set_2)) or (k, val3 in enumerate(newset))):
        for j, val2 in enumerate(bothsets[1]):
            if val1 == val2:
                bothsets.remove(bothsets[i])
                # for val3 in newset:
                #     if val1 != val3:
                #         newset.append(val1)
                #     if val2 != val3:
                #         newset.append(val2)
    return newset
