#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    return [i % 2 == 0 for i in range(len(my_list))]
