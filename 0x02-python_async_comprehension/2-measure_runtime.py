#!/usr/bin/env python3
"""
Run time for four parallel comprehensions
"""


import asyncio
import time
"""Run time for four parallel comprehensions"""


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    returns the total runtime for 4 asynchronous comprehension running in
    parallel
    """
    start = time.perf_counter()
    result = await asyncio.gather(*(async_comprehension() for _ in range(4)))
    total_time = time.perf_counter() - start
    return 