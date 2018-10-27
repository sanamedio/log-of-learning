# 28-oct-2018

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

