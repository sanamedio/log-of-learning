# 22-dec-2018

### 1 - list search

- http://effbot.org/zone/python-list.htm

```python
In [9]: def findall(L , value, start = 0 ):
   ...:     i = start - 1
   ...:     while 1:
   ...:         try:
   ...:             i = L.index (value , i + 1 )
   ...:             yield i
   ...:         except ValueError:
   ...:             raise StopIteration
   ...:         
   ...:         

In [10]: for index in findall([1,1,1,1,2,2,2,], 2):
    ...:     print "match at" , index
    ...:     
match at 4
match at 5
match at 6

In [11]: 
```
