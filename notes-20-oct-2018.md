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

