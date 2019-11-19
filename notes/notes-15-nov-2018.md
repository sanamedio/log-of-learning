# 15-nov-2018

### 18 - Really nice twisted chatserver and can work with telnet

- No idea why netcat doesn't send a proper newline. Need to google. Otherwise would not need telnet on ubuntu
- It's like state machine with per user instances which handle them, and there is a global factory instance where you store shared data, works like a charm
- orielly book on twisted example

```python
from twisted.internet.protocol import Factory
from twisted.protocols.basic import LineReceiver
from twisted.internet import reactor

def bytify(s):
    print('bytify : ' , s)
    
    if not isinstance(s,bytes):
        if s: return bytes(s,'utf-8')

    return b''


class ChatProtocol(LineReceiver):
    def __init__(self, factory):
        self.factory = factory
        self.name = None
        self.state ="REGISTER"

    def connectionMade(self):
        self.sendLine(bytify("What's your name?"))

    def connectionLost(self,reason):
        if self.name in self.factory.users:
            del self.factory.users[self.name]
            self.broadcastMessage(bytify("%s has left the channel." %(self.name,)))

    def lineReceived(self, line):
        if self.state == "REGISTER":
            self.handle_REGISTER(line)
        else:
            self.handle_CHAT(line)

    def handle_REGISTER(self, name):
        if name in self.factory.users:
            self.sendLine(bytify("name taken, please choose other"))
            return

        self.sendLine(bytify("Welcome , %s!" % (name,)))
        self.broadcastMessage(bytify("%s has joined the channel" % (name,)))
        self.name = name
        self.factory.users[name] = self
        self.state = "CHAT"


    def handle_CHAT(self, message):
        message  = "<%s> %s" %(self.name, message)
        self.broadcastMessage(bytify(message))

    def broadcastMessage(self,message):
        for name, protocol in self.factory.users.items():
            if protocol != self:
                protocol.sendLine(bytify(message))



class ChatFactory(Factory):
    def __init__(self):
        self.users=  {}

    def buildProtocol(self, addr):
        return ChatProtocol(self)

reactor.listenTCP(8000,ChatFactory())
reactor.run()
```

### 17 - Twisted quote server 

- May be idea is to build a quote abstraction over the default protocol and how that can be made using twisted. 
- Incrementing connection count when a new connection is created, and decrement when it is closed. Still why it is that even with too many requests count is remaining at 3 ::::: If we remove the lost connection call , it will not leave the connections and count will increase. So what probaby it shows is that how quickly requests come and get closed. What if I do a heavy processing?

```python
#server
from twisted.internet.protocol import Factory
from twisted.internet import reactor, protocol

class QuoteProtocol(protocol.Protocol):

    def __init__(self, factory):
        self.factory=  factory


    def connectionMade(self):
        self.factory.numConnection += 1

    def dataReceived(self, data):
        print ("Number of active connection : %d" % ( self.factory.numConnection, ))
        print ("> Recieved: %s " % (data))
        print ("> Sending : %s " % (self.getQuote()))

        self.transport.write(self.getQuote())
        self.updateQuote(data)

    def connectionLost(self, reason ):
        self.factory.numConnection -= 1

    def getQuote(self):
        return self.factory.quote

    def updateQuote(self, quote):
        self.factory.quote = quote



class QuoteFactory(Factory):
    numConnection = 0 # it counts the number of open connections

    def __init__(self, quote=None):
        self.quote = quote or b"Truth never dies"

    def buildProtocol(self, addr):
        return QuoteProtocol(self)


reactor.listenTCP(9000, QuoteFactory())
reactor.run()
```

