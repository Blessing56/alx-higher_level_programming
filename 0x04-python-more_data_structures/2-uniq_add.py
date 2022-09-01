#!/usr/bin/python3

def uniq_add(my_list=[]):
    result = 0
    lst = []
    for i in my_list:
        if i in lst:
            continue
        else:
            lst.append(i)
            result += i
    return result
