# 26-jul-2020

### 4 - deepdiff | DeepSearch

```python
In [7]: from deepdiff import grep
In [8]: from pprint import pprint
In [9]: obj = ["long somewhere", "string", 0, "somewhere great!"]
In [10]: item = "somewhere"
In [11]: ds = obj | grep(item)
In [12]: pprint(ds)
{'matched_values': OrderedSet(['root[0]', 'root[3]'])}
In [13]: obj = ["something somewhere", {"long": "somewhere", "string": 2, 0: 0,
    ...: "somewhere": "around"}]
In [14]: pprint( obj | grep(item) )
{'matched_paths': OrderedSet(["root[1]['somewhere']"]),
 'matched_values': OrderedSet(['root[0]', "root[1]['long']"])}
 ```

### 3 - deepdiff | DeepDiff

- https://github.com/seperman/deepdiff
- Library seems to be useful for operations in deeply nested objects

```python
#DeepDiff example
In [1]: t1 = [1, 3, 1 ,4 ]

In [2]: t2 = [4,4,1]

In [3]: from deepdiff import DeepDiff
D
In [4]: DeepDiff(t1,t2)
Out[4]:
{'values_changed': {'root[0]': {'new_value': 4, 'old_value': 1},
  'root[1]': {'new_value': 4, 'old_value': 3}},
 'iterable_item_removed': {'root[3]': 4}}

In [5]: DeepDiff(t1,t2, ignore_order=True)
Out[5]: {'iterable_item_removed': {'root[1]': 3}}

In [6]: DeepDiff(t1,t2, ignore_order=True, report_repetition=True)
Out[6]:
{'iterable_item_removed': {'root[1]': 3},
 'repetition_change': {'root[3]': {'old_repeat': 1,
   'new_repeat': 2,
   'old_indexes': [3],
   'new_indexes': [0, 1],
   'value': 4},
  'root[0]': {'old_repeat': 2,
   'new_repeat': 1,
   'old_indexes': [0, 2],
   'new_indexes': [2],
   'value': 1}}}

In [7]:
```


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
