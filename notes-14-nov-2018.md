# 14-nov-2018

### 16 - Multiprocessing vs Gevents

```python
import time


def echo(i):
    time.sleep(0.001)
    return i

def check_runs(Pool):

    p = Pool(10)

    run1 = [ a for a in p.imap_unordered(echo, range(10))]
    run2 = [ a for a in p.imap_unordered(echo, range(10))]
    run3 = [ a for a in p.imap_unordered(echo, range(10))]
    run4 = [ a for a in p.imap_unordered(echo, range(10))]

    print( Pool.__module__,run1 == run2 == run3 == run4 )


# dterminites
from gevent.pool import Pool
check_runs(Pool)


# non deterministic
from multiprocessing.pool import Pool
check_runs(Pool)
```
outputs:
```
gevent.pool True
multiprocessing.pool False
```

### 15 - Gevents spawns greenlets

- http://sdiehl.github.io/gevent-tutorial/

```python
Python 3.6.6 (default, Sep 12 2018, 18:26:19) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import gevent
>>> gevent.spawn(lambda : "hello" , 1,2,3)
<Greenlet "Greenlet-0" at 0x7fa104924c48: <lambda>(1, 2, 3)>
```
- greenlets are deterministic.

### 14 - Speeding up parallel requests using gevents

```python
import gevent.monkey
gevent.monkey.patch_socket()


import gevent
from urllib.request import urlopen
import simplejson as json
import time

def timethis(f):

    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        r = f(*args, **kwargs)
        end = time.perf_counter()
        print('{}{} : {}'.format( f.__module__, f.__name__ , end - start ))
        return r
    return wrapper


def fetch(pid):
    response =urlopen('http://icanhazip.com')
    result = response.read()
    print("Process {}: {}  ".format(pid,result))
    return result

@timethis
def synchronous():
    for i in range(1,10):
        fetch(i)

@timethis
def asynchronous():
    threads =  []
    for i in range(1,10):
        threads.append(gevent.spawn(fetch, i ))
    gevent.joinall(threads)


print("Synchrnous")
synchronous()

print("ASynchnorhous")
asynchronous()
```
output :
```
Synchrnous
Process 1: Hello python  
Process 2: Hello python  
Process 3: Hello python  
Process 4: Hello python  
Process 5: Hello python  
Process 6: Hello python  
Process 7: Hello python  
Process 8: Hello python  
Process 9: Hello python  
__main__synchronous : 7.785602852003649
ASynchnorhous
Process 7: Hello python  
Process 9: Hello python  
Process 6: Hello python  
Process 4: Hello python  
Process 3: Hello python  
Process 5: Hello python  
Process 8: Hello python  
Process 2: Hello python  
Process 1: Hello python  
__main__asynchronous : 0.5121218599961139
```

- Usefulness of monkey patching 

### 13 - Random non-deterministic event scheduling with gevents

```python
import gevent
import random
import time
from functools import wraps

def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        r = func(*args, **kwargs)
        end = time.perf_counter()
        print('{}.{} : {}'.format(func.__module__, func.__name__, end-start))
        return r
    return wrapper


def task(pid):
    """ Some non-deterministic task like random wait"""
    gevent.sleep(random.randint(0,2)*0.001)
    print("task %s done" % pid)


@timethis
def synchronous():
    for i in range(1,10):
        task(i)


@timethis
def asynchronous():
    threads = [ gevent.spawn(task, i ) for i in range(10)] #only instances are created not run
    gevent.joinall(threads) # what is I don't join ? this is necessary because it starts the tread instances



print ("Synchronous")

synchronous()

print ("Async")
asynchronous()
```


output:
```
Synchronous
task 1 done
task 2 done
task 3 done
task 4 done
task 5 done
task 6 done
task 7 done
task 8 done
task 9 done
__main__.synchronous : 0.011868374000187032
Async
task 0 done
task 1 done
task 3 done
task 6 done
task 7 done
task 9 done
task 2 done
task 4 done
task 5 done
task 8 done
__main__.asynchronous : 0.0031379409920191392
```
- notice that the async is faster than sync
- also, that its not time.sleep but gevent.sleep

### 12 - Greenlet select

- Select allows to timeout, which I guess is the minimum timeout ( doesnt mean necessarily you will get the processing time after that ).
- Select applies on the current greenlet only.

