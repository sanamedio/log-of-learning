# 29-dec-2018

## 1 - negative numbers python

- infinite precision causes it to not act like a normal 32-bit negative

```python
bin(-1+(1<<32))
#'0b11111111111111111111111111111111'

bin(-1)
#'-0b1'
```
