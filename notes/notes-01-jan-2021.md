# 01-jan-2021

### 10 - ruler function with yield

https://sahandsaba.com/the-infinite-in-haskell-and-python.html

```python

In [15]: def zeros():
    ...:     while True:
    ...:         yield 0
    ...:

In [17]: def alternate(xs, ys):
    ...:     while True:
    ...:         yield next(xs)
    ...:         yield next(ys)
    ...:
    ...:

In [18]: def ruler():
    ...:     yield from alternate(zeros(), map(lambda x: x+1, ruler()))
    ...:

In [19]: R = ruler()

In [20]: [ next(R) for _ in range(10) ]
Out[20]: [0, 1, 0, 2, 0, 1, 0, 3, 0, 1]
```

### 9 - yield to fibonacci

https://sahandsaba.com/the-infinite-in-haskell-and-python.html

```python
def fib():
    yield 0
    yield 1
    f1, f2 = fib(), fib()
    next(f2)
    while True:
        yield next(f1) + next(f2)

F = fib()
print([next(F) for _ in range(10)])

# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
```

zeros can also be done recursive
```python
def zeros():
    yield 0
    yield from zeros()
```

### 8 - fixed length strings using recursion

```python
In [55]: def strings(A, n):
    ...:     if n == 0:
    ...:         return ['']
    ...:     return [s+c for s in strings(A, n-1) for c in A]
    ...:

In [56]: strings(['0','1','2'], 2)
Out[56]: ['00', '01', '02', '10', '11', '12', '20', '21', '22']
```

### 7 - Y Z combinators

