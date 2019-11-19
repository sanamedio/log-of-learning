# 13-nov-2018


### 4 - How to connect to ngrok when firewall is interfering?

- ngrok exposes local ports to public IPs through the central ngrok server
- Tor can work behind the firewall
- How to reach to ngrok through a tor connection ?
- We can configure python to use the privproxy which is in turn using tor. But how to make tor make request there?
- Okay, it respects http_proxy env variable, so directly it can be passed. ( need to test)
- How to write a service like ngrok?
  - Need a publically exposed system
  - That system will accept connections and redirect them on random ports
- How to write something like Tor?
  - How tor works?
    - Multiple layers of encryption
    - Multiple nodes running the application
    - Bouncing of data between nodes
    - Establish a chain of nodes, and use it for sommetime. 
      - Where to store information about chain? Who will know the chain?
      - Does it mean every packet which gets initiated, contains data about all the nodes on the circuit?
      - Does it mean that information of Tor nodes is available to the tor browser?
      - Does it really matter if tor nodes become public known?
        - I think it doesn't work in that way
      - It will help to write a simple network simulator in python

```python
## Just trying my thinking, but what it means to write a Network simulator?
class NetworkNode:
       
       def __init__(self,ip,mac_adddress):
              self.ip = ip
              self.mac_address = mac_address
       
       def send_data_by_ip(self, target_ip):
              '''sends data to target_ip'''
              pass
       
       def send_data_by_mac(self, target_mac_address):
              '''sends data to target_mac_address'''
              pass
       
       def receive_data(self):
              '''reads one packet and returns that'''
              pass
       
```

### 3 - Tor using python

- https://gist.github.com/DusanMadar/8d11026b7ce0bce6a67f7dd87b999f6b

- Renewing Tor IP
```python
Python 3.6.6 (default, Sep 12 2018, 18:26:19) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from stem import Signal
>>> from stem.control import Controller
>>> with Controller.from_port(port=9051) as controller:
...     controller.authenticate()
...     controller.signal(Signal.NEWNYM)
... 
>>> 
```

```python
Python 3.6.6 (default, Sep 12 2018, 18:26:19) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import requests
>>> from stem import Signal
>>> from stem.control import Controller
>>> response = requests.get('http://icanhazip.com/', proxies={'http' : '127.0.0.1:8118' } )
>>> response.text.strip()
'204.85.191.30'
>>> with Controller.from_port(port=9051) as controller:
...     controller.authenticate(password='mypassword')
...     controller.signal(Signal.NEWNYM)
... 
>>> response = requests.get('http://icanhazip.com/' , proxies= {'http' : '127.0.0.1:8118' } )
>>> response.text.strip()
'66.70.217.179'
>>> 
```


### 2 - Plotly offline with Jupyter tutorial

- https://plot.ly/python/offline/

```python
from plotly import __version__
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

print __version__
import plotly.graph_objs as go

plot([go.Scatter(x=[1,2,3], y=[3,1,6])])

init_notebook_mode(connected=True)
iplot([{'x' : [1,2,3], 'y': [ 3,1,6]}])

import numpy as np

x = np.random.randn(2000)
y = np.random.randn(2000)

iplot([go.Histogram2dContour(x=x, y=y),
       go.Scatter(x=x, y=y)], show_link=False)

```

### 1 - Plotly offline interactive graphs

- https://github.com/SayaliSonawane/Plotly_Offline_Python

```python
import plotly
import numpy as np
from plotly.graph_objs import Layout,Scatter

N = 500
random_x = np.linspace(0, 1, N)
random_y = np.random.randn(N)

trace =Scatter(x = random_x,y=random_y)

plotly.offline.plot({ "data": [trace]})
```
