#!/usr/bin/env python3

import asyncio
from typing import List

wait_n = __import__('1-concurrent_coroutines').wait_n

def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay) and returns total_time / n.
    """
    start_time = asyncio.get_event_loop().time()
    asyncio.run(wait_n(n, max_delay))
    end_time = asyncio.get_event_loop().time()
    total_time = end_time - start_time
    return total_time / n

if __name__ == "__main__":
    n = 5
    max_delay = 9
    print(measure_time(n, max_delay))
