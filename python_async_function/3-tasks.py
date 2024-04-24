#!/usr/bin/env python3

import asyncio

task_wait_random = __import__('3-tasks').task_wait_random

def test(max_delay: int) -> None:
    """
    Asynchronous function to test task_wait_random.
    """
    task = task_wait_random(max_delay)
    asyncio.run(task)
    print(task.__class__)

if __name__ == "__main__":
    asyncio.run(test(5))
