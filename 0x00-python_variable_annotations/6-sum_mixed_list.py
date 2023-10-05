#!/usr/bin/env python3
'''Function sum_mixed_list that sums floats/integers in a list'''
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[float, int]]) -> float:
    '''
    Args:
        mxd_list (list): list of floats and integers

    Returns:
        float or int: sum of the list arg
    '''
    return sum(mxd_list)