```python
#client
from twisted.internet import reactor, protocol


quote_counter = 0

class QuoteProtocol(protocol.Protocol):
    def __init__(self, factory):
        self.factory = factory

    def connectionMade(self):
        self.sendQuote()


    def sendQuote(self):
        self.transport.write(self.factory.quote)


    def dataReceived(self, data):
        print("received quote:" , data)
        self.transport.loseConnection()





class QuoteClientFactory(protocol.ClientFactory):

    def __init__(self, quote):
        self.quote = quote


    def buildProtocol(self, addr):
        return QuoteProtocol(self)

    def clientConnectionFailed(self, connector, reason):
        print("conection failed : ", reason.getErrorMessage())
        maybeStopReactor()

    def clientConnectionLost(self, connector, reason):
        print ('connection lost' , reason.getErrorMessage())
        maybeStopReactor()

def maybeStopReactor():
    global quote_counter
    quote_counter -= 1
    if not quote_counter:
        reactor.stop()

quotes = [b"asdasda" , b"asdasqwerwertwert", b"asdafrhdfgasdasd"]


for quote in 10000*quotes:
    reactor.connectTCP('localhost', 9000, QuoteClientFactory(quote))
reactor.run()
```

### 16 - Twisted Echo Client server

- Twisted has nice event driven style of handling protocols


client.py:
```python
from twisted.internet import protocol, reactor


class Client(protocol.Protocol):
    def connectionMade(self):
        self.transport.write(b"Hello ,world!")

    def dataReceived(self,data):
        print("Server said:", data)
        self.transport.loseConnection()


class ClientFactory(protocol.ClientFactory):
    def buildProtocol(self, addr):
        return Client()

    def clientConnectionFailed(self, connector ,reason):
        print("Connection failed")
        reactor.stop()

    def clientConnectionLost(self, connection, reason):
        print("Connection lost")
        reactor.stop()


reactor.connectTCP("localhost", 8000 , ClientFactory())
reactor.run()
```

server.py
```python
from twisted.internet import protocol, reactor

class Echo(protocol.Protocol):
    def dataReceived(self, data):
        self.transport.write(data)
        print('Client sent to me:' ,data)

class EchoFactory(protocol.Factory):
    def buildProtocol(self, addr):
            return Echo()


reactor.listenTCP(8000, EchoFactory())
reactor.run()
```

### 15 - Gevent Group

```python

In [3]: def main(): 
   ...:     import gevent 
   ...:     from gevent.pool import Group 
   ...:     def talk(msg): 
   ...:         for i in range(3): 
   ...:             print(msg) 
   ...:     g1 = gevent.spawn(talk, 'bar') 
   ...:     g2 = gevent.spawn(talk, 'foo') 
   ...:     g3 = gevent.spawn(talk, 'bizz') 
   ...:     group = Group() 
   ...:     group.add(g1) 
   ...:     group.add(g2) 
   ...:     group.join() 
   ...:     group.add(g3) 
   ...:     group.join() 
   ...:                                                                                               

In [4]: main()                                                                                        
bar
bar
bar
foo
foo
foo
bizz
bizz
bizz
bar
bar
bar
foo
foo
foo
bizz
bizz
bizz
```

### 14 - Gevent Queue

- weird issues with python3 interpreter, not able to take in Queue , but worked well with ipython in pipenv

```python

In [7]:  
   ...: import gevent 
   ...: from gevent.queue import Queue 
   ...:  
   ...: tasks = Queue() 
   ...:  
   ...: def worker(n): 
   ...:     while not tasks.empty(): 
   ...:         task = tasks.get() 
   ...:         print('Worker %s got task %s' % (n, task)) 
   ...:         gevent.sleep(0) 
   ...:  
   ...:     print('Quitting time!') 
   ...:  
   ...: def boss(): 
   ...:     for i in range(1,25): 
   ...:         tasks.put_nowait(i) 
   ...:  
   ...: gevent.spawn(boss).join() 
   ...:  
   ...: gevent.joinall([ 
   ...:     gevent.spawn(worker, 'steve'), 
   ...:     gevent.spawn(worker, 'john'), 
   ...:     gevent.spawn(worker, 'nancy'), 
   ...: ]) 
   ...:  
   ...:  
   ...:                                                                                                  
Worker steve got task 1
Worker john got task 2
Worker nancy got task 3
Worker steve got task 4
Worker john got task 5
Worker nancy got task 6
Worker steve got task 7
Worker john got task 8
Worker nancy got task 9
Worker steve got task 10
Worker john got task 11
Worker nancy got task 12
Worker steve got task 13
Worker john got task 14
Worker nancy got task 15
Worker steve got task 16
Worker john got task 17
Worker nancy got task 18
Worker steve got task 19
Worker john got task 20
Worker nancy got task 21
Worker steve got task 22
Worker john got task 23
Worker nancy got task 24
Quitting time!
Quitting time!
Quitting time!
Out[7]: 
[<Greenlet "Greenlet-6" at 0x7f078538f598: _run>,
 <Greenlet "Greenlet-7" at 0x7f078538f6a8: _run>,
 <Greenlet "Greenlet-8" at 0x7f078538f7b8: _run>]

In [8]:  
```

