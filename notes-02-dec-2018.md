# 02-dec-2018 


### 2 - drawing a simple graph 0->1->2->3 using networkx


```python
In [1]: import networkx as nx                                                                                                               

In [2]: import matplotlib.pyplot as plt                                                                                                     

In [3]: G = nx.path_graph(4)                                                                                                                

In [4]: print(G.nodes())                                                                                                                    
[0, 1, 2, 3]

In [6]: print(G.edges())                                                                                                                    
[(0, 1), (1, 2), (2, 3)]

In [7]: nx.draw(G)                                                                                                                          
/home/whishworks/.local/lib/python3.6/site-packages/networkx/drawing/nx_pylab.py:611: MatplotlibDeprecationWarning: isinstance(..., numbers.Number)
  if cb.is_numlike(alpha):

In [8]: plt.show()                                                                                                                          
```

a better example:
```python
import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)
G.add_node(7)
G.add_node(9)

G.add_edge(1,2)
G.add_edge(3,1)
G.add_edge(2,4)
G.add_edge(4,1)
G.add_edge(9,1)
G.add_edge(1,7)
G.add_edge(2,9)


nx.draw(G,with_labels=True)
plt.show()
```

### 1 - secrets

- In particularly, secrets should be used in preference to the default pseudo-random number generator in the random module, which is designed for modelling and simulation, not security or cryptography.

```
Python 3.6.7 (default, Oct 22 2018, 11:32:17) 
Type 'copyright', 'credits' or 'license' for more information
IPython 7.1.1 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import secrets                                                                                             

In [2]: import string                                                                                              

In [3]: alphabet = string.ascii_letters + string.digits                                                            

In [4]: alphabet                                                                                                   
Out[4]: 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

In [5]: password = ''.join(secrets.choice(alphabet)  for i in range(10))                                           

In [6]: password                                                                                                   
Out[6]: 'cnXRWUqt2M'

In [7]: import random                                                                                              

In [8]: ''.join(random.choice(alphabet) for i in range(10))                                                        
Out[8]: 'JeCHRZPt6t'

In [9]:  
```
