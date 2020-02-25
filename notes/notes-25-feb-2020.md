# 25-feb-2020

### 3 - the side_effect can vary responses corresponding to args

```python
from unittest.mock import MagicMock

def side_effect(value):
    return value+1

m = MagicMock(side_effect=side_effect)

print(m(1))
#2
print(m(2))
#3
```
- https://stackoverflow.com/q/16162015/2091949

```python
def my_side_effect(*args, **kwargs):
    if args[0] == 42:
        return "Called with 42"
    elif args[0] == 43:
        return "Called with 43"
    elif kwargs['foo'] == 7:
        return "Foo is seven"

mockobj.mockmethod.side_effect = my_side_effect
```

### 2 - recursive patching external calls

- If there is a function and we need to patch a calls made by it 

```python
import os
from unittest.mock import patch, mock_open
from io import StringIO


def test_func():

    x = os.listdir()
    y = open("test.txt")
    z = os.getcwd()

    return (x,y,z)

def recursive_patch(func_list_to_patch, return_value_list, target_func):
    if len(func_list_to_patch)  == 0:
        return target_func()

    with patch(func_list_to_patch[0], return_value = return_value_list[0]):
        return recursive_patch( func_list_to_patch[1:], return_value_list[1:], target_func)


if __name__ == '__main__':

    func_list_to_patch = ["os.listdir", "os.getcwd","builtins.open"]
    mock_return_values = [["dummy"], "/home/funny", StringIO()]

    result = recursive_patch( func_list_to_patch, mock_return_values, test_func)

    print(result)
```

### 1 - aspectlib for AOP in python

https://python-aspectlib.readthedocs.io/en/latest/testing.html

```python
>>> from aspectlib import weave,test
>>> class ProductionClass(object):
...     def method(self):
...         return 'stuff'
>>> real = ProductionClass()
>>> patch = weave(real.method, [test.mock(3)])
>>> real.method(3, 4, 5, key='value')
3
```
