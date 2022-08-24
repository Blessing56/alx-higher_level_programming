#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number *= -1
    else:
        number = number

    l_digit = number % 10
    print('{}'.format(l_digit))
    l_digit = str(l_digit) + str(l_digit)
    return l_digit
