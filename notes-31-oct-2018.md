# 31-oct-2018

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
