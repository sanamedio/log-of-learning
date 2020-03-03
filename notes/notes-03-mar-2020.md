# 03-mar-2020

### 1 - modifying variables from the past

https://stackoverflow.com/questions/34650744/modify-existing-variable-in-locals-or-frame-f-locals

Kinda implementation specific, so better to just read than write.

```python
import inspect
import ctypes

def parent():
    a = 1
    z = 'foo'

    print('- Trying to add a new variable ---------------')
    hack(case=0)  # just try to add a new variable 'b'
    print(a)
    print(z)
    assert a == 1
    assert z == 'foo'

    try:
        print (b)
        assert False  # never is going to reach this point
    except NameError:
        print("ok, global name 'b' is not defined")

    print('- Trying to remove an existing variable ------')
    hack(case=1)
    print(a)
    assert a == 2
    try:
        print (z)
    except NameError:
        print("ok, we've removed the 'z' var")

    print('- Trying to update an existing variable ------')
    hack(case=2)
    print(a)
    assert a == 3


def hack(case=0):
    frame = inspect.stack()[1][0]
    if case == 0:
        frame.f_locals['b'] = "don't work"
    elif case == 1:
        frame.f_locals.pop('z')
        frame.f_locals['a'] += 1
    else:
        frame.f_locals['a'] += 1

    # passing c_int(1) will remove and update variables as well
    # passing c_int(0) will only update
    ctypes.pythonapi.PyFrame_LocalsToFast(
        ctypes.py_object(frame),
        ctypes.c_int(1))

if __name__ == '__main__':
    parent()
```
