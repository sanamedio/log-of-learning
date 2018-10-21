# 22-oct-2018

### 7 - Compile code and getting code object

```python
>> compile('test.py', 'test.py', 'exec')
```
This returns a code object for test.py module. Also you can use dis module from command line ```python -m dis test.py```

### 6 - Ternary operation

```python
False is False is False #True, which seems unintiutive because (False is False) is False will evaluate to False
1 < 2 < 3 #True
```
bytecodes:
```python
>>> def test():
...     False is False is False
... 
>>> dis.dis(test)
  2           0 LOAD_GLOBAL              0 (False)
              3 LOAD_GLOBAL              0 (False)
              6 DUP_TOP             
              7 ROT_THREE           
              8 COMPARE_OP               8 (is)
             11 JUMP_IF_FALSE_OR_POP    23
             14 LOAD_GLOBAL              0 (False)
             17 COMPARE_OP               8 (is)
             20 JUMP_FORWARD             2 (to 25)
        >>   23 ROT_TWO             
             24 POP_TOP             
        >>   25 POP_TOP             
             26 LOAD_CONST               0 (None)
             29 RETURN_VALUE        
>>> def test2():
...     1 < 2 < 3 
... 
>>> dis.dis(test2)
  2           0 LOAD_CONST               1 (1)
              3 LOAD_CONST               2 (2)
              6 DUP_TOP             
              7 ROT_THREE           
              8 COMPARE_OP               0 (<)
             11 JUMP_IF_FALSE_OR_POP    23
             14 LOAD_CONST               3 (3)
             17 COMPARE_OP               0 (<)
             20 JUMP_FORWARD             2 (to 25)
        >>   23 ROT_TWO             
             24 POP_TOP             
        >>   25 POP_TOP             
             26 LOAD_CONST               0 (None)
             29 RETURN_VALUE        
>>> 

```


### 5 - Inspect : tool for observation

```python
import random
import inspect

print( inspect.getsource(random.choice)) #prints source code of choice function

```

### 4 - Bytecode processor: BINARY_MULTIPLY

- This and previous few notes are from this talk : https://www.youtube.com/watch?v=XGF3Qu4dUqk

```C
TARGET(BINARY_MULTIPLY) // MACRO to hide whether it's old switch case or the newer goto jump
  w = POP() // w,v,x act as general purpose registers here
  v = TOP()
  x = PyNumber_Multiply(v,w); // v and w multiplication using Number protocol
  Py_DECREF(v); // why not do it safely? because it's guarenteed at this point that they will be legal
  Py_DECREF(w); // does order of these decrements matter?
  SET_TOP(x); // what if code has some failure at this point? will it revert the process to last stage?
  if ( x != NULL ) DISPATCH(); // earlier there wasn't being done in case of switch case style; but with new one i.e. labels as values version it does some work. In case the multiplication failed, x will be NULL and then this will break and exception needs to be handled. Also, None is not NULL. None is actually a legal value and is considered a positive case.
  break;
```

PyNumber_Multiply:
```c
PyObject * 
PyNumber_Multiply(PyObject *v, PyObject *w)
{
	PyObject *result = binary_op1(v,w,NB_SLOT(nb_multiply)); // binary_op1 is local function and tries to do multiplication
	if ( result == Py_NotImplemented){// then we try to see if one of them is a sequence and other is a number and do operation of multiplication according to that
		PySequenceMethods *mv = v->ob_type->tp_as_sequence;
		PySequenceMethods *mw = v->ob_type->tp_as_sequence;
		Py_DECREF(result);
		if( mv && mv->sq_repeat){
			return sequence_repeat(mv->sq_repeat,v,w);
		}
		else if( mw && mw->sq_repeat){
			return sequence_repeat(mw->sq_repeat, w,v);
		}
		result = binop_type_error(v,w,"*"); // if all above doesn't happen, creates new type error object and raises it internally

	}
	return result;
}
```

### 3 - .pyc files

- It uses marshal module 
  - Present in ```Include/marshal.h``` and ```Python/marshal.c```
- Starts with a magic tag documented in ```Python/import.c``` , and last modification time ```st_mtime of .py``` and python code objects serialized
- While loading modules which are pure python and haven't already been preloaded by the interpreter, first pycache directory is checked for corresponding .pyc file.

### 2 - Modules written in C (CPython source)

- All C Native modules are present in ```Modules/*module.c``` and generally end with ```module.c```
- These modules get initialized inside Py_Initialize which sits in ```Python/pythonrun.c```


### 1 - Python pre-loaded modules by interpreter

- kind of module cache. When you import modules, it basically checks whether sys.modules already have that or not.
```python
import sys
print sorted(sys.modules.keys())
```



