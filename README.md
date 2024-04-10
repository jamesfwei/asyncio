# README.md

## asyncio Q&A

### What is the asyncio library and what is it useful for?
`asyncio` is a Python library for writing concurrent code using the async/await syntax. It allows efficient handling of I/O operations such as reading from a file, querying a database, making a network request, especially if such operations can be performed concurrently.

### What is the event loop and what is its role?
The event loop is the central component used to manage and execute asynchronous tasks and handle I/O events. The event loop scheudles and executes tasks, keeping track of which tasks are ready to run. The event loop monitors for I/O events such as a file being ready to be read and schedules the corresponding task to handle the event. The event loop handles time-based operations such as timeouts. Finally, the event loop handles exceptions that occur in tasks, either returning or raising them.

### What is a coroutine?
A coroutine is a specialized Python function that can be suspended and resumed, enabling cooperative multitasking.

### What are the benefits of using asyncio over threading in Python?
asyncio applications are single-threaded which use fewer system resources compared to threading. Creating and managing thousands of asyncio coroutines is more efficient than creating and managing thousands of threads. Asynchronous code also naturally avoids common issues associated with multithreaded programming, such as race conditions, deadlocks, and the need for explicit locking and synchronization mechanisms.

Asynchronous code is often more clean and clear than thread-based programming due to the async/await syntax being more linear.

### What are the mechanisms for inter-task communication in asyncio?
* `asyncio.Queue` for inter-task communication.
* `asyncio.Event` for allowing one coroutine or task to signal one or more other coroutines or tasks.
* ...

### How would you implement rate limiting or throttling in an asyncio application?
Use `asyncio.Semaphore` which is a synchronization primitive that can be used to limit the number of concurrent tasks or coroutines

```Python
async def task(sema):
    async with sema:
        pass

async def main():
    sema = async.Semaphore(value=5)
    tasks = [task(sema) for _ in range(10)]
    await asyncio.gather(*tasks)
```

### How would you handle long-running tasks or background tasks in asyncio?
Run the task in a spearate event loop than the main event loop or run the task in a process or thread.

### How would you integrate synchronous code with asynchronous code?
Run the synchronous code in a separate thread using `asyncio.to_thread`.

### What are some examples of use cases for asyncio?
Web crawlers, web applications and APIS (handle multiple concurrent client connections), websocket applications, etc.

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

