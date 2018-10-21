# 21-oct-2018

### 15 - PyEval_EvalFrameEx

```bash
(gdb) b PyEval_EvalFrameEx
(gdb) c
```
- Sits in Python/ceval.c
- It's a stack based virtual machine


### 14 - PyObject_memory small block allocator

- There are two memory allocators. One uses C's default allocator and this is the other family of memory allocator
- This is enabled when we Compile python with WITH_PYMALLOC ```#define WITH_PYMALLOC```
- Sits in ```Include/objimpl.h``` anad ```Objects/obmalloc.c```
- ```PyObject_Malloc() custom small block allocator for python```
```C
#define PyObject_MALLOC
    PyObject_Malloc // by default maps to PyObject_MALLOC
    PYMALLOC_DEBUG -> _PyObject_DebugMalloc // In case of debug flag, it calls this
    ! WITH_PYMALLOC -> PyMem_MALLOC // falls back to PyMem_MALLOC
```

### 13 - Reference Counting

- All objects are ref counted
- Five MACROS
    - ```Py_INCREF(o)``` : Increase ref count
    - ```Py_DECREF(o)``` : Decrease ref count, if it's zero we deallocate
    - ```Py_XINCREF(o)```, ```Py_XINCREF(o)``` : are safer versions, have nullcheck before calling INCREF and DECREF
    - ```Py_CLEAR(o)``` : Makes copy of pointer first and then calls DECREF, used for things which are member of structure

### 12 - Protocols 

- Sits in ```Include/abstract.h``` and ```Objects/abstract.c```
- A protocol is another name for Abstract Base Class
- Five protocols
    - Object: everything needs to inherit from object
    - Buffer ```tp_as_buffer```
    - Number ```tp_as_number``` : things like multiplication, division , mod and other behaviour of numbers etc.
    - Mapping ```tp_as_mapping```: getitem, setitem etc.
    - Sequence ```tp_as_sequence```
        - "fast" sequence, can be used in C for performance
        - "fast" sequence is aware of internals so it does better than generic sequence interface calls, for objects which expose sequence protocol
- Sounds like Python and C are very closely related the way this implementation is done. We created memory structures in C and Python is kind of a abstraction over C to manipulate them with easier interface.


### 11 - PyTypeObject CPython

- Def. can be found in object.h as \_typeobject
- Contains lots of fields and function pointers and pointers to struct which again contain function pointers
- https://ref.readthedocs.io/en/latest/understanding_python/type_system/PyTypeObject.html
- https://github.com/python/cpython/blob/e42b705188271da108de42b55d9344642170aa2b/Doc/c-api/typeobj.rst#id600

### 10 - PyObject CPython
```bash
(gdb) break _PyObject_New
(gdb) c
(gdb) clear _PyObject_New //because this is very frequenct call 
```
- Everything in python is PyObject, very fundamental to Python
- sets, list, types, frames , etc. all are PyObject
- PyObject sits in ```Include/object.h``` and ```Objects/object.c```

```c
typedef struct _object {
    _PyObject_HEAD_EXTRA // it's a preprocessor macro, normally not used, there is no semicolor 
    // in case want to trace all objects, enable trace while compiling and it will add two fields here, prev pointer and next pointer
    // Normally interpreter does not know the objects, and where they are in heap 
    Py_ssize_t ob_refcnt; // reference count, big native integer 
    struct _typeobject *ob_type; // generally we use PyTypeObject
    // in legal objects, ob_type is never null
} PyObject;
```

### 9 - Py_Main CPython

```bash
(gdb) break Py_Main
(gdb) c
```

- Lives in ```Modules/main.c```
- Both main and Py_Main sits in modules ( unintiutive)
- Py_Main does
    - gets command line options
    - gets env variables
    - sets input and output stdio,stderr
    - Py_Initialize : initialize moduels and stuff
    - run script / -m module / -c command
    



### 8 - Memory Management Cpython

- Two "families" of Memory Management functionss : PyMem_ and PyObject_memory

- PyMem_
    - PyMem_ functions are present in ```Include/pymem.h``` and ```Objects/object.c``` ( Why not in module? )
    - PyMem_Malloc() -> calls malloc()
    - ```#define PyMem_MALLOC -> calls malloc()```
    - ```#define PYMALLOC_DEBUG -> _PyMem_DebugMalloc()```
        - kind of mini valgrind
        - turn this off if using real valgrind, else both will fight


- PyObject_memory

- For both of them there are malloc, realloc, and free
- suggested to not call malloc directly in C!

### 7 - main Cpython

```bash
$ gdb python3
$ break main
$ run the_program.py
```

- Main lives in ```Modules/python.c```
- Makes copes of argv ( WHy? )
- sets locale ( How does locale impact?)
- calls Py_Main, this is same for all platforms

