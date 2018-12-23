# 24-dec-2018

### 1 - z3-solver

- its a sat solver, given a constraint it will give solution.

```python

In [4]: from z3 import *

In [5]: x = Real('x')

In [6]: y = Real('y')

In [7]: s = Solver()

In [8]: s.add( x + y > 5 , x > 1 , y > 1 )

In [9]: print(s.check())
sat

In [10]: print(s.model())
[y = 3/2, x = 4]
```