```python
In [6]: def main(): 
   ...:     import gevent 
   ...:     from gevent.queue import Queue, Empty 
   ...:     tasks = Queue(maxsize=3) 
   ...:     def worker(name): 
   ...:         try: 
   ...:             while True: 
   ...:                 task = tasks.get(timeout=1) 
   ...:                 print('Worker %s got task %s' % (name, task)) 
   ...:                 gevent.sleep(0) 
   ...:         except Empty: 
   ...:             print('Quitting time!') 
   ...:     def boss(): 
   ...:         for i in range(1,10): 
   ...:             tasks.put(i) 
   ...:         print('assigned all work') 
   ...:         for i in range(10,20): 
   ...:             tasks.put(i) 
   ...:         print('Assigned all work in interaction 2') 
   ...:     gevent.joinall([ 
   ...:         gevent.spawn(boss), 
   ...:         gevent.spawn(worker,'steve'), 
   ...:         gevent.spawn(worker, 'john'), 
   ...:         gevent.spawn(worker, 'bob'), 
   ...:         ]) 
   ...:                                                                                               

In [7]: main()                                                                                        
Worker steve got task 1
Worker john got task 2
Worker bob got task 3
Worker steve got task 4
Worker john got task 5
Worker bob got task 6
assigned all work
Worker steve got task 7
Worker john got task 8
Worker bob got task 9
Worker steve got task 10
Worker john got task 11
Worker bob got task 12
Worker steve got task 13
Worker john got task 14
Worker bob got task 15
Worker steve got task 16
Worker john got task 17
Worker bob got task 18
Assigned all work in interaction 2
Worker steve got task 19
Quitting time!
Quitting time!
Quitting time!

In [8]:     
```
better example to understand how blocking queue impacts:

```python

In [10]: def main(): 
    ...:     import gevent 
    ...:     import random 
    ...:     from gevent.queue import Queue, Empty 
    ...:     tasks = Queue(maxsize=3) 
    ...:     def worker(name): 
    ...:         try: 
    ...:             while True: 
    ...:                 task = tasks.get(timeout=1) 
    ...:                 print('Worker %s got task %s' % (name, task)) 
    ...:                 gevent.sleep(random.randint(1,3)) 
    ...:                 gevent.sleep(0) 
    ...:         except Empty: 
    ...:             print('Quitting time!') 
    ...:     def boss(): 
    ...:         for i in range(1,10): 
    ...:             print('boss waiting to put work {}'.format(i)) 
    ...:             tasks.put(i) 
    ...:         print('assigned all work') 
    ...:         for i in range(10,20): 
    ...:             print('boss waiting to put work {}'.format(i)) 
    ...:             tasks.put(i) 
    ...:         print('Assigned all work in interaction 2') 
    ...:     gevent.joinall([ 
    ...:         gevent.spawn(boss), 
    ...:         gevent.spawn(worker,'steve'), 
    ...:         gevent.spawn(worker, 'john'), 
    ...:         gevent.spawn(worker, 'bob'), 
    ...:         ]) 
    ...:                                                                                              

In [11]: main()                                                                                       
boss waiting to put work 1
boss waiting to put work 2
boss waiting to put work 3
boss waiting to put work 4
Worker steve got task 1
Worker john got task 2
Worker bob got task 3
boss waiting to put work 5
boss waiting to put work 6
boss waiting to put work 7
Worker steve got task 4
boss waiting to put work 8
Worker john got task 5
boss waiting to put work 9
Worker bob got task 6
Worker steve got task 7
assigned all work
boss waiting to put work 10
boss waiting to put work 11
Worker john got task 8
boss waiting to put work 12
Worker steve got task 9
boss waiting to put work 13
Worker bob got task 10
boss waiting to put work 14
Worker steve got task 11
boss waiting to put work 15
Worker john got task 12
boss waiting to put work 16
Worker steve got task 13
boss waiting to put work 17
Worker bob got task 14
boss waiting to put work 18
Worker john got task 15
boss waiting to put work 19
Worker steve got task 16
Assigned all work in interaction 2
Worker john got task 17
Worker steve got task 18
Worker bob got task 19
Quitting time!
Quitting time!
Quitting time!
```


