#!/usr/bin/env python3
'''
    Function measure_time with integers n and max_delay as arguments that
    measures the total execution time for wait_n(n, max_delay), and returns
    total_time / n. Your function should return a float.
'''
import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''
        Function that measures the total execution time for
        wait_n(n, max_delay) and returns total_time / n as a float
    '''
    # Start time
    start = time.time()

    # Run the async routine
    asyncio.run(wait_n(n, max_delay))

    # End time
    end = time.time()

    # Return the total time divided by n
    return (end - start) / n
