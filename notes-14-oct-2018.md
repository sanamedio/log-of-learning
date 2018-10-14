# 14-oct-2018

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
