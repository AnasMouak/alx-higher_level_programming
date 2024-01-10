#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        max = next(iter(a_dictionary))
        for keys in a_dictionary:
            if keys > max:
                max = keys
        return max
