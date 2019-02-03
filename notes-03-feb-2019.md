# 03-feb-2019

### 1 - equating two sides of a license plate

- https://www.johndcook.com/blog/2019/02/02/landau-kolmogorov/

```python
from math import sqrt, cos, atan, floor

def f():
    sec = lambda x: 1/cos(x)
    y = sqrt(44)
    for _ in range(30):
        y = sec(atan(y))
    return floor(y)

def g():
    return floor(sqrt(77))


if __name__ == '__main__':
    print(f())
    print(g())
```
