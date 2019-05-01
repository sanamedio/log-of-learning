# 01-may-2019


### 1 - monotonic time in python

https://codeburst.io/why-shouldnt-you-trust-system-clocks-72a82a41df93

```python
Python 3.6.7 (default, Oct 22 2018, 11:32:17) 
[GCC 8.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import time
>>> time.monotonic
<built-in function monotonic>
>>> time.monotonic()
197735.477949047
>>> time.monotonic()
197736.922957192
>>> time.monotonic()
197737.817689814
>>>
```
