# 15-oct-2018

### 22 - Dunder 

- https://dbader.org/blog/python-dunder-methods

### 21 - Python 2 unicode and str are separate

```python
class Car(object):
  def __init__(self, color , mileage):
    self.color = color
    self.mileage = mileage
    
  def __repr__(self):
    return '{}({!r}, {!r})'.format(
      self.__class__.__name__,
      self.color, self.mileage)
    
  def __unicode__(self):
    return u'a {self.color} car'.format(self=self)
  
  def __str__(self):
    return unicode(self).encode('utf-8')


```

### 20 - getting classnames

```python
def __repr__(self):
  return (f'{self.__class__.__name__}('f'{self.color!r}, {self.mileage!r})')
#why !r ?

```

### 19 - __str__ and __repr__

```python
class Car:
  def __init__(self, color, mileage):
    self.color = color
    self.mileage = mileage
  
  def __str__(self):
    return f'a {self.color} car'


my_car = Car('red', 3434)
print(my_car)
```

- repr for inspecting objects in interpreter session
- repr strings are for debugging

### 18 - is vs ==

- 'is' is same object ( identity )
- '==' is a equality comparator ( content )
```python
a  = [1,2,3]
b = a
c = list(a)
a is b #True
a is c #False
a == b #True
a == c #True
```

### 17 - return None

- return None is added to every function without a return Value

### 16 - unpacking operator

- \* is the unpacking operator
- putting \* before a iterable, unpacks it
- \** unpacks the values from dicts

### 15 - metadata for decorator debugging

```python
import functools

def uppercase(func):
  @functools.wraps(func)
  def wrapper():
    return func().upper()
  return wrapper
```

### 14 - trace using decorators

```python
def trace(func):
  def wrapper(*args, **kwargs):
    print(f'TRACE: calling { func.__name__}() '
          f'with {args} , {kwargs}')
    
    original_result = func(*args, **kwargs)
    
    print(f'TRACE: {func.__name__}() '
          f'returned {original_result!r}')
          
    return original_result
  return wrapper

@trace
def say(name,line):
  return f'{name} : {line}'

```

### 13 - lambda again?

```python
>>> (lambda x+y: x + y )(5,3)

>>> tuples = [ (1,'d') , (2,'b') , (4,'a'), (3, 'c') ]
>>> sorted(tuples, key=lambda x : x[1] )

>>> sorted( range(-5,6), key=lambda x: x*x)
[0,-1,1,-2,2,-3,3,-4,4,-5,5]


```


### 12 - making objects callable

```python
class Adder:
  def __init__(self,n):
    self.n = n
    
  def __call__(self, x ):
    return self.n + x 

>>> plus_3 = Adder(3)
>>> plus_3(4)
7

>>> callable(plus_3)
True
```


### 11 - del

```python
def yell(text):
  return test.upper() + "!"

yell('hello')

bark = yell

bark('woof')

del yell

yell('hello?')
>>NameError blah

bark('hey')
>>Still works!

bark.__name__
>>'yell'

```

### 10 - String formatting

```python

>>> "Hello, %s" % name
>>> "%x" % errno
>>> "%s %x" % ( name, errno )
>>> "%(name)s, %(errno)x" % { "name" : name , "errno" : errno }

>>> 'Hello, {}'.format(name)

>>> 'Hey {name} 0x{errno:x} error '.format(name=name, errno=errno)

>>> f'Hello, {name}!'
>>> f'{5+5}'
```
```python
from string import Template
t = Template('Hey, $name!')
t.substitute(name=name)
```

- Template Strings avoid security issues



### 9 - var_ ( underscore after the name)

- Avoid clashes with keywords, convention

### 8 - _ ( don't care about it, it's underscore)

```python
for _ in range(10):
  print _
```

```python
color, _ , _ , mileage = car
```

```python
>>> list()
[]
>>> _.append(1)
>>> _.append(2)
>>> _
[1,2]
```


### 7 - __bam__ dunder bam

```python
class PrefixPostfixTest:
  def __init__(self):
    self.__bam__ = 42

>>> PrefixPostfixTest().__bam__

### 6 - __baz is name-mangled by python interpreter

- Happens both to methods and attributes
- Probably helps in keeping clashes out of the class heirarchy tree

```python
class Test:
  def __init__(self):
    self.foo = 11
    self._bar = 23
    self.__baz = 42

dir(Test())
```

```python
class ManglingTest:
  def __init__(self):
    self.__mangled = 'hello'
    
  def get_mangled(self):
    return self.__mangled
```

```python
class MangledMethod:
  def __method(self):
    return 42
    
  def call_it(self):
    return self.__method()
```

```python
_MangledGlobal__mangled = 23

class MangledGlobal:
  def test(self):
    return __mangled

>>> MangledGlobal().test()
23
```


### 5 - wildcard imports and underscore

```python
>>> from my_module import *
>>> external_func()
23
>>> _internal_func()
NameError: "name '_internal_func' is not defined"
```

### 4 - contextlib to create with interface, generator based

```python
from contextlib import contextmanager

@contextmanager
def managed_file(name):
  try:
    f = open(name,'w')
    yield f
  finally:
    f.close()

>>> with managed_file('hello.txt') as f:
      f.write('helloworld')
      f.write('be now')
```


### 3 - try except finally ~~ with

```python
some_lock = threading.Lock()

#Harmful
some_lock.acquire()
try:
  #Do something
finally:
  some_lock.release()

#Better
with some_lock:
  #Do something
```

### 2 - Context With

```python
class ManagedFile:
  def __init__(self,name):
    self.name= name
  
  def __enter__(self):
    self.file = open(self.name,"w")
    return self.file
    
  def __exit__(self,exc_type, exc_val , exc_tb):
    if self.file:
      self.file.close()

with ManagedFile('hello.txt') as f:
  f.write('hello world')
  f.write('bye now')
```


### 1 - assertions

- Assertions can be disabled globally, so don't use them for any real validations
- Assertions are good way to handle the remaining if-elif-else condition
- Assertions are to check internal consistencies, and cannot be handled
- assert <assert condition>
