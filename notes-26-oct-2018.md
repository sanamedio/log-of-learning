# 26-oct-2018

### 5 - PEP 201 - Lockstep interation

```python
>>> a = (1, 2, 3)
>>> b = (4, 5, 6)
>>> for i in map(None, a, b): print i
...
(1, 4)
(2, 5)
(3, 6)
>>> map(None, a, b)
[(1, 4), (2, 5), (3, 6)]

>>> c = (4, 5, 6, 7)
>>> map(None, a, c)
[(1, 4), (2, 5), (3, 6), (None, 7)]


```

### 4 - Core Developer Tutorial

- https://cpython-core-tutorial.readthedocs.io/en/latest/

### 3 - Weak references

- Tracking objects create another reference to them in Python
- weakref module provides tools to track objects without creating additional references to them
- When a object is not needed it's automatically removed from the weakref table

```python
import weakref, gc

class A:
  def __init__(self, value):
    self.value = value
  def __repr__(self):
    return str(self.value)

a = A(10) # create a refeirernce
d = weakref.WeakValueDictionary()
d['primary'] = a
d['primary'] # 10
del a
gc.collect #0
d['primary'] # raises exception , entry was automatically removed
```



### 2 - PEP8001 - Mostly about how the Python development will continue with BFDL and voting algo for same


- https://en.wikipedia.org/wiki/Instant-runoff_voting
- There is no perfect voting method. It has been shown by the Gibbard-Satterthwaite theorem that any single-winner ranked voting method which is not dictatorial must be susceptible to so-called "tactical voting".
  - Tactical voting occurs when a voter supports a candidate against their sincere preference in order to prevent an outcome they find most undesirable. There are four major tactical voting strategies (compromising, burying, push-over, and bullet voting).
- Instant run-off ranked voting is resistant to burying and bullet voting, while being somewhat vulnerable to compromising (less than the plurality method) and vulnerable to push-over voting. Let's summarize those two:
  - compromising - the voter ranks a less desirable alternative higher because they believe it has a higher chance of being elected; this is sometimes called "casting a useful vote");
  - push-over - if the voter is relatively sure their preferred candidate will survive the first counting round, they may rank "the weakest" alternative higher in the hope of that weak alternative being easily beatable in a subsequent round.



### 1 - Reading PEPs

- https://www.python.org/dev/peps/
- Python Enhancement Proposals(PEP)
