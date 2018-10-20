# 21-oct-2018

### 1 - asyncio

- asyncio is a library to write concurrent code using the async/await syntax.
- Event loops , Tasks and Coroutines together makes it simpler to achieve cooperative concurrency in python. They aren't same as multiprocessing
- An event loop basically waits for something to happen and then acts on the event.
- Event loop schedules tasks
- Coroutines (wrapped under tasks) are things which can be resumed and suspended
- The async and await keywords were added in Python 3.5 to define a native coroutine and make them a distinct type when compared with a generator based coroutine
- [ ] TODO Why other languages don't have such construct or is this because of GIL that we don't talk about multiple threads here? How does this compare to something like nodejs?


```python
# simple usage, without any benefit
import asyncio

# Define a coroutine that takes in a future
async def myCoroutine():
    print("My Coroutine")

# Spin up a quick and simple event loop 
# and run until completed
loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(myCoroutine())
finally:
    loop.close()
```


```python
import asyncio

async def say(what, when): #async 
    await asyncio.sleep(when) #at this point say function is giving control to or atleast telling that now this should get executed. But the event loop is gonna make that decision when to execute that future
    print(what)

loop = asyncio.get_event_loop()
loop.run_until_complete(say('hello world', 1))
loop.close()
```

```python
#this runs forever 
import asyncio

async def say(what, when):
    await asyncio.sleep(when)
    print(what)


loop = asyncio.get_event_loop()

loop.create_task(say('first hello', 2))
loop.create_task(say('second hello', 1))

loop.run_forever()
loop.close()
```


