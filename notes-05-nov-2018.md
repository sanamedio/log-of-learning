# 05-nov-2018

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
 
