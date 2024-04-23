#!/usr/bin/env python3
from typing import List, Union
''' Description: takes a list mxd_lst of floats and integers and
    returns their sum as a float.
    Arguments: mxd_lst: List[Union[int, float]]
'''

def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns the sum of a list of integers and floats."""
    return sum(mxd_lst)
