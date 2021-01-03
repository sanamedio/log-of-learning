# 04-jan-2021

### 3 - multi radix numbers with coroutines

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
