# 20-nov-2018

### 4 - Decorator for argument typechecking

```python
def check_arguments(*deco_args):
    def wrapper(f):
        def inner(*args):
            for t,a in zip(deco_args,args):
                print(t,a)
                if not isinstance(a,t):
                    raise AssertionError("Check arguments")
            r = f(args)
            return r
        return inner
    return wrapper


def check_return(t):
    def wrapper(f):
        def inner(*args):
            r = f(args)
            if not isinstance(r,t):
                raise AssertionError("Check return value")
            return r
        return inner
    return wrapper


@check_arguments(int,str)
def hello(*args):
    print ("the arguments are fine")
    return 1

@check_return(str)
def hello2(*args):
    print ("the same function for checking return")
    return 1


if __name__ == '__main__':
    hello(1,'hello')
    hello2(1,'hello')
```

### 3 - Rx python

```python
In [25]: from sqlalchemy import create_engine, text                                                      

In [26]: from rx import Observable                                                                       

In [27]: engine = create_engine('sqlite:///test.db')                                                     

In [28]: conn = engine.connect()                                                                         

In [29]: def customer_for_id(customer_id): 
    ...:     stmt = text("SELECT * FROM CUSTOMER WHERE CUSTOMER_ID = :id") 
    ...:     return Observable.from_(conn.execute(stmt, id=customer_id)) 
    ...:                                     

In [31]: Observable.of(1,3,5) \ 
    ...:     .flat_map(lambda id: customer_for_id(id)) \ 
    ...:     .subscribe(lambda r: print(r))                                                              
(1, 'loki')
(3, 'loki3')
Out[31]: <rx.disposables.anonymousdisposable.AnonymousDisposable at 0x7fb10f1c7630>

In [32]: Observable.of(1,3,5) \ 
    ...:     .flat_map(lambda id: customer_for_id(id)) \ 
    ...:     .subscribe(lambda r: print(r))                                                              
(1, 'loki')
(3, 'loki3')
Out[32]: <rx.disposables.anonymousdisposable.AnonymousDisposable at 0x7fb1135ba7b8>
```


```python
In [19]: from rx import Observable                                                                       

In [20]: from random import randint                                                                      

In [21]: three_emissions = Observable.range(1,10)                                                        

In [22]: three_random_ints = three_emissions.map(lambda i: randint(1,10000)).publish().auto_connect(2)   

In [23]: three_random_ints.subscribe(lambda i: print("1 >> {}".format(i)))                               
Out[23]: <rx.disposables.anonymousdisposable.AnonymousDisposable at 0x7fb10f83ee48>

In [24]: three_random_ints.subscribe(lambda i: print("2 >> {}".format(i)))                               
1 >> 4679
2 >> 4679
1 >> 8771
2 >> 8771
1 >> 2499
2 >> 2499
1 >> 2937
2 >> 2937
1 >> 7743
2 >> 7743
1 >> 5035
2 >> 5035
1 >> 3552
2 >> 3552
1 >> 7478
2 >> 7478
1 >> 5886
2 >> 5886
1 >> 1772
2 >> 1772
Out[24]: <rx.disposables.anonymousdisposable.AnonymousDisposable at 0x7fb10f80a240>
```


```python
In [11]: from rx import Observable                                                                       

In [12]: from random import randint                                                                      

In [13]: three_emissions = Observable.range(1,3)                                                         

In [14]: three_random_ints = three_emissions.map(lambda i: randint(1,10000)).publish()                   

In [15]: three_random_ints.subscribe(lambda i: print("1 >> {}".format(i)))                               
Out[15]: <rx.disposables.anonymousdisposable.AnonymousDisposable at 0x7fb10f9355c0>

In [16]: three_random_ints.subscribe(lambda i: print("2 >> {}".format(i)))                               
Out[16]: <rx.disposables.anonymousdisposable.AnonymousDisposable at 0x7fb10f8e1828>

In [17]: three_random_ints.connect()                                                                     
1 >> 9016
2 >> 9016
1 >> 964
2 >> 964
1 >> 2683
2 >> 2683
Out[17]: <rx.disposables.compositedisposable.CompositeDisposable at 0x7fb10f8e17b8>

In [18]:  
```



```python
In [3]: from rx import Observable                                                                        

In [4]: from random import randint                                                                       

In [5]: three_emissions = Observable.range(1,3)                                                          

In [6]: three_random_ints = three_emissions.map(lambda i: randint(1,10000))                              

In [7]: three_random_ints.subscribe(lambda i: print("1 >> {}".format(i)))                                
1 >> 1085
1 >> 3997
1 >> 4460
Out[7]: <rx.disposables.anonymousdisposable.AnonymousDisposable at 0x7fb10f9784a8>

In [8]: three_random_ints.subscribe(lambda i: print("2 >> {}".format(i)))                                
2 >> 9907
2 >> 7866
2 >> 7957
Out[8]: <rx.disposables.anonymousdisposable.AnonymousDisposable at 0x7fb10f95f7f0>

In [9]:  

```


