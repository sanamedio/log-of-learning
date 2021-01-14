# 15-jan-2021

### 13 - remove duplicates

```python
def remove_duplicates(L):
    it = L 
    while it:
        next_distinct = it.next
        while next_distinct and next_distinct.data == it.data:
            next_distinct = next_distinct.next
        it.next = next_distinct
        it = next_distinct
    return L
```

### 12 - remove kth last element

this is such a nice approach; no need to calculate size of list and retraverse(as I always did in past)
```python
def remove_kth_last(L, k):
    dummy_head = ListNode(0, L)
    first = dummy_head.next
    
    for _ in range(k):
        first = first.next
    
    second = dummy_head
    
    while first:
        first, second = first.next, second.next
        
    second.next = second.next.next
    return dummy_head.next
```

### 11 - overlapping lists


this has some interesting case by case handling(REVISE)
```python
def overlapping_list(L1,L2):
    root1, root2 = has_cycle(L1), has_cycle(L2)
    
    if not root1 and not root2:
        return overlapping_no_cycle_lists(L1,L2)

    elif (root1 and not root2) or (not root and root2):
        return None
        
    temp = root2
    
    while True:
        temp = temp.next
        if temp is root1 or temp is root2:
            break
            
    if temp is not root1:
        return None
        
    def distance(a, b):
        dis = 0
        while a is not b:
            a = a.next
            dis += 1
        return dis
    
    stem1_length, stemp2_length = distance(L1, root1), distance(L2, root2)
    
    if stem1_length > stem2_length:
        L2, L1 = L1, L2
        root1, root2 = root2, root1
    
    for _ in range(abs(stem1_length - stem2_length)):
        L2 = L2.next
    
    while L1 is not L2 and L1 is not root1 and L2 is not root2:
        L1, L2  = L1.next, L2.next
    
    return L1 if L1 is L2 else root1
```


with assumption is they are cycle free

```python
def overlapping_no_cycle_lists(L1, L2):
    def length(L):
        length = 0
        while L:
            length += 1
            L = L.next
        return length
    
    L1_len, L2_len = length(L1), length(L2)
    
    if L1_len > L2_len:
        L1, L2 = L2, L1
        
    for _ in range(abs(L1_len - L2_len)):
        L2 = L2.next
        
    while L1 and L2 and L1 is not L2:
        L1, L2 = L1.next, L2.next
    
    return L1
```

### 10 - cycle test in linked list


```python
def has_cycle(head):
    fast = slow = head
    while fast and fast.next and fast.next.next:
        slow, fast = slow.next, fast.next.next
        
        if slow is fast:
            slow = head
            while slow is not fast:
                slow, fast = slow.next, fast.next
            
            return slow
    return None
```

finds length of cycle as well
```python
def has_cycle(head):
   def cycle_len(end):
      start, step = end, 0
      while True:
        step += 1
        start = start.next
        if start is end:
            return step
  
  fast = slow = head
  
  while fast and fast.next and fast.next.next:
    slow, fast = slow.next, fast.next.next
    if slow is fast:
        cycle_len_advanced_iter = head
        for _ in range(cycle_len(slow)):
            cycle_len_advanced_iter = cycle_len_advanced_iter.next
        
        it = head
        
        while it is not cycle_len_advanced_iter:
            it = it.next
            cycle_len_advanced_iter = cycle_len_advanced_iter.next
        
        return it

  return None
```


### 9 - reverse sublist


```python
#7.2
def reverse_sublist(L, start, finish):
    dummy_head = sublist_head = ListNode(0,L)
    
    for _ in range(1, start):
        sublist_head = sublist_head.next
    
    sublist_iter = sublist_head.next
    
    for _ in range(finish - start):
        temp = sublist_iter.next
        #confusing way of writing it
        sublist_iter.next, temp.next, sublist_head.next = (temp.next, sublist_head.next, temp)
    
    return dummy_head.next
```

### 8 - merge sorted linked lists

iterative version

```python
def merge_sorted_ll(L1, L2):
    dummy_head = tail = ListNode()
    
    while L1 and L2:
        if L1.data < L2.data:
            tail.next, L1 = L1, L2.next
        else;
            tail.next, L2 = L2, L2.next
        tail = tail.next
    
    tail.next = L1 or L2
    return dummy_head.next
```

