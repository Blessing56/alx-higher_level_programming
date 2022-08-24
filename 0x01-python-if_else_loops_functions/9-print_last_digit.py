#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number *= 1
    else:
        number = number

    l_digit = number % 10
    l_digit = "0" + str(l_digit)
    return l_digit
