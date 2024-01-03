#!/usr/bin/env python3
"""Defines a function to_kv"""

from typing import Union, Tuple

def to_kv(k: str, v: Union[float, int]) -> Tuple[str, float]:
    """
    Create tuple with k and the square of int/float v.

    Parameters:
    - k: str
    - v: int/float

    Returns:
    - tuple: k, sq(v)
    """
    return (k, (v**2))
