"""An asynchronous function that waits for a random delay """
import asyncio
import random

async def wait_random(max_delay: int = 10):
    i = random.uniform(0,max_delay+1)
    await asyncio.sleep(i)
    return i
