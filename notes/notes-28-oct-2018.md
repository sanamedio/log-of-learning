# 28-oct-2018

### 16 - Interpreter and Thread state

- one of the steps during the bootstrapping of the python interpreter is the initialisation of the interpreter state and thread state data structures
- The Py_Initialize function from the pylifecycle.c module is one of the bootstrap functions invoked during the intialisation of the python interpreter. The function handles the set-up of the python runtime as well as the initialisation of the interpreter state and thread state data structures among other things.
- The interpreter state is a very simple data structure that captures the global state that is shared by a set of cooperating threads of execution in a python process.
```C
typedef struct _is {

	struct _is *next;
	struct _ts *tstate_head;

	PyObject *modules;
	PyObject *moduels_by_index;
	PyObject *sysdict;
	PyObject *builtins;
	PyObject *importlib;

	PyObject *codec_search_path;
	PyObject *codec_search_cache;
	PyObject *codec_error_registry;

	int codecs_initialized;
	int fscodec_initialized;


	...


	PyObject *builtins_copy;
	PyObject *import_func;
} PyInterpreterState;
```

- `*next` : There can be multiple interpreter states within a single OS process that is running a python executable. This `*next` field references another interpreter state data structure within the python process if such exist and these form a linked list of interpreter states. 
- Each interpreter state has its own set of variables that will be used by a thread of execution that references that interpreter state. 
- The memory and Global Interpreter Lock available to the process is however shared by all interpreter threads within that process.
- `*tstate_head` : This field references the thread state of the currently executing thread or in the case of a multithreaded program, the thread that currently holds the Global Interpreter Lock (GIL). This is a data structure that maps to an executin operating system thread.


### 15 - tstate : Thread State

- The thread state is just a data structure that encapsulates some state for an executing thread. Each thread state is
assocated with a native OS thread within the running python process.
- a single python process is home to at least one interpreter state and each interpreter state is home to one or more thread states and each of these thread states maps to an operation system thread of execution.
- The recursion_depth as the name suggest specifies how deep the stack frame should get during a recursive call. The overflowed flag is set when the stack overflows - after a stack overflow, the thread allows 50 more calls to enable some clean-up operations. 
- The recursion_critical flag is used to signal to the thread that the code being executed should not overflow. 
- The tracing and `use_tracing` flag are related to functionality for tracing the execution of the thread. 
- The `*curexc_-type , *currexc_value , *curexc_traceback , *exc_type , *exc_value` and `*curexc_traceback` are
fields that are all used in the exception handling process.
- The next and previous fields of a thread state data structure reference threads states created prior to and just after the given thread state. These fields form a doubly linked list of thread states that share a single interpreter state. The interp field references the interpreter state that the thread state belongs to. The frame references the current frame of execution; as the code object that is executed changes, the value referenced by this field also changes.

### 14 - The need for GIL

- Operating System threads and associated python thread states are created either during the initialization of the interpreters or when invoked by the threading module. Even with multiple threads alive within a python process, only one thread can actively carry out CPU bound tasks at any given time.
- Although python threads are operating system threads, a thread cannot execute python bytecode unless such thread holds the GIL . The operating system may schedule a thread that does not holdInterpreter and Thread States the GIL to run but as we will see, all such a thread can actually do is wait to get the GIL and only when it holds the GIL is it able to execute bytecode.
- First of all however, it is important to understand that the GIL is an implementation detail of CPython and not an actual language detail 
- Jython which is python implemented on the Java virtual machine has no notion of a GIL . The primary reason the GIL exist is for ease of implemenation of the CPython virtual machine. 
- It is way easier to implement a single global lock than to implement fine grained locks and the core developers have opted for this. There have however been projects to implement fine grained locks within the python virtual machine but these
have slowed down single threaded programs atimes. 
- A global lock also provides much needed synchronization when performing certain tasks. Take the reference counting mechanism that is used by CPython for memory management, without the concept of a GIL , you may have two thread interleave their increment and decrement of reference count leading to serious issues with memory handling. 
- Another reason for this lock is that some C libraries that CPython calls into are inherently not thread safe so some kind of synchronization is required when using them.

### 13 - How generators are able to capture execution state and update that at will

- Generators have a field that references a frame object and this is filled in when the generator is created. The frame object as we recall has all the state that is required to execute a code object so by having a reference to that execution frame, the generator object can capture all the state required for its execution.


### 12 - PyTypeObject

```C
typedef struct _typeobject {

	PyObject_VAR_HEAD
	const char *tp_name; //for printing in format <module>.<name>
	Py_ssize_t tp_basicsize, tp_itemsize; //for allocation


	destructor tp_dealloc;
	printfunc tp_print;
	getattrfunc tp_getattr;
	setattrfunc tp_setattr;
	PyAsyncMethods *tp_as_async;

	reprfunc tp_repr;

	PyNumberMethods *tp_as_number;
	PySequenceMethods *tp_as_sequence;
	PyMappingMethods *tp_as_mapping;

	hashfunc tp_hash;
	ternaryfunc tp_call;
	reprfunc tp_str;
	getattrofunc tp_getattro;
	setattrofunc tp_setattro;

	PyBufferProcs *tp_as_buffer;
	unsigned long tp_flags;
	const char *tp_doc; // documentation string


	traverseproc tp_traverse;

	inquiry tp_clear;
	richcmpfunc tp_richcompare;
	Py_ssize_t tp_weaklistoffset;


	getiterfunc tp_iter;
	iternextfunc tp_iternext;

	struct PyMethodDef *tp_methods;
	struct PyMemberDef *tp_members;
	struct PyGetSetDef *tp_getset;
	struct _typeobject *tp_base;
	PyObject *tp_dict;
	descrgetfunc tp_descr_get;
	descrsetfunc tp_descr_set;
	Py_ssize_t tp_dictoffset;
	initproc tp_init;
	allocfunc tp_alloc;
	newfunc tp_new;
	freefunc tp_free;
	inquiry tp_is_gc;
	PyObject *tp_bases;
	PyObject *tp_mro;
	PyObject *tp_cache;
	PyObject *tp_subclasses;
	PyObject *tp_weaklist;
	destructor tp_del;

	unsigned int tp_version_tag;
	destructor tp_finalize;

} PyTypeObject;
```


