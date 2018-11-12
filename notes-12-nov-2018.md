# 12-nov-2018

### 2 - dir() and dunder dict

- dir() doesn't just look up an object's ```__dict__``` (which sometimes doesn't even exist), it will use the object's heritage (its class or type, and any superclasses, or parents, of that class or type) to give you a complete picture of all available attributes.

- An instance ```__dict__``` is just the 'local' set of attributes on that instance, and does not contain every attribute available on the instance. Instead, you need to look at the class and the class's inheritance tree too.

### 1 - Async decorator


```python
from Queue import Queue
from threading import Thread


class asynchronous():

    def __init__(self, func):
        self.func = func

        def threaded(*args, **kwargs):
            self.queue.put(self.func(*args, **kwargs))


        self.threaded = threaded




    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)


    def start(self, *args, **kwargs):
        self.queue = Queue()
        thread = Thread(target=self.threaded, args=args,kwargs = kwargs)
        thread.start()
        return asynchronous.Result(self.queue, thread)



    class NotYetDoneException(Exception):
        def __init__(self, message):
            self.message = message


    class Result():
        def __init__(self, queue, thread):
            self.queue = queue
            self.thread = thread

        def is_done(self):
            return not self.thread.is_alive()


        def get_result(self):
            if not self.is_done():
                raise asynchronous.NotYetDoneException('the call has not completed yet')

            if not hasattr(self, 'result'):
                self.result = self.queue.get()


            return self.result




if __name__ == '__main__':


    import time


    @asynchronous
    def long_process(num):
        time.sleep(10)
        return num*num


    result = long_process.start(12)


    for i in range(20):
        print(i)
        time.sleep(1)


        if result.is_done():
            print "result {0}".format(result.get_result())





    result2 = long_process.start(13)



    try:
        print ( "result2 {0}".format(result2.get_result()))


    except asynchronous.NotYetDoneException as ex:
        print ex.message
```
