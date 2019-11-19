# 01-oct-2018

### 52 - Default argument initialization issue

```python
>>> def foo(x=[]):
...     x.append(1)
...     print x
... 
>>> foo()
[1]
>>> foo()
[1, 1]
>>> foo()
[1, 1, 1]
```
Instead do this:

```python
>>> def foo(x=None):
...     if x is None:
...         x = []
...     x.append(1)
...     print x
>>> foo()
[1]
>>> foo()
[1]
```

### 51 - Bytecode for CPython
```python
>>> def f(x, y):                # line 1
...    print("Hello")           # line 2
...    if x:                    # line 3
...       y += x                # line 4
...    print(x, y)              # line 5
...    return x+y               # line 6
...                             # line 7
>>> import dis                  # line 8
>>> dis.dis(f)                  # line 9
  2           0 LOAD_GLOBAL              0 (print)
              2 LOAD_CONST               1 ('Hello')
              4 CALL_FUNCTION            1
              6 POP_TOP

  3           8 LOAD_FAST                0 (x)
             10 POP_JUMP_IF_FALSE       20

  4          12 LOAD_FAST                1 (y)
             14 LOAD_FAST                0 (x)
             16 INPLACE_ADD
             18 STORE_FAST               1 (y)

  5     >>   20 LOAD_GLOBAL              0 (print)
             22 LOAD_FAST                0 (x)
             24 LOAD_FAST                1 (y)
             26 CALL_FUNCTION            2
             28 POP_TOP

  6          30 LOAD_FAST                0 (x)
             32 LOAD_FAST                1 (y)
             34 BINARY_ADD
36 RETURN_VALUE
```

### 50 - flavours of python

* CPython - The standard reference implementation from python.org. CPython is the reference implementation of Python, written in C. It compiles Python code to intermediate bytecode which is then interpreted by a virtual machine. CPython provides the highest level of compatibility with Python packages and C extension modules.If you are writing open-source Python code and want to reach the widest possible audience, targeting CPython is best. To use packages which rely on C extensions to function, CPython is your only implementation option.All versions of the Python language are implemented in C because CPython is the reference implementation.

* PyPy - Implementation of Python using the PyPy virtual machine. PyPy is a Python interpreter implemented in a restricted statically-typed subset of the Python language called RPython. The interpreter features a just-in-time compiler and supports multiple back-ends (C, CLI, JVM).PyPy aims for maximum compatibility with the reference CPython implementation while improving performance.If you are looking to increase performance of your Python code, it’s worth giving PyPy a try. On a suite of benchmarks, it’s currently over 5 times faster than CPython.

* Jython - An implementation of Python on the Java virtual machine. Jython is a Python implementation that compiles Python code to Java bytecode which is then executed by the JVM (Java Virtual Machine). Additionally, it is able to import and use any Java class like a Python module.If you need to interface with an existing Java codebase or have other reasons to need to write Python code for the JVM, Jython is the best choice.

### 49 - exec() and eval()

exec() is to execute code present as string whereas eval() is to evaluate expressions and get the value they evaluate to.

```python
>>> a = 5
>>> eval('37 + a')   # it is an expression
42
>>> exec('37 + a')   # it is an expression statement; value is ignored (None is returned)
>>> exec('a = 47')   # modify a global variable as a side effect
>>> a
47
>>> eval('a = 47')  # you cannot evaluate a statement
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<string>", line 1
    a = 47
      ^
SyntaxError: invalid syntax


>>> program = '''
for i in range(3):
    print("Python is cool")
'''
>>> exec(program)
Python is cool
Python is cool
Python is cool

>>> a = 2
>>> my_calculation = '42 * a'
>>> result = eval(my_calculation)
>>> result
84

```

### 48 - // % **
```python
7//2 #3
2**10 #1024
3.5%1.5 #0.5 
```

### 47 - lstrip, rstrip, strip

Functions to remove left, right and both side whitespace

### 46 - keywords
```python
and					
as					
assert					
break					
class					
continue				
def
del
elif
else
except
exec
False
finally
for
from
global
if
import
in
is
lambda
None
not
nonlocal
or
pass
print
raise
return
True
try
while
with
yield
```
### 45 - help() and dir() 

The help() function displays the documentation string and help for its argument.

The dir() function displays all the members of an object(any kind).

### 44 - ternary operator
```python
print("Hi") if a<b else print("Bye")

mint=a if a<b else b
```
### 43 - list to tuple
```python
weekdays = ['sun','mon','tue','wed','thu','fri','sat']
listAsTuple = tuple(weekdays)
print(listAsTuple)

#output: ('sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat')
```

### 42 - list to dict conversion
```python
weekdays = ['sun','mon','tue','wed','thu','fri']
listAsDict = dict(zip(weekdays[0::2], weekdays[1::2]))
print(listAsDict)

#output: {'sun': 'mon', 'thu': 'fri', 'tue': 'wed'}
```

### 41 - deepcopy

