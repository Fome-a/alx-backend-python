#!/usr/bin/env python3
"""List of delay time """


import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n:int, max_delay:int) -> list[float]:
    """Returns a list of max_delay times"""
    res = await asyncio.gather(*(wait_random(max_delay)for i in range (n)))
    sorted_list = sorted(res)
    return sorted_list