```python
Python 3.6.6 (default, Sep 12 2018, 18:26:19) 
Type 'copyright', 'credits' or 'license' for more information
IPython 7.1.1 -- An enhanced Interactive Python. Type '?' for help.

In [1]: from rx import Observable                                                                        

In [2]: Observable.interval(1000)                                                                        
Out[2]: <rx.core.anonymousobservable.AnonymousObservable at 0x7f69926ec6d8>

In [3]: Observable.interval(1000).map(lambda i: "{} loki".format(i))                                     
Out[3]: <rx.core.anonymousobservable.AnonymousObservable at 0x7f6991e93eb8>

In [4]: Observable.interval(1000).map(lambda i: "{} loki".format(i)).subscribe(lambda s: print(s))       
Out[4]: <rx.disposables.anonymousdisposable.AnonymousDisposable at 0x7f6993ff6cf8>

0 loki
1 loki
2 loki
3 loki
4 loki
5 loki
6 loki
7 loki
8 loki
In [5]:                                                                                                  
Do you really want to exit ([y]/n)? 9 loki
10 loki
y
```


```python
from rx import Observable

Observable.of("Alpha", "Beta", "Gamma", "Delta", "Epsilon") \
    .map(lambda s: len(s)) \
    .filter(lambda i: i >= 5) \
    .subscribe(lambda value: print("Received {0}".format(value)))
```

```python
from rx import Observable

source = Observable.of("adfgdfgdfgd","bdfgdfgdfg", "c")

lengths = source.map(lambda s: len(s))

filtered = lengths.filter(lambda i : i>= 5)


filtered.subscribe(lambda value: print("{}".format(value)))
```

```python
from rx import Observable

source  = Observable.of("alpha", "beta", "gamma", "delta" , "eps")


source.subscribe(lambda value: print("recieve {}".format(value)))


```


```python
from rx import Observable


source = Observable.of("Aplha", "beta", "gamma" , "delta", "eps")


source.subscribe(on_next=lambda value: print("received {}".format(value)),
                 on_completed=lambda :print("Done"),
                 on_error=lambda error:print("erro occured {}".format(error)))

```

```python
from rx import Observable, Observer

def push_five_strings(observer):

    observer.on_next("Alpha")
    observer.on_next("Beta")
    observer.on_next("Gamma")
   
    import time
    if int(time.time())%2 == 0 : #to show exceptions randomly between multiple runs
        raise Exception
    observer.on_next("Delta")
    observer.on_next("Delta")
    observer.on_next("Epsilon")
    observer.on_completed()




class PrintObserver(Observer):

    def on_next(self, value):
        print("Received {}".format(value))


    def on_completed(self):
        print("Done!")

    def on_error(self, error):
        print("erropr Occured: {}".format(error))


source = Observable.create(push_five_strings)

source.subscribe(PrintObserver())

```

```python
from rx import Observable, Observer

class PrintObserver(Observer):

    def on_next(self, value):
        print("Received {}".format(value))



    def on_completed(self):
        print("done!")

    def on_error(self, error):
        print("Error {}".format(error))



source = Observable.of("Alpha", "Beta", "Gamma", "delta", "epsilon")

source.subscribe(PrintObserver())
```




### 2 - websockets

```python
#server.py
import asyncio
import websockets

async def echo(websocket,path):
    async for message in websocket:
        print(message)
        await websocket.send(message)

asyncio.get_event_loop().run_until_complete(
        websockets.serve(echo, 'localhost', 8765))

asyncio.get_event_loop().run_forever()
```

```python
import asyncio
import websockets


async def hello(uri):
    async with websockets.connect(uri) as websocket:
        await websocket.send("hello world")
        await websocket.recv()


asyncio.get_event_loop().run_until_complete(
        hello('ws://localhost:8765'))
```

### 1 - visualizing python object space with json

- firefox renders json nicely
- expose a nested object created from python dir() output to a certain depth using flask

```python
## crappy code starts, need to work on writing better 
def visit_node__(node,parent, depth, spaces ):

    if depth == 0 :
        return {}

    else: 
        if len(set([parent,node]) & set(['dd_g_','dd_','visit_node__', 'flag__','expose_api__'])) >0 :
            return None
        print(spaces*" ", parent, " -> ", node ) 
        dd_ = {}
        try:
            for x in eval('dir(' + node + ')'):
                dd_[str(x)] = visit_node__(x,node, depth -1 , spaces + 1)
        except:
            pass
        finally:
            return dd_
    return None

from flask import Flask
app = Flask(__name__)


@app.route('/')
def expose_api__():
    from flask import jsonify
    return jsonify(dd_g_)

if __name__ == '__main__':
   
    global flag__
    flag__= set()
    global dd_g_
    dd_g_ = {}

    for x in eval('dir()'):
        dd_g_[x] = visit_node__(x ,"root",depth=10,spaces=1)

    import json


#    with open("test.json", 'w') as t:
#        json.dump(dd_g_,t )

    app.run()
```
