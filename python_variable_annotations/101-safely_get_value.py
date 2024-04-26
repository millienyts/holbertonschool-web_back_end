#!/usr/bin/env python3
"""
    Safely retrieves a value from a dictionary given a key.
"""
from typing import TypeVar, Mapping, Any, Union

T = TypeVar('T')


def safely_get_value(
        dct: Mapping, key: Any, default: Union[T, None] = None
        ) -> Union[Any, T]:
    """
        Returns a dict value or none if no key found
    """
    if key in dct:
        return dct[key]
    else:
        return default
