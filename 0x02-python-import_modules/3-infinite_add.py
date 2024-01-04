#!/usr/bin/python3
import sys

if __name__ == "__main__":

    if len(sys.argv) - 1 == 0:
        print("0")
    else:
        add = 0
        for c in range(1, len(sys.argv)):
            add += int(sys.argv[c])
        print("{}".format(int(add)))
