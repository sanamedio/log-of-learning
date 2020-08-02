# 02-aug-2020

### 13 - checking errors in unittest

```python
import unittest

class TestNoneTypeError(unittest.TestCase):


    def setUp(self):
        self.testListNone = None

    def testListSlicing(self):
        with self.assertRaises(TypeError) as ctx:
            self.testListNone[:1]

        self.assertEqual("'NoneType' object is not subscriptable", str(ctx.exception))

unittest.main()
```

### 12 - perf_counter and process_time

https://stackoverflow.com/q/25785243/2091949

```python
In [11]: from time import perf_counter as clock

In [12]: clock()
Out[12]: 968.82726198

In [13]: clock()
Out[13]: 969.962888333

In [14]: from time import process_time

In [15]: process_time()
Out[15]: 3.524516

In [16]: process_time()
Out[16]: 3.561495

In [17]: process_time()
Out[17]: 3.59703
```

### 11 - ctypes Structure objects

```python
In [1]: from ctypes import *

In [2]: class X(Structure):
   ...:     _fields_ = [("a",c_int),("b", c_int)]
   ...:

In [3]: x = X()

In [4]: dir(x)
Out[4]:
['__class__',
 '__ctypes_from_outparam__',
 '__delattr__',
 '__dict__',
 '__dir__',
 '__doc__',
 '__eq__',
 '__format__',
 '__ge__',
 '__getattribute__',
 '__gt__',
 '__hash__',
 '__init__',
 '__init_subclass__',
 '__le__',
 '__lt__',
 '__module__',
 '__ne__',
 '__new__',
 '__reduce__',
 '__reduce_ex__',
 '__repr__',
 '__setattr__',
 '__setstate__',
 '__sizeof__',
 '__str__',
 '__subclasshook__',
 '__weakref__',
 '_b_base_',
 '_b_needsfree_',
 '_fields_',
 '_objects',
 'a',
 'b']

In [5]: x.a
Out[5]: 0

In [6]: x.b
Out[6]: 0

In [7]: x.a = 42

In [8]: x.b = 96

In [9]: x.a
Out[9]: 42

In [10]: x.b
Out[10]: 96
```

### 10 - assertRaises

[stackoverflow](https://stackoverflow.com/questions/6103825/how-to-properly-use-unit-testings-assertraises-with-nonetype-objects)
https://ongspxm.gitlab.io/blog/2016/11/assertraises-testing-for-errors-in-unittest/

```python
from unittest import TestCase

class TestNoneTypeError(TestCase):

    def setUp(self):
        self.testListNone = None

    def testListSlicing(self):
        with self.assertRaises(TypeError) as ctx:
            self.testListNone[:1]

        self.assertEqual("'NoneType' object is not subscriptable", str(ctx.exception))
```

run via `python -m unittest <filename.py>` or import `unittest` and do a `unittest.main()` in the end.

### 9 - hexlify

```python
from binascii import hexlify
hexlify(memoryview(b"assdsd")).decode()
```

### 8 - pydispatcher

`pip install pydispatcher`

```python
from pydispatch import dispatcher

SIGNAL = "my-first-signal"


def handle_event( sender ):
    print("Signal was ent by ", sender)


dispatcher.connect( handle_event, signal=SIGNAL, sender=dispatcher.Any)


first_sender = object()
second_sender = {}


def main():
    dispatcher.send( signal=SIGNAL, sender=first_sender)
    dispatcher.send( signal=SIGNAL, sender=second_sender)

main()
```

### 7 - minimalistic hooks

https://stackoverflow.com/questions/4309607/whats-the-preferred-way-to-implement-a-hook-or-callback-in-python

```python
class hookify(object):

    def __init__(self, func):
        self.callbacks = []
        self.basefunc = func

    def __iadd__(self, func):
        if callable(func):
            self.callbacks.append(func)
        return self
    
    def callback(self, func):
        if callable(func):
            self.callbacks.append(func)
        return func
    
    def __call__(self, *args, **kwargs):
        result = self.basefunc(*args, **kwargs)
        for func in self.callbacks:
            newresult = func(result)
            result = result if newresult is None else newresult
        return result


@hookify
def intfactory(num):
    return int(num)

def notify(num):
    print("notify:", num)

def increment(num):
    return num + 1

intfactory += notify
intfactory += increment
intfactory += lambda num: num*2
intfactory += notify

intfactory(3)
```


### 6 - getting function signature

```python
>>> import inspect
>>> inspect.getargspec([].index)
<stdin>:1: DeprecationWarning: inspect.getargspec() is deprecated since Python 3.0, use inspect.signature() or inspect.getfullargspec()
ArgSpec(args=['self', 'value', 'start', 'stop'], varargs=None, keywords=None, defaults=(0, 9223372036854775807))
>>> inspect.signature([].index)
<Signature (value, start=0, stop=9223372036854775807, /)>
>>> inspect.getfullargspec([].index)
FullArgSpec(args=['self', 'value', 'start', 'stop'], varargs=None, varkw=None, defaults=(0, 9223372036854775807), kwonlyargs=[], kwonlydefaults=None, annotations={})
>>>
```

### 5 - extending a list

```python
>>> l = ["a","b" ]
>>> l[len(l):] = ["c","d"]
>>> l
['a', 'b', 'c', 'd']
>>> l[len(l):] = {"x":"y","Z":"W" }
>>> l
['a', 'b', 'c', 'd', 'x', 'Z']
>>>```
```

### 4 - columnwise matrix

```python
>>> matrix = [
...     [1, 2, 3, 4],
...     [5, 6, 7, 8],
...     [9, 10, 11, 12],
... ]

>>> [[row[i] for row in matrix] for i in range(4)]
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
```

### 3 - round function

```python
>>> from math import pi
>>> [str(round(pi, i)) for i in range(1, 6)]
['3.1', '3.14', '3.142', '3.1416', '3.14159']
```

### 2 - isnan

https://docs.python.org/3/tutorial/datastructures.html#comparing-sequences-and-other-types

```python
>>> import math
>>> raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
>>> filtered_data = []
>>> for value in raw_data:
...     if not math.isnan(value):
...         filtered_data.append(value)
...
>>> filtered_data
[56.2, 51.7, 55.3, 52.5, 47.8]
```

### 1 - math related funcs

- `math.inf` : positive infinity
- `float('-inf')` : negative infinity
- `floag(`inf`)`  : positive infinity
