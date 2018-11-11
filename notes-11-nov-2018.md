# 11-nov-2018

### 2 - Decorator Decorator

- From https://wiki.python.org/moin/PythonDecoratorLibrary

```python
def simple_decorator(decorator):

    '''This decorator can be used to turn simple functions
    into well-behaved decorators, so long as the decorators
    are fairly simple. If a decorator expects a function and
    returns a function (no descriptors), and if it doesn't
    modify function attributes or docstring, then it is
    eligible to use this. Simply apply @simple_decorator to
    your decorator and it will automatically preserve the
    docstring and function attributes of functions to which
    it is applied.'''


    def new_decorator(f):
        g = decorator(f)
        g.__name__ = f.__name__
        g.__doc__ = f.__doc__
        g.__dict__.update(f.__dict__)

        return g


    new_decorator.__name__ = decorator.__name__
    new_decorator.__doc__ = decorator.__doc__
    new_decorator.__dict__.update(decorator.__dict__)


    return new_decorator




@simple_decorator
def my_simple_logging_decorator(func):
    def you_will_never_see_this_name(*args, **kwargs):
        print( 'calling {}'.format(func.__name__))
        return func(*args, **kwargs)
    return you_will_never_see_this_name


@my_simple_logging_decorator
def double(x):
    'Doubles a nubmer.'
    return 2 * x
```

### 1 - Retry Decorator with exponential backoff

- https://wiki.python.org/moin/PythonDecoratorLibrary#Retry

```python
import time,math


def retry(tries, delay=3, backoff=2):

    if backoff <= 1 : raise ValueError("backoff must be greater than 1")
    tries = math.floor(tries)
    if tries < 0 : raise ValueError("tries must be 0 or greater")
    if delay <= 0: raise ValueError("delay must be greatear than 0")

    def deco_retry(f):
        def f_retry(*args, **kwargs):
            mtries, mdelay = tries, delay

            rv = f(*args, **kwargs)

            while mtries >0:
                if rv: return True

                mtries -= 1
                time.sleep(mdelay)
                mdelay *= backoff

                rv = f(*args, **kwargs)

            
            return False

        return f_retry

    return deco_retry



@retry(10,1,1.1)
def keep_trying():
    print("Trying")
    return False



if '__main__'  == __name__:
    keep_trying()
```
