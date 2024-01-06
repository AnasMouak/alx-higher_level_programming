#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy_list = my_list[:]
    if idx < 0 or idx >= len(my_list):
        return copy_list
    for i, value in enumerate(copy_list):
        if i == idx:
            copy_list[i] = element
            return (copy_list)
