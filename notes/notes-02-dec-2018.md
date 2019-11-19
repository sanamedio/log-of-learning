# 02-dec-2018 

### 5 - Scatterplot with animation frames

- from here https://stackoverflow.com/a/9416663

```python
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

def main():
    numframes = 100
    numpoints = 10
    color_data = np.random.random((numframes, numpoints))
    x, y, c = np.random.random((3, numpoints))

    fig = plt.figure()
    scat = plt.scatter(x, y, c=c, s=100)

    ani = animation.FuncAnimation(fig, update_plot, frames=xrange(numframes),
                                  fargs=(color_data, scat))
    plt.show()

def update_plot(i, data, scat):
    scat.set_array(data[i])
    return scat,

main()
```
- another example from https://stackoverflow.com/a/32276219

```python
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

dt = 0.005
n=20
L = 1
particles=np.zeros(n,dtype=[("position", float , 2),
                            ("velocity", float ,2),
                            ("force", float ,2),
                            ("size", float , 1)])

particles["position"]=np.random.uniform(0,L,(n,2));
particles["velocity"]=np.zeros((n,2));
particles["size"]=0.5*np.ones(n);

fig = plt.figure(figsize=(7,7))
ax = plt.axes(xlim=(0,L),ylim=(0,L))
scatter=ax.scatter(particles["position"][:,0], particles["position"][:,1])

def update(frame_number):
    particles["force"]=np.random.uniform(-2,2.,(n,2));
    particles["velocity"] = particles["velocity"] + particles["force"]*dt
    particles["position"] = particles["position"] + particles["velocity"]*dt

    particles["position"] = particles["position"]%L
    scatter.set_offsets(particles["position"])
    return scatter,

anim = FuncAnimation(fig, update, interval=10)
plt.show()
```


### 4 - Visualizing random numbers in 2d with scatter plot

```python

In [34]: import numpy as np                                                                                        

In [35]: import matplotlib.pyplot as plt                                                                           

In [36]: import random                                                                                             

In [37]: x = [ random.random() for x in range(500) ]                                                               

In [38]: y = [ random.random() for t in range(500) ]                                                               

In [39]: plt.scatter(x, y)                                                                                         
Out[39]: <matplotlib.collections.PathCollection at 0x7f4b0a5607b8>

In [40]: plt.show()                                                                                                

In [41]:  
```


### 3 - Matplotlib visualizing 2d arrays

- plt.imshow is good way to visualize large matrixes as it color codes magnitude

```python
Python 3.6.7 (default, Oct 22 2018, 11:32:17) 
Type 'copyright', 'credits' or 'license' for more information
IPython 7.1.1 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import  matplotlib.pyplot  as plt                                                                          

In [2]: x = [ [1,2,3],[1,2,3], [1,2,3]]                                                                            

In [3]: plt.plot(x)                                                                                                
Out[3]: 
[<matplotlib.lines.Line2D at 0x7f4ac1221f60>,
 <matplotlib.lines.Line2D at 0x7f4ac122e0f0>,
 <matplotlib.lines.Line2D at 0x7f4ac122e240>]

In [4]: plt.show()                                                                                                 

In [5]: plt.imshow(x)                                                                                              
Out[5]: <matplotlib.image.AxesImage at 0x7f4b0959c0b8>

In [6]: plt.show()                                                                                                 

In [7]: x = [ [1,2,3], [4,5,6], [7,8,9]]                                                                           

In [8]: plt.imshow(x)                                                                                              
Out[8]: <matplotlib.image.AxesImage at 0x7f4b094a4eb8>

In [9]: plt.show()                                                                                                 

In [10]:  

```

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

```python
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
