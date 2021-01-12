# 13-jan-2021


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




  
