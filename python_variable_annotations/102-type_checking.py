#!/usr/bin/env python3
"""
    Validation of task code in intranet
"""
from typing import Tuple, List, Any


def zoom_array(lst: Tuple[Any], factor: int = 2) -> List[Any]:
    """Repeats elements in a list 'factor' times.
        Args:
        lst: The input list.
        factor (int, optional): Number of times to repeat elements

    Returns:
        List with elements repeated 'factor' times.
  """
    zoomed_in: List[Any] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
