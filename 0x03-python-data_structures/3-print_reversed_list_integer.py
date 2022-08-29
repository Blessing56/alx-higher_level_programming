#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    my_lst = []
    for i in range(len(my_list)):
        my_lst = my_list[((len(my_list) - 1) - i)]
        print('{:d}'.format(my_lst))
