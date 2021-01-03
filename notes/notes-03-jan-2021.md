# 03-jan-2021

### 8 - inplace permutation generation

https://sahandsaba.com/combinatorial-generation-for-coding-interviews-in-python.html

```python
def perms_2(A, starting_index):
    if starting_index == len(A) - 1:
        yield A
        return
    for _ in perms_2(A, starting_index + 1):
        yield A
        # Keep moving A[starting_index] to the right one at a time
        for i in range(starting_index, len(A) - 1):
            A[i], A[i + 1] = A[i + 1], A[i]
            yield A
        # Now move it all the way back to where it was at the beginning
        for i in range(len(A) - 1, starting_index, -1):
            A[i], A[i - 1] = A[i - 1], A[i]

for pi in perms_2(['1', '2', '3'], 0):
   print(''.join(pi))
123
213
231
132
312
321
```


### 7 - using subprocess to check shell output

http://prooffreaderplus.blogspot.com/2014/11/top-10-python-idioms-i-wished-id.html

```python
import subprocess
output = subprocess.check_output('dir', shell=True)
print(output)
```


### 6 - using counter to bucket random numbers

http://prooffreaderplus.blogspot.com/2014/11/top-10-python-idioms-i-wished-id.html

```python
In [1]: from collections import Counter
   ...: from random import randrange
   ...: import pprint
   ...: mycounter = Counter()
   ...: for i in range(1000):
   ...:     random_number = randrange(10)
   ...:     mycounter[random_number] += 1
   ...: for i in range(10):
   ...:     print(i, mycounter[i])
   ...:
0 92
1 101
2 94
3 120
4 94
5 105
6 96
7 104
8 94
9 100
```

### 5 - generating a pyc manually from py file

https://stackoverflow.com/questions/5607283/how-can-i-manually-generate-a-pyc-file-from-a-py-file/5607315

```
python -m compileall filename.py
```

can print the content like, (pycache folder is where to look if not visible in current)
```
➜  ~ python -c 'print(open("__pycache__/filename.cpython-38.pyc","rb").read())'
b'U\r\r\n\x00\x00\x00\x00\xb1\xb6\xf1_\x15\x00\x00\x00\xe3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00@\x00\x00\x00s\x0c\x00\x00\x00e\x00d\x00\x83\x01\x01\x00d\x01S\x00)\x02z\x0bhello worldN)\x01\xda\x05print\xa9\x00r\x02\x00\x00\x00r\x02\x00\x00\x00\xfa\x08test3.py\xda\x08<module>\x01\x00\x00\x00\xf3\x00\x00\x00\x00'
```

### 4 - using sysaudithook to sandbox 

Runtime auditing can be done with sysaudithook

https://stackoverflow.com/questions/48992030/disable-built-in-module-import-in-embedded-python

https://stackoverflow.com/questions/3068139/how-can-i-sandbox-python-in-pure-python

example from here: https://tirkarthi.github.io/programming/2019/05/23/pep-578-overview.html
```python
import sys

from functools import reduce


def product(series):
    import urllib.request

    try:
        urllib.request.urlopen("http://example.com")
    except:
        pass
    return reduce(lambda acc, num: acc * num, series)


def audit_hook(event, args):
    if event in ["urllib.Request"]:
        print(f"Network {event=} {args=}")


sys.addaudithook(audit_hook)

print(product(range(1, 10)))

# OUTPUT
# Network event='urllib.Request' args=('http://example.com', None, {}, 'GET')
# 362880
```

For different type of audit events, different actions can be taken.
This can be really useful to do aspect oriented programming. Raise custom events, and execute a list of functions for them.


### 3 - creating pyc files manually

https://stackoverflow.com/questions/53833455/how-to-find-out-the-magic-number-for-the-pyc-header-in-python-3

```python
Python 3.8.0 (default, Apr 21 2020, 09:37:48)
Type 'copyright', 'credits' or 'license' for more information
IPython 7.15.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import dis
   ...: import marshal
   ...:
   ...: PYC_HEADER = b'\x42\x0d\x0d\x0a\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
   ...:
   ...: def f():
   ...:     print('Hello     World')
   ...:
   ...: with open('test.pyc', 'wb') as pyc:
   ...:     pyc.write(PYC_HEADER)
   ...:     marshal.dump(dis.Bytecode(f).codeobj, pyc)
   ...:

In [2]: exit
➜  ~ python test.pyc
RuntimeError: Bad magic number in .pyc file
```

This gives error because .pyc needs the correct magic number to be run directly by the python interpreter

