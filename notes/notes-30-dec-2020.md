# 30-dec-2020

### 3 - python quine

https://stackoverflow.com/questions/6223285/shortest-python-quine
```python
print((lambda s:s%s)('print((lambda s:s%%s)(%r))'))
```

### 2 - insort

keeping a sorted array while inserting

```python
>>> from bisect import insort
>>> arr = []
>>> insort(arr,12)
>>> arr
[12]
>>> insort(arr,1)
>>> arr
[1, 12]
>>> insort(arr,25)
>>> arr
[1, 12, 25]
>>> insort(arr,2)
>>> arr
[1, 2, 12, 25]
>>>
```

### 1 - bisect right

https://github.com/python/cpython/blob/master/Lib/bisect.py

the magic is in whether you are returning lo or hi

```python
lo = 0    
hi = len(nums)

while lo < hi:
    mid = (lo + hi) // 2
    if target < nums[mid]:
        hi = mid
    else:
        lo = mid + 1

return hi
```
