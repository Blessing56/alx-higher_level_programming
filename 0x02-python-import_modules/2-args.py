#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    args = argv[1:]

    print('{} '.format(len(args), end=""))

    if len(args) == 0:
        print('arguments.')
    else:
        print('arguments:')

    for i in range(len(arg)):
            print('{}: {}'.format(i+1, arg[i]))
