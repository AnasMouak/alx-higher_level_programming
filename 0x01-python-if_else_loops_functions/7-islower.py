#!/usr/bin/python3
def islower(c):
    alpha = 97
    while alpha < 123:
        if ord(c) >= 97 and ord(c) < 123:
            return True
        else:
            return False
    alpha += 1
