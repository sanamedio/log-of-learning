# 31-oct-2018

### 7 - python3 print(\*a)

```python
Python 3.5.2 (default, Nov 23 2017, 16:37:01) 
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> print(*[1,2,3]) # no need to do ' '.join([])
1 2 3
>>> print([1,2,3])
[1, 2, 3]
>>> 
```

### 6 - self wrapping Object

```python
>>> L = []
>>> L.append(L)
>>> print(L)
[[...]]
>>> 

```

### 5 - reading PyObject with ctypes

```python
import ctypes

class IntStruct(ctypes.Structure):
    _fields_ = [("ob_refcnt", ctypes.c_long),
                ("ob_type", ctypes.c_void_p),
                ("ob_size", ctypes.c_ulong),
                ("ob_digit", ctypes.c_long)]
    
    def __repr__(self):
        return ("IntStruct(ob_digit={self.ob_digit}, "
                "refcount={self.ob_refcnt})").format(self=self)


num = 42
IntStruct.from_address(id(42))
```
```python
import ctypes

class ListStruct(ctypes.Structure):
	_fields_ = [ ("ob_refcnt", ctypes.c_long),
			("ob_type", ctypes.c_void_p),
			("ob_size",ctypes.c_ulong),
			("ob_item", ctypes.c_long),
			("allocated", ctypes.c_ulong)]
	def __repr__(self):
		return("ListStruct(len={self.ob_size}, "
			"refcount={self.ob_refcnt})".format(self=self))

L = [1,2,3,4,5]
print(ListStruct.from_address(id(L)))
```



### 4 - concurrent.futures

```python
from time import time
from concurrent.futures import *


def gcd(pair):

	a , b = pair
	low = min(a,b)
	for i in range(low, 0 , -1 ):
		if a % i == 0 and b % i == 0:
			return i




numbers = [ (1231312,434344) , (2013123,111110),
	    (34423323,123123), (234345,345345)]


numbers = numbers * 100

def linear():
	start = time()
	results = list(map(gcd, numbers))
	end = time()
	print('linear : Took %.3f seconds' % ( end - start ) )



def threadpool():
	start = time()
	pool = ThreadPoolExecutor(max_workers = 2)
	results = list(pool.map(gcd, numbers))
	end = time()
	print('threadpool : Took %.3f seconds' % ( end - start ) )


def processpool():
	start = time()
	pool = ProcessPoolExecutor(max_workers=2)
	results = list(pool.map(gcd, numbers))
	end = time()
	print('processpool : Took %.3f seconds' %(end -start))


if __name__ == '__main__':
	linear()
	threadpool()
	processpool()


#linear : Took 6.746 seconds
#threadpool : Took 6.620 seconds
#processpool : Took 3.541 seconds
```
- ProcessPoolExecutor uses multiprocessing module low level constructs
- Steps
  - It takes all items from input numbers to a map
  - it serializes it into binary data using pickle module( pickle reliability using copyreg )
  - It copies the serilaized data into a child interpreter through local sockets
  - It deserializes the data using pickle in the child interpreter
  - It then imports pythotn module containing the gcd function
  - It runs that in the child process parallel with others
  - It serilaizes the result through bytes
  - it copies those bytes back through socket
  - deserilaizatoin of results in parent process
  - it merges results into single list and returns that




### 3 - coroutine yield and send together 

```python

def my_coroutine():
	while True:
		received = yield
		print('Received ', received)

it = my_coroutine()
next(it)
it.send('First')
it.send('Second')

```
```python
def minimize():
    current = yield
    while True:
        value = yield current
        current = min(value, current)
        
it = minimize()
next(it)
print(it.send(4)) # 4
print(it.send(22)) # 4
print(it.send(-1)) # -1
```



### 2 - Pipeline using a Queue class with Locks ( done wrong )

```python
from threading import *
from collections import *
from time import sleep



class MyQueue(object):
	
	def __init__(self):
		self.items = deque() # does it not contain lock already?
		self.lock = Lock()

	def put(self,item):
		with self.lock:
			self.items.append(item)


	def get(self):
		with self.lock:
			return self.items.popleft()



class Worker(Thread):

	def __init__(self, func, in_queue, out_queue):
		super().__init__()
		self.func = func
		self.in_queue = in_queue
		self.out_queue = out_queue
		self.polled_count = 0
		self.work_done = 0

	def run(self):
		while True:
			self.polled_count += 1
			try:
				item = self.in_queue.get()
			except IndexError:
				sleep(0.01) # No work to do
			else:
				result  = self.func(item)
				self.out_queue.put(result)
				self.work_done += 1
				
				


def download(x):
	print("Downloading : "+ x)
	return x

def resize(x):
	print("Resizing : " + x )
	return x

def upload(x):
	print("Uploading : " + x )
	return x



def main():
	download_queue = MyQueue()
	resize_queue = MyQueue()
	upload_queue = MyQueue()
	done_queue = MyQueue()
	
	threads = [
		Worker(download, download_queue, resize_queue),
		Worker(resize, resize_queue, upload_queue),
		Worker(upload, upload_queue, done_queue)
	]

	for thread in threads:
		thread.start()

	for _ in range(1000):
		download_queue.put( str(_))


if __name__ == '__main__':
	main()
```
- When the worker vary in speeds, a later phase might starve due to slow earlier state, doing nothing but checking whether anything is present in the queue or not.
- The size of data stored in queue can constantly increase if further phases are slow causing the program to crash arbirarily.
- We need to create a busy_waiting on the done_queue in order to know when it is the time to close.
- Writing a producer-consumer queue needs more effort.
- Instead Queue from python library can be used which solves many of these issues.



### 1 - Counter with and without locking

```python
how_many = 5000

from threading import *

def worker(sensor_index, how_many, counter):
	for _ in range(how_many):
		counter.increment(1)


def run_threads(func, how_many , counter):
	threads = []
	for i in range(5):
		args = ( i , how_many, counter)
		thread = Thread(target=func, args=args)
		threads.append(thread)
		thread.start()

	for thread in threads:
		thread.join()


class StupidCounter(object):

	def __init__(self):
		self.count = 0

	def increment(self,offset):
		self.count += offset

class LockingCounter(object):

	def __init__(self):
		self.lock = Lock()
		self.count = 0


	def increment(self, offset):
		with self.lock:
			self.count += offset


counter = LockingCounter()
run_threads(worker, how_many, counter)
print('Counter should be %d, found %d ' % ( 5 * how_many, counter.count ))

counter2 = StupidCounter()
run_threads(worker, how_many, counter2)
print('Counter should be %d, found %d ' % ( 5 * how_many, counter2.count ))

```
