#!/usr/bin/python3
def weight_average(my_list=[]):
    """a function that returns the weighted average of all integers"""
    if not my_list:
        return 0
    tot_score = 0
    tot_weight = 0
    
    for score, weight in my_list:
        tot_score += score * weight
        tot_weight += weight
    return (tot_score / tot_weight)
