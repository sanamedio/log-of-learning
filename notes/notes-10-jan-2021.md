# 10-jan-2020

### 1 - frozenset hash algo

https://stackoverflow.com/questions/20832279/python-frozenset-hashing-algorithm-implementation/20931478#20931478

```python
def _hash(self):
    MAX = sys.maxint
    MASK = 2 * MAX + 1
    n = len(self)
    h = 1927868237 * (n + 1)
    h &= MASK
    for x in self:
        hx = hash(x)
        h ^= (hx ^ (hx << 16) ^ 89869747)  * 3644798167
        h &= MASK
    h = h * 69069 + 907133923
    h &= MASK
    if h > MAX:
        h -= MASK + 1
    if h == -1:
        h = 590923713
    return h
```
