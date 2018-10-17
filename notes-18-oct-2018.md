# 18-oct-2018

### 3 - CPython garbage collector

- Standard CPython's garbage collector has two components, the reference counting collector and the generational garbage collector, known as gc module.
- The reference counting algorithm is incredibly efficient and straightforward, but it cannot detect reference cycles. That is why Python has a supplemental algorithm called generational cyclic GC, that deals with reference cycles.
- The reference counting is fundamental to Python and can't be disabled, whereas the cyclic GC is optional and can be used manually.

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
