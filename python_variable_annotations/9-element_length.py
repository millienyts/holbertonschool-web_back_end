#!/usr/bin/env python3
''' Description: Annotate the below function’s parameters and
                 return values with the appropriate types
    Arguments: lst: Iterable[Sequence]
'''
from typing import Iterable, Sequence, List, Tuple

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a list of tuples containing elements and their lengths."""
    return [(i, len(i)) for i in lst]
