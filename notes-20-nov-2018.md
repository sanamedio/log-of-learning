# 20-nov-2018

### 3 - Rx python

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
