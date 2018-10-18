# 18-oct-2018

### 20 - sys.getcounts

- get count of object allocation by python
- needs a custom debug build
```bash
$ git clone https://github.com/python/cpython
$ cd cpython
$ mkdir debug
$ cd debug
$ ../configure --with-pydebug
$ make EXTRA_CFLAGS="-DCOUNT_ALLOCS"
$ ./python
```

```python
import sys
sys.getcounts()

def print_allocations(top_k=None):
    allocs = sys.getcounts()
    if top_k:
        allocs = sorted(allocs, key=lambda tup: tup[1], reverse=True)[0:top_k]

    for obj in allocs:
        alive = obj[1]-obj[2]
        print("Type {},  allocs: {}, deallocs: {}, max: {}, alive: {}".format(*obj,alive))

print_allocations(10)
```
- https://rushter.com/blog/python-object-allocation-statistics/

### 19 - virtualenv and venv

- Both are used to create virtual environments
- venv is lighter version 
- [ ] TODO study each file of virtualenv and venv environment

virtualenv:
```bash
$ virtualenv ENV
$ source ENV/bin/activate
```

venv from PEP 405 
```bash
$ python3 -m venv ENV
$ source ENV/bin/activate
```

### 18 - inline unpacking is treated differently

```python
#Python 3.5.2 (default, Nov 23 2017, 16:37:01) 
#[GCC 5.4.0 20160609] on linux
#Type "help", "copyright", "credits" or "license" for more information.
>>> a=1.0
>>> b=1.0
>>> a is b
False
>>> a,b = 1.0,1.0
>>> a is b
True
>>> 
```
- [ ] Also, behaviour changes in a function scope, this one TODO: find out why?

```python
def test():
    a = 1.0
    b = 1.0
    return a is b
test() #outputs True
```

### 17 - Exiting Python

```python
os._exit(0) #method 1
sys.exit(0) #method 2
raise SystemExit #method 3
```

### 16 - String interning

- When working with empty strings or ASCII strings of one character Python uses string interning. Interned strings act as singletons, that is, if you have two identical strings that are interned, there is only one copy of them in the memory.
- string interning is not limed to characters or empty strings. Strings that are created during code compilation can also be interned if their length does not exceed 20 characters.

```python
>>> a = 'teststring'
>>> b = 'teststring'
>>> id(a), id(b), a is b
(4569487216, 4569487216, True)
>>> a = 'test'*5
>>> b = 'test'*5
>>> len(a), id(a), id(b), a is b
(20, 4569499232, 4569499232, True)
>>> a = 'test'*6
>>> b = 'test'*6
>>> len(a), id(a), id(b), a is b
(24, 4569479328, 4569479168, False)
```


### 15 - Loading libc and executing functions from that

```python
import ctypes
#cdll.LoadLibrary("libc.so.6")  
libc = CDLL("libc.so.6")       
libc.time(None)                           
```

### 14 - Memory used by Python objects

```python
from pympler import summary, muppy
mem_summary = summary.summarize(muppy.get_objects())
rows = summary.format_(mem_summary)
```
    

### 13 - Strict typing for function arguments

```python
def my_add(a: int, b: int) -> int:
  return a + b
```
- It is worth pointing out that the type annotations has (almost) completely no effect on the runtime, and the runtime could still violate the specified type hints. One needs a static type checker like mypy to actually see any type conflicts. (by @Gear5th from Reddit)


### 12 - SimpleNamespace

```python
from types import SimpleNamespace
car1 = SimpleNamespace(color='red', mileage=3812.4, automatic=True)

# The default repr:
>>> car1
namespace(automatic=True, color='red', mileage=3812.4)

# Instances are mutable
>>> car1.mileage = 12
>>> car1.windshield = 'broken'
>>> del car1.automatic
>>> car1
namespace(color='red', mileage=12, windshield='broken')
```

### 11 - Struct

```python
from struct import Struct

MyStruct = Struct('i?f')

data = MyStruct.pack(23, False, 42.0)

# All you get is a blob of data:
>>> data
b'\x17\x00\x00\x00\x00\x00\x00\x00\x00\x00(B'

# Data blobs can be unpacked again:
>>> MyStruct.unpack(data)
(23, False, 42.0)
```

