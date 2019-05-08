### 08-may-2019

### 4 - sched for scheduling

https://pymotw.com/2/sched/

```python
import sched
import time


scheduler = sched.scheduler(time.time, time.sleep)

def print_event(name):
    print( 'EVENT:', time.time(), name)


print('START:' , time.time())
scheduler.enter(2,1,print_event, ('first',))
scheduler.enter(3,1,print_event, ('second',))

scheduler.run()
```

### 3 - xml rpc server-client

- this is way too underrated 
- from pmotw
xrpc-server
```python
from xmlrpc.server import SimpleXMLRPCServer
import logging
import os

# Set up logging
logging.basicConfig(level=logging.INFO)

server = SimpleXMLRPCServer(
    ('localhost', 9000),
    logRequests=True,
)


# Expose a function
def list_contents(dir_name):
    logging.info('list_contents(%s)', dir_name)
    return os.listdir(dir_name)


server.register_function(list_contents)

# Start the server
try:
    print('Use Control-C to exit')
    server.serve_forever()
except KeyboardInterrupt:
    print('Exiting')

```

xrpc-client
```python
import xmlrpc.client

proxy= xmlrpc.client.ServerProxy('http://localhost:9000')
print(proxy.list_contents('/tmp'))
```


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
