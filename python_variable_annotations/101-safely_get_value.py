#!/usr/bin/env python3
"""
    Safely retrieves a value from a dictionary given a key.

    Args:
        dct (Mapping): A dictionary-like object.
        key (Any): The key to retrieve the value for.
        default (Union[T, None], optional): The default value to return if the key is not found. Defaults to None.

    Returns:
        Union[Any, T]: The value corresponding to the key if found, otherwise the default value.
    """
from typing import TypeVar, Mapping, Any, Union

T = TypeVar('T')

def safely_get_value(dct: Mapping, key: Any, default: Union[T, None] = None) -> Union[Any, T]:
    if key in dct:
        return dct[key]
    else:
        return default
