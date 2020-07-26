# 26-jul-2020

### 2 - functools.total_ordering

- https://docs.python.org/3/library/functools.html#functools.total_ordering

```python
In [3]: from functools import total_ordering

In [4]: @total_ordering
   ...: class Student:
   ...:
   ...:     def __init__(self,name):
   ...:         self.name = name
   ...:
   ...:     def __eq__(self, other):
   ...:         return self.name  == other.name
   ...:
   ...:     def __lt__(self, other):
   ...:         return self.name < other.name
   ...:

In [5]: Student("lokendra") > Student("loki")
Out[5]: False

```

### 1 - math.prod

```python3
from math import prod
prod([1,2,3]) #6
```
