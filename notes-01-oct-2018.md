# python-notes - 01-oct-2018

### 26 - print in python 2|3

It seems in python3 print is a function and not a keyword

```python
#python 2
>>> p = print
  File "<stdin>", line 1
    p = print
            ^
SyntaxError: invalid syntax

#python 3
>>> p = print
>>> p('hello')
hello
```

### 25 - multithreading

```python
# Python program to illustrate the concept 
# of threading 
# importing the threading module 
import threading 
  
def print_cube(num): 
    """ 
    function to print cube of given num 
    """
    print("Cube: {}".format(num * num * num)) 
  
def print_square(num): 
    """ 
    function to print square of given num 
    """
    print("Square: {}".format(num * num)) 
  
if __name__ == "__main__": 
    # creating thread 
    t1 = threading.Thread(target=print_square, args=(10,)) 
    t2 = threading.Thread(target=print_cube, args=(10,)) 
  
    # starting thread 1 
    t1.start() 
    # starting thread 2 
    t2.start() 
  
    # wait until thread 1 is completely executed 
    t1.join() 
    # wait until thread 2 is completely executed 
    t2.join() 
  
    # both threads completely executed 
    print("Done!") 
```

### 24 - \__init__

"\__init\__" is a reseved method in python classes. It is known as a constructor in object oriented concepts. This method called when an object is created from the class and it allow the class to initialize the attributes of a class.

### 23 - self 

self represents the instance of the class. By using the "self" keyword we can access the attributes and methods of the class in python.

### 22 - timing functions in python

```python
def timer(fn, *args):
    import time
    start = time.clock()
    return fn(*args), time.clock() - start

timer(max, range(1e6))
```

### 21 - dict

```python
dict(a=1, b=2, c=3, dee=4) 
```    

### 20 - cout << x << y ...

```python
import sys

class ostream:
    def __init__(self, file):
        self.file = file
        
    def __lshift__(self, obj):
        self.file.write(str(obj));
        return self

cout = ostream(sys.stdout)
cerr = ostream(sys.stderr)
nl = '\n'

cout << x << " " << y << nl
```

### 19 - __name__ == "__main__"

```python
# a.py
import b
```
```python
# b.py
print "Hello World from %s!" % __name__

if __name__ == '__main__':
    print "Hello World again from %s!" % __name__
```

### 18 - Code in finally clause 

The code in a finally clause does get executed after the try clause whether or not there is an exception, and even if sys.exit is called. However, the finally clause will not execute if execution never gets to it. This would happen regardless of the value of choice in the following: 

```python
try:
    if choice:
        while True:
            pass
    else:
        print "Please pull the plug on your computer sometime soon..."
        time.sleep(60 * 60 * 24 * 365 * 10000)
finally:
    print "Finally ..."
```

### 17 - Dynamic class creation

```python
def choose_class(name):
    if name == 'foo':
        class Foo(object):
            pass
        return Foo # return the class, not an instance
    else:
        class Bar(object):
            pass
        return Bar
```
```python
MyShinyClass = type('MyShinyClass', (), {}) # returns a class object
```

### 16 - Garbage collection in Python
With respect to CPython

* Python maintains a count of the number of references to each object in memory. If a reference count goes to zero then the associated object is no longer live and the memory allocated to that object can be freed up for something else
* Occasionally things called "reference cycles" happen. The garbage collector periodically looks for these and cleans them up. An example would be if you have two objects o1 and o2 such that o1.x == o2 and o2.x == o1. If o1 and o2 are not referenced by anything else then they shouldn't be live. But each of them has a reference count of 1.
* Certain heuristics are used to speed up garbage collection. For example, recently created objects are more likely to be dead. As objects are created, the garbage collector assigns them to generations. Each object gets one generation, and younger generations are dealt with first.

### 15 - Decorator with annotation

```python
@my_decorator
def my_func(stuff):
    do_things
```
above code is equivalent to:
```python
def my_func(stuff):
    do_things

my_func = my_decorator(my_func)
```

### 14 - Monkey Patching

* Modifying behaviour of something after it's already defined
```python
import datetime
datetime.datetime.now = lambda: datetime.datetime(2012, 12, 12)
```

### 13 - Classes are objects in Python

* While creating a class, a object of same is created.
* This object can be passed as argument, assigned to variables, attributes can be added or deleted from it and all other stuff that is supported for objects.
* Classes can be created dynamically.
* This object (the class) is itself capable of creating objects (the instances), and this is why it's a class.

```python
class ObjectCreator(object): 
    pass
print ObjectCreator()
print ObjectCreator
```

### 12 - Module import caching

* Module import are cached everytime they are imported; so it does not go through the whole import process again
* If import is inside a function; it's only imported when the function is run

