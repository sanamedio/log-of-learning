# 06-aug-2020

### 1 - heapq

```python
>>> nums = [1, 8, 2 , 23 , -4, 37 ]
>>> import heapq
>>> heap = list(nums)
>>> heapq.heapify(heap)
>>> heap
[-4, 1, 2, 23, 8, 37]
>>> heapq.heappop(heap)
-4
>>> heapq.heappop(heap)
1
>>> heapq.heappop(heap)
2
```
