# 05-jan-2021

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