https://nedbatchelder.com/blog/200804/the_structure_of_pyc_files.html
This blog gives some info on the structure of it, but isn't useful because lot of changes happened since python version it has used.

After comparing two pyc files of 3.8, was able to check the header is b'U\r\r\n\x00\x00\x00\x00\xb1\xb6\xf1_\x15\x00\x00\x00' and this works for the above program.

### 2 - python startup

Digging in old hacker news articles, found this discussion about startup time of interpreter of python.
https://mail.python.org/pipermail/python-dev/2018-May/153296.html
It mentions how it is impacting the overall performance of large applications where this has to happen thousands of times. They seem to be solving it with a workaround described as follows:

```
Mercurial provides a `chg` program that essentially spins up a daemon
`hg` process running a "command server" so the `chg` program [written in
C - no startup overhead] can dispatch commands to an already-running
Python/`hg` process and avoid paying the startup overhead cost. When you
run Mercurial's test suite using `chg`, it completes *minutes* faster.
`chg` exists mainly as a workaround for slow startup overhead.
```

On doing `python -v`, we get the following verbose output of startup of the interpreter. Certainly if we dont have to do it everytime and somehow directly whatever we want to execute can be passed to a running interpreter; it would be way faster. But isn't it how we do in general with celery based job queues. Only one time startup and rest is just functions getting queued and executed. But anyways, with containers getting popularity and the immutability benefits - it makes sense to have smaller startup time for anything. 

running ```python -v -c 'print("hello")'``` gives the following. Such an effort to print a simple hello.

