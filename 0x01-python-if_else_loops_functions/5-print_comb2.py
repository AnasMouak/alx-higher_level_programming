#!/usr/bin/python3
for d in range(100):
    if d != 99:
        print("{:02}".format(d), end=', ')
    else:
        print("{}".format(d))
