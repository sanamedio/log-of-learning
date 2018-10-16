# 17-oct-2018

### 4 - Frozen set

- Frozen sets : These represent an immutable set. They are created by the built-in frozenset() constructor. As a frozenset is immutable and hashable, it can be used again as an element of another set, or as a dictionary key.


### 3 - datamodel

- https://docs.python.org/3/reference/datamodel.html
- Objects are never explicitly destroyed; however, when they become unreachable they may be garbage-collected. 
- An implementation is allowed to postpone garbage collection or omit it altogether — it is a matter of implementation quality how garbage collection is implemented, as long as no objects are collected that are still reachable.
- CPython implementation detail: CPython currently uses a reference-counting scheme with (optional) delayed detection of cyclically linked garbage, which collects most objects as soon as they become unreachable, but is not guaranteed to collect garbage containing circular references.
- use of the implementation’s tracing or debugging facilities may keep objects alive that would normally be collectable. Also note that catching an exception with a ‘try…except’ statement may keep objects alive.

### 2 - id() and is

- CPython implementation detail: id() is the address of the object in memory.
- The ‘is’ operator compares the identity of two objects; the id() function returns an integer representing its identity.

### 1 - everything on this link

- https://sebastianraschka.com/Articles/2014_deep_python.html
