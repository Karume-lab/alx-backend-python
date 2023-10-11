#!/usr/bin/env python3


"""Import modules"""
from typing import List
import asyncio
import time
async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> List[float]:
    """
    Import async_comprehension from the previous file and write
    a measure_runtime coroutine that will execute async_comprehension
    four times in parallel using asyncio.gather.
    measure_runtime should measure the total runtime and return it.
    Notice that the total runtime is roughly 10 seconds.
    """
    start_time = time.perf_counter()
    lst = [async_comprehension()] * 4
    await asyncio.gather(*lst)
    end_time = time.perf_counter()
    return end_time - start_time