### 13 - gevents Events, and AsynResult

```python
import gevent
from gevent.event import Event

evt = Event()

def setter():
    ''' after 3 seconsd wake all the threads, waiting on evt'''

    print('A : wait, doin sumthin')
    gevent.sleep(3)
    print('DOne now!')
    evt.set()

def waiter():
    print('Will wait for you bro')
    evt.wait()
    print('its about time')

def main():
    gevent.joinall([
        gevent.spawn(setter),
        gevent.spawn(waiter),
        gevent.spawn(waiter),
        gevent.spawn(waiter)
        ])

if __name__ == '__main__': main()
```

```python
import gevent
from gevent.event import AsyncResult
a = AsyncResult()
b = AsyncResult()
c = AsyncResult()

def setter():
    gevent.sleep(3)

    a.set('Hello!')
    print(c.get())

def waiter():
    x = a.get()
    b.set(x)

def waiter2():
    print(b.get())
    c.set('World')

gevent.joinall([
    gevent.spawn(setter),
    gevent.spawn(waiter),
    gevent.spawn(waiter2)
])
```

### 12 - Monkey patching with gevents

```python
import socket
print(socket.socket)


print("Aftermonkey ")
from gevent import monkey
monkey.patch_socket()
print(socket.socket)


import select
print(select.select)
monkey.patch_select()
print("After monkey patch")
print(select.select)

```
```
<class 'socket.socket'>
Aftermonkey 
<class 'gevent._socket3.socket'>
<built-in function select>
After monkey patch
```

### 11 - gevent Timeout

```python
import gevent
from gevent import Timeout


seconds = 10

timeout = Timeout(seconds)
timeout.start()


def wait():
    gevent.sleep(10)


try:
    gevent.spawn(wait).join()
except Timeout:
    print('Could not complete')
```

```python
import gevent
from gevent import Timeout

time_to_wait = 5

class TooLong(Exception):
    pass

with Timeout(time_to_wait, TooLong):
    gevent.sleep(10)
```

```python
import gevent
from gevent import Timeout

def wait():
    gevent.sleep(2)


timer = Timeout(1).start()
thread1 = gevent.spawn(wait)


try:
    thread1.join(timeout=timer)
except Timeout:
    print('Thread 1 timed out')

timeer = Timeout.start_new(1)
thread2 = gevent.spawn(wait)

try:
    thread2.get(timeout=timer)
except Timeout:
    print('Thread 2 timed out')

try:
    gevent.with_timeout(1, wait)
except Timeout:
    print('Thread 3 timed out')
```

### 10 - gevent.kill

```python
import gevent
import signal

def run_forever():
    gevent.sleep(1000)


if __name__ == '__main__':
    gevent.signal(signal.SIGQUIT, gevent.kill)
    thread = gevent.spawn(run_forever)
    thread.join()
```

```python
import gevent
from gevent import Timeout

time_to_wait = 5

class TooLong(Exception):
    pass


with Timeout(time_to_wait, TooLong):
    gevent.sleep(10)
```


### 9 - exceptions in greenlets

- stacktrace is stopped inside greenlet themselves

```python
import gevent

def win():
    return 'you win'

def fail():
    raise Exception('You fail at failing')


winner = gevent.spawn(win)
loser = gevent.spawn(fail)

print(winner.started) 
print(loser.started)

try:
    gevent.joinall([winner, loser])
except Exception as e:
    #exceptions raised in greenlets stay inside greenlets? why?
    # that's why it won't reach here!
    print('This will never be reached')


print(winner.value)
print(loser.value)

print(winner.ready())
print(loser.ready())

print(winner.successful())
print(loser.successful())

print(loser.exception)

print(loser.get())
```

