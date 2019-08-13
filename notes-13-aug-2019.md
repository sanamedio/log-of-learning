# 13-aug-2019


### 1 - afl fuzzing using python

https://alexgaynor.net/2015/apr/13/introduction-to-fuzzing-in-python-with-afl/

```python
import sys
import afl


def isItNumber(n):
    for x in set(str(n)):
        if x not in '0123456789':
            return False

    return True

afl.init()

try:
    isItNumber(sys.stdin.read())
except ValueError:
    pass
```
