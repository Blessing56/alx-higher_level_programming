#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    length = []
    try:
        for item in list(map(lambda x,y: x / y, my_list_1, my_list_2)):
            length.append(item)
    except (ValueError, TypeError):
        print("wrong type")
    except ZeroDivisionError:
        print("division by 0")
    except IndexError:
        print("out of range")
    return length
