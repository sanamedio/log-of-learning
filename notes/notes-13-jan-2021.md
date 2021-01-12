# 13-jan-2021

### 5 - computing quotient with add, subtract and shift

when we say 5 divmod 2 = 2,1 it means we can take out two 2's from 5 and leave 1 as remainder. These bit operations work similarly to find out the quotient.

```python
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




  
