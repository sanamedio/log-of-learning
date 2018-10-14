# 14-oct-2018

### 29 - nonlocal vs global

```python
def outer():
    x = "local"
    
    def inner():
        nonlocal x
        x = "nonlocal"
        print("inner:", x)
    
    inner()
    print("outer:", x)

outer()
```

### 28 - gdb + python + reverse debugging 

- Python can be used inside gdb
- Can interact with GDB functionality
- We can do debugging in reverse using gdb
- Core dump can be directly imported to GDB after seg fault
- ```shell ps```
- https://undo.io/resources/presentations/cppcon-2015-greg-law-give-me-15-minutes-ill-change/
- https://www.youtube.com/watch?v=-n9Fkq1e6sg

### 27 - Breakpoint in python interpreter

```python
$ gdb python
(gdb) b bool_newbb
Breakpoint 1 at 0x44812f: file Objects/boolobject.c, line 44.
(gdb) r
[GCC 6.3.1 20170109] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> a = bool(1)

Breakpoint 1, bool_new (type=0x87a700 <PyBool_Type>, args=(1,), kwds=0x0) at Objects/boolobject.c:44
44	{
```

### 26 - ChainMap

```python
# importing collections for ChainMap operations 
import collections 
  
# initializing dictionaries 
dic1 = { 'a' : 1, 'b' : 2 } 
dic2 = { 'b' : 3, 'c' : 4 } 
  
# initializing ChainMap 
chain = collections.ChainMap(dic1, dic2) 
  
# printing chainMap using maps 
print ("All the ChainMap contents are : ") 
print (chain.maps) 
  
# printing keys using keys() 
print ("All keys of ChainMap are : ") 
print (list(chain.keys())) 
  
# printing keys using keys() 
print ("All values of ChainMap are : ") 
print (list(chain.values())) 
```

### 25 - Counters

```python
from collections import Counter 
  
coun = Counter(a=1, b=2, c=3) 
print(coun) 
  
print(list(coun.elements())) 
```

```python
# Python example to demonstrate most_elements() on 
# Counter 
from collections import Counter 
  
coun = Counter(a=1, b=2, c=3, d=120, e=1, f=219) 
  
# This prints 3 most frequent characters 
for letter, count in coun.most_common(3): 
    print('%s: %d' % (letter, count)) 
```
```python

# A Python program to demonstrate update() 
from collections import Counter 
coun = Counter() 
  
coun.update([1, 2, 3, 1, 2, 1, 1, 2]) 
print(coun) 
  
coun.update([1, 2, 4]) 
print(coun) 
```

```python

# Python program to demonstrate that counts in  
# Counter can be 0 and negative 
from collections import Counter 
  
c1 = Counter(A=4,  B=3, C=10) 
c2 = Counter(A=10, B=3, C=4) 
  
c1.subtract(c2) 
print(c1) 
```

### 24 - lambda, filter and reduce

```python

#  filtering odd numbers 
lst = filter(lambda x : x % 2 == 1, range(1, 20)) 
print lst 
  
#  filtering odd square which are divisble by 5 
lst = filter(lambda x : x % 5 == 0,  
      [x ** 2 for x in range(1, 11) if x % 2 == 1]) 
print lst 
  
#   filtering negative numbers 
lst = filter((lambda x: x < 0), range(-5,5)) 
print lst 
  
#  implementing max() function, using 
print reduce(lambda a,b: a if (a > b) else b, [7, 12, 45, 100, 15]) 
```

### 23 - list partitioning in python

```python
# Declaring the list geek 
geek = ['Sun', 'Flowers', 'Peoples', 'Animals', 'Day', 'Night'] 
  
# In python 2.7, just remove the list keyword 
partition = list(zip (*[iter(geek)] * 2)) 
print (partition) 
```

### 22 - setting recursion limit in python

```python
import sys

x=1001
print(sys.getrecursionlimit())

sys.setrecursionlimit(x)
print(sys.getrecursionlimit())

#1-> 1000
#2-> 1001
```

### 21 - zipping lists to dict

```python
t1 = (1, 2, 3)
t2 = (10, 20, 30)

print(dict (zip(t1,t2)))

#-> {1: 10, 2: 20, 3: 30}
```

