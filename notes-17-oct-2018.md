# 17-oct-2018

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
