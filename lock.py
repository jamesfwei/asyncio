import asyncio
import time
from collections import deque


class MyAsyncLock:
    def __init__(self) -> None:
        self._locked = False
        self._waiters = deque([])

    async def __aenter__(self):
        await self.acquire()
        return None

    async def __aexit__(self, exc_type, exc, tb):
        self.release()

    async def acquire(self) -> bool:
        if not self._locked:
            self._locked = True
            return True

        loop = asyncio.get_event_loop()
        fut = loop.create_future()
        self._waiters.append(fut)
        return await fut

    def release(self) -> None:
        if not self._locked:
            raise RuntimeError("Attempting to release a lock that is not acquired!")

        if not self._waiters:
            self._locked = False
            return

        waiter = self._waiters.popleft()
        waiter.set_result(True)

    def locked(self) -> bool:
        return self._locked


async def acquire_lock_and_sleep(lock: MyAsyncLock | asyncio.Lock, sleep_for: int = 1) -> None:
    print("Trying to acquire lock...")

    async with lock:
        print("Lock acquired!")
        await asyncio.sleep(sleep_for)


async def main():
    lock = MyAsyncLock()
    # lock = asyncio.Lock()
    tasks = [asyncio.create_task(acquire_lock_and_sleep(lock)) for _ in range(5)]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    start = time.perf_counter()
    asyncio.run(main())
    print(f"{__file__} finished running in {time.perf_counter() - start:0.2f} seconds.")
