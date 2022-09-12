#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):

    count = 0
    try:
        for item in my_list:
            if count < x:
                print(f'{item}', end='')
                count = count + 1
        print()
        return count
    except Indexerror:
        print(my_list)
