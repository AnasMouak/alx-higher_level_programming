#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        max = next(iter(a_dictionary))
        max_value = a_dictionary[max]
        for key, value in a_dictionary.items():
            if value > max_value:
                max = key
                max_value = value
        return max
