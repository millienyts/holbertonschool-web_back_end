#!/usr/bin/env python3

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Asynchronous routine that spawns wait_random n times with the specified max_delay.
    Returns a list of all the delays in ascending order.
    """
    tasks = [wait_random(max_delay) for _ in range(n)]
    return sorted(await asyncio.gather(*tasks))

if __name__ == "__main__":
    print(asyncio.run(wait_n(5, 5)))
    print(asyncio.run(wait_n(10, 7)))
    print(asyncio.run(wait_n(10, 0)))
