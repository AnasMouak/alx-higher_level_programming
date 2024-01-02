#!/usr/bin/python3
def uppercase(str):
    for alpha in str:
        if alpha >= 'a' and alpha <= 'z':
            alpha = chr(ord(alpha) - ord('a') + ord('A'))
        print("{}".format(alpha), end="")
    print()
