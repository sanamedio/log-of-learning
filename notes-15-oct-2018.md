# 15-oct-2018

### 6 - __baz is name-mangled by python interpreter

```python
class Test:
  def __init__(self):
    self.foo = 11
    self._bar = 23
    self.__baz = 42

dir(Test())
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
