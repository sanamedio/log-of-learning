# 17-nov-2018

### 2 - Min Queue and Max queue implementations ( not efficient )

```python
arr = [ 1,2,123,4534,23,434534,3,4234,234234234]

class MaxQueue:

    def __init__(self,size):
        self.size = size
        self.data = []

    def enq(self,item):

        if len(self.data) == self.size:
            if item > min(self.data):
                self.data.remove(min(self.data))
                self.data.append(item)
        else:
            self.data.append(item)


    def __repr__(self):
        return str(self.data)


class MinQueue:

    def __init__(self,size):
        self.size = size
        self.data = []

    def enq(self,item):

        if len(self.data) == self.size:
            if item < max(self.data):
                self.data.remove(max(self.data))
                self.data.append(item)
        else:
            self.data.append(item)


    def __repr__(self):
        return str(self.data)


mq = MaxQueue(3)

print(arr)

for item in arr:
    mq.enq(item)

print(mq)

mq = MinQueue(3)

for item in arr:
    mq.enq(item)

print(mq)
```
```python
import random

class RandomQueue:

    def __init__(self, size):
        self.size = size
        self.data = []

    def enq(self,item):
        self.data.append(item)

    def deq(self):

        if len(self.data) > 0 :

            x = random.choice(self.data)
            self.data.remove(x)
            return x

        return None

    def __repr__(self):
        return str(self.data)
```
        


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
