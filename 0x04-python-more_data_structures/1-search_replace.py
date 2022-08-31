#!/usr/bin/python3
def search_replace(my_list, search, replace):
    lst = my_list[:]
    for i in range(len(my_list) - 1):
        if lst[i] == search:
            lst[i] = replace
    return lst
