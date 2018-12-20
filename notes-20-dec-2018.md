# 20-dec-2018

### 1 - fibonacci over tcp socket

- exposing a simple fibonacci function over a TCP socket 

```python
from socket import *

def fib(n):
    if n == 0 or n == 1 :
        return 1
    else:
        return fib(n-1) + fib(n-2)


def fib_server(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1 )
    sock.bind(address)
    sock.listen(5)

    while True:
        client, addr = sock.accept()
        print("Connection" , addr)
        fib_handler(client)



def fib_handler(client):
    while True:
        req = client.recv(100)
        if not req:
            break
        n = int(req)
        result = fib(n)
        resp = str(result).encode('ascii') + b'\n'
        client.send(resp)
    print("closed")


fib_server(('',25000))
```

```bash
$ nc localhost 25000
3
3
```



