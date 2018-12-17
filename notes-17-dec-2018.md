# 17-dec-2018

### 1 - pampy

- https://github.com/santinic/pampy

```python
Python 3.6.7 (default, Oct 22 2018, 11:32:17) 
Type 'copyright', 'credits' or 'license' for more information
IPython 7.1.1 -- An enhanced Interactive Python. Type '?' for help.

In [1]: from pampy import match, _                                                                                                                                                                                                            

In [2]: input = [1,2,3]                                                                                                                                                                                                                       

In [3]: pattern = [1,2,_]                                                                                                                                                                                                                     

In [4]: action = lambda x: "it's {}".format(x)                                                                                                                                                                                                

In [5]: match(input, pattern, action)                                                                                                                                                                                                         
Out[5]: "it's 3"

In [6]:            
```


```python
In [6]: from pampy import match,_                                                                                                                                                                                                             

In [7]: def fibonacci(n): 
   ...:     return match(n, 
   ...:         1, 1, 
   ...:         2, 1, 
   ...:         _, lambda x: fibonacci(x-1) + fibonacci(x-2) 
   ...:         ) 
   ...:                                                                                                                                                                                                                                       

In [8]: fibonacci(1)                                                                                                                                                                                                                          
Out[8]: 1

In [9]: fibonacci(5)                                                                                                                                                                                                                          
Out[9]: 5

In [10]: fibonacci(10)                                                                                                                                                                                                                        
Out[10]: 55

In [11]: 
```

```python
match(x,
    3,              "this matches the number 3",

    int,            "matches any integer",

    (str, int),     lambda a, b: "a tuple (a, b) you can use in a function",

    [1, 2, _],      "any list of 3 elements that begins with [1, 2]",

    {'x': _},       "any dict with a key 'x' and any value associated",

    _,              "anything else"
)
```

```python
from pampy import match, _

x = [1, [2, 3], 4]

match(x, [1, [_, 3], _], lambda a, b: [1, [a, 3], b])           # => [1, [2, 3], 4]
```