### 10 - Disassembly of list and tuple

```python
>>> import dis
>>> dis.dis(compile("(23, 'a', 'b', 'c')", '', 'eval'))
  1       0 LOAD_CONST           4 ((23, 'a', 'b', 'c'))
          3 RETURN_VALUE

>>> dis.dis(compile("[23, 'a', 'b', 'c']", '', 'eval'))
  1       0 LOAD_CONST           0 (23)
          3 LOAD_CONST           1 ('a')
          6 LOAD_CONST           2 ('b')
          9 LOAD_CONST           3 ('c')
         12 BUILD_LIST           4
         15 RETURN_VALUE
```

### 9 - ABC abstract base classes

```python
class Base:
    def foo(self):
        raise NotImplementedError()

    def bar(self):
        raise NotImplementedError()

class Concrete(Base):
    def foo(self):
        return 'foo() called'

# In this case, Concrete has partially implemented the the Base sort of. Not clean approach.

```
This is better way of handling it:

```python
from abc import ABCMeta, abstractmethod

class Base(metaclass=ABCMeta):
    @abstractmethod
    def foo(self):
        pass

    @abstractmethod
    def bar(self):
        pass

class Concrete(Base):
    def foo(self):
        pass

# This will force the Concrete class to implement those methods
```

### 8 - Ctypes simple example

Write the C function which you wish to call from Python
```c
#include<stdio.h>

void myprint(void);

void myprint(void){
    printf("Hello world");
}
```

Compile the above C code as a shared library
```bash
gcc -shared  -o testlib.so -fPIC  testlib.c
```

Load the shared library and execute the myprint() function in Python
```python
import ctypes

testlib = ctypes.CDLL('/home/user/testlib.so') #absolute path is required
testlib.myprint()
```
- https://stackoverflow.com/a/5082294


### 7 - objgraph to visualize the memory reference information visually

- https://mg.pov.lt/objgraph/

```python
x = []
y = [x, [x], dict(x=x)]
import objgraph
objgraph.show_refs([y], filename='sample-graph.png') #Now this is reason why people fall in love with Python
```

### 6 - debugging reference cycles

- If you set debugging flags to DEBUG_SAVEALL, all unreachable objects found will be appended to gc.garbage list.

```python
import gc

gc.set_debug(gc.DEBUG_SAVEALL)

print(gc.get_count())
lst = []
lst.append(lst)
list_id = id(lst)
del lst
gc.collect()
for item in gc.garbage:
    print(item)
    assert list_id == id(item)
```

### 5 - Generational GC example

```python
import gc

# We are using ctypes to access our unreachable objects by memory address.
class PyObject(ctypes.Structure):
    _fields_ = [("refcnt", ctypes.c_long)]


gc.disable()  # Disable generational gc

lst = []
lst.append(lst)

# Store address of the list
lst_address = id(lst)

# Destroy the lst reference
del lst

object_1 = {}
object_2 = {}
object_1['obj2'] = object_2
object_2['obj1'] = object_1

obj_address = id(object_1)

# Destroy references
del object_1, object_2

# Uncomment if you want to manually run garbage collection process 
# gc.collect()

# Check the reference count
print(PyObject.from_address(obj_address).refcnt)
print(PyObject.from_address(lst_address).refcnt)
```

### 4 - refcounting example

```python
foo = []

# 2 references, 1 from the foo var and 1 from getrefcount
print(sys.getrefcount(foo))

def bar(a):
    # 4 references
    # from the foo var, function argument, getrefcount and Python's function stack
    print(sys.getrefcount(a))

bar(foo)
# 2 references, the function scope is destroyed
print(sys.getrefcount(foo))
```

### 3 - CPython garbage collector

- Standard CPython's garbage collector has two components, the reference counting collector and the generational garbage collector, known as gc module.
- The reference counting algorithm is incredibly efficient and straightforward, but it cannot detect reference cycles. That is why Python has a supplemental algorithm called generational cyclic GC, that deals with reference cycles.
- The reference counting is fundamental to Python and can't be disabled, whereas the cyclic GC is optional and can be used manually.
- https://rushter.com/blog/python-garbage-collector/

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
