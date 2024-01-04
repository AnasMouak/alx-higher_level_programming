#!/usr/bin/python3
import sys

if __name__ == "__main__":

    if len(sys.argv) - 1 == 0:
        print("0 arguments.")

    else:
        if len(sys.argv) - 1 == 1:
            print("1 argument:")
        else:
            print("{} arguments:".format(len(sys.argv) - 1))
        for c in range(1, len(sys.argv)):
            print("{}: {}".format(c, sys.argv[c]))
