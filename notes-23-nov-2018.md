# 23-nov-2018

### 4 - cherrypy

```python
Python 3.6.6 (default, Sep 12 2018, 18:26:19) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import cherrypy
>>> class HelloWorld():
...     @cherrypy.expose
...     def index(self):
...             return "Hello world"
... 
>>> cherrypy.quickstart(HelloWorld())
[23/Nov/2018:19:18:26] ENGINE Listening for SIGTERM.
[23/Nov/2018:19:18:26] ENGINE Listening for SIGHUP.
[23/Nov/2018:19:18:26] ENGINE Listening for SIGUSR1.
[23/Nov/2018:19:18:26] ENGINE Bus STARTING
CherryPy Checker:
The Application mounted at '' has an empty config.

[23/Nov/2018:19:18:26] ENGINE Started monitor thread 'Autoreloader'.
[23/Nov/2018:19:18:26] ENGINE Serving on http://127.0.0.1:8080
[23/Nov/2018:19:18:26] ENGINE Bus STARTED
```

### 3 - using github as a pypi server

https://medium.freecodecamp.org/how-to-use-github-as-a-pypi-server-1c3b0d07db2

### 2 - contextlib for perf

```python
from time import perf_counter
from array import array
from contextlib import contextmanager

@contextmanager
def timing(label: str):
    t0 = perf_counter()
    yield lambda: (label, t1 - t0)
    t1 = perf_counter()


with timing('ARray tests') as total:
    with timing('ARray creation innermul') as inner:
        x = array('d', [0] * 100000)
    with timing('Array creation outer mul') as outer:
        x = array('d', [0] * 100000)



print('total [%s]: %.6f s' %total())
print('   Timing [%s]: %.6f s' %inner())
print('   Timing [%s]: %.6f s' %outer())
```

### 1 - Typing usage

```python
from typing import List

Vector = List[float]
Matrix = List[Vector]

def addMatrix(a : Matrix, b : Matrix) -> Matrix:
  result = []
  for i,row in enumerate(a):
    result_row =[]
    for j, col in enumerate(row):
      result_row += [a[i][j] + b[i][j]]
    result += [result_row]
  return result

x = [[1.0, 0.0], [0.0, 1.0]]
y = [[2.0, 1.0], [0.0, -2.0]]

z = addMatrix(x, y)
print(z)
```
