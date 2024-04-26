#!/usr/bin/env python3
"""
    Get first element of sequence.
"""
from typing import Sequence, Any, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """
        get frist element of sequence or return none
    """
    if lst:
        return lst[0]
    else:
        return None
