# 21-mar-2019

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

```
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


