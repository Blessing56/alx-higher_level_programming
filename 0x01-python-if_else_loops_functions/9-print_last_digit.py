#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number *= -1
    else:
        number = number

    l_digit = number % 10
    return str(l_digit) + str(l_digit)
