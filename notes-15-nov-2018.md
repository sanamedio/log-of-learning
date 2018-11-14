# 15-nov-2018

### 2 - Seemingly weird

```python
Python 3.6.6 (default, Sep 12 2018, 18:26:19) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> a = 1
>>> def Foo(a):
...     a = 2
... 
>>> Foo(a)
>>> a
1
>>> b = []
>>> def Foo(b):
...     b.append(1)
... 
>>> Foo(b)
>>> b
[1]
>>> 
```

### 1 - Some tricks with list,set and maps

- from [here](https://github.com/taizilongxu/interview_python)

- unique without set directly
```python
>>> l1 = ['b','c','d','b','c','a','a']
>>> l2 = {}.fromkeys(l1).keys()
>>> print( l2)
dict_keys(['b', 'c', 'd', 'a'])
>>> 
```

- Maintaining order
```python
>>> l1 = ['b','c','d','b','c','a','a']
>>> l2 = list(set(l1))
>>> l2
['d', 'c', 'b', 'a']
>>> l2.sort(key=l1.index)
>>> l2
['b', 'c', 'd', 'a']
>>> 
```

- doing unique using list comprehension
```python
>>> l1 = ['b', 'c' , 'd' , 'b', 'c', 'a', 'a']
>>> l2 = []
>>> [ l2.append(i) for i in l1 if not i in l2 ]
[None, None, None, None]
>>> l2
['b', 'c', 'd', 'a']
>>> 
```
- from keys
```python
>>> dict1={}.fromkeys(('x','y'),-1)
>>> dict={'x':-1,'y':-1}
>>> dict2={}.fromkeys(('x','y'))
>>> dict2={'x':None, 'y':None}
>>> dict
{'x': -1, 'y': -1}
>>> dict1
{'x': -1, 'y': -1}
>>> dict2
{'x': None, 'y': None}
>>> 
```
