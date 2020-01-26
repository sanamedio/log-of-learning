# 26-jan-2020

### 1 - Python Mocks

- Mocks are objects which keep track of how they were used. If a function takes a http request object, one can replace that with a Mock
- Mock objects keep changing as per the way they are used, and attack more Mock objects to themselves



```python3
#https://medium.com/@yeraydiazdiaz/what-the-mock-cheatsheet-mocking-in-python-6a71db997832

In [1]: from unittest import mock

In [2]: m = mock.Mock()

In [3]: isinstance(m.foo, mock.Mock)
Out[3]: True

In [4]: isinstance(m.bar, mock.Mock)
Out[4]: True

In [5]: isinstance(m(), mock.Mock)
Out[5]: True

In [6]: m.foo is not m.bar is not m()
Out[6]: True

In [7]: m.foo
Out[7]: <Mock name='mock.foo' id='4478187984'>

In [8]: m.foo = 'bar'

In [9]: assert m.foo == 'bar'

In [10]: m.configure_mock(bar='baz')

In [11]: assert m.bar == 'baz'

In [12]:
```
