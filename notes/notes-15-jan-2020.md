# 15-jan-2020

### 6 - dircmp to compare directory structures

```python3
from filecmp import dircmp

dcmp = dircmp("/usr/local/bin", "/bin")

print(dcmp)
# outputs the difference and commonalities
```


### 5 - cProfile usage to identify performance bottlenecks

- https://docs.python.org/3/library/profile.html#introduction-to-the-profilers

```python3
import cProfile
import re

cProfile.run('re.compile("foo|bar")')
```

```bash
➜  python3 main.py
         214 function calls (207 primitive calls) in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        2    0.000    0.000    0.000    0.000 enum.py:284(__call__)
        2    0.000    0.000    0.000    0.000 enum.py:526(__new__)
        1    0.000    0.000    0.000    0.000 enum.py:836(__and__)
        1    0.000    0.000    0.000    0.000 re.py:232(compile)
        1    0.000    0.000    0.000    0.000 re.py:271(_compile)
        1    0.000    0.000    0.000    0.000 sre_compile.py:249(_compile_charset)
        1    0.000    0.000    0.000    0.000 sre_compile.py:276(_optimize_charset)
        2    0.000    0.000    0.000    0.000 sre_compile.py:453(_get_iscased)
        1    0.000    0.000    0.000    0.000 sre_compile.py:461(_get_literal_prefix)
        1    0.000    0.000    0.000    0.000 sre_compile.py:492(_get_charset_prefix)
        1    0.000    0.000    0.000    0.000 sre_compile.py:536(_compile_info)
        2    0.000    0.000    0.000    0.000 sre_compile.py:595(isstring)
        1    0.000    0.000    0.000    0.000 sre_compile.py:598(_code)
      3/1    0.000    0.000    0.000    0.000 sre_compile.py:71(_compile)
        1    0.000    0.000    0.000    0.000 sre_compile.py:759(compile)
        3    0.000    0.000    0.000    0.000 sre_parse.py:111(__init__)
        7    0.000    0.000    0.000    0.000 sre_parse.py:160(__len__)
       18    0.000    0.000    0.000    0.000 sre_parse.py:164(__getitem__)
        7    0.000    0.000    0.000    0.000 sre_parse.py:172(append)
      3/1    0.000    0.000    0.000    0.000 sre_parse.py:174(getwidth)
        1    0.000    0.000    0.000    0.000 sre_parse.py:224(__init__)
        8    0.000    0.000    0.000    0.000 sre_parse.py:233(__next)
        2    0.000    0.000    0.000    0.000 sre_parse.py:249(match)
        6    0.000    0.000    0.000    0.000 sre_parse.py:254(get)
        1    0.000    0.000    0.000    0.000 sre_parse.py:286(tell)
        1    0.000    0.000    0.000    0.000 sre_parse.py:411(_parse_sub)
        2    0.000    0.000    0.000    0.000 sre_parse.py:469(_parse)
        1    0.000    0.000    0.000    0.000 sre_parse.py:76(__init__)
        2    0.000    0.000    0.000    0.000 sre_parse.py:81(groups)
        1    0.000    0.000    0.000    0.000 sre_parse.py:897(fix_flags)
        1    0.000    0.000    0.000    0.000 sre_parse.py:913(parse)
        1    0.000    0.000    0.000    0.000 {built-in method _sre.compile}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
       25    0.000    0.000    0.000    0.000 {built-in method builtins.isinstance}
    29/26    0.000    0.000    0.000    0.000 {built-in method builtins.len}
        2    0.000    0.000    0.000    0.000 {built-in method builtins.max}
        9    0.000    0.000    0.000    0.000 {built-in method builtins.min}
        6    0.000    0.000    0.000    0.000 {built-in method builtins.ord}
       48    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        5    0.000    0.000    0.000    0.000 {method 'find' of 'bytearray' objects}
        1    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
```

### 4 - tracemalloc to find memory additions

- https://docs.python.org/3/library/tracemalloc.html

```python3
import tracemalloc
import uuid

tracemalloc.start()

snapshot1 = tracemalloc.take_snapshot()

### memory usage here
x = [ uuid.uuid4() for x in range(100000) ]

snapshot2 = tracemalloc.take_snapshot()

top_stats = snapshot2.compare_to(snapshot1, 'lineno')

print("[ Top 10 differences ]")
for stat in top_stats[:10]:
    print(stat)
```

### 3 - difflib to get edits

- https://docs.python.org/3/library/difflib.html

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
