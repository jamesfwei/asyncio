# README.md

## `countasync.py`
Contains simple example of awaiting multiple corountines simultaneously using `asyncio.gather`. Also, contains example of running the top-level `main` function using `asyncio.run`.

Output:
```
One
One
One
Two
Two
Two
/Users/jameswei/Documents/interviews/asyncio/countasync.py executed in 1.00 seconds.
```

## `countasync_with_timeout.py`
Same as the above but uses the asynchronous context manager, `asyncio.timeout`, to limit the amount of time spent waiting on something.

```
One
One
One
The long operation timed out!
This statement always runs.
/Users/jameswei/Documents/interviews/asyncio/countasync_with_timeout.py executed in 1.00 seconds.
```
