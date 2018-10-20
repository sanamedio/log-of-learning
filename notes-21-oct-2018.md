# 21-oct-2018

### 1 - asyncio

- asyncio is a library to write concurrent code using the async/await syntax.
- Event loops , Tasks and Coroutines
- An event loop basically waits for something to happen and then acts on the event.
- Event loop schedules tasks
- Coroutines are things which can be resumed and suspended
- The async and await keywords were added in Python 3.5 to define a native coroutine and make them a distinct type when compared with a generator based coroutine


```python
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
    await asyncio.sleep(when)
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