A deep copy copies an object into another. This means that if you make a change to a copy of an object. Shallow copy keeps internal references to the original object.

```python
import copy
b = copy.deepcopy(a)
shallow_copy = copy.copy(a)
```

### 40 - globals()

```python
# Example: globals() function 
x = 9
def fn(): 
    y = 3
    z = y + x
    # Calling the globals() method
    z = globals()['x'] = z
    return z
       
# Test Code     
ret = fn() 
print(ret)
```

### 39 - enumerate

```python
alist = ["apple","mango", "orange"] 
astr = "banana"

print(list(enumerate(alist)) )  
# Move the starting index to two from zero
print(list(enumerate(astr, 2)))
```

### 38 - inline conditional

```python
is_leap_year = "Yes" if no_of_days == 366 else "No"
```

### 37 - dict comprehension

```python
adict = {var:var**2 for var in range(10, 20)}
print(adict)
```

### 36 - closure

```python
def multiply_number(num):
    def product(number):
        'product() here is a closure'
        return num * number
    return product

num_2 = multiply_number(2)
print(num_2(11))
print(num_2(24))

num_6 = multiply_number(6)
print(num_6(1))
```

### 35 - yield vs return

```python
# Simple Python function
def fn():
    return "Simple Python function."

# Python Generator function
def generate():
    yield "Python Generator function."

print(next(generate()))
```
another example:

```python
def testgen(index):
  weekdays = ['sun','mon','tue','wed','thu','fri','sat']
  yield weekdays[index]
  yield weekdays[index+1]

day = testgen(0)
print next(day), next(day)

#output: sun mon
```

### 34 - Iterator and Iterable

* The collection type like a list, tuple, dictionary, and set are all iterable objects whereas they are also iterable containers which return an iterator while traversing. 
* Iterable is a interface or behaviour associated with a object whereas iterator is a object which can be used to interact with interable property of the object.

### 33 - Composition

```python
class PC: # Base class
    processor = "Xeon" # Common attribute
    def __init__(self, processor, ram):
        self.processor = processor
        self.ram = ram

    def set_processor(self, new_processor):
        processor = new_processor

    def get_PC(self):
        return "%s cpu & %s ram" % (self.processor, self.ram)

class Tablet():
    make = "Intel"
    def __init__(self, processor, ram, make):
        self.PC = PC(processor, ram) # Composition
        self.make = make

    def get_Tablet(self):
        return "Tablet with %s CPU & %s ram by %s" % (self.PC.processor, self.PC.ram, self.make)

if __name__ == "__main__":
    tab = Tablet("i7", "16 GB", "Intel")
    print(tab.get_Tablet())
```

### 32 - Inheritance

```python
class PC: # Base class
    processor = "Xeon" # Common attribute
    def set_processor(self, new_processor):
        processor = new_processor

class Desktop(PC): # Derived class
    os = "Mac OS High Sierra" # Personalized attribute
    ram = "32 GB"

class Laptop(PC): # Derived class
    os = "Windows 10 Pro 64" # Personalized attribute
    ram = "16 GB"

desk = Desktop()
print(desk.processor, desk.os, desk.ram)

lap = Laptop()
print(lap.processor, lap.os, lap.ram)
```

### 31 - GIL

* Python supports GIL (the global interpreter lock) which is a mutex used to secure access to Python objects, synchronizing multiple threads from running the Python bytecodes at the same time.
* The GIL (Global Interpreter Lock) ensures that a single thread executes at a time. A thread holds the GIL and does a little work before passing it on to the next thread. This makes for an illusion of parallel execution. But in reality, it is just threaded taking turns at the CPU. Of course, all the passing around adds overhead to the execution.

### 30 - id()

Inbuilt function to give a unique id which remains same during lifetime of the object. 
```python
id(object)
```

### 29 - try except

There are two optional clauses you can use in the try-except block.

###### The “else” clause:
It is useful if you want to run a piece of code when the try block doesn’t create an exception.

###### The “finally” clause:
It is useful when you want to execute some steps which run, irrespective of whether there occurs an exception or not.



### 28 - builtin datatypes

Immutable built-in datatypes of Python
* Numbers
* Strings
* Tuples

Mutable built-in datatypes of Python
* List
* Dictionaries
* Sets

### 27 - memory management

* Python memory is managed by Python private heap space. All Python objects and data structures are located in a private heap. The programmer does not have an access to this private heap and interpreter takes care of this Python private heap.
* The allocation of Python heap space for Python objects is done by Python memory manager. The core API gives access to some tools for the programmer to code.
* Python also have an inbuilt garbage collector, which recycle all the unused memory and frees the memory and makes it available to the heap space.

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
Another example:

```python
def decorator_sample(func):
    def decorator_hook(*args, **kwargs):
        print("Before the function call")
        result = func(*args, **kwargs)
        print("After the function call")
        return result
    return decorator_hook

@decorator_sample
def product(x, y):
    "Function to multiply two numbers."
    return x * y

print(product(3, 3))
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
