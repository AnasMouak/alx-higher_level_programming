#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    c_dict = a_dictionary.copy()
    for keys in c_dict:
        c_dict[keys] *= 2
    return c_dict
