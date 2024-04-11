import asyncio
import time


class MyAsyncEvent:
    def __init__(self) -> None:
        self._set = False
        self._waiters = set()

    async def wait(self) -> bool:
        if self._set:
            return True

        fut = asyncio.get_event_loop().create_future()
        self._waiters.add(fut)
        return await fut

    def set(self) -> None:
        if self._set:
            raise RuntimeError("Cannot set event that is already set!")

        self._set = True

        for waiter in self._waiters:
            waiter.set_result(True)

        self._waiters.clear()

    def clear(self) -> None:
        self._set = False

    def is_set(self) -> bool:
        return self._set


async def wait_on_event(event: MyAsyncEvent | asyncio.Event) -> None:
    print("Waiting on event...")
    await event.wait()
    print("Event happened!")


async def main():
    event = MyAsyncEvent()
    # event = asyncio.Event()
    assert not event.is_set()
    tasks = [asyncio.create_task(wait_on_event(event)) for _ in range(5)]
    await asyncio.sleep(1)
    print("Setting event")
    event.set()
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    start = time.perf_counter()
    asyncio.run(main())
    print(f"{__file__} finished running in {time.perf_counter() - start:0.2f} seconds.")