```python
import time
import gevent
from gevent import select


start = time.time()
tic = lambda: 'at %1.1f seconds' % ( time.time() - start)


def gr1():
    print('Started POlling :%s' % tic())
    select.select([] , [] , [] , 2 )
    print('Ended polling : %s' %tic())



def gr2():
    print('Start polling:%s' %tic())
    select.select([], [] , [] , 2 )
    print( ' Ending polling : %s' % tic())



def gr3():
    print("hey lets do some stuff while the greenlets poll, %s" % tic())
    gevent.sleep(1)


gevent.joinall([
    gevent.spawn(gr1),
    gevent.spawn(gr2),
    gevent.spawn(gr3),
])

```


### 11 - Concurrency using gevent

- Gevent makes it easier to do cooperative yield style concurrency between different parts of code
- It is built on top of greenlet: Only one greenlet is ever running at any given time.

```python
import gevent


def foo():
    print('Running in foo')
    gevent.sleep(0) #forcing yield
    print('Explicit context switch to foo again')
    
def bar():
    print('Explicit context switch to bar')
    gevent.sleep(0)
    print('Implicit context switch back to bar')

gevent.joinall([
    gevent.spawn(foo),
    gevent.spawn(bar)
    ])
```

Same thing with decorator(just for sake of it)
```python
import gevent


def logger(f):
    def inner():
        print( '>> ' , f.__name__)
        r = f()
        print( '<< ' , f.__name__)
        return r
    return inner


@logger
def foo():
    gevent.sleep(0)


@logger
def bar():
    gevent.sleep(0)



gevent.joinall([
    gevent.spawn(foo),
    gevent.spawn(bar)
    ])
```

- Why the order of adding the functions in gevent joinall, impacts the order of execution of steps ? Is it because we are spawning the first one few steps earlier(in the interpreter) than the second one and since python interpreter is kind of single threaded ; 


### 10 - event driven network programming using Twisted

- Echo server
```python
from twisted.internet import protocol, reactor, endpoints


class Echo(protocol.Protocol):
    def dataReceived(self, data):
        self.transport.write(data)

class EchoFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Echo()


# starts tcp server at 1234 , can be tested with netcat
endpoints.serverFromString(reactor, "tcp:1234").listen(EchoFactory())

reactor.run()
```

- web server
```python
from twisted.web import server, resource
from twisted.internet import reactor, endpoints

# object persistent beteween requests in memory, test with curl get


class Counter(resource.Resource):

    isLeaf = True
    numberRequests = 0

    def render_GET(self, request):
        self.numberRequests += 1
        request.setHeader(b"content-type", b"text/plain")
        content = u"I am request #{}\n".format(self.numberRequests)
        return content.encode("ascii")


endpoints.serverFromString(reactor, "tcp:8080").listen(server.Site(Counter()))
reactor.run()                  
```
- Broadcast server
```python
from twisted.internet import reactor, protocol, endpoints
from twisted.protocols import basic


#every client can see what others are sending(while they are connected), pubsub : use curl to test

class PubProtocol(basic.LineReceiver):

    def __init__(self, factory):
        self.factory = factory

    def connectionMade(self):
        self.factory.clients.add(self)

    def lineReceived(self,line):
        for c in self.factory.clients:
            source = "<{}>".format(self.transport.getHost()).encode('ascii')
            c.sendLine(source + line )





class PubFactory(protocol.Factory):
    def __init__(self):
        self.clients = set()

    def buildProtocol(self, addr):
        return PubProtocol(self)



endpoints.serverFromString(reactor, "tcp:1025").listen(PubFactory())
reactor.run()
```

### 9 - sys.getsizeof for int, byteobject, string

```python
Python 3.6.6 (default, Sep 12 2018, 18:26:19) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import sys
>>> sys.getsizeof(1)
28
>>> sys.getsizeof('1')
50
>>> sys.getsizeof("1")
50
>>> sys.getsizeof(b'1')
34
>>> 
```

### 8 - SQLAlchemy simple example

