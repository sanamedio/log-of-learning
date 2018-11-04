# 05-nov-2018

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
 
