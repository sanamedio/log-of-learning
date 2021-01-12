# 13-jan-2021

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




  
