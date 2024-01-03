#!/usr/bin/python3
i = 0
alpha = 122
while alpha >= 97:
    print("{}".format(chr(alpha - i)), end="")
    i = 32 if i == 0 else 0
    alpha -= 1
