#!/usr/bin/env python3


"""An asynchronous function that waits for a random delay """

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Maximum delay"""
    i: float = random.uniform(0, max_delay)
    await asyncio.sleep(i)
    return i
