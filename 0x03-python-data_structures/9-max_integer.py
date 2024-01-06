#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    max = my_list[0]
    for i in my_list:
        if my_list[i] > max:
            max = my_list[i]
            return max
