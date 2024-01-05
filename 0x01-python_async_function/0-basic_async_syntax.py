#!/usr/bin/env python3
"""Defines an asynchronous coroutine"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Return a random delay time
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
