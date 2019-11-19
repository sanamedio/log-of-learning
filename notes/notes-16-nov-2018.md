# 16-nov-2018

### 3 - Rotation of 2d matrix

```python
clockwise = zip(*original[::-1])
c_clockwise = zip(*original)[::-1]
```

### 2 - combinations yielding

```python
In [1]: def combinations(n,seq): #n size combinations from a seq 
   ...:     if n  == 0 :
   ...:         yield ()
   ...:     elif len(seq) == 0:
   ...:         pass
   ...:     else:
   ...:         first = seq[0]
   ...:         rest = seq[1:]
   ...:         for a in combinations(n, rest):
   ...:             yield a
   ...:         for a in combinations(n-1,rest): # invariant is that the length of your sequence should be n
   ...:             yield (first,) + a
   ...:             

In [2]: combinations(3,"abcde")
Out[2]: <generator object combinations at 0x7fba95092c80>

In [3]: g = combinations(3,"abcde")

In [4]: next(g)
Out[4]: ('c', 'd', 'e')

In [5]: next(g)
Out[5]: ('b', 'd', 'e')

In [6]: next(g)
Out[6]: ('b', 'c', 'e')

In [7]: next(g)
Out[7]: ('b', 'c', 'd')

In [8]: next(g)
Out[8]: ('a', 'd', 'e')

In [9]: next(g)
Out[9]: ('a', 'c', 'e')

In [10]: next(g)
Out[10]: ('a', 'c', 'd')

In [11]: 
```

### 1 - another twisted server 

- python3 byte change I guess has caused me to write bytify in order to send bytes to twisted

```python
from twisted.protocols import basic
from twisted.internet import protocol, reactor

def bytify(x):
    if x is None : return b''
    if isinstance(x,bytes): return x
    return bytes(x,'utf-8')


class HTTPEchoProtocol(basic.LineReceiver):
    def __init__(self):
        self.lines = []

    def lineReceived(self, line):
        self.lines.append(bytify(line))
        if not line:
            self.sendResponse()


    def sendResponse(self):
        self.sendLine(b"HTTP/1.1 200 OK")
        self.sendLine(b"")
        responseBody=  b"You said:\r\n\r\n" + b"\r\n".join(self.lines)
        self.transport.write(bytify(responseBody))
        self.transport.loseConnection()

class HTTPEchoFactory(protocol.ServerFactory):
    def buildProtocol(self, addr):
        return HTTPEchoProtocol()

reactor.listenTCP(8000, HTTPEchoFactory())
reactor.run()
```
