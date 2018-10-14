# 14-oct-2018

### 1 - Path of imports 

```python
import os; 
import socket; 
  
print(os) 
print(socket) 
```

### 2 - Enums

```python

class MyName: 
    Geeks, For, Geeks = range(3) 
  
print(MyName.Geeks) 
print(MyName.For) 
print(MyName.Geeks) 
```

### 3 - Return Multiple values from a function

```python

def x(): 
    return 1, 2, 3, 4
a, b, c, d = x() 
  
print(a, b, c, d) 
```

### 4 - Check Memory usage of an object

```python
import sys 
x = 1
print(sys.getsizeof(x)) 
```

### 5 - Checking if strings are anagram or not

```python

from collections import Counter 
def is_anagram(str1, str2): 
     return Counter(str1) == Counter(str2) 
print(is_anagram('geek', 'eegk')) 
  
print(is_anagram('geek', 'peek'))     
```


