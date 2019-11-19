# 01-may-2019

### 3 - Locks with python-etcd3


On a key, a lock can be acquired. This can happen to coordinate between two separate nodes

start this first:-
```python
In [14]: etcd = etcd3.client()
    ...: 
    ...: # create a lock that expires after 20 seconds
    ...: with etcd.lock('toot', ttl=20) as lock:
    ...:     # do something that requires the lock
    ...:     print(lock.is_acquired())
    ...:     print("Hello ")
    ...:     # refresh the timeout on the lease
    ...:     import time;
    ...:     time.sleep(10)
    ...:     
    ...:     
    ...:     
    ...:     
True
Hello 
```

a moment later start this:-
```python
In [13]: import etcd3
    ...: 
    ...: etcd = etcd3.client()
    ...: 
    ...: # create a lock that expires after 20 seconds
    ...: with etcd.lock('toot', ttl=20) as lock:
    ...:     # do something that requires the lock
    ...:     print(lock.is_acquired())
    ...: 
    ...:     # refresh the timeout on the lease
    ...:     print("World")
    ...:     
    ...:     
True
World

```



### 2 - python with etcd - getting notified of key creation

etcd is distributed store, and used inside a kubernete cluster to keep distributed configs

- https://dzone.com/articles/apache-zookeeper-vs-etcd3
- https://coreos.com/etcd/docs/latest/learning/why.html
- https://github.com/kragniz/python-etcd3

Can create notification on key creation like this:-
```python3
import etcd3
import time

etcd = etcd3.client()

def testfunc(event):
    print event

watch_id = etcd.add_watch_callback("foo", testfunc, range_end="foo2")


while True:
    time.sleep(1)

```


start the callback server 
```
~$ python test.py
<class 'etcd3.events.PutEvent'> key=foo value=test
```

test it like:
```python3
In [3]: import etcd3

In [4]: etcd = etcd3.client()

In [5]: etcd.put("foo" , "asdas")
Out[5]: 
header {
  cluster_id: 14841639068965178418
  member_id: 10276657743932975437
  revision: 36
  raft_term: 2
}

```


### 1 - monotonic time in python

https://codeburst.io/why-shouldnt-you-trust-system-clocks-72a82a41df93

```python
Python 3.6.7 (default, Oct 22 2018, 11:32:17) 
[GCC 8.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import time
>>> time.monotonic
<built-in function monotonic>
>>> time.monotonic()
197735.477949047
>>> time.monotonic()
197736.922957192
>>> time.monotonic()
197737.817689814
>>>
```
