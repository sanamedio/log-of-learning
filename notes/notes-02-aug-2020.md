# 02-aug-2020

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

### 003 - round function

```python
>>> from math import pi
>>> [str(round(pi, i)) for i in range(1, 6)]
['3.1', '3.14', '3.142', '3.1416', '3.14159']
```

### 002 - isnan

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

### 001 - math related funcs

- `math.inf` : positive infinity
- `float('-inf')` : negative infinity
- `floag(`inf`)`  : positive infinity
