#!/usr/bin/env python3
"""Defines a function sum_mixed_list"""

from typing import List, Union

def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """
    Calculate the sum of a list of floats and integers.

    Parameters:
    - mxd_list (List[float, int]): A list of floats.

    Returns:
    - float: The sum of the mxd_list.
    """
    return sum(mxd_list)
