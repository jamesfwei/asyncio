import asyncio


async def count():
    print("One")
    await asyncio.sleep(10)
    print("Two")


async def main():
    try:
        async with asyncio.timeout(1):
            await asyncio.gather(count(), count(), count())
    except asyncio.TimeoutError:
        print("The long operation timed out!")
    
    print("This statement always runs.")


if __name__ == "__main__":
    import time

    s = time.perf_counter()
    asyncio.run(main())
    elapsed = time.perf_counter() - s
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")
