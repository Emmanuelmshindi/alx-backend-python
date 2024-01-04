#!/usr/bin/env python3
"""Define method to tcalculate length of elements"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculate the length of each element in the input list.

    Parameters:
    - lst: Iterable[Sequence]

    Returns:
    - List[Tuple[Sequence, int]]
    """
    return [(i, len(i)) for i in lst]
