# 23-oct-2018

### 11 - tuple syntax

```python
t = ('one', 'two')
for i in t:
    print(i)

t = ('one') # this is string
for i in t:
    print(i)

t = () # this is a tuple type Tuple()
print(t)
```

### 10 - zen of python source code

- https://github.com/python/cpython/blob/master/Lib/this.py   
```python
import this
```

### 9 - memory_profiler

- very useful https://github.com/fabianp/memory_profiler

```python
@profile
def my_func():
    a = [1] * (10 ** 6)
    b = [2] * (2 * 10 ** 7)
    del b
    return a

if __name__ == '__main__':
    my_func()
```

```bash
$ python -m memory_profiler test.py
Filename: test.py

Line #    Mem usage    Increment   Line Contents
================================================
     1   26.605 MiB   26.605 MiB   @profile
     2                             def my_func():
     3   34.062 MiB    7.457 MiB   	a = [1] * ( 10**6)
     4  186.688 MiB  152.625 MiB   	b = [2] * ( 2* 10**7)
     5   34.238 MiB -152.449 MiB   	del b
     6   34.238 MiB    0.000 MiB   	return a
```

### 8 - return statements

```python
def some_func():
    try:
        return 'from_try'
    finally:
        return 'from_finally'
        
>>> some_func()
from_finally
```
- When a return, break or continue statement is executed in the try suite of a "try…finally" statement, the finally clause is also executed ‘on the way out.
- The last executed return gets to say what value to return

### 7 - Dictionary hash keys

