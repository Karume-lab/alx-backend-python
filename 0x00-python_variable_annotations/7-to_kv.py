#!/usr/bin/env python3
'''Function to_kv that sums floats/integers in a list'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''
    Args:
        mxd_list (list): list of floats and integers

    Returns:
        float: sum of the list args
    '''
    return (k, v ** 2)
