#!/usr/bin/env python3
'''
Import wait_random from 0-basic_async_syntax.


'''
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''
        returns asyncio.task from wait_random()
    '''
    return asyncio.create_task(wait_random(max_delay))
