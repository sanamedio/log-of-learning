# 23-dec-2020

### 13 - buy and sell stocks 2

https://www.geeksforgeeks.org/stock-buy-sell/

```python
def max_profit(prices):

    n = len(prices)
    cost = 0
    maxcost = 0

    if not n:
        return 0

    min_price = prices[0]

    for i in range(n):
        min_price = min(min_price, prices[i])

        cost = prices[i] - min_price

        maxcost = max(maxcost, cost)

    return maxcost


print(max_profit([0, 0, 0]))
print(max_profit([1, 2, 3]))
print(max_profit([3, 2, 1]))
print(max_profit([1, 1, 1]))
print(max_profit([1, 0, 1, 0, 1]))
```

### 12 - buy and sell stocks 1

```python
def stock_buy_sell(price):
    n = len(price)
    if n == 1:
        return

    i = 0
    while i < n - 1:
        while (i < (n - 1)) and (price[i + 1] <= price[i]):
            i += 1

        if i == n - 1:
            break

        buy = i
        i += 1

        while (i < n) and (price[i] >= price[i - 1]):
            i += 1

        sell = i - 1

        print(buy, sell)


stock_buy_sell([10, 18, 26, 31, 4, 53, 69])
```


### 11 - generate sorted zigzag array from two array

```python
def generate_sorted(A, B, C, i, j, m, n, length, flag):

    if flag:

        if length:
            print(C[: length + 1])

        for k in range(i, m):

            if not length:

                C[length] = A[k]

                generate_sorted(A, B, C, k + 1, j, m, n, length, not flag)
            else:
                if A[k] > C[length]:
                    C[length + 1] = A[k]
                    generate_sorted(A, B, C, k + 1, j, m, n, length + 1, not flag)
    else:
        for l in range(j, n):

            if B[l] > C[length]:
                C[length + 1] = B[l]
                generate_sorted(A, B, C, i, l + 1, m, n, length + 1, not flag)


def generate(A, B):
    m = len(A)
    n = len(B)

    C = []
    for i in range(m + n + 1):
        C.append(0)

    generate_sorted(A, B, C, 0, 0, m, n, 0, True)


A = [0, 1, 2]
B = [16, 1, 5]

generate(A, B)
```

### 10 - zigzag pattern

```python
def zig_zag(arr):
    n = len(arr)
    flag = True

    for i in range(n - 1):

        if (flag and arr[i] > arr[i + 1]) or (not flag and arr[i] < arr[i + 1]):
            arr[i], arr[i + 1] = arr[i + 1], arr[i]
        flag = not flag
    return arr


print(zig_zag([1, 2, 3, 4, 5, 6]))
```

### 9 - count lesser triplets

https://www.geeksforgeeks.org/count-triplets-with-sum-smaller-that-a-given-value/

```python
def count_triplets(arr: list, total: int):

    arr.sort()
    n = len(arr)

    ans = 0

    for i in range(0, n - 2):

        j = i + 1
        k = n - 1

        while j < k:

            if arr[i] + arr[j] + arr[k] >= total:
                k = k - 1
            else:
                ans += k - j
                j = j + 1
    return ans


if __name__ == "__main__":
    print(count_triplets([6, 1, 2, 3, 4, 5], 11))
```


### 8 - finding palindrome partition

https://www.geeksforgeeks.org/given-a-string-print-all-possible-palindromic-partition/

```python
def is_palindrome(string: str,  low: int, high: int):
    while low < high:
        if string[low] != string[high]:
            return False
        low += 1
        high -= 1
    return True


def find_pal_part(all_part: list, curr_part:list,
        start:int, n:int, string:str):

    if start >= n:

        x = curr_part.copy()

        all_part.append(x)
        return

    for i in range(start, n):
        if is_palindrome(string, start, i):
            curr_part.append(string[start:i + 1])
            find_pal_part(all_part, curr_part, i+1, n, string)
            curr_part.pop()

def all_pal_part(string: str):

    n = len(string)

    all_part = []

    curr_part = []

    find_pal_part(all_part, curr_part, 0, n, string)

    for i in range(len(all_part)):
        for j in range(len(all_part[i])):
            print(all_part[i][j], end = " ")
        print()

if __name__ == "__main__":
    string = "xoxoxoxi"
    all_pal_part(string)
```


### 7 - reverse string avoiding special chars

```python
def reverse_special(arr) 
    
    r = len(arr) - 1
    l = 0; 
  
    while (l < r):
        if (!isAlphabet(str[l])):
            l+=1 
        elif(!isAlphabet(str[r])):
            r-=1
        else:
            swap(str[l], str[r]) 
            l+=1 
            r-=1 
        
```

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
