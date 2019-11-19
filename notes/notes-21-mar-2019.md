# 21-mar-2019

### 2 - dining philosophers

- https://rosettacode.org/wiki/Dining_philosophers#Python
- TODO 


### 1 - multithreaded hello world

- https://bytes.yingw787.com/posts/2019/01/12/concurrency_with_python_threads_and_locks/

```python
import threading
import time

def hello_world():
    print(
        'Hello from {0}'.format(
            threading.get_ident()
        )
    )

t1 = threading.Thread(target=hello_world)
t2 = threading.Thread(target=hello_world)

t1.start()
t2.start()
```

```python
import threading
import time

class MyThread(threading.Thread):
    def run(self):
        print(
            "Hello from {}!".format(
                self.getName()
            )
        )
        # Thread execution is spaced out by
        # at least 1.0 seconds.
        time.sleep(1)
        print(
            "{} finished!".format(
                self.getName()
            )
        )

def main():
    for x in range(4):
        mythread = MyThread(
            name = "Thread-{}".format(
                x + 1)
            )
        mythread.start()
        # Thread creation is spaced out
        # by at least 0.9 seconds.
        time.sleep(.9)

if __name__ == '__main__':
    main()
```

```python
import threading
import time

class MyThread(threading.Thread):
    def run(self):
        print(
            "Hello from {}!".format(
                self.getName()
            )
        )
        # Thread execution is spaced out by
        # at least 1.0 seconds.
        time.sleep(1)
        print(
            "{} finished!".format(
                self.getName()
            )
        )

def main():
    for x in range(4):
        mythread = MyThread(
            name = "Thread-{}".format(
                x + 1)
            )
        mythread.start()
        # Thread creation is spaced out
        # by at least 0.9 seconds.
        time.sleep(.9)

if __name__ == '__main__':
    main()
```


```python
import threading
import time

class Counter():
    def __init__(self):
        self.count = 0

    def increment_until_100(self):
        while self.count != 100:
            print(
                '{0} incrementing.'.format(
                    threading.current_thread().getName()
                )
            )
            self.count += 1
            time.sleep(1)

def worker(counter):
    counter.increment_until_100()

def main():
    counter = Counter()
    for x in range(7):
        count_thread = threading.Thread(
            name="Thread-{}".format(
                x + 1
            ),
            args=[counter],
            target=worker
        )
        count_thread.start()
        time.sleep(.9)

    print(
        'Counter final value is {0}'.format(
            counter.count
        )
    )

if __name__ == '__main__':
    main()
```

```python
def dine(self):
    fork1, fork2 = self.forkOnLeft, self.forkOnRight

    while self.running:
        fork1.acquire(True)
        # NOTE: Do not block the lock when attempting to acquire,
        # in order to avoid deadlock.
        locked = fork2.acquire(False)
        if locked: break
        # NOTE: If the lock acquisition is not successful, then
        # release the lock on the first object.
        fork1.release()
        print '%s swaps forks' % self.name
        fork1, fork2 = fork2, fork1
    else:
        return

    self.dining()
    fork2.release()
    fork1.release()
```






