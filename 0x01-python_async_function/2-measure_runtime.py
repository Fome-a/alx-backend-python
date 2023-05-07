#!/usr/bin/env python3
"""
Creating a measure_time function
"""
import random
import asyncio
from typing import List
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int = 10) -> float:
    """measure the runtime"""
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapse = time.perf_counter() - start
    return elapse / n