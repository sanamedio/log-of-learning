# 19-oct-2018

### 4 - yield syntax in python3

```python
yield from gen()
```

### 3 - LEGB scoping rules of Python

LEGB Rule.

L, Local — Names assigned in any way within a function (def or lambda), and not declared global in that function.

E, Enclosing-function locals — Name in the local scope of any and all statically enclosing functions (def or lambda), from inner to outer.

G, Global (module) — Names assigned at the top-level of a module file, or by executing a global statement in a def within the file.

B, Built-in (Python) — Names preassigned in the built-in names module : open,range,SyntaxError,...


### 2 - Naming list slices

```python
>>> a = [0, 1, 2, 3, 4, 5]
>>> LASTTHREE = slice(-3, None)
>>> LASTTHREE
slice(-3, None, None)
>>> a[LASTTHREE]
[3, 4, 5]
```

### 1 - get python config information

```bash
$ python -m sysconfig
```
