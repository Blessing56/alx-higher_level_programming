#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0

    for item in my_list:
        try:
            if count < x:
                print("{:d}".format(item), end='')
                count = count + 1
    except (ValueError, TypeError):
        continue
    print()
    return count
