# 22-may-2019

### 1 - pythonic palindrome

https://treyhunner.com/2019/05/python-builtins-worth-learning/

```python
def palindromic(sequence):
    """Return True if the sequence is the same thing in reverse."""
    for n, m in zip(sequence, reversed(sequence)):
        if n != m:
            return False
    return True
```

```python
def palindromic(sequence):
    """Return True if the sequence is the same thing in reverse."""
    return all(
        n == m
        for n, m in zip(sequence, reversed(sequence))
    )
```
