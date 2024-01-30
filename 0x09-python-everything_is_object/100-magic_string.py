#!/usr/bin/python3
def magic_string(iter_count=[0]):
    iter_count[0] += 1
    return "BestSchool" + ", BestSchool" * (iter_count[0] - 1)
