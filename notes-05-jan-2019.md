# 05-jan-2019

### 1 - destructors and constructors

- https://eli.thegreenplace.net/2009/06/12/safely-using-destructors-in-python/

```python
class FooType():
    def __init__(self, id):
        self.id = id
        print (self.id, 'born')

    def __del__(self):
        print (self.id, 'died')


ft = FooType(1)
```

```python
class FooType():
    def __init__(self, id):
        self.id = id
        print (self.id, 'born')

    def __del__(self):
        print (self.id, 'died')

def make_foo():
    print ('Making...')
    ft = FooType(1)
    print ('Returning...')
    return ft

print ('Calling...')
ft = make_foo()
print ('End...')
```

```python
class FooType():
    def __init__(self, id, parent):
        self.id = id
        self.parent = parent
        print ('Foo', self.id, 'born')

    def __del__(self):
        print ('Foo', self.id, 'died')


class BarType():
    def __init__(self, id):
        self.id = id
        self.foo = FooType(id, self)
        print ('Bar', self.id, 'born')

    def __del__(self):
        print ('Bar', self.id, 'died')


b = BarType(12)
```

python2 begs to differ!
```python
class FooType(object):
    def __init__(self, id, parent):
        self.id = id
        self.parent = parent
        print 'Foo', self.id, 'born'

    def __del__(self):
        print 'Foo', self.id, 'died'


class BarType(object):
    def __init__(self, id):
        self.id = id
        self.foo = FooType(id, self)
        print 'Bar', self.id, 'born'

    def __del__(self):
        print 'Bar', self.id, 'died'


b = BarType(12)
```

weakref solves problem in python2
```
import weakref

class FooType(object):
    def __init__(self, id, parent):
        self.id = id
        self.parent = weakref.ref(parent)
        print 'Foo', self.id, 'born'

    def __del__(self):
        print 'Foo', self.id, 'died'


class BarType(object):
    def __init__(self, id):
        self.id = id
        self.foo = FooType(id, self)
        print 'Bar', self.id, 'born'

    def __del__(self):
        print 'Bar', self.id, 'died'

b = BarType(12)
```







