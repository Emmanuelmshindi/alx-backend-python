#!/usr/bin/env python3
"""Define function to safely get value"""

from Typing import TypeVar, Mapping, Any, Union


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union(Any, T):
    """
    Function to safely get values
    """
    if key in dct:
        return dct[key]
    else:
        return default