### 7 - rabin karp

idea is to keep a rolling hash to not repeat expensive comparisions

```python
def rabin_karp(t, s):
    import functools

    if len(s) > len(t):
        return -1

    BASE = 26

    t_hash = functools.reduce(lambda h, c: h * BASE + ord(c), t[: len(s)], 0)
    s_hash = functools.reduce(lambda h, c: h * BASE + ord(c), s, 0)

    power_s = BASE ** max(len(s) - 1, 0)

    for i in range(len(s), len(t)):
        if t_hash == s_hash and t[i - len(s) : i] == s:
            return i - len(s)

        t_hash -= ord(t[i - len(s)]) * power_s
        t_hash = t_hash * BASE + ord(t[i])

    if t_hash == s_hash and t[-len(s) :] == s:
        return len(t) - len(s)

    return -1
```

### 6 - ispalindromic

```python
# Note that s[~i] for i in [0,len(s) - 1] is s[-(i + 1)]
def is_palindromic(s):
  return all(s[i] == s[~i] for i in range(len(s) // 2))
```

### 5 - pascal triangle

```python
def gen_pascal(n):
  result [[1]*(i+1) for i in range(n)]
  
  for i in range(n):
    for j in range(1,i):
      result[i][j] = result[i-1][j-1] + result[i-1][j]
  
  return result
```

### 4 - rotate matrix

EOPI book pg. 65

``` python
# A[-i] for i in [0, len(A) - 1] is A[-(i + 1)]
def rotate_matrix(square_matrix):
  matrix_size = len(square_matrix) - 1
  for i in range(len(square_matrix) // 2):
    for j in range(i, matrix_size - i):
      (square_matrix[i][j], square_matrix[~j][i], square_matrix[~i][~j], square_matrix[j][~i])=
        (square_matrix[~j][i], square_matrix[~i][~j], square_matrix[j][~i], square_matrix[i][j] )
```

a wrapper can also give a view of rotated matrix with copy on write

```python
class RotatedMatrix:
  def __init__(self, square_matrix):
    self._matrix = square_matrix
    
  def read(self,i,j):
    return self._matrix[~j][i]
    
  def write(self, i, j, v):
    self._matrix[~j][i] =  v
```

### 3 - spiral ordering of matrix

nice trick with anding 3, gets equivalent to mod 4
```
>>> 0 & 3
0
>>> 1 & 3
1
>>> 2 & 3
2
>>> 3 & 3
3
>>> 4 & 3
0
>>>
```

```python
def matrix_in_spiral_order(matrix):
  SHIFT = ((0,1), (1,0), (0,-1), (-1,0))
  direction = x = y = 0
  
  spiral_ordering = []
  
  for _ in range(len(square_matrix)**2):
    spiral_ordering.append(square_matrix[x][y])
    square_matrix[x][y] = 0
    next_x, next_y = x + SHIFT[direction][0], y+ SHIFT[direction][1]
    if (next_x not in range(len(square_matrix))
      or next_y not in range(len(square_matrix))
      or square_matrix[next_x][next_y] == 0):
      direction = (direction + 1) & 3
      next_x, next_y = x + SHIFT[direction][0], y + SHIFT[direction][1]
    x, y = next_x, next_y
  
  return spiral_ordering
```

### 2 - valid sudoku

```python
def is_valid_sudoku(partial_assignment):
  def has_duplicate(block):
    block = list(filter(lambda x: x != 0, block))
    return len(block) != len(set(block))
    
  n = len(partial_assignment)
  
  if any(
    has_duplicate([partial_assignment[i][j] for j in range(n)]) or
    has_duplicate([partial_assignment[j][i] for j in range(n)])
    for i in range(n)):
    return False
  
  region_size = int(math.sqrt(n))
  return all(not has_duplicate([
    partial_assignment[a][b]
    for a in range(region_size * I, region_size * (I + 1))
    for b in range(region_size * J, region_size * (J + 1))
    ]) for I in range(region_size) for J in range(region_size))
```  


### 1 - nonuniform random number

p.g 59 EOPI

```python
def nonuniform_random_number_generator(values, probs):
  prefix_sum_of_probs = list(itertools.accumulate(probs))
  interval_idx = bisect.bisect(prefix_sum_of_probs, random.random())
  return values[interval_idx]
```
