#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0

    try:
        for item in my_list:
        if count < x:
            print("{:d}".format(item), end='')
            count = count + 1
        print()
        return count
    except (ValueError, TypeError):
        pass
