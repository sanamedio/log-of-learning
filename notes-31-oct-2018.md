# 31-oct-2018

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
