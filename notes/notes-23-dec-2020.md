# 23-dec-2020

### 6 - pythagorean triplet with hashing

```python
import math 
  
def checkTriplet(arr, n): 
    maximum = 0
  
    for i in range(n): 
        maximum = max(maximum, arr[i]) 
  
    hash = [0]*(maximum+1) 
  
    for i in range(n): 
        hash[arr[i]] += 1
  
    for i in range(1, maximum+1): 
        if (hash[i] == 0): 
            continue
  
        for j in range(1, maximum+1): 
            if ((i == j and hash[i] == 1) or hash[j] == 0): 
                continue
  
            val = int(math.sqrt(i * i + j * j)) 
  
            if ((val * val) != (i * i + j * j)): 
                continue
  
            if (val > maximum): 
                continue
  
            if (hash[val]): 
                return True
    return False
```

### 5 - pythagorean triplet

https://www.geeksforgeeks.org/find-pythagorean-triplet-in-an-unsorted-array/

```python
# meet in the middle approach
def is_triplet(ar, n): 
    for i in range(n): 
        ar[i] = ar[i] * ar[i] 
  
    ar.sort() 
  
    for i in range(n-1, 1, -1): 
        j = 0
        k = i - 1
        while (j < k): 
            if (ar[j] + ar[k] == ar[i]): 
                return True
            else: 
                if (ar[j] + ar[k] < ar[i]): 
                    j = j + 1
                else: 
                    k = k - 1
    return False
```


### 4 - largest continuous section of array with duplicates

we ignore the duplicate subarrays
https://www.geeksforgeeks.org/length-largest-subarray-contiguous-elements-set-2/

```python
def find_length(arr, n): 
    max_len = 1
    for i in range(0,n - 1): 
  
        myset = set() 
        myset.add(arr[i]) 
  
        mn = arr[i] 
        mx = arr[i] 
        for j in range(i + 1,n): 
  
            if arr[j] in myset: 
                break
            myset.add(arr[j]) 
            mn = min(mn, arr[j]) 
            mx = max(mx, arr[j]) 
  
            if mx - mn == j - i: 
                max_len = max(max_len, mx - mn + 1) 
  
    return max_len 
```


### 3 - largest contiguous section of array

Array with disctinct elements
Observe that to have a contiguous section of distinct element and maximise it; min-max == i-j

```python
def find_length(arr, n): 
	
	max_len = 1
	for i in range(n - 1): 
	
		mn = arr[i] 
		mx = arr[i] 

		for j in range(i + 1, n): 
		
			mn = min(mn, arr[j]) 
			mx = max(mx, arr[j]) 

			if ((mx - mn) == j - i): 
				max_len = max(max_len, mx - mn + 1) 
		
	return max_len 
```

### 2 - smallest unrepresented element in sorted array

Minimum positive integer which cannot be represented by summing the subset of array

```python
def findSmallest(arr, n): 
    res = 1
    for i in range (0, n ): 
        if arr[i] <= res: 
            res = res + arr[i] 
        else: 
            break
    return res 
```


### 1 - krukshal algo


```python
class Graph:

    def __init__(self, vertices):

        self.V = vertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):

        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruksal_mst(self):

        result = []

        i = 0
        e = 0
        self.graph = sorted(self.graph,
                            key=lambda item: item[2])

        parent = []
        rank = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e += 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)
```