### 8 - Creating Greenlets for gevent

```python
import gevent
from gevent import Greenlet


def foo(message,n):
    gevent.sleep(n)
    print(message)


thread1 = Greenlet.spawn(foo, "Hello", 1)
thread2 = gevent.spawn(foo, "I live!", 2)
thread3 = gevent.spawn(lambda x :print (x+1) ,2 )
threads = [thread1, thread2, thread3]

gevent.joinall(threads)
```

- subclassing Greenlet
```python
import gevent
from gevent import Greenlet


class MyGreenlet(Greenlet):


    def __init__(self, message, n ):
        Greenlet.__init__(self)
        self.message = message
        self.n = n

    #overriding
    def _run(self):
        print(self.message)
        gevent.sleep(self.n)


g = MyGreenlet("Hi there!", 3 )
g.start()
g.join()
```





### 7 - Using partials

```python
In [21]: def derivAt(f, x, dx): 
    ...:     return (f(x+dx) - f(x))/dx 
    ...:                                                                        

In [22]: def deriv(f,dx): 
    ...:     def d(x): 
    ...:         return derivAt(f,x,dx) 
    ...:     return d 
    ...:                                                                        

In [23]: derivOfSquare(square, 0.00001) #returns a function with predefined function and h value   
```
```python

In [27]: def deriv(f,dx): 
    ...:     return lambda x : derivAt(f,x,dx) 
    ...:     
In [30]: derivOfSquare= deriv( lambda x: x*x , 0.0001) 
```


### 6 - Write your own square root function

```python

In [12]:  
    ...: def sqroot(n , eps ,mx): 
    ...:    x = 1.0 
    ...:    itr = 0 
    ...:    while abs( x*x - n ) > eps and itr < mx: 
    ...:       x = x - (x*x-n)/2*x 
    ...:       itr = itr + 1 
    ...:    return x 
    ...:     
    ...:     
    ...:     
    ...:                                                                        

In [13]: sqroot(2,0.0001, 10)                                                   
Out[13]: 1.3351578377717581

In [14]: sqroot(2,0.0001, 100)                                                  
Out[14]: 1.3801553432658384

In [15]: sqroot(2,0.0001, 1000)                                                 
Out[15]: 1.403003973690669

In [16]: sqroot(2,0.0001, 10000)                                                
Out[16]: 1.4106685607006662

In [17]: sqroot(2,0.0001, 100000)                                               
Out[17]: 1.4130943389174646

In [18]: sqroot(2,0.0001, 10000000)                                             
Out[18]: 1.4141017458848133
```
   

### 5 - Multiple inheritence differs between 2 and 3

```python

Python3 : 
In [6]: class A(): 
   ...:     def foo1(self): 
   ...:         print( "A") 
   ...: class B(A): 
   ...:     def foo2(self): 
   ...:         pass 
   ...: class C(A): 
   ...:     def foo1(self): 
   ...:         print( "C" ) 
   ...: class D(B, C): 
   ...:     pass 
   ...:  
   ...: d = D() 
   ...: d.foo1()                                                                
C
```

Python2 :
```python
In [2]: class A():
   ...:     def foo1(self):
   ...:         print "A"
   ...: class B(A):
   ...:     def foo2(self):
   ...:         pass
   ...: class C(A):
   ...:     def foo1(self):
   ...:         print "C"
   ...: class D(B, C):
   ...:     pass
   ...: 
   ...: d = D()
   ...: d.foo1()
   ...: 
A
```

### 4 - Class variable

```python
class Test():  
    num_of_instance = 0  
    def __init__(self, name):  
        self.name = name  
        Test.num_of_instance += 1  
  
if __name__ == '__main__':  
    print (Test.num_of_instance)   # 0
    t1 = Test('jack')  
    print (Test.num_of_instance )  # 1
    t2 = Test('lucy')  
    print (t1.name , t1.num_of_instance)  # jack 2
    print (t2.name , t2.num_of_instance ) # lucy 2
```

