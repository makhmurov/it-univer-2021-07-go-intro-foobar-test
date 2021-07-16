#!/usr/bin/env python3

import sys

MSG_FOO = "Foo"
MSG_BAR = "Bar"

def check_item(number):
    if number % 3 == 0:
        msg = MSG_BAR
    else:
        msg = MSG_FOO
    print('{:d} {:s}'.format(number, msg))
    return None

if __name__ == "__main__":
    maximum = 0
    if len(sys.argv) > 1:
        maximum = int(sys.argv[1])
    else:
        print("Input number greater than 0: ")
        maximum = int(input())
    map_it = filter(check_item, range(1, maximum + 1))
    list(map_it)