# 15-jan-2021

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