```python
class Person:
    name="aaa"

p1=Person()
p2=Person()
p1.name="bbb"
print (p1.name)  # bbb
print (p2.name)  # aaa
print (Person.name)  # aaa

## so counter intituive 

class Person:
    name=[]

p1=Person()
p2=Person()
p1.name.append(1)
print (p1.name)  # [1]
print (p2.name)  # [1]
print (Person.name)  # [1]
```

### 3 - method types example

```python
def foo(x):
    print "executing foo(%s)"%(x)

class A():
    def foo(self,x):
        print( "executing foo(%s,%s)"%(self,x))

    @classmethod
    def class_foo(cls,x):
        print( "executing class_foo(%s,%s)"%(cls,x))

    @staticmethod
    def static_foo(x):
        print( "executing static_foo(%s)"%x)

a=A()

a.foo('bar')
A.class_foo('bar')
A.static_foo('bar')
foo('bar')
```

- static method don't have access to cls

### 2 - Seemingly weird

- Immutables and Mutables can behave quite differently
- How can I combine id and python inspection capability to map state of python interpreter; to help me see scope changes and other stuff better?

```python
Python 3.6.6 (default, Sep 12 2018, 18:26:19) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> a = 1
>>> def Foo(a):
...     a = 2
... 
>>> Foo(a)
>>> a
1
>>> b = []
>>> def Foo(b):
...     b.append(1)
... 
>>> Foo(b)
>>> b
[1]
>>> 
```



- https://stackoverflow.com/questions/633127/viewing-all-defined-variables

```python
>>> from pprint import pprint
>>> pprint(vars())
{'__annotations__': {},
 '__builtins__': <module 'builtins' (built-in)>,
 '__doc__': None,
 '__loader__': <class '_frozen_importlib.BuiltinImporter'>,
 '__name__': '__main__',
 '__package__': None,
 '__spec__': None,
 'pprint': <function pprint at 0x7f4c0e8b7598>}
>>> pprint(dir())
['__annotations__',
 '__builtins__',
 '__doc__',
 '__loader__',
 '__name__',
 '__package__',
 '__spec__',
 'pprint']
>>> pprint(globals())
{'__annotations__': {},
 '__builtins__': <module 'builtins' (built-in)>,
 '__doc__': None,
 '__loader__': <class '_frozen_importlib.BuiltinImporter'>,
 '__name__': '__main__',
 '__package__': None,
 '__spec__': None,
 'pprint': <function pprint at 0x7f4c0e8b7598>}
>>> pprint(locals())
{'__annotations__': {},
 '__builtins__': <module 'builtins' (built-in)>,
 '__doc__': None,
 '__loader__': <class '_frozen_importlib.BuiltinImporter'>,
 '__name__': '__main__',
 '__package__': None,
 '__spec__': None,
 'pprint': <function pprint at 0x7f4c0e8b7598>}
>>> 
```



### 1 - Some tricks with list,set and maps

- from [here](https://github.com/taizilongxu/interview_python)

- unique without set directly
```python
>>> l1 = ['b','c','d','b','c','a','a']
>>> l2 = {}.fromkeys(l1).keys()
>>> print( l2)
dict_keys(['b', 'c', 'd', 'a'])
>>> 
```

- Maintaining order
```python
>>> l1 = ['b','c','d','b','c','a','a']
>>> l2 = list(set(l1))
>>> l2
['d', 'c', 'b', 'a']
>>> l2.sort(key=l1.index)
>>> l2
['b', 'c', 'd', 'a']
>>> 
```

- doing unique using list comprehension
```python
>>> l1 = ['b', 'c' , 'd' , 'b', 'c', 'a', 'a']
>>> l2 = []
>>> [ l2.append(i) for i in l1 if not i in l2 ]
[None, None, None, None]
>>> l2
['b', 'c', 'd', 'a']
>>> 
```
- from keys
```python
>>> dict1={}.fromkeys(('x','y'),-1)
>>> dict={'x':-1,'y':-1}
>>> dict2={}.fromkeys(('x','y'))
>>> dict2={'x':None, 'y':None}
>>> dict
{'x': -1, 'y': -1}
>>> dict1
{'x': -1, 'y': -1}
>>> dict2
{'x': None, 'y': None}
>>> 
```