### 6 - CPython Directory Structure
```
Folder - Use

Doc - Documentation 
Grammar - Parser grammar for python
Mac PCbuild - Platform
Miscellany -  Misc Tools

Important for core devs:

Include - public include files, and gets installed with Python. There are other include files not present in this folder but are used internally
Lib - Python portion of standard library
Modules - C portion of standard library
Objects - Implementation of objects like sets, tuples, lists , some internal objects etc
Python - importer, parser , majorly Python, bookeeping etc

There can be other stuff also in these folder here and there.
```

### 5 - Python is dynamically typed! lower level details

```python
def mod(a,b):
    result = a % b
    return result

print mod(13,3) # 1
print mod("%s%s", ( 'Hello' , 'World' ) ) # HelloWorld
```
- Compiler will produce the same bytecode in both cases. Can check with dis.dis
- Interpreter will need to do the corrrect thing
- To improve performance, type information can help ( coming in future python )
- https://www.youtube.com/watch?v=HVUTjQzESeo

```C
//binary modulo in ceval cpython, the code is from a old pycon talk so might not map exactly to cpython
// BINARY_MODULO is for instance a compiled bytecode and now interpreter has to take action on the stack machine so that a correct outcome is calculated
// one of the case of a giant switch case or goto whatever
case BINARY_MODULO:
        w = POP();// two arguments are needed to do a modulo. Both are avaialble on the stack. Pops first value
        v = TOP();// doesn't pop, but just takes the value
        if( PyString_CheckExact(v)) // if it is pystring, apply pyformat i.e. print format, but it's just a optimization;
                x = PyString_Format(v,w);
        else
                x = PyNumber_Remainder(v,w); // all other cases even custom ones are handled here

        Py_DECREF(v);// now since v is not needed anymore; decrease reference for garbage collection
        Py_DECREF(w);// same for w , but are these PyObjects? probably yes
        SET_TOP(x); // put the answer on the top of the stack overwriting
        if ( x != NULL) continue; // if top of stack is not null ; then do a continue, but what will continue do? this doesn't seem to be doing anything significant before the break
        break;
```               

```python
class Surprising(object);
        def __mod__(self, other):
                print "surprise!"


s = Surprising()
t = Surprising()
s % t # Surprise!
```

### 4 - call stack and data stack

- Each level of your code, module , main , function , corresponds to one frame in call stack
- Each frame in call stack has it's own data stack
- In cpython souce code, ceval.c contains opcode to operation mapping, i.e. if this instruction, do this on the stack. This is probably not same in python3 and became a goto or something

### 3 - python bytecode 

```python
def mod(a,b):
    ans = a%b
    return ans

print mod.func_code.co_code

print [ord(b) for b in mod.func_code.co_code] # observe that all are between 0 - 256

# use dis for getting proper byte code names
import dis
dis.dis(mod) # prints bytecode information but not return it
```

### 2 - Python program steps

- Lexing
- Parsing
- Compilation
- Interpreting, Python interpreter is a stack based virtual machine which excecutes bytecode

### 1 - asyncio

- asyncio is a library to write concurrent code using the async/await syntax.
- Event loops , Tasks and Coroutines together makes it simpler to achieve cooperative concurrency in python. They aren't same as multiprocessing
- An event loop basically waits for something to happen and then acts on the event.
- Event loop schedules tasks
- Coroutines (wrapped under tasks) are things which can be resumed and suspended
- The async and await keywords were added in Python 3.5 to define a native coroutine and make them a distinct type when compared with a generator based coroutine
- Future is an awaitable object. Coroutines can await on Future objects until they either have a result or an exception set, or until they are cancelled.
- Generators and coroutines have similarity, i.e. both are things that can be suspended and resumed.
- [ ] TODO Why other languages don't have such construct or is this because of GIL that we don't talk about multiple threads here? How does this compare to something like nodejs?
- [ ] Is asyncio fundamental construct? How much does is take this kind of Task scheduler?
- [ ] TODO READ THIS https://snarky.ca/how-the-heck-does-async-await-work-in-python-3-5/

Simplest example:
```python
import asyncio

async def main():
    print('Hello ...')
    await asyncio.sleep(1)
    print('... World!')

# Python 3.7+
asyncio.run(main())
```

```python
# simple usage, without any benefit
import asyncio

# Define a coroutine that takes in a future
async def myCoroutine():
    print("My Coroutine")

# Spin up a quick and simple event loop 
# and run until completed
loop = asyncio.get_event_loop()
try:
    loop.run_until_complete(myCoroutine())
finally:
    loop.close()
```


```python
import asyncio

async def say(what, when): #async 
    await asyncio.sleep(when) #at this point say function is giving control to or atleast telling that now this should get executed. But the event loop is gonna make that decision when to execute that future
    print(what)

loop = asyncio.get_event_loop()
loop.run_until_complete(say('hello world', 1))
loop.close()
```

```python
#this runs forever 
import asyncio

async def say(what, when):
    await asyncio.sleep(when)
    print(what)


loop = asyncio.get_event_loop()

loop.create_task(say('first hello', 2))
loop.create_task(say('second hello', 1))

loop.run_forever()
loop.close()
```


