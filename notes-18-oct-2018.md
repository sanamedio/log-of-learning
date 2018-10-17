# 18-oct-2018

### 2 - Reversing a list using recursion

```python
def reverse(S, start, stop):
  """Reverse elements in implicit slice S[start:stop]."""
  if start < stop − 1:
    S[start], S[stop−1] = S[stop−1], S[start]
    reverse(S, start+1, stop−1)
```

### 1 - efficient recursion of fibonacci

Exponential running time:
```python
def bad_fibonacci(n):
  """Return the nth Fibonacci number."""
  if n <= 1:
    return n
  else:
    return bad_fibonacci(n−2) + bad_fibonacci(n−1)
```

Linear running time:
```python
def good_fibonacci(n):
  """Return pair of Fibonacci numbers, F(n) and F(n-1)."""
  if n <= 1:
    return (n,0)
  else:
    (a, b) = good_fibonacci(n−1)
    return (a+b, a)
```
