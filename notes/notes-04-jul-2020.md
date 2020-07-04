# 04-jul-2020

### 1 - accumulate from itertools

```python
In [1]: import itertools

In [2]: import functools

In [3]: lis = [1,3,4,10,4]

In [4]: list(itertools.accumulate(lis, lambda x,y: x+y))
Out[4]: [1, 4, 8, 18, 22]

In [5]: functools.reduce(lambda x,y: x+y, lis)
Out[5]: 22
```