### 20 - pygorithm module 

```python
from pygorithm.data_structures import stack 
```

### 19 - list flattening using DFS

```python
def unifylist(l_input, l_target):
    for it in l_input:
        if isinstance(it, list):
            unifylist(it, l_target)
        elif isinstance(it, tuple):
            unifylist(list(it), l_target)
        else:
            l_target.append(it)
    return l_target

test =  [[-1, -2], [1,2,3, [4,(5,[6,7])]], (30, 40), [25, 35]]

print(unifylist(test,[]))

#Output => [-1, -2, 1, 2, 3, 4, 5, 6, 7, 30, 40, 25, 35]
```


### 18 - Switch case with system_dict
```python
def xswitch(x): 
	return xswitch._system_dict.get(x, None) 

xswitch._system_dict = {'files': 10, 'folders': 5, 'devices': 2}

print(xswitch('default'))
print(xswitch('devices'))

#1-> None
#2-> 2
```

### 17 - Infinity in python
```python
p_infinity = float('Inf') 
n_infinity = float('-Inf')
```

### 16 - Dictionary switch
```python
stdcalc = {
	'sum': lambda x, y: x + y,
	'subtract': lambda x, y: x - y
}

print(stdcalc['sum'](9,3))
print(stdcalc['subtract'](9,3))

#1-> 12
#2-> 6
```

### 15 - unpacking using splat operator
```python
def test(x, y, z):
	print(x, y, z)

testDict = {'x': 1, 'y': 2, 'z': 3} 
testList = [10, 20, 30]

test(*testDict)
test(**testDict)
test(*testList)

#1-> x y z
#2-> 1 2 3
#3-> 10 20 30
```

### 14 - enumerate in python
```python
testlist = [10, 20, 30]
for i, value in enumerate(testlist):
	print(i, ': ', value)

#1-> 0 : 10
#2-> 1 : 20
#3-> 2 : 30
```

### 13 - python version
```python
import sys
print sys.version
```

### 12 - set comprehension
```python
testSet = {i * 2 for i in xrange(10)}
```

### 11 - underscore in interactive prompt

```python
>>> 2 + 1
3
>>> _
3
>>> print _
3
```

### 10 - multiline string

```python
multiStr = "select * from multi_row \
where row_id < 5"
print(multiStr)
```
or
```python
multiStr = """select * from multi_row 
where row_id < 5"""
print(multiStr)
```
or
```python
multiStr= ("select * from multi_row "
"where row_id < 5 "
"order by age") 
print(multiStr)
```


### 9 - Lambda and raw input

```python
>>> result = map(lambda x:int(x) ,raw_input().split())
1 2 3 4
>>> result
[1, 2, 3, 4]
>>> x, y = map(int, raw_input().split()) 
```

### 8 - Flattening list

```python
>>> a = [ [1,2] , [3,4] , [5,6] ]
>>> import itertools 
>>> list(itertools.chain.from_iterable(a))
[1, 2, 3, 4, 5, 6]
```

### 7 - Zipping lists

```python
>>> for x, y in zip(list1,list2):
...    print x, y
...
a p
b q
c r
d s
```

### 6 - Transposing matrix

```python
>>> mat = [[1, 2, 3], [4, 5, 6]]
>>> zip(*mat)
[(1, 4), (2, 5), (3, 6)]
```

### 5 - Checking if strings are anagram or not

```python

from collections import Counter 
def is_anagram(str1, str2): 
     return Counter(str1) == Counter(str2) 
print(is_anagram('geek', 'eegk')) 
  
print(is_anagram('geek', 'peek'))     
```

### 4 - Check Memory usage of an object

```python
import sys 
x = 1
print(sys.getsizeof(x)) 
```

### 3 - Return Multiple values from a function

```python

def x(): 
    return 1, 2, 3, 4
a, b, c, d = x() 
  
print(a, b, c, d) 
```

### 2 - Enums

```python

class MyName: 
    Geeks, For, Geeks = range(3) 
  
print(MyName.Geeks) 
print(MyName.For) 
print(MyName.Geeks) 
```

### 1 - Path of imports 

```python
import os; 
import socket; 
  
print(os) 
print(socket) 
```
