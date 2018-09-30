# python-notes
Just notes from here and there.

1 List

```python
mylist  = [ x for x in range(3) ]
```

2 Generator List

```python
mygenerator = ( x for x in range(3) )
```

3 Yeild list from function

```python
def createGenerator()
  mylist = range(3)
  for i in mylist:
    yield i*i

mygenerator = createGenerator()
```

4 *args, \**kwargs 

We use *args when we aren’t sure how many arguments are going to be passed to a function, or if we want to pass a stored list or tuple of arguments to a function. 
\**kwargs is used when we don’t know how many keyword arguments will be passed to a function, or it can be used to pass the values of a dictionary as keyword arguments. The identifiers args and kwargs are a convention, you could also use *bob and \**billy but that would not be wise.


5 Random Shuffle

```python
from random import shuffle
x = ['Keep', 'The', 'Blue', 'Flag', 'Flying', 'High']
shuffle(x)
print(x)
```
6 List Sort

```python
list = ["1", "4", "0", "6", "9"]
list = [int(i) for i in list]
list.sort()
print (list)
```
7 Decorators

Decorators in Python are used to modify or inject code in functions or classes. Using decorators, you can wrap a class or function method call so that a piece of code can be executed before or after the execution of the original code. Decorators can be used to check for permissions, modify or track the arguments passed to a method, logging the calls to a specific method, etc.



