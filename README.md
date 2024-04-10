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
countasync.py executed in 1.00 seconds.
```

## `countasync_with_timeout.py`
Same as the above but uses the asynchronous context manager, `asyncio.timeout`, to limit the amount of time spent waiting on something.

```
One
One
One
The long operation timed out!
This statement always runs.
countasync_with_timeout.py executed in 1.00 seconds.
```

## `async_queue.py`
Contains example of an `asyncio.Queue` and creating producer and consumer tasks to the queue. After awaiting the producers to finish producing to the queue, we wait on the `Queue.join()` call which waits on all tasks added to the queue to be retrieved and marked as done. Then, the consumers waiting on tasks to be added to the queue are cancelled.

Output:
```
Producer 0 sleeping for 5 seconds.
Producer 1 sleeping for 1 seconds.
Producer 2 sleeping for 2 seconds.
Producer 3 sleeping for 1 seconds.
Producer 4 sleeping for 5 seconds.
Consumer 0 sleeping for 3 seconds.
Consumer 1 sleeping for 3 seconds.
Consumer 2 sleeping for 5 seconds.
Consumer 3 sleeping for 1 seconds.
Consumer 4 sleeping for 4 seconds.
Consumer 5 sleeping for 2 seconds.
Consumer 6 sleeping for 4 seconds.
Consumer 7 sleeping for 4 seconds.
Consumer 8 sleeping for 4 seconds.
Consumer 9 sleeping for 1 seconds.
Producer 1 sleeping for 2 seconds.
Producer 3 sleeping for 3 seconds.
Got item 0 in 0.0001959750079549849 seconds.
Consumer 3 sleeping for 2 seconds.
Got item 0 in 0.00039140897570177913 seconds.
Consumer 9 sleeping for 1 seconds.
Producer 2 sleeping for 5 seconds.
Got item 0 in 0.00011857401113957167 seconds.
Consumer 5 sleeping for 4 seconds.
Producer 1 sleeping for 4 seconds.
Got item 1 in 0.00015462498413398862 seconds.
Consumer 9 sleeping for 5 seconds.
Producer 3 sleeping for 5 seconds.
Got item 1 in 0.00010598095832392573 seconds.
Consumer 0 sleeping for 2 seconds.
Producer 0 sleeping for 3 seconds.
Producer 4 sleeping for 4 seconds.
Got item 0 in 0.00018827104941010475 seconds.
Consumer 2 sleeping for 5 seconds.
Got item 0 in 0.0001727120252326131 seconds.
Consumer 1 sleeping for 4 seconds.
Producer 2 sleeping for 5 seconds.
Got item 1 in 0.00017226597992703319 seconds.
Consumer 4 sleeping for 3 seconds.
Producer 4 sleeping for 4 seconds.
Got item 1 in 0.0001272209919989109 seconds.
Consumer 1 sleeping for 1 seconds.
Producer 3 sleeping for 3 seconds.
Got item 2 in 9.231001604348421e-05 seconds.
Consumer 6 sleeping for 1 seconds.
Producer 2 sleeping for 1 seconds.
Producer 3 sleeping for 2 seconds.
Got item 2 in 0.0002169579965993762 seconds.
Consumer 8 sleeping for 2 seconds.
Got item 3 in 0.00016360002337023616 seconds.
Consumer 3 sleeping for 5 seconds.
Producer 4 sleeping for 2 seconds.
Got item 2 in 0.00017922604456543922 seconds.
Consumer 5 sleeping for 5 seconds.
Producer 4 sleeping for 3 seconds.
Got item 3 in 0.00016523804515600204 seconds.
Consumer 0 sleeping for 4 seconds.
Producer 4 sleeping for 1 seconds.
Got item 4 in 0.00018366897711530328 seconds.
Consumer 9 sleeping for 3 seconds.
async_queue.py executed in 21.01 seconds.
```

