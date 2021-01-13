# 13-jan-2021



### 17 - buy and sell stock variants

buy sell once
```python
def buy_and_sell_stock_once(prices):
  min_price_so_far, max_profit = float('inf'), 0.0

  for price in prices:
    max_profit_sell_today = price - min_price_so_far
    max_profit = max( max_profit, max_profit_sell_today)
    min_price_so_far = mihn( min_price_so_far, price)
  
  return max_profit
```



buy sell twice - calculate one buy profits and then two buy profits derived from that in another phase; need to see to proof that it's optimal
```python
def buy_and_sell_stock_twice(prices):
  max_total_profit, min_price_so_far = 0.0, float('inf')
  first_buy_sell_profits = [0] * len(prices)

  for i, price in enumerate(prices):
    min_price_so_far = min(min_price_so_far, price)
    max_total_profit = max(max_total_profit, price - min_price_so_far)
    first_buy_sell_profits[i] = max_total_profit

  max_price_so_far = float('-inf')
  for i, price in reversed(list(enumerate(prices[1:], 1))):
    max_price_so_far = max(max_price_so_far, price)
    max_total_profit = max(
        max_total_profit,
        max_price_so_far - price + first_buy_sell_profits[i-1])
  return max_total_profit
```

### 16 - delete duplicates from an array

```python
def delete_duplicates(A):
  if not A:
    return 0

  write_index = 1
  for i in range(1, len(A)):
    if A[write_index - 1] != A[i]:
      A[write_index] = A[i]
      write_index += 1
  
  return write_index
```

### 15 - furtherst reach by jumping

standard problem about reachability given indexes and steps you can take from there

```python
def can_reach_end(A):
  furthest_reach_so_far, last_index = 0, len(A) - 1
  i = 0
  while i <= furthest_reach_so_far and furthest_reach_so_far < last_index:
    furthest_reach_so_far = max(furthest_reach_so_far, A[i] +i )
    i += 1
  return furthest_reach_so_far >= last_index
```

### 14 - bigint multiplication

straightforward school method of multiplication simulated

```python
# 5.3 section EOPI
def multiply(num1, num2):
  sign = -1 if (num1[0] < 0) ^ (num2[0] < 0) else 1
  num1[0], num2[0] = abs(num1[0]), abs(num2[0])

  result = [0] * (len(num1) + len(num2))

  for i in reversed(range(len(num1))):

    for j in reversed(range(len(num2))):

      result[i + j + 1] += num1[i] * num2[j]
      result[i + j] += result[i + j + 1] // 10
      result[i + j + 1] %= 10

  result = result[next((i for i,x in enumerate(result) if x != 0), len(result)):] or [0]

  return [sign * result[0]] + result[1:]
```


### 13 - addition on an array

D = D + 1, when D is an array represending a base 10 number
```python
def plus_one(A):
  A[-1] += 1
  for i in reversed(range(1, len(A))):
    if A[i] != 10:
      break
    A[i] = 0
    A[i-1] += 1
  
  if A[0] == 10: # for example 999
    A[0] = 1
    A.append(0)
  return A
```

```bash
(Pdb) plus_one([0,0,0])
[0, 0, 1]
(Pdb) plus_one([0,0,9])
[0, 1, 0]
(Pdb) plus_one([9,9,9])
[1, 0, 0, 0]
```

### 12 - dutch flag partition

single pass
```python
def dutch_flag_partition(pivot_index, A):

  pivot = A[pivot_index]
  
  smaller, equal, larger = 0, 0, len(A)
  
  while equal < larger:
  
    if A[equal] < pivot:
      A[smaller], A[equal] = A[equal], A[smaller]
      smaller, equal = smaller + 1, equal + 1
    elif A[equal] == pivot:
      equal += 1
    else:
      larger -= 1
      A[equal], A[larger] = A[larger], A[equal]
```


linear
```python
RED, WHITE, BLUE = range(3)

def dutch_flag_partition(pivot_index, A):
  pivot = A[pivot_index]
  
  smaller = 0
  for i in range(len(A)):
    if A[i] < pivot:
      A[i], A[smaller] = A[smaller], A[i]
      smaller += 1
      
  larger = len(A) - 1
  
  for i in reversed(range(len(A))):
    if A[i] < pivot:
      break
    elif A[i] > pivot:
      A[i], A[larger] = A[larger], A[i]
      larger -= 1
```

brute force
```python
RED, WHITE, BLUE = range(3)

def dutch_flag_partition(pivot_index, A):
  pivot = A[pivot_index]
  
  for i in range(len(A)):
    for j in range(i+1, len(A)):
      if A[j] < pivot:
        A[i], A[j] = A[j], A[i]
        break
  
  for i in reversed(range(len(A))):
    if A[i] < pivot:
      break
      
    for j in reversed(range(i)):
      if A[j] > pivot:
        A[i], A[j] = A[j], A[i]
        break

```

### 11 - even odd sort

```python
def even_odd(A):
  next_even, next_odd = 0, len(A) - 1
  while next_even < next_odd:
    if A[next_even] % 2 == 0:
      next_even += 1
    else:
      A[next_even], A[next_odd] = A[next_odd], A[next_even]
      next_odd -= 1
```

### 10 - rectangle intersection

sides are parallel to x and y axis and we have to return the intersection rectangle if there is one. We are representing the rectangle with one point and width and height

