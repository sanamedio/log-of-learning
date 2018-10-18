# 19-oct-2018

### 2 - Naming list slices

```python
>>> a = [0, 1, 2, 3, 4, 5]
>>> LASTTHREE = slice(-3, None)
>>> LASTTHREE
slice(-3, None, None)
>>> a[LASTTHREE]
[3, 4, 5]
```

### 1 - get python config information

```bash
$ python -m sysconfig
```
