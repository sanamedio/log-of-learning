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

```python3
In [1]: from unittest import mock                                                                                                                          

In [2]: m = mock.Mock()                                                                                                                                    

In [3]: m                                                                                                                                                  
Out[3]: <Mock id='4354175440'>

In [4]: m.return_value = 42                                                                                                                                

In [5]: m                                                                                                                                                  
Out[5]: <Mock id='4354175440'>

In [6]: m()                                                                                                                                                
Out[6]: 42

In [7]: m.side_effect = ['foo', 'bar', 'baz' ]                                                                                                             

In [8]: m()                                                                                                                                                
Out[8]: 'foo'

In [9]: m()                                                                                                                                                
Out[9]: 'bar'

In [10]: m()                                                                                                                                               
Out[10]: 'baz'

In [11]: m()                                                                                                                                               
---------------------------------------------------------------------------
StopIteration                             Traceback (most recent call last)
<ipython-input-11-ec2213f3535c> in <module>
----> 1 m()

~/.pyenv/versions/3.6.1/lib/python3.6/unittest/mock.py in __call__(_mock_self, *args, **kwargs)
    937         # in the signature
    938         _mock_self._mock_check_sig(*args, **kwargs)
--> 939         return _mock_self._mock_call(*args, **kwargs)
    940 
    941 

~/.pyenv/versions/3.6.1/lib/python3.6/unittest/mock.py in _mock_call(_mock_self, *args, **kwargs)
    996 
    997             if not _callable(effect):
--> 998                 result = next(effect)
    999                 if _is_exception(result):
   1000                     raise result

StopIteration: 

In [12]:           
```


```python3
In [15]: m.assert_called()                                                                                     

In [16]: m.assert_called_once()                                                                                
---------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)
<ipython-input-16-397f8db66d8b> in <module>
----> 1 m.assert_called_once()

~/.pyenv/versions/3.6.1/lib/python3.6/unittest/mock.py in assert_called_once(_mock_self)
    793             msg = ("Expected '%s' to have been called once. Called %s times." %
    794                    (self._mock_name or 'mock', self.call_count))
--> 795             raise AssertionError(msg)
    796 
    797     def assert_called_with(_mock_self, *args, **kwargs):

AssertionError: Expected 'mock' to have been called once. Called 6 times.

In [17]:  m.reset_mock() #reset all interactions
```






