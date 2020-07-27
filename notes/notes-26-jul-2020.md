# 26-jul-2020

### 6 - deepdiff Delta

- getting diffs and storing them in a serializable delta object. Might be handy someday.

```python
In [20]: from deepdiff import DeepDiff, Delta

In [22]: t1 = [1,2,3]

In [23]: t2 = ['a', 2, 3, 4]

In [24]: diff = DeepDiff(t1,t2)

In [25]: diff
Out[25]:
{'type_changes': {'root[0]': {'old_type': int,
   'new_type': str,
   'old_value': 1,
   'new_value': 'a'}},
 'iterable_item_added': {'root[3]': 4}}

In [26]: delta = Delta(diff)

In [27]: delta
Out[27]: <Delta: {'type_changes': {'root[0]': {'old_type': <class 'int'>, 'new_type': <class 'str'>, 'new_value': ...}>

In [28]: t1 + delta
Out[28]: ['a', 2, 3, 4]

In [29]: t1 + delta == t2
Out[29]: True

In [30]: delta.dumps()
Out[30]: b'\x80\x04\x95\x8d\x00\x00\x00\x00\x00\x00\x00}\x94(\x8c\x0ctype_changes\x94}\x94\x8c\x07root[0]\x94}\x94(\x8c\x08old_type\x94\x8c\x08builtins\x94\x8c\x03int\x94\x93\x94\x8c\x08new_type\x94h\x06\x8c\x03str\x94\x93\x94\x8c\tnew_value\x94\x8c\x01a\x94us\x8c\x13iterable_item_added\x94}\x94\x8c\x07root[3]\x94K\x04su.'

```

### 5 - deepdiff | DeepHash

```python
In [15]: from deepdiff import DeepHash

In [16]: obj = {1:2, "a": "b" }

In [17]: hash(obj)
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-17-e3ef47dce4f7> in <module>
----> 1 hash(obj)

TypeError: unhashable type: 'dict'

In [18]: DeepHash(obj)
Out[18]: {1: 'c1800a30c736483f13615542e7096f7973631fef8ca935ee1ed9f35fb06fd44e', 2: '610e2bb86cee5362640bd1ab01b8a4a4559cced9dd6058376894c041629a7b69', 'a': '980410da9522db17c3ab8743541f192a5ab27772a6154dbc7795ee909e653a5c', 'b': 'd05faa460a5b4fbbfbd54286ef4e3080f5420c61daf22663163af098cd10182c', '!>*id4346798976': 'bf5478de322aa033da36bf3bcf9f0599e13a520773f50c6eb9f2487377a7929b'}

In [19]: DeepHash(obj)[obj]
Out[19]: 'bf5478de322aa033da36bf3bcf9f0599e13a520773f50c6eb9f2487377a7929b'

```

### 4 - deepdiff DeepSearch

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

### 3 - deepdiff DeepDiff

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


### 2 - functools total_ordering

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

### 1 - math prod

```python3
from math import prod
prod([1,2,3]) #6
```
