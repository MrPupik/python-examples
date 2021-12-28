import asyncio
from time import sleep


def blocking():
    print("b start")
    sleep(2)
    print("b finish")


async def non_blocking():
    print("nb start")
    sleep(2)
    print("nb finish")


async def runner():
    print("hi")
    b = non_blocking()
    print("bi")
    await b


asyncio.run(runner())
