#!/usr/bin/env python3
'''
    Async routine called wait_n that takes in 2 int arguments (in this order):
    n and max_delay. wait_n should return a list of all the delays (float
    values). The list of the delays should be in ascending order without using
    sort() because of concurrency.
'''
import asyncio
from typing import List

# Import the wait_random function from the previous python file
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''
        Returns a list of all the delays (float values)
    '''
    # List comprehension to create a list of delays
    delays = [wait_random(max_delay) for _ in range(n)]

    # Return the list of delays in ascending order
    return [await delay for delay in asyncio.as_completed(delays)]