- The Y combinator is a central concept in lambda calculus, which is the formal foundation of functional languages. Y allows one to define recursive functions without using self-referential definitions.(REF: [link](https://lptk.github.io/programming/2019/10/15/simple-essence-y-combinator.html#:~:text=The%20Y%20combinator%20is%20a,without%20using%20self-referential%20definitions.))

- Y combinator allows to find out fixed points of a meta-function. fixed point of a fibonaaci function would be itself (or exact same func probably)

- it helps to avoid explicit self reference in a generic manner

simple example of indirection
```python
#indirect
def f(g):
  print("in f")
  return lambda: g(g)

#explicit
def ff():
  print("in f")
  return lambda: ff()
```

mkrec_nice is a Z combinator
```
In [7]: mkrec = lambda f: f(f)
   ...:
   ...: mkrec_nice = (lambda g:
   ...:   mkrec(lambda rec:
   ...:     g(lambda y: rec(rec)(y))))
   ...:
   ...: fact = mkrec_nice(lambda rec: lambda x:
   ...:   1 if x == 0 else rec(x - 1) * x)

In [8]: fact
Out[8]: <function __main__.<lambda>.<locals>.<lambda>(x)>

In [9]: fact(10)
Out[9]: 3628800
```


### 6 - fsm for n cross m tilings

https://sahandsaba.com/understanding-recurrence-relations-using-python-automata-and-matrices-visualized.html

```python
from collections import deque

def construct_fsm(m):
    """Construct an fsm that reco domino tilings of an m x n board"""

    fsm = {}
    starting_state = frozenset(range(m))

    Q = deque()

    def construct_outgoing_transitions(source):

        if source in fsm:
            return

        fsm[source] = []

        if not source:
            fsm[source].append((starting_state, []))
            return

        def recurse(j, target, tiling):
            if j > max(source):
                fsm[source].append((target, tiling))
                Q.append(target)
            elif j in source:
                if j + 1 in source:
                    recurse(j + 2, target, tiling + [(j, "V")])
                recurse(j + 1, target - {j}, tiling + [(j, "H")])

        recurse(min(source), starting_state, [])

    Q.append(starting_state)
    while Q:
        state = Q.popleft()
        construct_outgoing_transitions(state)

    return fsm


def generate_fsm_language(fsm, n, initial_state, accepting_states):
    """
    Generate all strings of length n accepted by the given FSM.
    Assumes no epsilon-cycles exist in the FSM.
    """

    def dfs(current_state, string_so_far):
        if len(string_so_far) == n:
            if current_state in accepting_states:
                yield string_so_far
            return
        for target_state, label in fsm[current_state]:
            yield from dfs(target_state, string_so_far + [label])

    yield from dfs(initial_state, [])


def tilings(m, n):
    """Generate all tilings of an m x n board using dominoes,"""
    fsm = construct_fsm(m)
    initial_state = accepting_state = frozenset(range(m))
    yield from generate_fsm_language(fsm, n, initial_state, [accepting_state])


#Ipython
In [16]: list(tilings(1,1))
Out[16]: []

In [17]: list(tilings(1,2))
Out[17]: [[[(0, 'H')], []]]

In [18]: list(tilings(2,1))
Out[18]: [[[(0, 'V')]]]

In [19]: list(tilings(2,2))
Out[19]: [[[(0, 'V')], [(0, 'V')]], [[(0, 'H'), (1, 'H')], []]]

In [20]: list(tilings(2,4))
Out[20]:
[[[(0, 'V')], [(0, 'V')], [(0, 'V')], [(0, 'V')]],
 [[(0, 'V')], [(0, 'V')], [(0, 'H'), (1, 'H')], []],
 [[(0, 'V')], [(0, 'H'), (1, 'H')], [], [(0, 'V')]],
 [[(0, 'H'), (1, 'H')], [], [(0, 'V')], [(0, 'V')]],
 [[(0, 'H'), (1, 'H')], [], [(0, 'H'), (1, 'H')], []]]

```

### 5 - visualising tilings

https://sahandsaba.com/understanding-recurrence-relations-using-python-automata-and-matrices-visualized.html

```python
In [24]: def tilings(n):
    ...:     if n < 0:
    ...:         return
    ...:     if n == 0:
    ...:         yield ''
    ...:     for tiling in tilings(n - 1):
    ...:         yield '|' + tiling
    ...:     for tiling in tilings(n - 2):
    ...:         yield '==' + tiling
    ...:

In [27]: for x in tilings(5): print(x)
|||||
|||==
||==|
|==||
|====
==|||
==|==
====|
```

### 4 - von neuman extraction

given a biased coin, how to get fair outcome

https://sahandsaba.com/interview-question-fairness-from-unfairness-randomness-extraction.html

```python
In [1]: import random
   ...:
   ...:
   ...: def bernoulli_process(p):
   ...:     if p > 1.0 or p < 0.0:
   ...:         raise ValueError("p should be between 0.0 and 1.0.")
   ...:     while True:
   ...:         yield random.random() > p
   ...:
   ...:
   ...: def von_neumann_extractor(process):
   ...:     while True:
   ...:         x, y = next(process), next(process)
   ...:         if x != y:
   ...:             yield x
   ...:

In [17]: vne = von_neumann_extractor(bernoulli_process(0.1))

In [19]: from collections import Counter

In [21]: Counter([ next(vne) for x in range(100)])
Out[21]: Counter({False: 55, True: 45})

In [22]: Counter([ next(vne) for x in range(1000)])
Out[22]: Counter({False: 490, True: 510})

In [23]: Counter([ next(vne) for x in range(10000)])
Out[23]: Counter({True: 5074, False: 4926})

```

### 3 - sort letter vs count letter prehash

https://sahandsaba.com/interview-question-grouping-words-into-anagrams.html

```python
import collections

def sort_prehash(word):
    return ''.join(sorted(word))


def count_letters_prehash(word):
    return tuple(collections.Counter(word).items())


def group_anagrams(words, hash_function):
    result = {}
    for w in words:
        s = hash_function(w.lower())
        if s in result:
            result[s] |= {w}
        else:
            result[s] = {w}
    return result.values()

# Usage:
>>> group_anagrams(['tsar', 'rat', 'tar', 'star', 'tars', 'cheese'], sort_prehash)
[set(['tars', 'tsar', 'star']), set(['cheese']), set(['rat', 'tar'])]
>>> group_anagrams(['tsar', 'rat', 'tar', 'star', 'tars', 'cheese'], count_letters_prehash)
[set(['tars', 'tsar', 'star']), set(['cheese']), set(['rat', 'tar'])]
```

### 2 - fast inverse square root

http://h14s.p5r.org/2012/09/0x5f3759df.html

```c
float FastInvSqrt(float x) {
  float xhalf = 0.5f * x;
  int i = *(int*)&x;         // evil floating point bit level hacking
  i = 0x5f3759df - (i >> 1);  // what the fuck?
  x = *(float*)&i;
  x = x*(1.5f-(xhalf*x*x));
  return x;
}
```

### 1 - overlayfs

This is used in containers

https://en.wikipedia.org/wiki/OverlayFS

- OverlayFS is a union mount filesystem implementation for Linux. It combines multiple different underlying mount points into one, resulting in single directory structure that contains underlying files and sub-directories from all sources. Common applications overlay a read/write partition over a read-only partition, such as with LiveCDs and IoT devices with limited flash memory write cycles.

- The main mechanics of OverlayFS relate to the merging of directory access when both filesystems present a directory for the same name. Otherwise, OverlayFS presents the object, if any, yielded by one or the other, with the "upper" filesystem taking precedence. Unlike some other overlay filesystems, the directory subtrees being merged by OverlayFS do not necessarily have to be from distinct filesystems.[8]

- OverlayFS supports whiteouts and opaque directories in the upper filesystem to allow file and directory deletion.[8]

- OverlayFS does not support renaming files without performing a full copy-up of the file; however, renaming directories in an upper filesystem has limited support.

- OverlayFS does not support merging changes from an upper filesystem to a lower filesystem.


https://askubuntu.com/questions/109413/how-do-i-use-overlayfs

```
# Create the filesystems.
dd if=/dev/zero of=lower.ext4 bs=1024 count=102400
mkfs -t ext4 lower.ext4
cp lower.ext4 upper.ext4
mkdir lower upper overlay
sudo mount lower.ext4 lower
sudo mount upper.ext4 upper
sudo chown "$USER:$USER" lower upper
printf lower-content > lower/lower-file
# Upper and work must be on the same filesystem.
mkdir upper/upper upper/work
printf upper-content > upper/upper/upper-file
# Work must be empty. E.g. this would be bad:
#printf work-content > upper/work/work-file
# Make the lower readonly to show that that is possible:
# writes actually end up on the upper filesystem.
sudo mount -o remount,ro lower.ext4 lower

# Create the overlay mount.
sudo mount \
  -t overlay \
  -o lowerdir=lower,upperdir=upper/upper,workdir=upper/work \
  none \
  overlay \
;

# Interact with the mount.
printf 'overlay-content' > overlay/overlay-file
ls lower upper/upper upper/work overlay

# Write to underlying directories while mounted
# gives undefined behaviour.
#printf lower-content-2 > lower/lower-file-2
#printf upper-content-2 > upper/upper-file-2

# Unmount the overlay and observe state.
sudo umount overlay
ls lower upper/upper upper/work

# Cleanup.
sudo umount upper lower
```
