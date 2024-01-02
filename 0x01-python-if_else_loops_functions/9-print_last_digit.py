#!/usr/bin/python3
def print_last_digit(number):
    last_d = abs(number) % 10
    print(last_d, end="")
    return(last_d)
