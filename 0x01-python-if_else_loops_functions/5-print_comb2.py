#!/usr/bin/python3
for i in range(0, 98):
    if i < 10:
        i = '0' + str(i)
    print('{}'.format(i), end=", ")
print(99)
