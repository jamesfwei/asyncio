import asyncio
import random
import time


async def randsleep(caller: str = None) -> None:
    i = random.randint(1, 5)
    if caller:
        print(f"{caller} sleeping for {i} seconds.")
    await asyncio.sleep(i)


async def produce(name: int, q: asyncio.Queue) -> None:
    # Mimic startup
    await randsleep(caller=f"Producer {name}")

    for i in range(name + 1):
        t = time.perf_counter()
        await q.put((i, t))
        await randsleep(caller=f"Producer {name}")


async def consume(name: int, q: asyncio.Queue) -> None:
    # Mimic startup
    await randsleep(caller=f"Consumer {name}")

    while True:
        i, t = await q.get()
        print(f"Got item {i} in {time.perf_counter() - t} seconds.")
        await randsleep(caller=f"Consumer {name}")
        q.task_done()


async def main(nproducers: int = 5, nconsumers: int = 10):
    q = asyncio.Queue()
    producers = [asyncio.create_task(produce(_, q)) for _ in range(nproducers)]
    consumers = [asyncio.create_task(consume(_, q)) for _ in range(nconsumers)]
    await asyncio.gather(*producers)
    await q.join()

    for c in consumers:
        c.cancel()


if __name__ == "__main__":
    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
