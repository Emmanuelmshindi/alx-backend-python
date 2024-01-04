#!/usr/bin/env python3
"""Defines a function make_multiplier"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a function that multiplies a float by the given multiplier.

    Parameters:
    - multiplier: float

    Returns:
    - function: Callable[[float], float]
    """
    def multiplier_function(x: float) -> float:
        return x * multiplier

    return multiplier_function
