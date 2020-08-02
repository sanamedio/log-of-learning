# 02-aug-2020

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
