#!/usr/bin/env python3
from typing import Tuple, List, Any

def zoom_array(lst: Tuple[Any], factor: int = 2) -> List[Any]:
    zoomed_in: List[Any] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)  # Corrected to pass an integer as factor
