# 19-oct-2018

### 30 - Dumping information about threads

```python
import sys
import traceback


def dump_threads():
        for thread_id, frame in sys._current_frames().iteritems():
                print 'Thread #%d' % thread_id
                print ''.join(traceback.format_stack(frame))


import time, threading


def foo():
        for x in xrange(10):
                time.sleep(1)


threading.Thread(target=foo).start()
dump_threads()
```

### 29- Source code of core libs

https://github.com/python/cpython/tree/master/Lib

- [ ] TODO Go through each file in that directory!  

### 28 - Summary till now and Questions in my mind

- GIL i.e. Global Interpreter Lock. It seems to be a big issue with python and unsolved problem. Where is GIL code? [ ] TODO find out GIL source code in cpython source tree.
- Zen of Python says There should be one preferred way of doing things. But, even simple cases like dataclasses has tonnes of different solutions. And probably every new version of Python is bringing a new way of doing things. 
- Most part of learning resources are focussed on idioms of Python and doing it in Pythonic way. I think that is one reason python felt so different from the start. 
- The behaviour and features differ greatly between different python implementations and versions. It's difficult to know whether a piece of code will work reliably accross multiple versions. 
- Package management seems to be done in a different way. But it seems to be a universal problem. Dependency management and version management are not easy.
- There are lot of shiny things like generators and decorators and coroutines; but these are just abstractions to shorten LOC. These can be achieved with different OOPs patterns, datastructures and algorithms. 
- Garbage collection is a module. Can we override it? Where is source code of it? Are these core packages present in Cpython source tree? [ ] TODO check

### 27 - Property decorator

```python
class Foo:
  @property
  def hello():
    return 'hello world'

Foo().hello() # 'hello world' not function object
```

### 26 - Performance optimization - coroutine - and dangers

 - Go to lower level API and yeild from there
 - Write a C extension and yield from there
 - do .send() also in C
 - ref : http://www.dabeaz.com/coroutines/Coroutines.pdf( page 35/ slide 70 )
 
 - If you send on already executing coroutine, it will crash your program. For example, Multiple threads sending data to same target routine
   - [ ] Does this mean there is no default queue involved?
   - [ ] What is solution? 
   - [ ] TODO This seems weird; need to check 
 - [ ] TODO Coroutines for cooperative multitasking code

### 25 - How does coroutine differ from simple argument passing?

```python
@coroutine
def filter_on_field(fieldname,value,target):
     while True:
          d = (yield)
          if d.get(fieldname) == value:
               target.send(d)
```
- Difference between simple functions and coroutine seems like coroutine maintains a state internally using yield points, whereas functions will start from top. It seems more like a useful abstraction then something fundamentally different.
- [X] What will happen if I send to same coroutine? Is it possible to define in such a loopy way? Ans: Can't be done. Coroutine don't allow this. Check dabeaz slides on coroutine.

### 24 - Coroutines ~~ OOPS

- coroutine in the below case is faster than OOPS version
- [ ] self.lookups take time, that contributes to slowness of it

OOPS version:
```python
class GrepHandler(object):
     def __init__(self,pattern,target):
          self.pattern = pattern
          self.target  = target
     def send(self,line):
          if self.pattern in line:
               self.target.send(line)
```
- [ ] TODO Can I use dataclasses in GrepHandler to reduce boilerplate?

Coroutine version
```python
@coroutine
def grep(pattern, target):
     while True:
          line = (yield)
          if pattern in line:
               target.send(line)
```

### 23 - Variable assignment not being expression

- In python variable assignment cannot be used as a expression for conditionals

```python
     while (line = yield): ## syntax error
```

### 22 - coroutine with single source and multiple targets

- (yield) is the place where anything sent to this coroutine goes; and using target.send we pass that value to multiple target coroutines
- [ ] Is it possible to take multiple source yield in a non-conflicting way apart from just depending on their order?
- You can send object to coroutine, i.e. you can pass for example a tuple ('a',1,1.0), and target can receive it

