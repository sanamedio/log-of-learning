# 12-nov-2018

### 7 - Code from numpy quickstart

```python
In [1]: import numpy as np                                                                                                                                                                                         

In [2]: a = np.arange(15).reshape(3,5)                                                                                                                                                                             

In [3]: a                                                                                                                                                                                                          
Out[3]: 
array([[ 0,  1,  2,  3,  4],
       [ 5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14]])

In [4]: a.shape                                                                                                                                                                                                    
Out[4]: (3, 5)

In [5]: a.ndim                                                                                                                                                                                                     
Out[5]: 2

In [6]: a.dtype.name                                                                                                                                                                                               
Out[6]: 'int64'

In [7]: a.size                                                                                                                                                                                                     
Out[7]: 15

In [8]: type(a)                                                                                                                                                                                                    
Out[8]: numpy.ndarray

In [9]: b = np.array([1,2,34,5])                                                                                                                                                                                   

In [10]: type(b)                                                                                                                                                                                                   
Out[10]: numpy.ndarray

```
```python
In [9]: b = np.array([1,2,34,5])                                                                                                                                                                                   

In [10]: type(b)                                                                                                                                                                                                   
Out[10]: numpy.ndarray

In [11]: a = np.array([2,3,4])                                                                                                                                                                                     

In [12]: a                                                                                                                                                                                                         
Out[12]: array([2, 3, 4])

In [13]: a.dtype                                                                                                                                                                                                   
Out[13]: dtype('int64')

In [14]: b = np.array([1.2, 3.5, 5.1] )                                                                                                                                                                            

In [15]: b.dtype                                                                                                                                                                                                   
Out[15]: dtype('float64')
```


### 6 - Difference between cls and self

```python

In [36]: class Test: 
    ...:     def __new__(cls): 
    ...:         print(cls) 
    ...:                                                                                                                                                                                                           

In [37]: Test()                                                                                                                                                                                                    
<class '__main__.Test'>

In [38]: class Test: 
    ...:     def __init__(self): 
    ...:         print(self) 
    ...:                                                                                                                                                                                                           

In [39]: Test()                                                                                                                                                                                                    
<__main__.Test object at 0x7f46bf69e470>
Out[39]: <__main__.Test at 0x7f46bf69e470>
```

### 5 - Self or call it anything, doesnt matter

```python
In [29]: class Test: 
    ...:     def __init__(elf, x ): 
    ...:         elf.x = x 
    ...:                                                                                                                                                                                                           

In [30]: Test(2)                                                                                                                                                                                                   
Out[30]: <__main__.Test at 0x7f46bf6016d8>
```

### 4 - Numpy reshaping

```python
In [1]: import numpy                                                                                                                                                                                               

In [2]: numpy.arange(15)                                                                                                                                                                                           
Out[2]: array([ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 13, 14])

In [3]: numpy.arange(15).reshape(3,5)                                                                                                                                                                              
Out[3]: 
array([[ 0,  1,  2,  3,  4],
       [ 5,  6,  7,  8,  9],
       [10, 11, 12, 13, 14]])
```

### 3 - @total_ordering to do less work

- no need to implement all of the comparators

```python
from functools import total_ordering

@total_ordering
class Account:


    def __init__(self, owner, amount=0):
        self.owner = owner
        self.amount = amount
        self._transactions = []

    def __repr__(self):
        return 'Account({}, {})'.format(self.owner, self.amount)

    def __str__(self):
        return 'Account of {} with starting amount : {}'.format(self.owner, self.amount)

    def add_transaction(self, amount):
        if not isinstance(amount , int ):
            raise ValueError('please use int for amount')
        self._transactions.append(amount)

    @property
    def balance(self):
        return self.amount + sum(self._transactions)

    def __eq__(self, other):
        return self.balance == other.balance

    def __lt__(self, other):
        return self.balance < other.balance



acc = Account('gigs',10)


acc2 = Account('loki', 100)
acc2.add_transaction(20)
acc2.add_transaction(30)


print(acc.balance)
print(acc2.balance)


print ( acc2 > acc)
```

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
