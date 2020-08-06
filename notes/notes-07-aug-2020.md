# 07-aug-2020

### 1 - weird python scoping

```python
>>> [f(1) for f in [lambda y: x+y for x in range(10)]]
[10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
```
