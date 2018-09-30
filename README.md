# python-notes
Just notes from here and there.

1. List
```
mylist  = [ x for x in range(3) ]
```

2. Generator List
```
mygenerator = ( x for x in range(3) )
```

3. Yeild list from function
```
def createGenerator()
  mylist = range(3)
  for i in mylist:
    yield i*i

mygenerator = createGenerator()
```

4. *args, \**kwargs 

We use *args when we aren’t sure how many arguments are going to be passed to a function, or if we want to pass a stored list or tuple of arguments to a function. 
\**kwargs is used when we don’t know how many keyword arguments will be passed to a function, or it can be used to pass the values of a dictionary as keyword arguments. The identifiers args and kwargs are a convention, you could also use *bob and \**billy but that would not be wise.


5 Random Shuffle
```
from random import shuffle
x = ['Keep', 'The', 'Blue', 'Flag', 'Flying', 'High']
shuffle(x)
print(x)
```