```python
@coroutine
def broadcast(targets):
    while True:
        item = (yield)
        for target in targets:
            target.send(item)
```

### 21 - coroutine vs generator

- [ ] http://www.dabeaz.com/coroutines/Coroutines.pdf

- Key difference between generator chain and coroutine chain is that Generators pulldata through the pipe with iteration whereas Coroutines push data into the pipeline with send().

### 20 - Decimal math with floating point error

```python
from decimal import Decimal
a = Decimal(str(0.2))
b = Decimal(str(3))
c = Decimal(str(0.7))
d = Decimal(str(0.3))
e = Decimal(str(2))
f = Decimal(str(7))

print(f'0.2 * 3 = {a * b}')
print(f'0.7 * 3 = {c * b}')
print(f'0.3 * 2 = {d * e}')
print(f'0.3 * 7 = {e * f}')
```

### 19 - (yield)

```python
def grep(pattern):
    print "Looking for %s" % pattern
    while True:
        line = (yield)
        if pattern in line:
            print line,
            

g = grep("python")
g.next()
g.send("Yeah, but no, but yeah, but no")
g.send("A series of tubes")
g.send("python generators rock!") #python generators rock!
 
```
- (yield) returns what is sent to the generator
- .next() or .send(None) advances the execution to the first yield


### 18 - python 3 faulthandler

- faulthandler handles failures like page seg faults and displays exception and stuff (limited traceback) even in case of crash failures. Won't handle kill -9

```python
import faulthandler
faulthandler.enable()

def killme():
        import sys
        from ctypes import CDLL

        dll = 'dylib' if sys.platform == 'darwin' else 'so.6'
        libc = CDLL("libc.%s"%dll)
        libc.time(-1)

killme()
```
Can also be enabled by:
```bash
python -X faulthandler
```


### 17 - Exception handling silly mistake

```python
>>> try:
...     l = ["a", "b"]
...     int(l[2])
... except ValueError, IndexError:  # To catch both exceptions, right?
...     pass
...
Traceback (most recent call last):
  File "<stdin>", line 3, in <module>
IndexError: list index out of range
```
rather do,
```python
>>> try:
...     l = ["a", "b"]
...     int(l[2])
... except (ValueError, IndexError) as e:  
...     pass
...
>>>
```

### 16 - python3 unicode 

- In Python 2, str acts like bytes of data. There is also unicode type to represent Unicode strings.
- In Python 3, str is a string. bytes are bytes. There is no unicode. str strings are Unicode.

### 15 - ipython_memory_usage

