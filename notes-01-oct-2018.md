# python-notes

python is sweet, gentle and elegant :)

### 1 - List

```python
mylist  = [ x for x in range(3) ]
```

### 2 - Generator List

```python
mygenerator = ( x for x in range(3) )
```

### 3 - Yeild list from function

```python
def createGenerator()
  mylist = range(3)
  for i in mylist:
    yield i*i

mygenerator = createGenerator()
```

### 4 - *args, \**kwargs 

We use *args when we aren’t sure how many arguments are going to be passed to a function, or if we want to pass a stored list or tuple of arguments to a function. 
\**kwargs is used when we don’t know how many keyword arguments will be passed to a function, or it can be used to pass the values of a dictionary as keyword arguments. The identifiers args and kwargs are a convention, you could also use *bob and \**billy but that would not be wise.

```python
def myFun(arg1, *argv): 
    print ("First argument :", arg1) 
    for arg in argv: 
        print("Next argument through *argv :", arg) 
  
myFun('Hello', 'Well', '2', 'SEe') 
```

```python
def myFun(arg1, **kwargs):  
    for key, value in kwargs.items(): 
        print ("%s == %s" %(key, value)) 
  
# Driver code 
myFun("Hi", first ='second', mid ='third', last='First')     
```

### 5 - Random Shuffle

```python
from random import shuffle
x = ['Keep', 'The', 'Blue', 'Flag', 'Flying', 'High']
shuffle(x)
print(x)
```
### 6 - List Sort

```python
list = ["1", "4", "0", "6", "9"]
list = [int(i) for i in list]
list.sort()
print (list)
```
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
### 8 - What is PEP 8?

PEP 8 is a coding convention, a set of recommendation, about how to write your Python code more readable. 

### 9 - Counter
```python
from collections import Counter 
c=Counter(['a','b','c','a','b','a']) 
c
```
