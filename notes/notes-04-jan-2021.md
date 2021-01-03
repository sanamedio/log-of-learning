# 04-jan-2021

### 2 - generating cross product withi itertools

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
