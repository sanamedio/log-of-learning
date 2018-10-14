# 14-oct-2018

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
