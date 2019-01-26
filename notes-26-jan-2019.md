# 26-jan-2019


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
