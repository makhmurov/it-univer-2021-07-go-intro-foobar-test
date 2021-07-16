#!/usr/bin/env python3

import sys

G_RECUSRION_LIMIT = 2**11

sys.setrecursionlimit(G_RECUSRION_LIMIT)

MSG_FOO = "Foo"
MSG_BAR = "Bar"

def foo_bar(counter, maximum):
    if counter > maximum:
        return
    if counter % 3 == 0:
        msg = MSG_BAR
    else:
        msg = MSG_FOO
    print('{:d} {:s}'.format(counter, msg))
    foo_bar(counter + 1, maximum)

if __name__ == "__main__":
    maximum = 0
    if len(sys.argv) > 1:
        maximum = int(sys.argv[1])
    else:
        print("Input number greater than 0: ")
        maximum = int(input())
    if maximum < 1:
        print("Incorrect input! Number must be greater than 0.")
    elif maximum >= G_RECUSRION_LIMIT:
        print("Sorry, too big value. Please use numbers up to {:d}. It is recursion limit.".format(G_RECUSRION_LIMIT))
    else:
        foo_bar(1, maximum)