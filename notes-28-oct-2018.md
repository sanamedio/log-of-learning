# 28-oct-2018


### 5 - Py_Initialize

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

