# 29-oct-2018

### 3 - py_compile

- Python is both a interpreted and compiled language

If you have a python program called server123.py, then

```python
import py_compile
py_compile.compile('server123.py')
```

```bash
$ python ./server123.pyc
```

- for python3 the pyc file will be in pycache folder
- it will give magic number error if you run a different version interpreter over a different python version pyc.

This also works

```bash
python -c "import server123"
python -m server123
```
There is also a compileall, i.e.
```python
python -m compileall .
```

### 2 - New style and old style classes

```python
# old-style class, python2
class A:
    pass
class B(A):
    pass
a = A()
b = B()
print(type(A), type(B))
print(type(a), type(b))
```
After having executed the Python code above we received the following:

```python
(<type 'classobj'>, <type 'classobj'>)
(<type 'instance'>, <type 'instance'>)
```

```python
# new-style class python 3
class A(object):
    pass
class B(A):
    pass
a = A()
b = B()
print(type(A), type(B))
print(type(a), type(b))
```

The Python code above returned the following:

```python
(<type 'type'>, <type 'type'>)
(<class '__main__.A'>, <class '__main__.B'>)
```

### 1 - What I learned till now ( revision )

- CPython source code has lot of structures defined. There is a structure for interpreter state, Thread state, Python Object, Python String Object, Instruction, Code Object, Frame Object, Types and so on.
- The GIL can be held by only one thread at a time. This makes Python only capable of doing one CPU intensive task at a time. So even if you have multiple threads on multicore CPU, only one thread will be executing at a moment. 
- Generators are good way to save memory and makes code simpler.
- CPython by default don't know the full list of objects which are allocated. If we want to enable that, we need to compile it with a tracing flag. That adds few next/prev kind of pointers in PyObject which makes all allocations become part of a list.
- String interning is a optimization done at compile time which is cause of many "is" operator unintiutive outcomes.
- Ctypes module can be used to access C struct fields of Python objects in a program. It can also be used to call functions from shared libraries like libc
- Python is a battery included language. It has a very rich set of prepackage libraries sufficient for normal tasks. 
- The major code of interpreter is present in `eval.c` in CPython with a giant switch-case kind of construct( goto/label).
- Py_INCREF and Py_DECREF are functions which are used to increase refcnt or decrease it in CPython. Other implementation don't need to follow this and can have their own mechanisms to deal with this.
- CPython has Arena memory allocator which works differently than simply mallocing stuff.
- Due to the implementation of structs in C, any Py* object can be casted to PyObject and standard fields like refcnt, type etc. can be read from that. 
- With new style classes in CPython, it's not necessary to subclass from object in Python code. But it should be done for previous versions where new style classes were not supported.