```python
#wtfpython repo example
some_dict = {}
some_dict[5.5] = "Ruby"
some_dict[5.0] = "JavaScript"
some_dict[5] = "Python"

>>> some_dict[5.5]
"Ruby"
>>> some_dict[5.0]
"Python"
>>> some_dict[5]
"Python"
>>> 5 == 5.0 
True
>>> hash(5) == hash(5.0)
True
```
- Very good explanation on the rationale [SO link](https://stackoverflow.com/questions/32209155/why-can-a-floating-point-dictionary-key-overwrite-an-integer-key-with-the-same-v/32211042#32211042) about making 1.0 equal 1 causing theire hash values to also be same.


### 6 - Peephole optimization and interpreter optimization

- https://en.wikipedia.org/wiki/Peephole_optimization
- Constant folding is a technique for peephole optimization in Python. This means the expression 'a'\*20 is replaced by 'aaaaaaaaaaaaaaaaaaaa' during compilation to reduce few clock cycles during runtime. Constant folding only occurs for strings having length less than 20. (Why? Imagine the size of .pyc file generated as a result of the expression 'a'*10\**10). 
- Peephole optimization code : https://github.com/python/cpython/blob/3.6/Python/peephole.c#L288
- When we do assignments in the same line in interpreter, it has better visibility sort of and can save memory by assigning to the same object
```python
>>> a = "wtf"
>>> b = "wtf"
>>> a is b
True

>>> a = "wtf!"
>>> b = "wtf!"
>>> a is b
False

>>> a, b = "wtf!", "wtf!"
>>> a is b
True

>>> 'a' * 20 is 'aaaaaaaaaaaaaaaaaaaa'
True
>>> 'a' * 21 is 'aaaaaaaaaaaaaaaaaaaaa'
False
```
- (from wtfpython repo) In the snippets above, strings are implicitly interned. The decision of when to implicitly intern a string is implementation dependent. There are some facts that can be used to guess if a string will be interned or not:
  - All length 0 and length 1 strings are interned.
  - Strings are interned at compile time ('wtf' will be interned but ''.join(\['w', 't', 'f'] will not be interned)
  - Strings that are not composed of ASCII letters, digits or underscores, are not interned. This explains why 'wtf!' was not interned due to !. Cpython implementation of this rule can be found at this line: https://github.com/python/cpython/blob/3.6/Objects/codeobject.c#L19



### 5 - Zero-argument and variable-argument lambdas

Lambda functions are usually used for a quick transformation of one value into another, but they can also be used to wrap a value in a function:
```python
>>> f = lambda: 'foo'
>>> f()
'foo'
```
```python
#They can also accept the usual *args and **kwargs syntax:
>>> g = lambda *args, **kwargs: args[0], kwargs['thing']
>>> g(1, 2, 3, thing='stuff')
(1, 'stuff')
```


### 4 - Interpreter inside interpreter

```python
>>> shared_var = "Set in main console"
>>> import code
>>> ic = code.InteractiveConsole({ 'shared_var': shared_var })
>>> try:
...     ic.interact("My custom console banner!")
... except SystemExit, e:
...     print "Got SystemExit!"
... 
My custom console banner!
>>> shared_var
'Set in main console'
>>> shared_var = "Set in sub-console"
>>> import sys
>>> sys.exit()
Got SystemExit!
>>> shared_var
'Set in main console'
```

### 3 - Dynamically creating type and object from that

```python
>>> NewType = type("NewType", (object,), {"x": "hello"})
>>> n = NewType()
>>> n.x
"hello"
```
which is exactly the same as
```python
>>> class NewType(object):
>>>     x = "hello"
>>> n = NewType()
>>> n.x
"hello"
```

### 2 - code object and func object

- related files
  - ```Include/code.h```
  - ```Include/funcobject.h```
  - ```Objects/codeobject.c```
  - ```Objects/funcobject.c```
- defining a function, causes a corresponding func object to be created
- Each func object contains func_globals which points to the same global table
- If python project has 10 different files, there would be 10 different globals.That is why we keep pointer to global for each function. What it means is there is real "global" global which everyone can access but might be different globals for different functions.
- func object has a fiend func_code field which contains the code object which contains the bytecode
- The same code object can get executed with different global pointer and give different results
- PyCode_New present in codeobject.c is constructor for a PyCodeObject


### 1 - PyStringObject

- related files
  - ```Objects/abstract.c``` 
  - ```Include/stringobject.h``` PyStringObject
  - ```Objects/stringobject.c```

- ```PyStringObject``` represents a string of characters, defined and documented in ```pystringobject.h```
```C
/*
 * The PyStringObject represents a character string. An extra zero byte is reserved at the end to ensure it's 
 * zero terminated, but a size is added so that string with null bytes can be properly represented. This is a 
 * immutable object type.
 *
 * There are functions to create string objects , to test an object for string-ness ( A general theme in whole
 * design of python is that behaviour identifies things and anything that sounds like a duck, walks like a duck
 * is a DUCK. Probably this is duck-typing. verify! ) and to get the string value. The latter function returns 
 * null if the string is not of proper type. There is a variant which assumes null terminated string and one 
 * which takes a size. None of the function should be applied to Nil.
 */

/*
 * Caching the ob_shash  saves recalculation of string's hash value. Interning strings (ob_sstate) ensure that 
 * only one string with a given value exists, so equality tests can be pointer comparision. This is generally 
 * restricted to strings that look like python identifiers( WHY WHY WHY ?) , although the intern() builtin 
 * can be used to force interning of any string. Together these have contributed to 20% speedup of Python interpreter.
 */


typedef struct {
  PyObject_VAR_HEAD // ref_cnt , size, type
  long ob_shash;
  int ob_sstate;
  char ob_sval[1];
  /*  ob_sval contains space for ob_size+1 elements
   *  ob_sval[ob_size] = 0
   *  ob_shash is the hash of the string or -1 if not computed
   *  ob_sstate != 0 if the string object is in stringobject.c's 'interned' dictionary: 
   *  in this case the two references from 'interned' to this object are not counted in ob_refcnt
   */
 } PyStringObject;
```
- In the above implementation every PyStringObject is of different size, as string is saved in ob_sval ( BUT HOW, this is not pointer) and exists at the end of the object. Memory is allocated according toe the size of the string.

- If we create a PyObject pointer to PyStringObject we will only be able access limited fields

- https://en.wikipedia.org/wiki/String_interning
- pyObject_richCompare and pyStringObject_richCompare
- String interning happens on compile time
