# 05-jan-2021

### 2 - number of steps required to reduce to 1

https://www.geeksforgeeks.org/number-of-steps-required-to-convert-a-binary-number-to-one/

one is to simulate the process, but that would be slow. Next thing is to observe multiple optimizations and handle to process with those cases. 

```python
def calc(s):
    if len(s) == 0:
        return 0

    count = 0

    i = len(s) - 1
    while i > 0:
        if s[i] == "0":
            count += 1
            i -= 1
        else:
            count += 1
            while s[i] == "1" and i > 0:
                count += 1
                i -= 1
            if i == 0:
                count += 1
            s = s[:i] + "1" + s[i + 1 :]
    return count


print(calc("10000100000"))
```

this program looks like a state machine; all programs are though.

### 1 - k smallest element in sorted matrix

The idea is to look at the N rows as N parallel lists, whose first item we put into heap. Then we keep taking out elements, and adding elements into heap from the row which took it out from

So, in general; for any sort of organized data structure where we have an order, we can make heap connect to peak and sort of find the k minimum accross just by updaing the correponding points which gets popped out

```python
import heapq
def solve(matrix, n):
    heap = []
    for i in range(len(matrix)):
        heap.append((matrix[i][0], i, 0))

    heapq.heapify(heap)
    val = heap[0][0]
    for i in range(n + 1):
        val, row, col = heapq.heappop(heap)
        if col + 1 < len(matrix[row]):
            heapq.heappush(heap, (matrix[row][col + 1], row, col + 1))
    return val
