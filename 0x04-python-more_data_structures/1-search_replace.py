#!/usr/bin/python3
def search_replace(my_list, search, replace):

    myListCopy = my_list.copy()
    for i in range(0, len(my_list)):
        if myListCopy[i] == search:
            myListCopy[i] = replace
    return myListCopy
