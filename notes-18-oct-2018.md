# 18-oct-2018

### 9 - ABC abstract base classes

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

testlib = ctypes.CDLL('testlib.so')
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
