# 05-jan-2021

### 4 - min perfect squares summing upto n

dp
```
from math import ceil, sqrt
 
def getMinSquares(n):
 
    dp = [0, 1, 2, 3]
 
    for i in range(4, n + 1):
         
        dp.append(i)
 
        for x in range(1, int(ceil(sqrt(i))) + 1):
            temp = x * x;
            if temp > i:
                break
            else:
                dp[i] = min(dp[i], 1 + dp[i-temp])
 
    return dp[n]
 
print(getMinSquares(6))
```


bfs
```python
import sys
 
def numSquares(n) : 
 
    visited = [0]*(n + 1) 
    q = []
    ans = sys.maxsize
    q.append([n, 0])
     
    visited[n] = 1
    while(len(q) > 0) :
         
        p = q[0]
        q.pop(0)
     
        if(p[0] == 0) :
            ans = min(ans, p[1])
     
        i = 1
        while i * i <= p[0] :
           
            path = p[0] - i * i
         
            if path >= 0 and (visited[path] == 0 or path == 0):
                visited[path] = 1         
                q.append([path,p[1] + 1])
             
            i += 1
     
    return ans
 
print(numSquares(12))
```

### 3 - derandomize virtual memory

https://youtu.be/JRyrhsx-L5Y?t=696

```bash
echo 0 > /proc/sys/kernel/randomize_va_space
```


### 2 - number of steps required to reduce to one

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
