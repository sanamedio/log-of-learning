# 23-oct-2018

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
