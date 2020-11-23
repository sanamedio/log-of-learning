# 24-nov-2020

### 1 - overriding traceback handler

- https://rich.readthedocs.io/en/latest/traceback.html
- traceback handlers could be overridden as in this case where beauty of output has been increased using rich library

```python
➜  richtest python
Python 3.6.1 (default, Jan 25 2020, 16:43:10)
[GCC 4.2.1 Compatible Apple LLVM 11.0.0 (clang-1100.0.33.16)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> from rich.traceback import install
>>> install()
<built-in function excepthook>
>>> 1/0
╭───────────────────── Traceback (most recent call last) ──────────────────────╮
│ <stdin>:1 in <module>                                                        │
╰──────────────────────────────────────────────────────────────────────────────╯
ZeroDivisionError: division by zero
>>> raise Exception("fun thing")
╭───────────────────── Traceback (most recent call last) ──────────────────────╮
│ <stdin>:1 in <module>                                                        │
╰──────────────────────────────────────────────────────────────────────────────╯
Exception: fun thing
>>> request
╭───────────────────── Traceback (most recent call last) ──────────────────────╮
│ <stdin>:1 in <module>                                                        │
╰──────────────────────────────────────────────────────────────────────────────╯
NameError: name 'request' is not defined
>>> import requests
>>> requests.get("dlkfjsdf")[too beautiful to paste here]
```
