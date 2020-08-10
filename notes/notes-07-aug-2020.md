# 07-aug-2020

### 4 - merging two dicts

```python
a = dict()
b = dict()
a.update(b)
```

```python
a = dict()
b = dict()
c = { **a, **b }
```

### 3 - accumulate from itertools

```python
>>> from itertools import accumulate
>>> accumulate([1,2,3,4])
<itertools.accumulate object at 0x10ad3ef40>
>>> list(accumulate([1,2,3,4]))
[1, 3, 6, 10]
```

### 2 - groupby from itertools

```python
>>> [ (k,list(g)) for (k,g) in groupby([0,0,0,1,1,1,0,0,0])]
[(0, [0, 0, 0]), (1, [1, 1, 1]), (0, [0, 0, 0])]
```

### 1 - weird python scoping

```python
>>> [f(1) for f in [lambda y: x+y for x in range(10)]]
[10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
```
