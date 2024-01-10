#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        max = next(iter(a_dictionary))
        for key in a_dictionary:
            if key > max:
                max = key
        return max
