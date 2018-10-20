# 20-oct-2018


### 1 - pyrasite shell

- Allows to get shell on a running python process
- https://pyrasite.readthedocs.io/en/latest/Shell.html

Step 1:
```bash
$ pip install pyrasite
$ echo 0 | sudo tee /proc/sys/kernel/yama/ptrace_scope
```
Step 2:
Run a Python program or something like ipython

Step 3:
```bash
$ pyrasite-shell <pid of python process>
```

### 2 - uncompyle6

- Good combination with pyrasite to get source code of attached code
- https://github.com/rocky/python-uncompyle6

This is python program I tested:
```python
def secret():
  for x in xrange(10000000):
    print("hello")
secret()
```

Left it running on another shell, and attached pyrasite to it

```python
#pyrasite shell
>> import uncompyle6
>> import sys
>> import __main__
>> uncompyle6.main.decompile(2.7 , __main__.secret.func_code, sys.stdout)
# uncompyle6 version 3.2.3
# Python bytecode 2.7
# Decompiled from: Python 2.7.12 (default, Dec  4 2017, 14:50:18) 
# [GCC 5.4.0 20160609]
# Embedded file name: test23.py
for x in xrange(100000000000):
    print 'hello'<uncompyle6.semantics.pysource.SourceWalker object at 0x7f073594ef50>
```

### 3 - magic methods

- getitem
```python
class Test(object):
    def __getitem__(self, items):
        print '%-15s  %s' % (type(items), items)

t = Test()
t[1]
t['hello world']
t[1, 'b', 3.0]
t[5:200:10]
t['a':'z':3]
t[object()]
```

- call
```python
class Test(object):
    def __call__(self, *args, **kwargs):
        print args
        print kwargs
        print '-'*80

t = Test()
t(1, 2, 3)
t(a=1, b=2, c=3)
t(4, 5, 6, d=4, e=5, f=6)
```
- getattr
```python
class Test(object):
    def __init__(self):
        self.a = 'a'
        self.b = 'b'

    def __getattr__(self, name):
        return 123456

t = Test()
print 'object variables: %r' % t.__dict__.keys()
print t.a
print t.b
print t.c
print getattr(t, 'd')
print hasattr(t, 'x')
```

- setattr
```python
class Test(object):
    def __init__(self):
        self.a = 'a'
        self.b = 'b'

    def __setattr__(self, name, value):
        print 'set %s to %s' % (name, repr(value))

        if name in ('a', 'b'):
            object.__setattr__(self, name, value)

t = Test()
t.c = 'z'
setattr(t, 'd', '888')
```
