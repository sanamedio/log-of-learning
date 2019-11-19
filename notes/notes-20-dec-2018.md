# 20-dec-2018

### 2 - colored terminal output in IDLE

```python
import sys


try: color = sys.stdout.shell
except AttributeError: raise RuntimeError("use IDLE")


color.write("hi, asdasd", "KEYWORD")
color.write("No\n", "COMMENT")
```

- The "Colors" you can put are: SYNC, stdin, BUILTIN, STRING, console, COMMENT, stdout, TODO, stderr, hit, DEFINITION, KEYWORD, ERROR, and sel.
- IDLE is a popular python IDE

### 1 - fibonacci over tcp socket

- exposing a simple fibonacci function over a TCP socket 
- from this talk : https://www.youtube.com/watch?v=MCs5OvhV9S4&amp=&feature=share

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
Threaded server to support multiple clients:
```python
from socket import *
from threading import Thread

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
        Thread( target= fib_handler, args=(client,),).start()



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
testing time per request:
```python
from socket import *
import time



sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('localhost', 25000))



while True:
    start =time.time()
    sock.send(b'30')
    resp = sock.recv(100)
    end = time.time()
    print(end-start)

```

testing req per second:
```python

## calculating requests per second

from socket import *
import time
from threading import Thread


sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('localhost', 25000))


n = 0




def monitor():
    global n
    while True:
        time.sleep(1)
        print(n,'req/sec')
        n = 0 


Thread(target=monitor).start()


while True:
    sock.send(b'1')
    resp = sock.recv(100)
    n += 1    
```





