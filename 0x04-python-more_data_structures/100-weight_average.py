#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    n = len(my_list)
    weighted_sum = sum(my_list[i][0] * my_list[i][1] for i in range(n))
    total_weights = sum(my_list[i][1] for i in range(n))
    if total_weights == 0:
        return 0
    average = weighted_sum / total_weights
    return average
