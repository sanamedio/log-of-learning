# 27-apr-2020

### 1 - adding a new attribute

```python
obj = someobject
obj.a = lambda: None
setattr(obj.a, 'somefield', 'somevalue')
```

```python
>>> class Foo(object):
...     pass
... 
>>> foo = Foo()
>>> foo.a = 3
>>> Foo.b = property(lambda self: self.a + 1)
>>> foo.b
4
```

```python
class Foo():
  pass

def get_x(self):
  return 3

def set_x(self, value):
  print("set x on %s to %d" % (self, value))

setattr(Foo, 'x', property(get_x, set_x))

foo1 = Foo()
foo1.x = 12
print(foo1.x)
```