- Object mapping to database
```python
import os,sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()


class Person(Base):

    __tablename__ = 'person'

    person_id = Column(Integer, primary_key = True)
    person_name = Column(String(250), nullable = False)


class Address(Base):
    __tablename__ = 'address'
    
    id_ = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)
    person_id = Column(Integer, ForeignKey('person.person_id'))
    person = relationship(Person)

engine = create_engine('sqlite:///sqlalchemy_example.db')

Base.metadata.create_all(engine)


Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

new_person = Person(person_name='new person')
session.add(new_person)
session.commit()


new_address = Address(post_code='0001' , person=new_person)
session.add(new_address)
session.commit()


print(session.query(Person).all())


person = session.query(Person).first()
print(person.person_name)
```


### 7 - Pyglet multimedia library Hello World

```python
Python 3.6.6 (default, Sep 12 2018, 18:26:19) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import pyglet
>>> window = pyglet.window.Window()
>>> label = pyglet.text.Label('Hello, world',
...                           font_name='Times New Roman',
...                           font_size=36,
...                           x=window.width//2, y=window.height//2,
...                           anchor_x='center', anchor_y='center')
>>> @window.event
... def on_draw():
...     window.clear()
...     label.draw()
... 
>>> pyglet.app.run()
```

```python
import pyglet

window = pyglet.window.Window()

@window.event
def on_key_press(symbol, modifiers):
    print('A key was pressed' , symbol , modifiers)

@window.event
def on_draw():
    window.clear()

@window.event
def on_mouse_press(x,y,button, modifiers):
    print('The  mouse button '  , x , y , button, modifiers)

# this logs all the events
#window.push_handlers(pyglet.window.event.WindowEventLogger())

pyglet.app.run()
```

### 6 - Sympy

```python
>>> from sympy import *
>>> x , y , z = symbols('x y z')
>>> x
x
>>> y
y
>>> z
z
>>> expr = cos(x) + 1
>>> expr.subs(x,y)
cos(y) + 1
>>> expr.subs(x, 0)
2
>>> expr.subs(y, 0)
cos(x) + 1
>>> expand_
expand_complex(      expand_log(          expand_multinomial(  expand_power_exp(    
expand_func(         expand_mul(          expand_power_base(   expand_trig(         
>>> expand_func((x+y)**2)
(x + y)**2
>>> expand_func((x+y)**2)
(x + y)**2
>>> symplify("(x+y)**2")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'symplify' is not defined
>>> sympify("(x+y)**2")
(x + y)**2
>>> 
```

### 5 - Newton Raphson

- https://en.wikipedia.org/wiki/Newton%27s_method

```python
H = 1e-5

def derivative(f,x): return (f(x+H) - f(x))/H
def newton(f, x): return x - ( f(x) / derivative(f,x))
def runner(f,n): 
    x = 0
    itr = 0
    while itr < n:
        x = newton(f,1) if itr == 0 else newton(f,x)
        itr = itr + 1
    return x

if __name__ == '__main__':
    import sys 
    print( runner( lambda x: eval(sys.argv[1]) , 100) )
```

```bash
python newton.py x*x-2
```


### 4 - Smallest Number in python

```python
Python 3.6.6 (default, Sep 12 2018, 18:26:19) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import sys
>>> sys.float_info
sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.2250738585072014e-308, min_exp=-1021, min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)
>>> 
```

### 3 - SHA256 for subsequent bytes

```python
>>> hashlib.sha256(b'1').hexdigest()
'6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b'
>>> hashlib.sha256(b'2').hexdigest()
'd4735e3a265e16eee03f59718b9b5d03019c07d8b6c51f90da3a666eec13ab35'
>>> hashlib.sha256(b'3').hexdigest()
'4e07408562bedb8b60ce05c1decfe3ad16b72230967de01f640b7e4729b49fce'
```

### 2 - Dunder import 

```python
Python 3.6.6 (default, Sep 12 2018, 18:26:19) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> __import__('IPython').embed()
Python 3.6.6 (default, Sep 12 2018, 18:26:19) 
Type 'copyright', 'credits' or 'license' for more information
IPython 7.1.1 -- An enhanced Interactive Python. Type '?' for help.

In [1]: ls                                                                                                                                            
Desktop/	 Downloads/   Music/	  Public/	 Documents/	 Pictures/   __pycache__/	 

In [2]: #in IPython shell                                                                                                                             
```

### 1 - Floating point errors!

```python
Python 3.6.6 (default, Sep 12 2018, 18:26:19) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> [0.1] * 10
[0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
>>> sum( [0.1]*10)
0.9999999999999999
>>> import math
>>> math.fsum([0.1]*10)
1.0
>>> 
```