### 11 - basicblock data structure

- A basic block is sequence of instructions which has one entry point and multiple exit points
- A CFG(Control Flow Graph) is basically composed of basicblocks and connections between them
```C
typedef struct basicblock_ {
	/* Each basicblock in a compilation unit is linked via
	 * b_list in the reverse order that the blocks are
	 * allocated. b_list points to the next block, not 
	 * to be confused with b_next, which is next by
	 * control flow 
	 */ 

	 struct basicblock_ *b_list;
	 // number of instructions used
	 int b_iused;
	 // lenght of instruction array ( b_instr )
	 int b_ialloc;
	 // pointer to an array of instructions , initially NULL
	 struct instr *b_instr;
	 /* if b_next!= NULL, it is pointer to next block
	  * reached by normal control flow
	  */
	 struct basicblock_ *b_next;
	 // b_seen is used to perform a DFS of basicblocks
	 unsigned b_seen :1;
	 // b_return is true if a RETURN_VALUE opcode is inserted
	 unsigned b_return :1;
	 // depth of stack upon entry of block, computed by stackdepth()
	 int b_startdepth;
	 // instruction offset for block ,computued by assemble_jupm_offsets()
	
	 int b_offset;
  } basicblock;
```
```C
struct instr {
	unsigned i_jabs : 1;
	unsigned i_jrel : 1;
	unsigned char i_opcode;
	int i_oparg;
	struct basicblock_ *i_target; // target block ( if jump instruction )
	int i_lineno;
};
```



### 10 - Variable flags to specify context of name def. (CPython SC)

```C
#define DEF_GLOBAL 1 // global stmt
#define DEF_LOCAL 2 // assignment in code block
#define DEF_PARAM 2<<1 // formal parameter
#define DEF_NONLOCAL 2<<2 //non local stmt
#define DEF_FREE 2<<4 // name used but not defined in nested block
```

### 9 - Other data structures Cpython

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

```C
struct compiler_unit {
	PySTEntryObject *u_ste;

	PyObject *u_name;
	PyObject *u_qualname; //dot-separated qualified name (lazy)
	int u_scope_type;


	/* the following fields are dicts that maps objects to the index
	 * of them in co_XXX. The index is used as the argument for opcodes
	 * that refer to those collections
 	 */



	PyObject *u_consts; //all constants
	PyObject *u_names;  // all names
	PyObject *u_varnames; // local variables
	PyObject *u_cellvars; // cell variables
	PyObject *u_freevars; // free variables


	PyObject *u_private; // for private name mangling

	Py_ssize_t u_argcount; // number of arguments for block
	Py_ssize_t u_kwonlyargcount; // Number of keyword only arguments for block
	
	// pointer to mosts recently allocated block. by following b_list members, you can reach all early allocated blocks

	basicblock *u_blocks;
	basicblock *u_curblock;

	int u_nfblocks;
	struct fblockinfo u_fblock[CO_MAXBLOCKS];

	int u_firstlineno; // the first lineno of the block
	int u_lineno; // the line no of the current stmt
	int u_col_offset; // the offset of the current stmt
	int u_lineno_set; // boolean to indicate whether instr has been generated with current lineno
};

	

```


```C
struct symtable{
	PyObject *st_filename;
	struct _symtable_entry *st_cur;
	struct _symtable_entry *st_top;
	PyObject *st_blocks;
	
	PyObject *st_stack;
	PyObject *st_global;
	
	int st_nblocks;
	
	PyObject *st_private;
	PyFutureFeatures *st_future;
	
	int recursion_depth;
	int recursion_limit;
	
};
```

```C
typedef struct _symtable_entry {

	PyObject_HEAD
	PyObject *ste_id; // int : key in ste_table->st_blocks
	PyObject *ste_symbols; // variable names to flags mapping
	PyObject *ste_name; // string: name of current block
	PyObject *ste_varnames; //list of function parameters
	PyObject *ste_children; // list of child blocks
	PyObject *ste_directives; // locations of global and non local statements
	_Py_block_ty ste_type; // module , class , function
	int ste_nested; //true if block is nested
	unsigned ste_free : 1 ; // true if block has free variables
	unsigned ste_child_free : 1; //true if a child block has free vars including free refs to globals
	unsigned ste_generator : 1; // true if namespace is a generator
	unsigned ste_varargs : 1; // true if block has varargs
	unsigned ste_varkeywords : 1; // true if block has varkeywords
	
	unsigned ste_needs_class_Closure : 1; // for class scopes, true if a closure over __class__ should be created

	int ste_lineno; // first line of block 
	int ste-col_offset; // offset of first line of block
	int ste_opt_lineno; // lineno of last exec or import 
	int ste_opt_col_offset; // offset of last exec or import 
	int ste_tmpname; // counter for listcomp temp vars
	struct symtable *ste_table;
} PySTEntryObject;
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

