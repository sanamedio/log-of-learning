# 22-dec-2018

### 2 - center the string

```python

In [13]: "asdasdsad".center(20)
Out[13]: '     asdasdsad      '

```

### 1 - list 

- http://effbot.org/zone/python-list.htm
- The list object consists of two internal parts; one object header, and one separately allocated array of object references. The latter is reallocated as necessary. 
- The list object stores pointers to objects, not the actual objects themselves. The size of a list in memory depends on the number of objects in the list, not the size of the objects.
- The time needed to get or set an individual item is constant, no matter what the size of the list is (also known as “O(1)” behaviour).
- The time needed to append an item to the list is “amortized constant”; whenever the list needs to allocate more memory, it allocates room for a few items more than it actually needs, to avoid having to reallocate on each call (this assumes that the memory allocator is fast; for huge lists, the allocation overhead may push the behaviour towards O(n*n)).
- The time needed to insert an item depends on the size of the list, or more exactly, how many items that are to the right of the inserted item (O(n)). In other words, inserting items at the end is fast, but inserting items at the beginning can be relatively slow, if the list is large.
- The time needed to remove an item is about the same as the time needed to insert an item at the same location; removing items at the end is fast, removing items at the beginning is slow.
- The time needed to reverse a list is proportional to the list size (O(n)).
- The time needed to sort a list varies; the worst case is O(n log n), but typical cases are often a lot better than that. 


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

```python
#printing lists
print ", ".join(map(str, L))

sys.stdout.writelines(L) # if all items are strings
```

```python

#min and max can also take a mapping function
lo = min(L, key=int)
hi = max(L, key=int)

#sorting
def compare(a, b):
     return cmp(int(a), int(b)) # compare as integers

L.sort(compare)

def compare_columns(a, b):
     # sort on ascending index 0, descending index 2
     return cmp(a[0], b[0]) or cmp(b[2], a[2])

out = sorted(L, compare_columns)

#creates a key array where all elements are mapped to int, and uses that for sorting
L.sort(key=int)

out = sorted(L, key=int)
```

```python
# just to remind me, last item is not included, but first item is
list(range(10,1,-1))
[10, 9, 8, 7, 6, 5, 4, 3, 2]
```
