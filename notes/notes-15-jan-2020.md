# 15-jan-2020


### 3 - difflib to get edits

```python3
import sys
from difflib import unified_diff


s1 = [ x+"\n" for x in "a b c d".split()]
s2 = [ x+"\n" for x in "aa bb dd cc".split()]


sys.stdout.writelines(unified_diff(s1, s2, fromfile='before.py', tofile='after.py'))
```

```bash
➜  python differ.py
--- before.py
+++ after.py
@@ -1,4 +1,4 @@
-a
-b
-c
-d
+aa
+bb
+dd
+cc
```


### 2 - termios handy password prompt

- https://docs.python.org/3/library/termios.html

```python3
def getpass(prompt="Password: "):
    import termios, sys
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    new = termios.tcgetattr(fd)
    new[3] = new[3] & ~termios.ECHO          # lflags
    try:
        termios.tcsetattr(fd, termios.TCSADRAIN, new)
        passwd = input(prompt)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)
    return passwd
```


### 1 - faulthandler

- Allows to get stacktraces in case of segmentation faults and similar 
- https://docs.python.org/3/library/faulthandler.html

```bash
$ python3 -c "import ctypes; ctypes.string_at(0)"
Segmentation fault

$ python3 -q -X faulthandler
>>> import ctypes
>>> ctypes.string_at(0)
Fatal Python error: Segmentation fault

Current thread 0x00007fb899f39700 (most recent call first):
  File "/home/python/cpython/Lib/ctypes/__init__.py", line 486 in string_at
  File "<stdin>", line 1 in <module>
Segmentation fault
```
