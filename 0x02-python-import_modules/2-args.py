#!/usr/bin/python3
def args(arg):
    print('{} arguments:'.format(len(arg)))
    for i in range(len(arg)):
        print('{}: {}'.format((i + 1), arg[i]))
