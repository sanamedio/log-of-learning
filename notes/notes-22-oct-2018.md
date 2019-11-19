# 22-oct-2018

### 12 - Python Object Model

- Every piece of data is a object
- The python object protocol
  - ```Include/object.h``` (Contains good documentation about objects)
  - ```Objects/object.c```
- When we store a number like 456, it gets wrapped in PyObject, and a PyInteger and then it is stored.
- Code for dunder add and other stuff can be found in ```objects/intobject.c```
```C
static PyObject *
int_add(PyIntObject *v, PyIntObject *w)
{
        register long a,b,x;
        CONVERT_TO_LONG(v, a);
        CONVERT_TO_LONG(w, b);
        /* casts in the line below avoid undefined behaviour on overflow */
        x = (long)((unsigned long)a + b );
        if ((x^a) >= 0 || (x^b) >= 0)
                return PyInt_FromLong(x);
        return PyLong_Type.tp_as_number->nb_add((PyObject *)v, (PyObject *)w);
}
```

- C don't have inheritence, so struct subtyping is used. What this means is PyObject , PyIntObject and PyTypeObject will all have similar structure with more specific fields getting added to those types where they are needed. In that way we can refer to all of them using PyObject pointer and the fields which are present can be accessed in uniform way.
- The building of these different type of objects structures/types is done by using MACROS

- Reference counting is Cpython thing, and is not a part of general python spec( Verify this! )
- tp_str is like toString() of Java i.e. basically every struct which follows the protocol have tp_str implemented and before using this in code we check whether this is implemented or not based on type and all. ( Read object.c in CPython source tree)

- [ ] TODO https://docs.python.org/3/reference/datamodel.html
- [ ] TODO (All bytecodes can be seen here : https://docs.python.org/3/library/dis.html)

### 11 - Frame

- Frame objects are linked to each other in memory. For example: global_frame -> foo -> bar , where foo and bar are functions and foo is calling bar internally. It happens using ```struct _frame *f_back``` pointer in ```pyFrameObject```(```_frame typedef```). So a frame object contains pointer to last frame object.
- Each frame has it's own private value stack ```f_valuestack```
- ```PyEval_EvalFrameEx``` function takes a ```PyFrameObject```, and executes it and gives back a ```PyObject``` as result.
- Functions, Frames and Code objects
  - Code Object is a primitive thing; contains bytecodes and semantic information like constants, variables etc.
  - A Function has a Code object and a environment, but function is a static representation
  - A Frame also has a code object and an environment but Frame is a runtime representation
  - A Recursive function for example, may have only one function object reference but hundreds of frames.
- When a new frame is created, the argument parameters are copied. (ceval.c L:4000)

### 10 - Interpreter and Opcodes

- ```/Include/opcode.h``` has all the opcodes defined.
- CPython runtime’s main interpreter loop locates in ```/Python/ceval.c```.

### 9 - PyFrameObject
 
- Frames are represented by PyFrameObject present in ```include/frameobject.h```
- [ ] TODO understand the fields

```c
typedef struct _frame {
    PyObject_VAR_HEAD
    struct _frame *f_back;      /* previous frame, or NULL */
    PyCodeObject *f_code;       /* code segment */
    PyObject *f_builtins;       /* builtin symbol table (PyDictObject) */
    PyObject *f_globals;        /* global symbol table (PyDictObject) */
    PyObject *f_locals;         /* local symbol table (any mapping) */
    PyObject **f_valuestack;    /* points after the last local */
    /* Next free slot in f_valuestack.  Frame creation sets to f_valuestack.
       Frame evaluation usually NULLs it, but a frame that yields sets it
       to the current stack top. */
    PyObject **f_stacktop;
    PyObject *f_trace;          /* Trace function */
    char f_trace_lines;         /* Emit per-line trace events? */
    char f_trace_opcodes;       /* Emit per-opcode trace events? */

    /* Borrowed reference to a generator, or NULL */
    PyObject *f_gen;

    int f_lasti;                /* Last instruction if called */
    /* Call PyFrame_GetLineNumber() instead of reading this field
       directly.  As of 2.3 f_lineno is only valid when tracing is
       active (i.e. when f_trace is set).  At other times we use
       PyCode_Addr2Line to calculate the line from the current
       bytecode index. */
    int f_lineno;               /* Current line number */
    int f_iblock;               /* index in f_blockstack */
    char f_executing;           /* whether the frame is still executing */
    PyTryBlock f_blockstack[CO_MAXBLOCKS]; /* for try and loop blocks */
    PyObject *f_localsplus[1];  /* locals+stack, dynamically sized */
} PyFrameObject;
```

### 8 - PyCodeObject 

- When we use compile and create code object; this is what is getting created
- When we define functions, they get saved as code objects
- PyCodeObject struct is defined in ```include/code.h```
- [ ] TODO study this structure and understand how these fields are used?
```c
/* Bytecode object */
typedef struct {
    PyObject_HEAD
    int co_argcount;            /* #arguments, except *args */
    int co_kwonlyargcount;      /* #keyword only arguments */
    int co_nlocals;             /* #local variables */
    int co_stacksize;           /* #entries needed for evaluation stack */
    int co_flags;               /* CO_..., see below */
    int co_firstlineno;         /* first source line number */
    PyObject *co_code;          /* instruction opcodes */
    PyObject *co_consts;        /* list (constants used) */
    PyObject *co_names;         /* list of strings (names used) */
    PyObject *co_varnames;      /* tuple of strings (local variable names) */
    PyObject *co_freevars;      /* tuple of strings (free variable names) */
    PyObject *co_cellvars;      /* tuple of strings (cell variable names) */
    /* The rest aren't used in either hash or comparisons, except for co_name,
       used in both. This is done to preserve the name and line number
       for tracebacks and debuggers; otherwise, constant de-duplication
       would collapse identical functions/lambdas defined on different lines.
    */
    Py_ssize_t *co_cell2arg;    /* Maps cell vars which are arguments. */
    PyObject *co_filename;      /* unicode (where it was loaded from) */
    PyObject *co_name;          /* unicode (name, for reference) */
    PyObject *co_lnotab;        /* string (encoding addr<->lineno mapping) See
                                   Objects/lnotab_notes.txt for details. */
    void *co_zombieframe;       /* for optimization only (see frameobject.c) */
    PyObject *co_weakreflist;   /* to support weakrefs to code objects */
    /* Scratch space for extra data relating to the code object.
       Type is a void* to keep the format private in codeobject.c to force
       people to go through the proper APIs. */
    void *co_extra;
} PyCodeObject;
```

### 7 - Compile code and getting code object

```python
>>> compile(open('test.py').read(), 'test.py', 'exec')
```
This returns a code object for test.py module. Also you can use dis module from command line ```python -m dis test.py```. Also, it generally compiles any code to bytecode which is correct till that stage. For example, a file containing ```test.py``` string will also give out a valid bytecode assuming test as a object and .py as attribute. You can check it with:
```python
>>> compile('test.py', 'test.py', 'exec')
```
- Reference : http://www.pgbovine.net/cpython-internals.htm
- Visualize execution : http://www.pythontutor.com

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
- There is cinspect also which shows source code for C modules; 

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



