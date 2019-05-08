### 08-may-2019

### 2 - sysconfig to get details about python env

https://pymotw.com/3/sysconfig/index.html

```python
import sysconfig

config_values = sysconfig.get_config_vars()
print('Found {} configuration settings'.format(
    len(config_values.keys())))

print('\nSome highlights:\n')

print(' Installation prefixes:')
print('  prefix={prefix}'.format(**config_values))
print('  exec_prefix={exec_prefix}'.format(**config_values))

print('\n Version info:')
print('  py_version={py_version}'.format(**config_values))
print('  py_version_short={py_version_short}'.format(
    **config_values))
print('  py_version_nodot={py_version_nodot}'.format(
    **config_values))

print('\n Base directories:')
print('  base={base}'.format(**config_values))
print('  platbase={platbase}'.format(**config_values))
print('  userbase={userbase}'.format(**config_values))
print('  srcdir={srcdir}'.format(**config_values))

print('\n Compiler and linker flags:')
print('  LDFLAGS={LDFLAGS}'.format(**config_values))
print('  BASECFLAGS={BASECFLAGS}'.format(**config_values))
print('  Py_ENABLE_SHARED={Py_ENABLE_SHARED}'.format(
    **config_values))
```


### 1 - linecache module

https://pymotw.com/3/linecache/index.html
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
