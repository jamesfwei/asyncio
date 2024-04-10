import asyncio


async def sleep(name: int, sema: asyncio.Semaphore) -> None:
    async with sema:
        print(f"Task {name} sleeping for 5 seconds...")
        await asyncio.sleep(5)
        print(f"Finished task {name}!")


async def main():
    sema = asyncio.Semaphore(5)
    tasks = [sleep(_, sema) for _ in range(10)]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    import time

    start = time.perf_counter()
    asyncio.run(main())
    print(f"{__file__} finished in {time.perf_counter() - start:0.2f} seconds.")
