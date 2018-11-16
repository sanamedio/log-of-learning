# 17-nov-2018

### 1 - Permutations (without inbulit)

```python
In [1]: def permute(a, l , r ):
   ...:     if l == r : print a
   ...:     else:
   ...:         for i in range(l,r+1):
   ...:             a[l],a[i] = a[i], a[l]
   ...:             permute(a,l+1,r)
   ...:             a[l],a[i] = a[i],a[l]
   ...:             

In [2]: permute('abcd', 0,4)
--------------------------------------------------------------------------
TypeError                                Traceback (most recent call last)
<ipython-input-2-80a18831164e> in <module>()
----> 1 permute('abcd', 0,4)

<ipython-input-1-73a1e6e1fc67> in permute(a, l, r)
      3     else:
      4         for i in range(l,r+1):
----> 5             a[l],a[i] = a[i], a[l]
      6             permute(a,l+1,r)
      7             a[l],a[i] = a[i],a[l]

TypeError: 'str' object does not support item assignment

In [3]: permute(list('abcd'), 0,4)
['a', 'b', 'c', 'd']
--------------------------------------------------------------------------
IndexError                               Traceback (most recent call last)
<ipython-input-3-e6e905ac2e89> in <module>()
----> 1 permute(list('abcd'), 0,4)

<ipython-input-1-73a1e6e1fc67> in permute(a, l, r)
      4         for i in range(l,r+1):
      5             a[l],a[i] = a[i], a[l]
----> 6             permute(a,l+1,r)
      7             a[l],a[i] = a[i],a[l]
      8 

<ipython-input-1-73a1e6e1fc67> in permute(a, l, r)
      4         for i in range(l,r+1):
      5             a[l],a[i] = a[i], a[l]
----> 6             permute(a,l+1,r)
      7             a[l],a[i] = a[i],a[l]
      8 

<ipython-input-1-73a1e6e1fc67> in permute(a, l, r)
      4         for i in range(l,r+1):
      5             a[l],a[i] = a[i], a[l]
----> 6             permute(a,l+1,r)
      7             a[l],a[i] = a[i],a[l]
      8 

<ipython-input-1-73a1e6e1fc67> in permute(a, l, r)
      3     else:
      4         for i in range(l,r+1):
----> 5             a[l],a[i] = a[i], a[l]
      6             permute(a,l+1,r)
      7             a[l],a[i] = a[i],a[l]

IndexError: list index out of range

In [4]: permute(list('abcd'), 0,3)
['a', 'b', 'c', 'd']
['a', 'b', 'd', 'c']
['a', 'c', 'b', 'd']
['a', 'c', 'd', 'b']
['a', 'd', 'c', 'b']
['a', 'd', 'b', 'c']
['b', 'a', 'c', 'd']
['b', 'a', 'd', 'c']
['b', 'c', 'a', 'd']
['b', 'c', 'd', 'a']
['b', 'd', 'c', 'a']
['b', 'd', 'a', 'c']
['c', 'b', 'a', 'd']
['c', 'b', 'd', 'a']
['c', 'a', 'b', 'd']
['c', 'a', 'd', 'b']
['c', 'd', 'a', 'b']
['c', 'd', 'b', 'a']
['d', 'b', 'c', 'a']
['d', 'b', 'a', 'c']
['d', 'c', 'b', 'a']
['d', 'c', 'a', 'b']
['d', 'a', 'c', 'b']
['d', 'a', 'b', 'c']
```
