# 11-nov-2018

### 12 - Flask Authorizatoin

```python
from functools import wraps

def check_auth(username, password):
    return username == 'admin' and password == 'secret'

def authenticate():
    message = {'message': "Authenticate."}
    resp = jsonify(message)

    resp.status_code = 401
    resp.headers['WWW-Authenticate'] = 'Basic realm="Example"'

    return resp

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth: 
            return authenticate()

        elif not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)

    return decorated

@app.route('/secrets')
@requires_auth
def api_hello():
    return "Shhh this is top secret spy stuff!"
```


Adding more authentication schemes:
```
resp.headers['WWW-Authenticate'] = 'Basic realm="Example"'
resp.headers.add('WWW-Authenticate', 'Bearer realm="Example"')
```



### 11 - Flask handling 404

```python
@app.errorhandler(404)
def not_found(error=None):
    message = {
            'status': 404,
            'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp

@app.route('/users/<userid>', methods = ['GET'])
def api_users(userid):
    users = {'1':'john', '2':'steve', '3':'bill'}
    
    if userid in users:
        return jsonify({userid:users[userid]})
    else:
        return not_found()

```

### 10 - Flask Response

```python
from flask import Response

@app.route('/hello', methods = ['GET'])
def api_hello():
    data = {
        'hello'  : 'world',
        'number' : 3
    }
    js = json.dumps(data)

    resp = Response(js, status=200, mimetype='application/json')

    return resp
```

### 9 - Flask Request Data and Headers

- Flask examples are from [this](http://blog.luisrei.com/articles/flaskrest.html)

```python
from flask import json

@app.route('/messages', methods = ['POST'])
def api_message():

    if request.headers['Content-Type'] == 'text/plain':
        return "Text Message: " + request.data

    elif request.headers['Content-Type'] == 'application/json':
        return "JSON Message: " + json.dumps(request.json)

    elif request.headers['Content-Type'] == 'application/octet-stream':
        f = open('./binary', 'wb')
        f.write(request.data)
                f.close()
        return "Binary message written!"

    else:
        return "415 Unsupported Media Type ;)"
```

### 8 - Flask Request type

```python
@app.route('/echo', methods = ['GET', 'POST', 'PATCH', 'PUT', 'DELETE'])
def api_echo():
    if request.method == 'GET':
        return "ECHO: GET\n"

    elif request.method == 'POST':
        return "ECHO: POST\n"

    elif request.method == 'PATCH':
        return "ECHO: PACTH\n"

    elif request.method == 'PUT':
        return "ECHO: PUT\n"

    elif request.method == 'DELETE':
        return "ECHO: DELETE"
```


### 7 - Flask parameters

```python
from flask import request

@app.route('/hello')
def api_hello():
    if 'name' in request.args:
        return 'Hello ' + request.args['name']
    else:
        return 'Hello John Doe'
```

```
GET /hello
Hello John Doe

GET /hello?name=Luis
Hello Luis
```

### 6 - Averaging and Summing decorators

```python
import functools


def summed(f):
    return lambda *x : sum(f(*x))


def averaged(f):
    def aux(acc,x):
        return ( acc[0] + x , acc[1] + 1)

    def out(*x):
        s, n = functools.reduce(aux , f(*x), (0,0))
        return s/ n if n > 0 else 0


    return out




@averaged
def producer2():
    yield 10
    yield 5
    yield 2.5
    yield 7.5


assert producer2() == (10 + 5 + 2.5 + 7.5) / 4

@summed
def producer1():
    yield 10
    yield 5
    yield 2.5
    yield 7.5

assert producer1() == (10 + 5 + 2.5 + 7.5)
```


### 5 - Adding a method to a instance using decorator

```python
def addto(instance):
    def decorator(f):
        import types
        f =  types.MethodType(f , instance)
        setattr(instance, f.__name__, f)
        return f
    return decorator



#example


class Foo:
    def __init__(self):
        self.x = 42

foo = Foo()

@addto(foo)
def print_x(self):
    print (self.x)


foo.print_x()
```

### 4 - Writing your own debug decorator

- https://wiki.python.org/moin/PythonDecoratorLibrary

```python
import sys

WHAT_TO_DEBUG = set(['io', 'core'])


class debug:

    def __init__(self, aspects=None):
        self.aspects = set(aspects)


    def __call__(self, f):
        if self.aspects & WHAT_TO_DEBUG:
            def newf(*args, **kwargs):
                print ( f.__name__, args, kwargs, file=sys.stderr)
                f_result = f(*args, *kwargs)
                print (sys.stderr, f.__name__, "returned", f_result, file=sys.stderr)
                print (f_result, file=sys.stderr)

            newf.__doc__ = f.__doc__
            return newf
        else:
            return f

@debug(['io'])
def prn(x):
    print(x)


@debug(['core'])
def mult(x,y):
    return x*y


prn(mult(2,2))
```


### 3 - pseudo-Currying

```python
class curried():
  '''
  Decorator that returns a function that keeps returning functions
  until all arguments are supplied; then the original function is
  evaluated.
  '''

  def __init__(self, func, *a):
    self.func = func
    self.args = a

  def __call__(self, *a):
    args = self.args + a
    if len(args) < self.func.func_code.co_argcount:
      return curried(self.func, *args)
    else:
      return self.func(*args)


@curried
def add(a, b):
    return a + b

add1 = add(1)

print(add1(2))
```


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
