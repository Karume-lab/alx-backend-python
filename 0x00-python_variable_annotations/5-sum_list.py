#!/usr/bin/env python3
'''Function sum_list that sums floats in a list'''
from typing import List


def sum_list(input_list: List[float]) -> float:
    '''
    Args:
        input_list (list): list of floats

    Returns:
        float: sum of the list of floats
    '''
    return sum(input_list)
