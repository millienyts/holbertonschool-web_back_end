#!/usr/bin/env python3
''' This function graciously accepts a list of floating-point numbers as its input and then, like a diligent accountant, meticulously adds them all up, returning the grand total as a shiny float. It's like a skilled conductor harmonizing a symphony of numbers into a beautiful sum.
'''
from typing import List

def sum_list(input_list: List[float]) -> float:
    """Returns the sum of a list of floats."""
    return sum(input_list)
