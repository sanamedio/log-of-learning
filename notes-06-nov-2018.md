# 06-nov-2018

### 8 - Listing Errors Classes

```python
>>> print(* [ x for x in dir(locals()['__builtins__']) if x.endswith('Error') ]) 
ArithmeticError AssertionError AttributeError BlockingIOError BrokenPipeError BufferError ChildProcessError ConnectionAbortedError ConnectionError ConnectionRefusedError ConnectionResetError EOFError EnvironmentError FileExistsError FileNotFoundError FloatingPointError IOError ImportError IndentationError IndexError InterruptedError IsADirectoryError KeyError LookupError MemoryError ModuleNotFoundError NameError NotADirectoryError NotImplementedError OSError OverflowError PermissionError ProcessLookupError RecursionError ReferenceError RuntimeError SyntaxError SystemError TabError TimeoutError TypeError UnboundLocalError UnicodeDecodeError UnicodeEncodeError UnicodeError UnicodeTranslateError ValueError ZeroDivisionError
```

### 7 - Writing your own enumerator

```python
class my_enumerate:


        def __init__(self, some_iter):
                self.some_iter = iter(some_iter)
                self.count = 0


        def __iter__(self):
                return self


        def __next__(self):
                val = next(self.some_iter)
                self.count += 1

                return self.count , val





for n,val in my_enumerate(['a','b','c']):
        print (n,val)

```

### 6 - Overriding Control:C

```python
from time import sleep
while True:
    try:
        sleep(.1)
    except: # THIS Catches all, even Keyboard Interrupt
        pass 
```

### 5 - listing all available modules

```python
help('modules')
```

### 4 - generating primes as list or generator

```python
def generate_primes(n):

        limit = n
        root = int(n**0.5)
        flags = [ True for x in range(n+1)]

        flags[1] = False
        flags[2] = True


        i = 0
        for i in range(2,root+1):
                t = i*i
                while t <= limit:
                        flags[t] = False
                        t += i

        zipped= zip(range(1,n+1),flags[1:])
        return ( [ key for key,value in dict(zipped).items() if value  ] )




from collections import defaultdict

def generate_primes_yield():


        v = 2
        composites = defaultdict(lambda: list())


        while True:
                yield v
                composites[v*v].append(v)
                v+=1
                while v in composites:
                        for f in composites[v]:
                                composites[v+f].append(f)
                        del composites[v]
                        v += 1

```


### 3 - Tracing asyncio

python program with asyncio Queues named ```asynciotest.py```:
```python
import asyncio
from asyncio.queues import Queue
import os


main_queue = Queue(50)
counter = 0
message = os.urandom(1024) # random 1kb message


async def producer():
	while loop.is_running:
		await main_queue.put(message)



async def consumer():
	global counter
	while loop.is_running():
		await main_queue.get()
		counter += 1
		await asyncio.sleep(0.1)



async def end():
	await asyncio.sleep(2)


	asyncio.get_event_loop().stop()
	print("in queue :{}".format(main_queue.qsize()))
	print("processed items : {}".format(counter))


if __name__ == '__main__':
	loop = asyncio.get_event_loop()
	asyncio.ensure_future(producer())
	asyncio.ensure_future(consumer())
	asyncio.ensure_future(end())

	try:
		loop.run_forever()
	except KeyboardInterrupt:
		import sys
		sys.exit()	
```

