# 17-oct-2018

### 22 - Disable Automatic Garbage collection

```python
import gc
gc.disable()
```
Also, this alone might not be enough so:
```python
# gc.disable() doesn't work, because some random 3rd-party library will
# enable it back implicitly.
gc.set_threshold(0)
# Suicide immediately after other atexit functions finishes.
# CPython will do a bunch of cleanups in Py_Finalize which
# will again cause Copy-on-Write, including a final GC
atexit.register(os._exit, 0)
```

### 21 - Re-entrant lock in Python

- The standard Lock doesn’t know which thread is currently holding the lock. If the lock is held, any thread that attempts to acquire it will block, even if the same thread itself is already holding the lock.In such cases, RLock (re-entrant lock) is used. 

```python
import threading

num = 0
lock = Threading.Lock()

lock.acquire()
num += 1
lock.acquire() # This will block.
num += 2
lock.release()


# With RLock, that problem doesn’t happen.
lock = Threading.RLock()

lock.acquire()
num += 3
lock.acquire() # This won’t block.
num += 4
lock.release()
lock.release() # You need to call release once for each call to acquire.
```


### 20 - Synchronizing threads using Lock

```python

from threading import Lock, Thread
lock = Lock()
g = 0

def add_one():
   """
   Just used for demonstration. It’s bad to use the ‘global’
   statement in general.
   """
   
   global g
   lock.acquire()
   g += 1
   lock.release()

def add_two():
   global g
   lock.acquire()
   g += 2
   lock.release()

threads = []
for func in [add_one, add_two]:
   threads.append(Thread(target=func))
   threads[-1].start()

for thread in threads:
   """
   Waits for threads to complete before moving on with the main
   script.
   """
   thread.join()

print(g)
```

### 19 - Underscore for readability in Python 3

```python
dec_base = 1_000_000
bin_base = 0b_1111_0000
hex_base = 0x_1234_abcd

print(dec_base) # 1000000
print(bin_base) # 240
print(hex_base) # 305441741
```

### 18 - Getter and setter using @decorators

```python
class Vehicle:
    def __init__(self, number_of_wheels, type_of_tank, seating_capacity, maximum_velocity):
        self.number_of_wheels = number_of_wheels
        self.type_of_tank = type_of_tank
        self.seating_capacity = seating_capacity
        self.maximum_velocity = maximum_velocity

    @property
    def number_of_wheels(self):
        return self.number_of_wheels

    @number_of_wheels.setter
    def number_of_wheels(self, number):
        self.number_of_wheels = number

#testing
tesla_model_s = Vehicle(4, 'electric', 5, 250)
print(tesla_model_s.number_of_wheels) # 4
tesla_model_s.number_of_wheels = 2 # setting number of wheels to 2
print(tesla_model_s.number_of_wheels) # 2
```



### 17 - Dropping to shell from within the program (not PDB)

```python
#regular python shell
import code
code.interact(local=locals())


#ipython shell
import IPython; IPython.embed()

#regular python shell but with both locals and globals passed
import code
code.interact(local=dict(globals(), **locals()))
```


### 16 - identity weird behaviour

```python
a = 256
b = 256
a is b #True

a = 257
b = 257
a is b #False

[] is [] #False
{} is {} #False
"" is "" #True
0 is 0 #True
```

### 15 - slots

- https://elfsternberg.com/2009/07/06/python-what-the-hell-is-a-slot/
- A slot is nothing more than a memory management nicety: when you define __slots__ on a class, you’re telling the Python interpreter that the list of attributes described within are the only attributes this class will ever need, and a dynamic dictionary is not needed to manage the references to other objects within the class. This can save enormous amounts of space if you have thousands or millions of objects in memory.

```python
class Foo:
    __slots__ = ['x']
    def __init__(self, n):
        self.x = n

y = Foo(1)
print y.x  # prints "1"
y.x = 2
print y.x  # prints "2"
y.z = 4    # Throws exception.
print y.z
```


### 14 - revisiting comprehensions

```python
[ k*k for k in range(1, n+1) ] #list
{ k*k for k in range(1, n+1) } #set
( k*k for k in range(1, n+1) ) #generator
{ k : k*k for k in range(1, n+1) } #map
```

### 13 - inline absolute value

```python
param = n if n >= 0 else −n
```

### 12 - revisiting yield

```python
def factors(n):
   k=1
   while k*k < n:
      if n % k == 0:
         yield k
         yield n // k
      k += 1
      if k*k == n:
         yield k
```

### 11 - isinstance

```python
if not isinstance(values, collections.Iterable):
   raise TypeError( parameter must be an iterable type )
```

```python
if not isinstance(x, (int, float)):
   raise TypeError( x must be numeric )
```

### 10 - __getitem__ , next() , __iter__

- An object can be iterated over with "for" if it implements
   __iter__() or __getitem__().
- An object can function as an iterator if it implements next().
- https://stackoverflow.com/a/926649
- https://stackoverflow.com/a/20551346

### 9 - locals()

- Get the variables in local scope. There is no nonlocals() though.

### 8 - pip -> pipenv

- create requirement.txt using pip freeze
- pipenv = pip + virtualenv combined: better way to manage python 

### 7 - NamedTuple

```python
import collections

Person = collections.namedtuple('Person', 'name age gender')

print 'Type of Person:', type(Person)

bob = Person(name='Bob', age=30, gender='male')
print '\nRepresentation:', bob

jane = Person(name='Jane', age=29, gender='female')
print '\nField by name:', jane.name

print '\nFields by index:'
for p in [ bob, jane ]:
    print '%s is a %d year old %s' % p
```
If names are not good, it has got auto-rename too:

```python
import collections

with_class = collections.namedtuple('Person', 'name class age gender', rename=True)
print with_class._fields

two_ages = collections.namedtuple('Person', 'name age gender age', rename=True)
print two_ages._fields
```


### 6 - Asynchronous generator functions

- A function or method which is defined using async def and which uses the yield statement is called a asynchronous generator function. Such a function, when called, returns an asynchronous iterator object which can be used in an async for statement to execute the body of the function.

### 5 - Coroutine function

- A function or method which is defined using async def is called a coroutine function. Such a function, when called, returns a coroutine object. It may contain await expressions, as well as async with and async for statements. 

### 4 - Frozen set

- Frozen sets : These represent an immutable set. They are created by the built-in frozenset() constructor. As a frozenset is immutable and hashable, it can be used again as an element of another set, or as a dictionary key.


### 3 - datamodel

- https://docs.python.org/3/reference/datamodel.html
- Objects are never explicitly destroyed; however, when they become unreachable they may be garbage-collected. 
- An implementation is allowed to postpone garbage collection or omit it altogether — it is a matter of implementation quality how garbage collection is implemented, as long as no objects are collected that are still reachable.
- CPython implementation detail: CPython currently uses a reference-counting scheme with (optional) delayed detection of cyclically linked garbage, which collects most objects as soon as they become unreachable, but is not guaranteed to collect garbage containing circular references.
- use of the implementation’s tracing or debugging facilities may keep objects alive that would normally be collectable. Also note that catching an exception with a ‘try…except’ statement may keep objects alive.

### 2 - id() and is

- CPython implementation detail: id() is the address of the object in memory.
- The ‘is’ operator compares the identity of two objects; the id() function returns an integer representing its identity.

### 1 - everything on this link

- https://sebastianraschka.com/Articles/2014_deep_python.html