- [https://github.com/ianozsvald/ipython_memory_usage](https://github.com/ianozsvald/ipython_memory_usage)
- [http://book.pythontips.com/en/latest/__slots__magic.html](http://book.pythontips.com/en/latest/__slots__magic.html)


```python
In [1]: import ipython_memory_usage.ipython_memory_usage as imu

In [2]: imu.start_watching_memory()
In [2] used 0.0000 MiB RAM in 5.31s, peaked 0.00 MiB above current, total RAM usage 15.57 MiB

In [3]: %cat slots.py
class MyClass(object):
        __slots__ = ['name', 'identifier']
        def __init__(self, name, identifier):
                self.name = name
                self.identifier = identifier

num = 1024*256
x = [MyClass(1,1) for i in range(num)]
In [3] used 0.2305 MiB RAM in 0.12s, peaked 0.00 MiB above current, total RAM usage 15.80 MiB

In [4]: from slots import *
In [4] used 9.3008 MiB RAM in 0.72s, peaked 0.00 MiB above current, total RAM usage 25.10 MiB

In [5]: %cat noslots.py
class MyClass(object):
        def __init__(self, name, identifier):
                self.name = name
                self.identifier = identifier

num = 1024*256
x = [MyClass(1,1) for i in range(num)]
In [5] used 0.1758 MiB RAM in 0.12s, peaked 0.00 MiB above current, total RAM usage 25.28 MiB

In [6]: from noslots import *
In [6] used 22.6680 MiB RAM in 0.80s, peaked 0.00 MiB above current, total RAM usage 47.95 MiB
```

### 14 - dataclasses 

- [ ] https://realpython.com/python-data-classes/

```python
from dataclasses import dataclass

@dataclass
class DataClassCard:
    rank: str
    suit: str
```

### 13 - unzipping

```python
>>> a = [1, 2, 3]
>>> b = ['a', 'b', 'c']
>>> z = zip(a, b)
>>> z
[(1, 'a'), (2, 'b'), (3, 'c')]
>>> zip(*z)
[(1, 2, 3), ('a', 'b', 'c')]
```

### 12 - benefits of yield

- Only one value is computed at a time. Low memory impact example above
- Can break in the middle. Don't have to compute everything just to find out you needed none of it. Compute just what you need. 
- If you often don't need it all, you can gain a lot of performance here.
- If you need a list (e.g., for slicing), just call list() on the generator.
- Function state is "saved" between yields.

### 11 - yield where possible

bad
```python
def dup(n):
    A = []
    for i in range(n):
        A.extend([i,i])
    return A
```

good
```python
def dup(n):
    for i in range(n):
        yield i
        yield i
```

good2
```python
def dup(n):
    for i in xrange(n):
        yield from [i,i]
```



### 10 - danger with format strings

- format string can access object attributes directly

```python
>> 'class of {0} is {0.__class__}'.format(42)
"class of 42 is <class 'int'>"
```

### 9 - rounding up floats

```python
2.2 * 3.0 == 3.3 * 2.0 #False

>>> 2.2*3.0
6.6000000000000005
>>> 3.3*2.0
6.6
```

### 8 - pytest benchmark

- nice function performance benchmarking

```bash
pip3 install pytest pytest-benchmark
```

```python
import re
import string
import random

# Python ZIP version
def count_doubles(val):
    total = 0
    for c1, c2 in zip(val, val[1:]):
        if c1 == c2:
            total += 1
    return total


# Python REGEXP version
double_re = re.compile(r'(?=(.)\1)')

def count_doubles_regex(val):
    return len(double_re.findall(val))


# Benchmark it
# generate 1M of random letters to test it
val = ''.join(random.choice(string.ascii_letters) for i in range(1000000))

def test_pure_python(benchmark):
    benchmark(count_doubles, val)

def test_regex(benchmark):
    benchmark(count_doubles_regex, val)
```

### 7 - input(): disaster

- [ ] TODO find out why this is designed like this: to evaluate the input string
- Also, notice the dunder import

```python
>>> input()
dir()
['__builtins__', '__doc__', '__name__', '__package__']
>>> input()
__import__('sys').exit()
```

### 6 - public, private , secret simple example

```python
class Foo(object):
    def __init__(self):
        self.public = 'public'
        self._private = 'public'
        self.__secret = 'secret'

>>> foo = Foo()
>>> foo.public
'public'
>>> foo._private
'public'
>>> foo.__secret
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'Foo' object has no attribute '__secret'
>>> foo._Foo__secret
'secret'
```

### 5 - list comprehension for flattening

```python
words = ['her', 'name', 'is', 'rio']
letters = [letter for word in words for letter in word]
```    

### 4 - yield syntax in python3

```python
yield from gen()
```

### 3 - LEGB scoping rules of Python

LEGB Rule.

L, Local — Names assigned in any way within a function (def or lambda), and not declared global in that function.

E, Enclosing-function locals — Name in the local scope of any and all statically enclosing functions (def or lambda), from inner to outer.

G, Global (module) — Names assigned at the top-level of a module file, or by executing a global statement in a def within the file.

B, Built-in (Python) — Names preassigned in the built-in names module : open,range,SyntaxError,...


### 2 - Naming list slices

```python
>>> a = [0, 1, 2, 3, 4, 5]
>>> LASTTHREE = slice(-3, None)
>>> LASTTHREE
slice(-3, None, None)
>>> a[LASTTHREE]
[3, 4, 5]
```

### 1 - get python config information

```bash
$ python -m sysconfig
```
