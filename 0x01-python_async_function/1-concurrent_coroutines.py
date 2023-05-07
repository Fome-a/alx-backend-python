#!/usr/bin/env python3
"""List of delay time """


import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n:int, max_delay:int) -> list[float]:
    """Returns a list of max_delay times"""
    res = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return [await res for res in asyncio.as_completed(res)]
