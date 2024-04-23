#!/usr/bin/env python3
"""
    Safely retrieves the first element of a sequence.

    Args:
        lst (Sequence[Any]): A sequence of elements.

    Returns:
        Optional[Any]: The first element of the sequence if it exists, otherwise None.
    """
from typing import Sequence, Any, Optional

def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    if lst:
        return lst[0]
    else:
        return None