```python
Rectangle = collections.namedtuple("Rectangle", ("x", "y", "width", "height"))

def intersect_rectangle(R1, R2):
  def is_intersect(R1, R2):
    return (R1.x <= R2.x + R2.width and R1.x + R1.width >= R2.x and R1.y <= R2.y + R2.height and R1.y + R1.height >= R2.y)
    
  if not is_intersect(R1, R2):
    return Rectangle(0, 0, -1, -1) # No intersection
  
  return Rectangle(
    max(R1.x, R2.x),
    max(R1.y, R2.y),
    min(R1.x + R1.width, R2.x + R2.width) - max(R1.x, R2.x),
    min(R1.y + R1.height, R2.y + R2.height) - max(R1.y, R2.y))
```

### 9 - generate uniform random numbers

Assuming we have zero_one_random() which gives us random bits
we find out the capacity of range, let our while loop build a result worthy of that range by giving it that many size times to do flip, and then we take out whatever we get and add it to lower_bound (example from EOPS book)

```python
def uniform_random(lower_bound, upper_bound):

  number_of_outcomes = upper_bound - lower_bound + 1
  
  while True:
    result, i = 0, 0
    while ( 1 << i ) < number_of_outcomes:
      # zero_one_random() is provided random number generator
      result = (result << 1) | zero_one_random()
      i += 1
    if result < number_of_outcomes:
      break
  
  return result + lower_bound
```
    

### 8 - integer is palindrome

```python
def is_palindrome_number(x):
  if x <= 0:
    return x == 0
    
  num_digits = math.floor(math.log10(x)) + 1
  msd_mask = 10**(num_digits - 1)
  for i in range(num_digits // 2):
    if x // msd_mask != x % 10:
      return False
    x %= msd_mask
    x //= 10
    msd_mask //= 100
  return True
```


### 7 - reverse digits

```python
def reverse(x):
  result, x_remaining = 0, abs(x)
  while x_remaining:
    result = result * 10 + x_remaining % 10
    x_remaining //= 10
  return -result if x < 0 else result
```

### 6 - compute x pow y

```python
def power(x, y):
  result, power = 1.0, y
  if y < 0:
    power, x = -power, 1.0/x
  while power:
    if power & 1:
      result *= x
    x, power = x*x, power >> 1
  return result
```

### 5 - computing quotient with add, subtract and shift

when we say 5 divmod 2 = 2,1 it means we can take out two 2's from 5 and leave 1 as remainder. These bit operations work similarly to find out the quotient.

```python
#4.6 section
def divide(x,y):
  result, power = 0, 32
  y_power = y << power
  while x >= y:
    while y_power > x:
      y_power >>= 1
      power -= 1
    
    result += 1 << power
    x -= y_power
  return result
```

### 4 - computer a x b without arithimetic operators

this seems to be loosely based on formula ```x*y = x/2 * 2*y```

```python
#4.6 section
def multiply(x, y):
  def add(a, b):
    running_sum, carryin, k , temp_a, temp_b = 0, 0, 1, a, b
    while temp_a or temp_b:
      ak, bk = a & k, b & k
      carryout = (ak & bk) | (ak & carryin) | (bk & carryin)
      running_sum |= ak ^ bk ^ carryin
      carryin, k, temp_a, temp_b = ( carryout << 1, k << 1, temp_a >> 1, temp_b >> 1)
      
    return running_sum | carryin
    
  running_sum = 0
  while x:
    if x & 1:
      running_sum = add(running_sum, y)
    x, y = x >> 1, y << 1
  return running_sum
```


### 3 - closest integer with same weight

weight of non negative integer x as number of set bits

```python
#page.29
def closest_int_same_bit_count(x):
  NUM_UNSIGNED_BITS = 64
  for i in range(NUM_UNSIGNED_BITS - 1):
    if (x >> i) & 1 != (x >> (i + 1)) & 1:
      x ^= (1 << i) | ( 1 << (i + 1)) # swap bits 
      return x
  
  raise ValueError("All bits are 0 or 1")
```


### 2 - swap bits

```python
def swap_bits(x, i, j):
  if (x >> i) & 1 != (x >> j) & 1:
    bit_mask = (1 << i) | ( 1 << j)
    x ^= bit_mask
  return x
```
- reversing bits can be handled by swapping as well
- precomputation for faster reversing

### 1 - bit parity

- EOPI book

```python
def parity(x):
  result = 0
  while x: 
    result ^= x & 1
    x >>= 1
```

#optimization

```python
def parity(x):
  result = 0
  while x:
    result ^= 1
    x &= x - 1
  return result
```

precomputation

```python
def parity(x):
  MASK_SIZE = 16
  BIT_MASK = 0xFFFF
  return (PRECOMPUTED_PARITY[ x >> ( 3 * MASK_SIZE ) ] ^
          PRECOMPUTED_PARITY[ (x >> (2*MASK_SIZE)) & BIT_MASK ]^
          PRECOMPUTED_PARITY[(x >> MASK_SIZE) & BIT_MASK] ^ PRECOMPUTED_PARITY[ x & BIT_MASK])
```

```python
def parity(x):
  x ^= x >> 32
  x ^= x >> 16
  x ^= x >> 8
  x ^= x >> 4
  x ^= x >> 2
  x ^= x >> 1
  return x & 0x1
```




  
