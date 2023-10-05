#!/usr/bin/env python3
'''Function make_multiplier that multiplies a float by a multiplier'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
    Args:
        multiplier (float): multiplier number

    Returns:
        function: multiplies a float by a multiplier
    '''
    return lambda mult: mult * multiplier
