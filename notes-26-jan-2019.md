# 26-jan-2019

### 4 - websockets and asyncio

```python
#!/usr/bin/env python3

# WS server that sends messages at random intervals

import asyncio
import datetime
import random
import websockets

async def time(websocket, path):
    while True:
        now = datetime.datetime.utcnow().isoformat() + 'Z'
        await websocket.send(now)
        await asyncio.sleep(random.random() * 3)

start_server = websockets.serve(time, '127.0.0.1', 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
```

```html
<!DOCTYPE html>
<html>
    <head>
        <title>WebSocket demo</title>
    </head>
    <body>
        <script>
            var ws = new WebSocket("ws://127.0.0.1:5678/"),
                messages = document.createElement('ul');
            ws.onmessage = function (event) {
                var messages = document.getElementsByTagName('ul')[0],
                    message = document.createElement('li'),
                    content = document.createTextNode(event.data);
                message.appendChild(content);
                messages.appendChild(message);
            };
            document.body.appendChild(messages);
        </script>
    </body>
</html>
```


### 3 - websockets at lower level

```python
#!/usr/bin/env python

import socket, threading, time

def handle(s):
  print repr(s.recv(4096))
  s.send('''
HTTP/1.1 101 Web Socket Protocol Handshake\r
Upgrade: WebSocket\r
Connection: Upgrade\r
WebSocket-Origin: http://localhost:8888\r
WebSocket-Location: ws://localhost:9876/\r
WebSocket-Protocol: sample
  '''.strip() + '\r\n\r\n')
  time.sleep(1)
  s.send('\x00hello\xff')
  time.sleep(1)
  s.send('\x00world\xff')
  s.close()

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(('', 9876));
s.listen(1);
while 1:
  t,_ = s.accept();
  threading.Thread(target = handle, args = (t,)).start()
```


```html
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
  <head>
    <title>Web Socket Example</title>
    <meta charset="UTF-8">
    <script>
      window.onload = function() {
        var s = new WebSocket("ws://localhost:9876/");
        s.onopen = function(e) { alert("opened"); }
        s.onclose = function(e) { alert("closed"); }
        s.onmessage = function(e) { alert("got: " + e.data); }
      };
    </script>
  </head>
    <body>
      <div id="holder" style="width:600px; height:300px"></div>
    </body>
</html>
```


### 2 - websocketd send-receive

- data can be both sent and received over websocketd from and to python to browser

```python
#!/usr/bin/python
from sys import stdout,stdin
from time import sleep

# Count from 1 to 10 with a sleep
for count in range(0, 10):
  line = stdin.readline().strip()
  while len(line) == 0:
    line = stdin.readline().strip()
 
  print(count + 1,line)
  stdout.flush()
  sleep(0.1)
```

```html
<!DOCTYPE html>
<html>
  <head>
    <title>websocketd count example</title>
    <style>
      #count {
        font: bold 150px arial;
        margin: auto;
        padding: 10px;
        text-align: center;
      }
    </style>
  </head>
  <body>
    
    <div id="count"></div>
    
    <script>
      var ws = new WebSocket('ws://localhost:8080/');
      ws.onopen = function() {
        document.body.style.backgroundColor = '#cfc';
	ws.send("hello onopen\n")
      };
      ws.onclose = function() {
        document.body.style.backgroundColor = null;
	ws.send("hello onclone\n")
      };
      ws.onmessage = function(event) {
        document.getElementById('count').textContent = event.data;
	ws.send("hello onmessage\n");
      };
    </script>
    
  </body>
</html>
```

### 1 - websocketd

- can be used to communicate between any webpage and a local program
- http://websocketd.com/

```python
#!/usr/bin/python
from sys import stdout
from time import sleep

# Count from 1 to 10 with a sleep
for count in range(0, 10):
  print(count + 1)
  stdout.flush()
  sleep(0.5)
```

```js
var ws = new WebSocket('ws://localhost:8080/');

ws.onmessage = function(event) {
  console.log('Count is: ' + event.data);
};
```

```bash
$ websocketd --port=8080 ./my-program 
Sat, 26 Jan 2019 17:29:11 +0530 | INFO   | server     |  | Serving using application   : ./my-program 
Sat, 26 Jan 2019 17:29:11 +0530 | INFO   | server     |  | Starting WebSocket server   : ws://kuroop-Lenovo-G580:8080/
Sat, 26 Jan 2019 17:29:15 +0530 | ACCESS | session    | url:'http://localhost:8080/' id:'1548503955611529129' remote:'127.0.0.1' command:'./my-program' origin:'http://websocketd.com' | CONNECT
Sat, 26 Jan 2019 17:29:21 +0530 | ACCESS | session    | url:'http://localhost:8080/' id:'1548503955611529129' remote:'127.0.0.1' command:'./my-program' origin:'http://websocketd.com' pid:'821' | DISCONNECT
```

```html
<!DOCTYPE html>
<html>
  <head>
    <title>websocketd count example</title>
    <style>
      #count {
        font: bold 150px arial;
        margin: auto;
        padding: 10px;
        text-align: center;
      }
    </style>
  </head>
  <body>
    
    <div id="count"></div>
    
    <script>
      var ws = new WebSocket('ws://localhost:8080/');
      ws.onopen = function() {
        document.body.style.backgroundColor = '#cfc';
      };
      ws.onclose = function() {
        document.body.style.backgroundColor = null;
      };
      ws.onmessage = function(event) {
        document.getElementById('count').textContent = event.data;
      };
    </script>
    
  </body>
</html>
```
