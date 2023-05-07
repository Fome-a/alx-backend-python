#!/usr/bin/env python3
"""
 not creating an async function but using the regular function syntax to
"""

import time
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int = 0) -> asyncio.Task:
    """task"""
    task = asyncio.create_task(wait_random(max_delay))
    return task
