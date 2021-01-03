# 04-jan-2021

### 6 - Steinhaus-Johnson-Trotter permutation generation

https://sahandsaba.com/combinatorial-generation-using-coroutines-in-python.html

SJT is an algorithm for generating all permutations in Gray order. Here, Gray order means that "distance" between two subsequent permutations is one, where a distance of one means that they differ from each other by one swap of adjacent elements, also called a transposition. The basic idea of the algorithm is recursive. Given a list of permutations of n-1 , we can produce a list of permutations of n by inserting nn into each permutation of n-1 , first by starting at the very right end and moving to the left, and then moving to the right, and so on. 

recursive
```python
def permutations(n):
    if n:
        r = list(range(n))
        for pi in permutations(n - 1):
            for i in r:
                yield pi[i:] + [n] + pi[:i]
            r.reverse()
    else:
        yield []
```

### 5 - binary reflected gray codes

https://sahandsaba.com/combinatorial-generation-using-coroutines-in-python.html

A binary Gray code is a listing of all binary strings of length nn such that each two subsequent strings are different in exactly one index. The binary reflected Gray code (BGRC), is one such code. It is given by recursively generating the BGRC for n - 1n−1 , then prepending a zero to all strings, and a one to all the strings in reverse order

recursive
```python
def gray(n):
    if n > 0:
        g = gray(n - 1)
        gr = reversed(g)
        return (['0' + a for a in g] +
                ['1' + a for a in gr])
    else:
        return ['']
And example output:

>>> for a in gray(3):
...     print(a)
...
000
001
011
010
110
111
101
100
```

with coroutines
```
def nobody():
    while True:
        yield False

def troll(a, i):
    previous = troll(a, i - 1) if i > 0 else nobody()
    while True:
        a[i] = 1 - a[i]
        yield True
        yield next(previous)


def setup(n):
    a = [0] * n
    lead_coroutine = troll(a, n - 1)
    return a, lead_coroutine


def gray(n):
    a, lead = setup(n)
    yield a
    while next(lead):
        yield a
```


### 4 - itertools product implementation

itertools product uses iterative approach

```c
/* Update the pool indices right-to-left.  Only advance to the
   next pool when the previous one rolls-over */
for (i=npools-1 ; i >= 0 ; i--) {
    pool = PyTuple_GET_ITEM(pools, i);
    indices[i]++;
    if (indices[i] == PyTuple_GET_SIZE(pool)) {
        /* Roll-over and advance to next pool */
        indices[i] = 0;
        elem = PyTuple_GET_ITEM(pool, 0);
        Py_INCREF(elem);
        oldelem = PyTuple_GET_ITEM(result, i);
        PyTuple_SET_ITEM(result, i, elem);
        Py_DECREF(oldelem);
    } else {
        /* No rollover. Just increment and stop here. */
        elem = PyTuple_GET_ITEM(pool, indices[i]);
        Py_INCREF(elem);
        oldelem = PyTuple_GET_ITEM(result, i);
        PyTuple_SET_ITEM(result, i, elem);
        Py_DECREF(oldelem);
        break;
    }
}
```

### 3 - multi radix numbers with coroutines

https://sahandsaba.com/combinatorial-generation-using-coroutines-in-python.html

very unconventional approach

```python
def nobody():
    while True:
        yield False


def troll(M, a, i):
    previous = troll(M, a, i - 1) if i > 0 else nobody()

    while True:
        if a[i] == M[i] - 1:
            a[i] = 0
            yield next(previous)
        else:
            a[i] += 1
            yield True


def multiradix_coroutine(M):
    n = len(M)
    a = [0] * n
    lead = troll(M, a, n - 1)
    yield a
    while next(lead):
        yield a


for x in multiradix_coroutine([4, 3, 2]):
    print(x)
```

### 2 - generating multi radix numbers

https://sahandsaba.com/combinatorial-generation-using-coroutines-in-python.html

```python
In [6]: from itertools import product

In [7]: def multiradix_product(M):
   ...:     return product(*(range(x) for x in M))
   ...:

In [8]: multiradix_product([1,2,3])
Out[8]: <itertools.product at 0x1071ffd80>

In [9]: list(multiradix_product([1,2,3]))
Out[9]: [(0, 0, 0), (0, 0, 1), (0, 0, 2), (0, 1, 0), (0, 1, 1), (0, 1, 2)]

In [10]: list(multiradix_product([3,3,3]))
Out[10]:
[(0, 0, 0),
 (0, 0, 1),
 (0, 0, 2),
 (0, 1, 0),
 (0, 1, 1),
 (0, 1, 2),
 (0, 2, 0),
 (0, 2, 1),
 (0, 2, 2),
 (1, 0, 0),
 (1, 0, 1),
 (1, 0, 2),
 (1, 1, 0),
 (1, 1, 1),
 (1, 1, 2),
 (1, 2, 0),
 (1, 2, 1),
 (1, 2, 2),
 (2, 0, 0),
 (2, 0, 1),
 (2, 0, 2),
 (2, 1, 0),
 (2, 1, 1),
 (2, 1, 2),
 (2, 2, 0),
 (2, 2, 1),
 (2, 2, 2)]

```

There is another arithimetic approach, whereis we generate binary but just transform them to multi radix

```python
from operator import mul
from functools import reduce


def number_to_multiradix(M, x, a):
    n = len(M)
    for i in range(1, n + 1):
        x, a[-i] = divmod(x, M[-i])
    return a


def multiradix_counting(M):
    n = len(M)
    a = [0] * n
    last = reduce(mul, M, 1)
    for x in range(last):
        yield number_to_multiradix(M, x, a)
```

Then another approach is to use recursion over subproblems

```python
def multiradix(M, n, a, i):
    if i < 0:
        yield a
    else:
        for __ in multiradix(M, n, a, i - 1):
            # Extend each multi-radix number of length i with all possible
            # 0 <= x < M[i] to get a multi-radix number of length i + 1.
            for x in range(M[i]):
                a[i] = x
                yield a


def multiradix_recursive(M):
    n = len(M)
    a = [0] * n
    return multiradix(M, n, a, n - 1)
```

then there is this iterative approach
```python
def multiradix_iterative(M):
    n = len(M)
    a = [0] * n
    while True:
        yield a
        # Find right-most index k such that a[k] < M[k] - 1 by scanning from
        # right to left, and setting everything to zero on the way.
        k = n - 1
        while a[k] == M[k] - 1:
            a[k] = 0
            k -= 1
            if k < 0:
                # Last lexicographic item
                return
        a[k] += 1
```






### 1 - postorder with generators

https://sahandsaba.com/combinatorial-generation-using-coroutines-in-python.html

```python
def postorder(tree):
    if not tree:
        return
    yield from postorder(tree['left'])
    yield from postorder(tree['right'])
    yield tree['value']

tree = lambda: defaultdict(tree)

# Let's build a simple tree representing (1 + 3) * (4 - 2)
T = tree()
T['value'] = '*'
T['left']['value'] = '+'
T['left']['left']['value'] = '1'
T['left']['right']['value'] = '3'
T['right']['value'] = '-'
T['right']['left']['value'] = '4'
T['right']['right']['value'] = '2'

postfix = ' '.join(str(x) for x in postorder(T))
print(postfix)  # Prints 1 3 + 4 2 - *
```
