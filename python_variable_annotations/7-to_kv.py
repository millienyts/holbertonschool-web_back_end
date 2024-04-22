#!/usr/bin/env python3
from typing import Tuple, Union

def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple with string k and the square of int/float v."""
    return (k, v ** 2)
