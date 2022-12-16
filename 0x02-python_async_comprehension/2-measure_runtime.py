#!/usr/bin/env python3

""" Run time for four parallel comprehensions """

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    
    """
    n = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for x in range(5)))
    return (time.perf_counter() - n)