### 11 - Module import location in python code

Module importing is quite fast, but not instant. This means that:

* Putting the imports at the top of the module is fine, because it's a trivial cost that's only paid once.
* Putting the imports within a function will cause calls to that function to take longer.

### 10 - Print directory listings recursively
```python
def print_directory_contents(sPath):
    import os                                       
    for sChild in os.listdir(sPath):                
        sChildPath = os.path.join(sPath,sChild)
        if os.path.isdir(sChildPath):
            print_directory_contents(sChildPath)
        else:
            print(sChildPath)
```

### 9 - Counter
```python
from collections import Counter 
c=Counter(['a','b','c','a','b','a']) 
c
```

### 8 - What is PEP 8?

PEP 8 is a coding convention, a set of recommendation, about how to write your Python code more readable. 

### 7 - Decorators

Decorators in Python are used to modify or inject code in functions or classes. Using decorators, you can wrap a class or function method call so that a piece of code can be executed before or after the execution of the original code. Decorators can be used to check for permissions, modify or track the arguments passed to a method, logging the calls to a specific method, etc.

```python
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

def say_whee():
    print("Whee!")

say_whee = my_decorator(say_whee)
```

### 6 - List Sort

```python
list = ["1", "4", "0", "6", "9"]
list = [int(i) for i in list]
list.sort()
print (list)
```

### 5 - Random Shuffle

```python
from random import shuffle
x = ['Keep', 'The', 'Blue', 'Flag', 'Flying', 'High']
shuffle(x)
print(x)
```

### 4 - *args, \**kwargs 

We use *args when we aren’t sure how many arguments are going to be passed to a function, or if we want to pass a stored list or tuple of arguments to a function. 
\**kwargs is used when we don’t know how many keyword arguments will be passed to a function, or it can be used to pass the values of a dictionary as keyword arguments. The identifiers args and kwargs are a convention, you could also use *bob and \**billy but that would not be wise.

```python
def f(*args,**kwargs): print(args, kwargs)

l = [1,2,3]
t = (4,5,6)
d = {'a':7,'b':8,'c':9}

f()
f(1,2,3)                    # (1, 2, 3) {}
f(1,2,3,"groovy")           # (1, 2, 3, 'groovy') {}
f(a=1,b=2,c=3)              # () {'a': 1, 'c': 3, 'b': 2}
f(a=1,b=2,c=3,zzz="hi")     # () {'a': 1, 'c': 3, 'b': 2, 'zzz': 'hi'}
f(1,2,3,a=1,b=2,c=3)        # (1, 2, 3) {'a': 1, 'c': 3, 'b': 2}

f(*l,**d)                   # (1, 2, 3) {'a': 7, 'c': 9, 'b': 8}
f(*t,**d)                   # (4, 5, 6) {'a': 7, 'c': 9, 'b': 8}
f(1,2,*t)                   # (1, 2, 4, 5, 6) {}
f(q="winning",**d)          # () {'a': 7, 'q': 'winning', 'c': 9, 'b': 8}
f(1,2,*t,q="winning",**d)   # (1, 2, 4, 5, 6) {'a': 7, 'q': 'winning', 'c': 9, 'b': 8}

def f2(arg1,arg2,*args,**kwargs): print(arg1,arg2, args, kwargs)

f2(1,2,3)                       # 1 2 (3,) {}
f2(1,2,3,"groovy")              # 1 2 (3, 'groovy') {}
f2(arg1=1,arg2=2,c=3)           # 1 2 () {'c': 3}
f2(arg1=1,arg2=2,c=3,zzz="hi")  # 1 2 () {'c': 3, 'zzz': 'hi'}
f2(1,2,3,a=1,b=2,c=3)           # 1 2 (3,) {'a': 1, 'c': 3, 'b': 2}

f2(*l,**d)                   # 1 2 (3,) {'a': 7, 'c': 9, 'b': 8}
f2(*t,**d)                   # 4 5 (6,) {'a': 7, 'c': 9, 'b': 8}
f2(1,2,*t)                   # 1 2 (4, 5, 6) {}
f2(1,1,q="winning",**d)      # 1 1 () {'a': 7, 'q': 'winning', 'c': 9, 'b': 8}
f2(1,2,*t,q="winning",**d)   # 1 2 (4, 5, 6) {'a': 7, 'q': 'winning', 'c': 9, 'b': 8} 
```

### 3 - Yeild list from function

```python
def createGenerator()
  mylist = range(3)
  for i in mylist:
    yield i*i

mygenerator = createGenerator()
```

### 2 - Generator List

```python
mygenerator = ( x for x in range(3) )
```

### 1 - List

```python
mylist  = [ x for x in range(3) ]
```
