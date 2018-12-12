# 12-dec-2018

### 3 - knuth shuffle

```python

In [5]: def knuth_shuffle(items):
   ...:        for i in xrange(len(items)):
   ...:            j = randrange(i,len(items))
   ...:            items[i], items[j] = items[j], items[i]
   ...:        print items
   ...:        

In [6]: knuth_shuffle([1,2,3])
[2, 3, 1]

In [7]: 

```


### 2 - random number quiz 

- from here https://pynative.com/python-random-number-generation-exercise-questions-and-challenge/


```python
# numbers between 100 and 999 which are divisible by 5
In [1]: import random
In [2]: for num in xrange(3):
   ...:     print(random.randrange(100,999,5))
   ...:     
630
650
880
```

### 1 - tsne in python

- TSNE can help visualize high dimensional datasets and can make it easy to visually decode.
- Below example plots four points which are kindof nearly a plane in 3D but doing TSNE makes it easy to see that.

```python
In [1]: 

In [1]: import numpy as np

In [2]: from sklearn.manifold import TSNE

In [3]: X = np.array([[ 0,0,0 ] , [0,1,1], [1,0,1] , [1,1,1]])

In [4]: import matplotlib.pyplot as plt

In [5]: from mpl_toolkits.mplot3d import Axes3D

In [6]: fig = plt.figure()

In [7]: ax = fig.add_subplot(111, projection='3d')

In [8]: ax.scatter( X[:,0] , X[:,1] , X[:,2] )
Out[8]: <mpl_toolkits.mplot3d.art3d.Path3DCollection at 0x7f69eb9b8d90>

In [9]: plt.show()

In [10]: X_embedded = TSNE(n_components=2).fit_transform(X)

In [11]: plt.scatter(X_embedded[:,0], X_embedded[:,1])
Out[11]: <matplotlib.collections.PathCollection at 0x7f69eb07f290>

In [12]: plt.show()

In [13]: 
```
