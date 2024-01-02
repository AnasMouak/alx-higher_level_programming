#!/usr/bin/python3
for d in range(10):
    for w in range(d + 1, 10):
        if d != 8 or w != 9:
            print("{}{}".format(d, w), end=', ')
        else:
            print("{}{}".format(d, w))
