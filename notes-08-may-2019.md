### 08-may-2019


### 1 - linecache module

- it can be used to read code of python modules like 
```python
$ python3
Python 3.6.7 (default, Oct 22 2018, 11:32:17) 
[GCC 8.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import linecache
>>> linecache.getline('linecache.py',3)
'This is intended to read lines from modules imported -- hence if a filename\n'
>>> linecache.getline('linecache.py',10)
'import os\n'
>>> 
>>> 
>>> 
>>> import os
>>> os.getline('os.py',10)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: module 'os' has no attribute 'getline'
>>> linecache.getline('os.py',10)
"  - os.extsep is the extension separator (always '.')\n"
>>> linecache.getline('os.py',100)
'    def _add(str, fn):\n'
>>> 
```
