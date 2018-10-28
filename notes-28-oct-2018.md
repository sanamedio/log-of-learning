# 28-oct-2018

### 9 - Compiler data structure

```C
struct compiler {
	PyObject *c_filename;
	struct symtable *c_st;
	PyFutureFeatures *c_future; /* pointer to module's __future__ */
	PyCompilerFlags *c_flags;
	
	int c_optimize;
	int c_interactive;
	int c_nestlevel;
	
	struct compiler_unit *u /*compiler state for current block*/
	PyObject *c_stack; /*Python list holding compiler_unit ptrs*/
	PyArena *c_arena; /*pointer to memory allocation area*/
};
```

### 8 - Symbol table ( CPython source)

- The symbol table requires two passes to determine the scope of each name. The first pass collects raw facts from the AST via the symtable_visit_* functions while the second pass analyzes these facts during a pass over the PySTEntryObjects created during pass
- When a function is entered during the second pass, the parent passes the set of all name bindings visible to its children. These bindings are used to determine if non-local variables are free or implicit globals. Names which are explicitly declared nonlocal must exist in this set of visible names - if they do not, a syntax error is raised. After doing the local analysis, it analyzes each of its child blocks using an updated set of name bindings.
- There are two kind of globals: implicit and explicit. Explicit is what gets declared with global statement. Whereas, An implicit global variable is one for which compiler has found no binding to the enclosing function scope. The implicit global is either a global or a builtin.


### 7 - What happens when we load a module

- When executing a module passed to the interpreter on the command line, a call to the `PyParser_ParseFileObject` function initiates the parsing of the module. This function calls the tokenization function, `PyTokenizer_FromFile` , passing the module file name as argument. The tokenization function breaks up the content of the module into legal python tokens or throws an exception when an illegal value is found.
- The `PyTokenizer_FromFile` function in the `Parser/parsetok.c` module scans the python source file from left to right and top to bottom tokenizing the content of the file.
- The python parser is an LL(1) parser that is based on the description of such parsers as laid out the Dragon book. The Grammar/Grammar module contains the Extended Backus-Naur Form (EBNF) grammar specification for the Python language.
- We can use the parser module to see the tokens:

```python
code_str = """def hello_world(): return 'hello world' """
import parser
from pprint import pprint
st = parser.suite(code_str)
pprint(parser.st2list(st))
```

### 6 - Thread State

- The Thread State data struct contains all the information needed by thread to execute some python code object.
- A portion of Thread State data struct:
```C
typedef struct _ts {

        struct _ts *prev;
        struct -ts *next;
        PyInterpreterState *interp;

        struct _frame *frame;
        int recursion_depth;
        char overflowed;

        char recursion_critical;
        int tracing;
        int use_tracing;

        Py_tracefunc c_profilefunc;
        Py_tracefunc c_tracefunc;
        PyObject *c_profileobj;
        PyObject *c_traceobj;

        PyObject *curexc_type;
        PyObject *curexc_value;
        PyObject *curexc_traceback;


        PyObject *exc_type;
        PyObject *exc_value;
        PyObject *exc_traceback;

        PyObject *dict; //Stores per thread state
        int gilstate_counter;

        ...
} PyThreadState;
```
- Just like `Py_Initialize` was called for setting up stuff, once the program gets executed, `Py_FinalizeEx` is called. This clean-up process involves waiting for threads to exit, calling any exit hooks and also freeing up any memory allocated by the interpreter that is still in use.

### 5 - Py_Initialize  and Interpreter startup

- As part of the initialization process, `Py_Initialize` from `pylifecycle.c` is called; this handles the initialization of the interpreter and thread state data structures - two very important data structures.

- Interpreter state data structure
```c
typedef struct _is {

        struct _is *next;
        struct _ts *tstate_head;

        PyObject *modules;
        PyObject *tstate_head;
        PyObject *sysdict;
        PyObject *builtins;
        PyObject *importlib;


        PyObject *codec_search_path;
        PyObject *codec_search_cache;
        PyObject *codec_error_registry;

        int codecs_initialized;
        int fscodec_initialized;

        PyObject *builtins_copy;
} PyInterpreterState;
```
- The `*next` field is a reference to another interpreter instance as multiple python interpreters
can exist within the same process.
- The `*tstate_head` field points to the main thread of execution - in the event that the python program is multithreaded then the interpreter is shared by all threads created by the program
- The `codec*` related fields hold information that help with the location and loading of encodings. These are very important for decoding bytes.
- The modules , modules_by_index , sysdict , builtins and importlib are self explanatory - they are all defined as instances of PyObject which is the root type for all python objects in the virtual machine world.


### 4 - Objects that behave both as String and File Interface

- https://docs.python.org/2/library/mmap.html

### 3 - Wrapping a String in File interface

```python
s = io.StringIO('Hello world')
s.read(4)
s.read()
```

### 2 - Iterating over a tree

```python
class Node:

	def __init__(self, value):
		self._value = value
		self._children = []

	def __repr__(self):
		return 'Node({!r})'.format(self._value)

	def add_child(self,node):
		self._children.append(node)


	def __iter__(self):
		return iter(self._children)

	def depth_first(self):
		yield self
		for c in self:
			yield from c.depth_first()




if __name__ == '__main__':
	root = Node(0)
	child1 = Node(1)
	child2 = Node(2)

	root.add_child(child1)
	root.add_child(child2)

	child1.add_child(Node(3))
	child2.add_child(Node(4))

	for ch in root.depth_first():
		print(ch)
```

### 1 - Deduplication 

```python
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)
            

#for unhashable type, a key can be provided as lamda during function call in the following


def dedupe(items , key= None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)
            
a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]

print( list(dedupe(a,key=lambda t: t['x'])))
```