```bash
~ python -v -c 'print("hello")'
import _frozen_importlib # frozen
import _imp # builtin
import '_thread' # <class '_frozen_importlib.BuiltinImporter'>
import '_warnings' # <class '_frozen_importlib.BuiltinImporter'>
import '_weakref' # <class '_frozen_importlib.BuiltinImporter'>
import '_frozen_importlib_external' # <class '_frozen_importlib.FrozenImporter'>
import '_io' # <class '_frozen_importlib.BuiltinImporter'>
import 'marshal' # <class '_frozen_importlib.BuiltinImporter'>
import 'posix' # <class '_frozen_importlib.BuiltinImporter'>
import _thread # previously loaded ('_thread')
import '_thread' # <class '_frozen_importlib.BuiltinImporter'>
import _weakref # previously loaded ('_weakref')
import '_weakref' # <class '_frozen_importlib.BuiltinImporter'>
# installing zipimport hook
import 'time' # <class '_frozen_importlib.BuiltinImporter'>
import 'zipimport' # <class '_frozen_importlib.FrozenImporter'>
# installed zipimport hook
import 'faulthandler' # <class '_frozen_importlib.BuiltinImporter'>
# /Users/myUser/.pyenv/versions/3.8.0/lib/python3.8/encodings/__pycache__/__init__.cpython-38.pyc matches /Users/myUser/.pyenv/versions/3.8.0/lib/python3.8/encodings/__init__.py
# code object from '/Users/myUser/.pyenv/versions/3.8.0/lib/python3.8/encodings/__pycache__/__init__.cpython-38.pyc'
# /Users/myUser/.pyenv/versions/3.8.0/lib/python3.8/__pycache__/codecs.cpython-38.pyc matches /Users/myUser/.pyenv/versions/3.8.0/lib/python3.8/codecs.py
# code object from '/Users/myUser/.pyenv/versions/3.8.0/lib/python3.8/__pycache__/codecs.cpython-38.pyc'
import '_codecs' # <class '_frozen_importlib.BuiltinImporter'>
import 'codecs' # <_frozen_importlib_external.SourceFileLoader object at 0x1029012b0>
# /Users/myUser/.pyenv/versions/3.8.0/lib/python3.8/encodings/__pycache__/aliases.cpython-38.pyc matches /Users/myUser/.pyenv/versions/3.8.0/lib/python3.8/encodings/aliases.py
# code object from '/Users/myUser/.pyenv/versions/3.8.0/lib/python3.8/encodings/__pycache__/aliases.cpython-38.pyc'
import 'encodings.aliases' # <_frozen_importlib_external.SourceFileLoader object at 0x102913880>
import 'encodings' # <_frozen_importlib_external.SourceFileLoader object at 0x10287ae80>
# /Users/myUser/.pyenv/versions/3.8.0/lib/python3.8/encodings/__pycache__/utf_8.cpython-38.pyc matches /Users/myUser/.pyenv/versions/3.8.0/lib/python3.8/encodings/utf_8.py
# code object from '/Users/myUser/.pyenv/versions/3.8.0/lib/python3.8/encodings/__pycache__/utf_8.cpython-38.pyc'
import 'encodings.utf_8' # <_frozen_importlib_external.SourceFileLoader object at 0x102901e80>
import '_signal' # <class '_frozen_importlib.BuiltinImporter'>
# /Users/myUser/.pyenv/versions/3.8.0/lib/python3.8/encodings/__pycache__/latin_1.cpython-38.pyc matches /Users/myUser/.pyenv/versions/3.8.0/lib/python3.8/encodings/latin_1.py
# code object from '/Users/myUser/.pyenv/versions/3.8.0/lib/python3.8/encodings/__pycache__/latin_1.cpython-38.pyc'
import 'encodings.latin_1' # <_frozen_importlib_external.SourceFileLoader object at 0x102913970>
# /Users/myUser/.pyenv/versions/3.8.0/lib/python3.8/__pycache__/io.cpython-38.pyc matches /Users/myUser/.pyenv/versions/3.8.0/lib/python3.8/io.py
# code object from '/Users/myUser/.pyenv/versions/3.8.0/lib/python3.8/__pycache__/io.cpython-38.pyc'
# /Users/myUser/.pyenv/versions/3.8.0/lib/python3.8/__pycache__/abc.cpython-38.pyc matches /Users/myUser/.pyenv/versions/3.8.0/lib/python3.8/abc.py
# code object from '/Users/myUser/.pyenv/versions/3.8.0/lib/python3.8/__pycache__/abc.cpython-38.pyc'
import '_abc' # <class '_frozen_importlib.BuiltinImporter'>
import 'abc' # <_frozen_importlib_external.SourceFileLoader object at 0x102913df0>
import 'io' # <_frozen_importlib_external.SourceFileLoader object at 0x102913b20>
# /Users/myUser/.pyenv/versions/3.8.0/lib/python3.8/__pycache__/site.cpython-38.pyc matches /Users/myUser/.pyenv/versions/3.8.0/lib/python3.8/site.py
# code object from '/Users/myUser/.pyenv/versions/3.8.0/lib/python3.8/__pycache__/site.cpython-38.pyc'
# /Users/myUser/.pyenv/versions/3.8.0/lib/python3.8/__pycache__/os.cpython-38.pyc matches /Users/myUser/.pyenv/versions/3.8.0/lib/python3.8/os.py
# code object from '/Users/myUser/.pyenv/versions/3.8.0/lib/python3.8/__pycache__/os.cpython-38.pyc'
# /Users/myUser/.pyenv/versions/3.8.0/lib/python3.8/__pycache__/stat.cpython-38.pyc matches /Users/myUser/.pyenv/versions/3.8.0/lib/python3.8/stat.py
# code object from '/Users/myUser/.pyenv/versions/3.8.0/lib/python3.8/__pycache__/stat.cpython-38.pyc'
import '_stat' # <class '_frozen_importlib.BuiltinImporter'>
import 'stat' # <_frozen_importlib_external.SourceFileLoader object at 0x1029aa790>
# /Users/myUser/.pyenv/versions/3.8.0/lib/python3.8/__pycache__/posixpath.cpython-38.pyc matches /Users/myUser/.pyenv/versions/3.8.0/lib/python3.8/posixpath.py
# code object from '/Users/myUser/.pyenv/versions/3.8.0/lib/python3.8/__pycache__/posixpath.cpython-38.pyc'
# /Users/myUser/.pyenv/versions/3.8.0/lib/python3.8/__pycache__/genericpath.cpython-38.pyc matches /Users/myUser/.pyenv/versions/3.8.0/lib/python3.8/genericpath.py
# code object from '/Users/myUser/.pyenv/versions/3.8.0/lib/python3.8/__pycache__/genericpath.cpython-38.pyc'
import 'genericpath' # <_frozen_importlib_external.SourceFileLoader object at 0x1029bb280>
import 'posixpath' # <_frozen_importlib_external.SourceFileLoader object at 0x1029aa820>
# /Users/myUser/.pyenv/versions/3.8.0/lib/python3.8/__pycache__/_collections_abc.cpython-38.pyc matches /Users/myUser/.pyenv/versions/3.8.0/lib/python3.8/_collections_abc.py
# code object from '/Users/myUser/.pyenv/versions/3.8.0/lib/python3.8/__pycache__/_collections_abc.cpython-38.pyc'
import '_collections_abc' # <_frozen_importlib_external.SourceFileLoader object at 0x1029bb6a0>
import 'os' # <_frozen_importlib_external.SourceFileLoader object at 0x10292fe80>
# /Users/myUser/.pyenv/versions/3.8.0/lib/python3.8/__pycache__/_sitebuiltins.cpython-38.pyc matches /Users/myUser/.pyenv/versions/3.8.0/lib/python3.8/_sitebuiltins.py
# code object from '/Users/myUser/.pyenv/versions/3.8.0/lib/python3.8/__pycache__/_sitebuiltins.cpython-38.pyc'
import '_sitebuiltins' # <_frozen_importlib_external.SourceFileLoader object at 0x1029a2730>
import 'site' # <_frozen_importlib_external.SourceFileLoader object at 0x10292f790>
Python 3.8.0 (default, Apr 21 2020, 09:37:48)
[Clang 11.0.0 (clang-1100.0.33.16)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
hello
# clear sys.audit hooks
# clear builtins._
# clear sys.path
# clear sys.argv
# clear sys.ps1
# clear sys.ps2
# clear sys.last_type
# clear sys.last_value
# clear sys.last_traceback
# clear sys.path_hooks
# clear sys.path_importer_cache
# clear sys.meta_path
# clear sys.__interactivehook__
# restore sys.stdin
# restore sys.stdout
# restore sys.stderr
# cleanup[2] removing sys
# cleanup[2] removing builtins
# cleanup[2] removing _frozen_importlib
# cleanup[2] removing _imp
# cleanup[2] removing _warnings
# cleanup[2] removing _frozen_importlib_external
# cleanup[2] removing _io
# cleanup[2] removing marshal
# cleanup[2] removing posix
# cleanup[2] removing _thread
# cleanup[2] removing _weakref
# cleanup[2] removing time
# cleanup[2] removing zipimport
# destroy zipimport
# cleanup[2] removing faulthandler
# cleanup[2] removing _codecs
# cleanup[2] removing codecs
# cleanup[2] removing encodings.aliases
# cleanup[2] removing encodings
# destroy encodings
# cleanup[2] removing encodings.utf_8
# cleanup[2] removing _signal
# cleanup[2] removing __main__
# destroy __main__
# cleanup[2] removing encodings.latin_1
# cleanup[2] removing _abc
# cleanup[2] removing abc
# cleanup[2] removing io
# cleanup[2] removing _stat
# cleanup[2] removing stat
# cleanup[2] removing genericpath
# cleanup[2] removing posixpath
# cleanup[2] removing os.path
# cleanup[2] removing _collections_abc
# destroy _collections_abc
# cleanup[2] removing os
# cleanup[2] removing _sitebuiltins
# cleanup[2] removing site
# destroy site
# destroy time
# destroy faulthandler
# destroy _signal
# destroy _abc
# destroy _sitebuiltins
# destroy io
# destroy abc
# destroy posixpath
# destroy _stat
# destroy genericpath
# destroy os
# destroy stat
# cleanup[3] wiping encodings.latin_1
# cleanup[3] wiping encodings.utf_8
# cleanup[3] wiping encodings.aliases
# cleanup[3] wiping codecs
# cleanup[3] wiping _codecs
# cleanup[3] wiping _weakref
# cleanup[3] wiping _thread
# cleanup[3] wiping posix
# cleanup[3] wiping marshal
# cleanup[3] wiping _io
# cleanup[3] wiping _frozen_importlib_external
# destroy io
# destroy posix
# destroy marshal
# cleanup[3] wiping _warnings
# cleanup[3] wiping _imp
# cleanup[3] wiping _frozen_importlib
# destroy _frozen_importlib_external
# destroy _imp
# destroy _thread
# destroy _warnings
# destroy _weakref
# cleanup[3] wiping sys
# cleanup[3] wiping builtins
# destroy _frozen_importlib
```

importlib is bootstrapped https://hg.python.org/cpython/file/62cf4e77f785/Python/importlib.h
https://stackoverflow.com/questions/22378507/globals-frozen-importlib-builtinimporter


### 1 - zipfly for big files

Saw this cool python project on hacker news. 

https://github.com/BuzonIO/zipfly#lib

Use case is to write zips in a memory efficient manner. 

```python
import zipfly

    paths = [
        {
            'fs': '/path/to/large/file'
        },
    ]

    zfly = zipfly.ZipFly(paths = paths)

    generator = zfly.generator()
    print (generator)
    # <generator object ZipFly.generator at 0x7f74d52bcc50>


    with open("large.zip", "wb") as f:
        for i in generator:
            f.write(i)
```

It appears like a generator wrapper looking at the implementation file on an existing library.
https://github.com/BuzonIO/zipfly/blob/master/zipfly/zipfly.py

