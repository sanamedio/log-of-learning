# 30-dec-2020

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
