# 03-dec-2018


# 2 - modulus and floor div with python

- from here : https://luminousmen.com/post/7

```python
>>> -12 % 10
8
>>> -12 // 10
-2
>>> -12 / 10
-1.2
>>> 
```

# 1 - default argument initialization

- always gets me into thinking otherwise; quite unintiutive at first

```python
>>> def extendList(val, l = [] ):
...     l.append(val)
...     return l
... 
>>> list1 = extendList(10)
>>> list2 = extendList(123,[])
>>> list3 = extendList('a')
>>> list1,list2,list3
([10, 'a'], [123], [10, 'a'])
>>> 
```

