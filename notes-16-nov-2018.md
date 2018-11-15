# 16-nov-2018

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
