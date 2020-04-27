# 27-apr-2020

### 2 - coverage tool using sys.settrace

https://akaptur.com/blog/2014/08/02/the-cpython-peephole-optimizer-and-you/

```python
import sys
import tests
import inspect

class TinyCoverage(object):
    def __init__(self, file_to_watch):
        self.source_file = file_to_watch
        self.source_code = open(file_to_watch).readlines()
        self.executed_code = []

    def trace(self, frame, event, arg):
        current_file = inspect.getframeinfo(frame).filename

        if self.source_file in current_file and \
            (event == "line" or event == "call"):

            self.executed_code.append(frame.f_lineno)

        return self.trace

    def unexecuted_code(self):
        skipped = []
        for line_num in range(1, len(self.source_code)+1):
            if line_num not in self.executed_code:
                src = self.source_code[line_num - 1]
                if src != "\n":
                    skipped.append(line_num)
        return skipped

    def report(self):
        skipped = self.unexecuted_code()
        percent_skipped = float(len(skipped)) / len(self.source_code)
        if skipped:
            print "{} line(s) did not execute ({:.0%})".format(len(skipped), percent_skipped)
            for line_num in skipped:
                print line_num, self.source_code[line_num - 1]
        else:
            print "100% coverage, go you!"

if __name__ == '__main__':
    t = TinyCoverage('example.py')
    sys.settrace(t.trace)
    tests.run_tests()
    sys.settrace(None)
    t.report()
```


### 1 - adding a new attribute to existing object

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
