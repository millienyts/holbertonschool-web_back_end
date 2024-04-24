#!/usr/bin/env python3
"""
    Import wait_random from a previously defined Python module.
    Define an asynchronous function called wait_n that takes two integer arguments: n and max_delay.
    This function spawns n instances of wait_random with the specified max_delay.
    wait_n returns a list containing all the delays (float values).
    The list is sorted in ascending order without using the sort() method due to concurrency.
"""
from basic_async_syntax import wait_random
import asyncio
from typing import List


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''
        Returns list of delays in floats ascending order
    '''
    results = []
    tasks = [asyncio.ensure_future(wait_random(max_delay)) for _ in range(n)]
    while tasks:
        done, tasks = await asyncio.wait(
            tasks, return_when=asyncio.FIRST_COMPLETED
            )
        for task in done:
            results.append(await task)
    return results
