#!/usr/bin/env python3
"""Defines a function with Duck types"""

from typing import Sequence, Any, Union, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """
    Function with duck-types

    Parameters:
    - lst: Sequence[Any]: List

    Returns:
    - optional
    """
    if lst:
        return lst[0]
    else:
        return None