python trace:
```python
$ python -m trace -t asynciotest.py  | grep asynciotest.py

asynciotest.py(1): import asyncio
<frozen importlib._bootstrap>(177): <frozen importlib._bootstrap>(178): <frozen importlib._bootstrap>(182): <frozen importlib._bootstrap>(183): <frozen importlib._bootstrap>(185): asynciotest.py(2): from asyncio.queues import Queue
<frozen importlib._bootstrap>(1019): <frozen importlib._bootstrap>(1044): asynciotest.py(3): import os
asynciotest.py(6): main_queue = Queue(50)
asynciotest.py(7): counter = 0
asynciotest.py(8): message = os.urandom(1024) # random 1kb message
asynciotest.py(11): async def producer():
asynciotest.py(17): async def consumer():
asynciotest.py(26): async def end():
asynciotest.py(35): if __name__ == '__main__':
asynciotest.py(36): 	loop = asyncio.get_event_loop()
asynciotest.py(37): 	asyncio.ensure_future(producer())
asynciotest.py(38): 	asyncio.ensure_future(consumer())
asynciotest.py(39): 	asyncio.ensure_future(end())
asynciotest.py(41): 	try:
asynciotest.py(42): 		loop.run_forever()
asynciotest.py(12): 	while loop.is_running:
asynciotest.py(13): 		await main_queue.put(message)
asynciotest.py(12): 	while loop.is_running:
asynciotest.py(13): 		await main_queue.put(message)
asynciotest.py(12): 	while loop.is_running:
asynciotest.py(13): 		await main_queue.put(message)
asynciotest.py(12): 	while loop.is_running:
asynciotest.py(13): 		await main_queue.put(message)
asynciotest.py(12): 	while loop.is_running:
asynciotest.py(13): 		await main_queue.put(message)
asynciotest.py(12): 	while loop.is_running:
asynciotest.py(13): 		await main_queue.put(message)
asynciotest.py(12): 	while loop.is_running:
asynciotest.py(13): 		await main_queue.put(message)
asynciotest.py(12): 	while loop.is_running:
asynciotest.py(13): 		await main_queue.put(message)
asynciotest.py(12): 	while loop.is_running:
asynciotest.py(13): 		await main_queue.put(message)
asynciotest.py(12): 	while loop.is_running:
asynciotest.py(13): 		await main_queue.put(message)
asynciotest.py(12): 	while loop.is_running:
asynciotest.py(13): 		await main_queue.put(message)
asynciotest.py(12): 	while loop.is_running:
asynciotest.py(13): 		await main_queue.put(message)
asynciotest.py(12): 	while loop.is_running:
asynciotest.py(13): 		await main_queue.put(message)
asynciotest.py(12): 	while loop.is_running:
asynciotest.py(13): 		await main_queue.put(message)
asynciotest.py(12): 	while loop.is_running:
asynciotest.py(13): 		await main_queue.put(message)
asynciotest.py(12): 	while loop.is_running:
asynciotest.py(13): 		await main_queue.put(message)
asynciotest.py(12): 	while loop.is_running:
asynciotest.py(13): 		await main_queue.put(message)
asynciotest.py(12): 	while loop.is_running:
asynciotest.py(13): 		await main_queue.put(message)
asynciotest.py(12): 	while loop.is_running:
asynciotest.py(13): 		await main_queue.put(message)
asynciotest.py(12): 	while loop.is_running:
asynciotest.py(13): 		await main_queue.put(message)
asynciotest.py(12): 	while loop.is_running:
asynciotest.py(13): 		await main_queue.put(message)
asynciotest.py(12): 	while loop.is_running:
asynciotest.py(13): 		await main_queue.put(message)
asynciotest.py(12): 	while loop.is_running:
asynciotest.py(13): 		await main_queue.put(message)
asynciotest.py(12): 	while loop.is_running:
asynciotest.py(13): 		await main_queue.put(message)
asynciotest.py(12): 	while loop.is_running:
asynciotest.py(13): 		await main_queue.put(message)
asynciotest.py(12): 	while loop.is_running:
asynciotest.py(13): 		await main_queue.put(message)
asynciotest.py(12): 	while loop.is_running:
asynciotest.py(13): 		await main_queue.put(message)
asynciotest.py(12): 	while loop.is_running:
asynciotest.py(13): 		await main_queue.put(message)
asynciotest.py(12): 	while loop.is_running:
asynciotest.py(13): 		await main_queue.put(message)
asynciotest.py(12): 	while loop.is_running:
asynciotest.py(13): 		await main_queue.put(message)
asynciotest.py(12): 	while loop.is_running:
asynciotest.py(13): 		await main_queue.put(message)
asynciotest.py(12): 	while loop.is_running:
asynciotest.py(13): 		await main_queue.put(message)
asynciotest.py(12): 	while loop.is_running:
asynciotest.py(13): 		await main_queue.put(message)
asynciotest.py(12): 	while loop.is_running:
asynciotest.py(13): 		await main_queue.put(message)
asynciotest.py(12): 	while loop.is_running:
asynciotest.py(13): 		await main_queue.put(message)
asynciotest.py(12): 	while loop.is_running:
asynciotest.py(13): 		await main_queue.put(message)
asynciotest.py(12): 	while loop.is_running:
asynciotest.py(13): 		await main_queue.put(message)
asynciotest.py(12): 	while loop.is_running:
asynciotest.py(13): 		await main_queue.put(message)
asynciotest.py(12): 	while loop.is_running:
asynciotest.py(13): 		await main_queue.put(message)
asynciotest.py(12): 	while loop.is_running:
asynciotest.py(13): 		await main_queue.put(message)
asynciotest.py(12): 	while loop.is_running:
asynciotest.py(13): 		await main_queue.put(message)
asynciotest.py(12): 	while loop.is_running:
asynciotest.py(13): 		await main_queue.put(message)
asynciotest.py(12): 	while loop.is_running:
asynciotest.py(13): 		await main_queue.put(message)
asynciotest.py(12): 	while loop.is_running:
asynciotest.py(13): 		await main_queue.put(message)
asynciotest.py(12): 	while loop.is_running:
asynciotest.py(13): 		await main_queue.put(message)
asynciotest.py(12): 	while loop.is_running:
asynciotest.py(13): 		await main_queue.put(message)
asynciotest.py(12): 	while loop.is_running:
asynciotest.py(13): 		await main_queue.put(message)
asynciotest.py(12): 	while loop.is_running:
asynciotest.py(13): 		await main_queue.put(message)
asynciotest.py(12): 	while loop.is_running:
asynciotest.py(13): 		await main_queue.put(message)
asynciotest.py(12): 	while loop.is_running:
asynciotest.py(13): 		await main_queue.put(message)
asynciotest.py(12): 	while loop.is_running:
asynciotest.py(13): 		await main_queue.put(message)
asynciotest.py(19): 	while loop.is_running():
asynciotest.py(20): 		await main_queue.get()
asynciotest.py(21): 		counter += 1
asynciotest.py(22): 		await asyncio.sleep(0.1)
asynciotest.py(27): 	await asyncio.sleep(2)
asynciotest.py(12): 	while loop.is_running:
asynciotest.py(13): 		await main_queue.put(message)
asynciotest.py(19): 	while loop.is_running():
asynciotest.py(20): 		await main_queue.get()
asynciotest.py(21): 		counter += 1
asynciotest.py(22): 		await asyncio.sleep(0.1)
asynciotest.py(12): 	while loop.is_running:
asynciotest.py(13): 		await main_queue.put(message)
asynciotest.py(19): 	while loop.is_running():
asynciotest.py(20): 		await main_queue.get()
asynciotest.py(21): 		counter += 1
asynciotest.py(22): 		await asyncio.sleep(0.1)
asynciotest.py(12): 	while loop.is_running:
asynciotest.py(13): 		await main_queue.put(message)
asynciotest.py(19): 	while loop.is_running():
asynciotest.py(20): 		await main_queue.get()
asynciotest.py(21): 		counter += 1
asynciotest.py(22): 		await asyncio.sleep(0.1)
asynciotest.py(12): 	while loop.is_running:
asynciotest.py(13): 		await main_queue.put(message)
asynciotest.py(19): 	while loop.is_running():
asynciotest.py(20): 		await main_queue.get()
asynciotest.py(21): 		counter += 1
asynciotest.py(22): 		await asyncio.sleep(0.1)
asynciotest.py(12): 	while loop.is_running:
asynciotest.py(13): 		await main_queue.put(message)
asynciotest.py(19): 	while loop.is_running():
asynciotest.py(20): 		await main_queue.get()
asynciotest.py(21): 		counter += 1
asynciotest.py(22): 		await asyncio.sleep(0.1)
asynciotest.py(12): 	while loop.is_running:
asynciotest.py(13): 		await main_queue.put(message)
asynciotest.py(19): 	while loop.is_running():
asynciotest.py(20): 		await main_queue.get()
asynciotest.py(21): 		counter += 1
asynciotest.py(22): 		await asyncio.sleep(0.1)
asynciotest.py(12): 	while loop.is_running:
asynciotest.py(13): 		await main_queue.put(message)
asynciotest.py(19): 	while loop.is_running():
asynciotest.py(20): 		await main_queue.get()
asynciotest.py(21): 		counter += 1
asynciotest.py(22): 		await asyncio.sleep(0.1)
asynciotest.py(12): 	while loop.is_running:
asynciotest.py(13): 		await main_queue.put(message)
asynciotest.py(19): 	while loop.is_running():
asynciotest.py(20): 		await main_queue.get()
asynciotest.py(21): 		counter += 1
asynciotest.py(22): 		await asyncio.sleep(0.1)
asynciotest.py(12): 	while loop.is_running:
asynciotest.py(13): 		await main_queue.put(message)
asynciotest.py(19): 	while loop.is_running():
asynciotest.py(20): 		await main_queue.get()
asynciotest.py(21): 		counter += 1
asynciotest.py(22): 		await asyncio.sleep(0.1)
asynciotest.py(12): 	while loop.is_running:
asynciotest.py(13): 		await main_queue.put(message)
asynciotest.py(19): 	while loop.is_running():
asynciotest.py(20): 		await main_queue.get()
asynciotest.py(21): 		counter += 1
asynciotest.py(22): 		await asyncio.sleep(0.1)
asynciotest.py(12): 	while loop.is_running:
asynciotest.py(13): 		await main_queue.put(message)
asynciotest.py(19): 	while loop.is_running():
asynciotest.py(20): 		await main_queue.get()
asynciotest.py(21): 		counter += 1
asynciotest.py(22): 		await asyncio.sleep(0.1)
asynciotest.py(12): 	while loop.is_running:
asynciotest.py(13): 		await main_queue.put(message)
asynciotest.py(19): 	while loop.is_running():
asynciotest.py(20): 		await main_queue.get()
asynciotest.py(21): 		counter += 1
asynciotest.py(22): 		await asyncio.sleep(0.1)
asynciotest.py(12): 	while loop.is_running:
asynciotest.py(13): 		await main_queue.put(message)
asynciotest.py(19): 	while loop.is_running():
asynciotest.py(20): 		await main_queue.get()
asynciotest.py(21): 		counter += 1
asynciotest.py(22): 		await asyncio.sleep(0.1)
asynciotest.py(12): 	while loop.is_running:
asynciotest.py(13): 		await main_queue.put(message)
asynciotest.py(19): 	while loop.is_running():
asynciotest.py(20): 		await main_queue.get()
asynciotest.py(21): 		counter += 1
asynciotest.py(22): 		await asyncio.sleep(0.1)
asynciotest.py(12): 	while loop.is_running:
asynciotest.py(13): 		await main_queue.put(message)
asynciotest.py(19): 	while loop.is_running():
asynciotest.py(20): 		await main_queue.get()
asynciotest.py(21): 		counter += 1
asynciotest.py(22): 		await asyncio.sleep(0.1)
asynciotest.py(12): 	while loop.is_running:
asynciotest.py(13): 		await main_queue.put(message)
asynciotest.py(19): 	while loop.is_running():
asynciotest.py(20): 		await main_queue.get()
asynciotest.py(21): 		counter += 1
asynciotest.py(22): 		await asyncio.sleep(0.1)
asynciotest.py(12): 	while loop.is_running:
asynciotest.py(13): 		await main_queue.put(message)
asynciotest.py(19): 	while loop.is_running():
asynciotest.py(20): 		await main_queue.get()
asynciotest.py(21): 		counter += 1
asynciotest.py(22): 		await asyncio.sleep(0.1)
asynciotest.py(12): 	while loop.is_running:
asynciotest.py(13): 		await main_queue.put(message)
asynciotest.py(19): 	while loop.is_running():
asynciotest.py(20): 		await main_queue.get()
asynciotest.py(21): 		counter += 1
asynciotest.py(22): 		await asyncio.sleep(0.1)
asynciotest.py(12): 	while loop.is_running:
asynciotest.py(13): 		await main_queue.put(message)
asynciotest.py(30): 	asyncio.get_event_loop().stop()
asynciotest.py(31): 	print("in queue :{}".format(main_queue.qsize()))
asynciotest.py(32): 	print("processed items : {}".format(counter))
```

### 2 - using List comprehension to shorten code

- Follow ```process``` and ```process2``` do the same thing:

```python
def process(data_set, condition, modify):
        """process data_set by modify function on condition"""

        collection = list()

        for datus in data_set:
                if condition(datum):
                        collection.append(datum)
                else:
                        new = modify(datum)
                        collection.append(new)


def process2(data_set, condition, modify):
        return [ d if condition(d) else modify(d) for d in data_set ] #more elegant
```

### 1 - Factorial in three ways

```python
def factorialR(N):
	"""Recursive function"""
	assert isinstance(N, int) and N >= 1
	return 1 if N <= 1 else N * factorialR(N-1)




def factorialI(N):
	"""Iterative Funtion"""
	assert isinstance(N, int) and N >= 1
	product = 1
	while N >= 1:
		product *= N
		N -= 1
	return product



from functools import reduce
from operator import mul

def factorialHOF(n):
	"""Higher order functions"""
	return reduce(mul, range(1,n+1), 1)
		
	


print(factorialR(5))
print(factorialI(5))
print(factorialHOF(5))
```
