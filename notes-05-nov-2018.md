# 05-nov-2018

### 6 - While writing a library ( like Django ) things to take care of for portability between VMs

- https://jacobian.org/writing/python-implementation-details/
  - Using the \_\_builtins__ super-global instead of import \_\_builtin__.
  - Assumptions about the terminal that’s available. Not all terminals will support curses, so anything involving term colors or even isatty is a bit suspect.
  - Assumptions about what’s available in the os module. os.access, os.chmod, os.getpid, may not be available.
  - Relying on features of “old-style” classes, or dynamically creating classes at runtime based on types.ClassType. In general, avoid old-style classes completely if at all possible.
  - Assumptions about function internals, especially im_func.func_code.
  - Assumptions about dict ordering. Remember that dict really is unordered; just because you “usually” get the same order doesn’t mean that you’ve gotten a magic ordered dict.
  - Making code that requires gc.collect.
  - Relying on built-in exception message strings; some (IndexError) differ between VMs.
  - Not paying close attention to type conversion at boundaries (sockets, databases); you might get a boxed type (i.e. a java.lang.String) from the underlying VM where you’re not expecting it.
  - Not thinking carefully about PYTHONPATH, or ignoring things like JYTHONPATH.
  - Not using \_\_import__ properly. Use importlib instead.
  - Assuming the existence or format of .pyc or .pyo objects, or assuming that Python modules must be \*.py, or really any assumptions about the names of files.


### 5 - FUSE : filesystem in userspace

- https://en.wikipedia.org/wiki/Filesystem_in_Userspace
- ```sudo apt install python-fuse``` (no idea how to install for python3)

### 4 - using pandas to directly load data ( pandas is kinda awesome)

install:
```bash
pip install pandas
```

run:
```python
Python 3.7.0 (default, Nov  4 2018, 00:07:25) 
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import pandas as pd
>>> 
>>> direct_link = 'http://www.randalolson.com/wp-content/uploads/percent-bachelors-degrees-women-usa.csv'
>>> women_majors = pd.read_csv(direct_link)
>>> 
>>> print(women_majors.info())
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 42 entries, 0 to 41
Data columns (total 18 columns):
Year                             42 non-null int64
Agriculture                      42 non-null float64
Architecture                     42 non-null float64
Art and Performance              42 non-null float64
Biology                          42 non-null float64
Business                         42 non-null float64
Communications and Journalism    42 non-null float64
Computer Science                 42 non-null float64
Education                        42 non-null float64
Engineering                      42 non-null float64
English                          42 non-null float64
Foreign Languages                42 non-null float64
Health Professions               42 non-null float64
Math and Statistics              42 non-null float64
Physical Sciences                42 non-null float64
Psychology                       42 non-null float64
Public Administration            42 non-null float64
Social Sciences and History      42 non-null float64
dtypes: float64(17), int64(1)
memory usage: 6.0 KB
None
>>> women_majors.head()
   Year             ...               Social Sciences and History
0  1970             ...                                      36.8
1  1971             ...                                      36.2
2  1972             ...                                      36.1
3  1973             ...                                      36.4
4  1974             ...                                      37.3

[5 rows x 18 columns]
>>> 
```

### 3 - test data generation in python using mimesis

```python
Python 3.7.0 (default, Nov  4 2018, 00:07:25) 
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from mimesis import Person
>>> person = Person('en')
>>> person.full_name()
'Sheldon Mcdonald'
>>> person.occupation()
'Preacher'
>>> person.occupation()
'Scrap Dealer'
>>> person.telephone()
'436.227.0495'
>>> person.identifier()
'53-04/14'
>>> person.identifier(mask='####/##-#')
'0299/48-5'
```

### 2 - better way to refer to libc

```python
>>> import ctypes
>>> import ctypes.util
>>> libc = ctypes.CDLL(ctypes.util.find_library("c")
... )
>>> libc
<CDLL 'libc.so.6', handle 7fae30f804e0 at 0x7fae2fb44a58>
>>> 
```

### 1 - type hints for python 3

- Can generate types automatically using instagram's https://github.com/Instagram/MonkeyType
- using typing module, the type hints can be read and appropriate exception can be raised like follows

```python
from typing import get_type_hints
from functools import wraps
from inspect import getfullargspec

def validate_input( obj, **kwargs ):

	hints = get_type_hints(obj)

	# iterate all type hints

	for attr_name, attr_type in hints.items():
		if attr_name == 'return':
			continue


		if not isinstance(kwargs[attr_name], attr_type ):
			raise TypeError(
				'Argument %r is not of the type %s' % (attr_name, attr_type))


def type_check(f):
	@wraps(f)
	def wrapped_decorator( *args, **kwargs):
		func_args = getfullargspec(f)[0]
		kwargs.update(dict(zip(func_args, args)))
		
		validate_input(f, **kwargs)
		return f(**kwargs)

	return wrapped_decorator


@type_check
def addition(number : int , other_number: int ) -> int :
	return number + other_number

print(addition ( 1,2 ))

print( addition( 1, '2' )) 
```

output:
```bash
3
Traceback (most recent call last):
  File "test2.py", line 41, in <module>
    print( addition( 1, '2' ))
           └ <function addition at 0x7f43edbea510>
  File "test2.py", line 29, in wrapped_decorator
    validate_input(f, **kwargs)
    │              │    └ {'number': 1, 'other_number': '2'}
    │              └ <function addition at 0x7f43edbea488>
    └ <function validate_input at 0x7f43eef26b70>
  File "test2.py", line 18, in validate_input
    'Argument %r is not of the type %s' % (attr_name, attr_type))
TypeError: Argument 'other_number' is not of the type <class 'int'>

```
 
