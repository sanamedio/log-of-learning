# 09-dec-2018



### 3 - Matplotlib subplots for plotting multiple data

```python
# https://matplotlib.org/tutorials/introductory/sample_plots.html#sphx-glr-tutorials-introductory-sample-plots-py
import matplotlib.pyplot as plt
import numpy as np

np.random.seed(19233232)
data = np.random.randn(2,100)


fig, axs = plt.subplots(2,2, figsize=(5,5))

axs[0,0].hist(data[0])
axs[1,0].scatter(data[0],data[1])
axs[0,1].plot(data[0],data[1])
axs[1,1].hist2d(data[0],data[1])

plt.show()
```


### 2 - Different interpolation methods in matplotlib

- from https://matplotlib.org/gallery/images_contours_and_fields/interpolation_methods.html

```python
import matplotlib.pyplot as plt
import numpy as np

methods = [None, 'none', 'nearest', 'bilinear', 'bicubic', 'spline16',
           'spline36', 'hanning', 'hamming', 'hermite', 'kaiser', 'quadric',
           'catrom', 'gaussian', 'bessel', 'mitchell', 'sinc', 'lanczos']

# Fixing random state for reproducibility
np.random.seed(19680801)

grid = np.random.rand(4, 4)

fig, axs = plt.subplots(nrows=3, ncols=6, figsize=(9.3, 6),
                        subplot_kw={'xticks': [], 'yticks': []})

fig.subplots_adjust(left=0.03, right=0.97, hspace=0.3, wspace=0.05)

for ax, interp_method in zip(axs.flat, methods):
    ax.imshow(grid, interpolation=interp_method, cmap='viridis')
    ax.set_title(str(interp_method))

plt.tight_layout()
plt.show()
```

### 1 - visualizing sorts using matplotlib nearest imshow

```python
import  matplotlib.pyplot as plt
from pprint import pprint
import random

def shellSort(arr):

    n = len(arr)
    gap = n//2
    ppp = [list(arr)]

    while gap > 0:

        for i in range(gap,n):

            temp = arr[i]

            j = i
            while  j >= gap and arr[j-gap] >temp:
                arr[j] = arr[j-gap]
                j -= gap

            arr[j] = temp
            ppp+= [list(arr)]
        gap //= 2
    plt.imshow(ppp, interpolation='nearest', cmap='gist_heat')
    plt.show()


def selectionSort(A):
    arr = A 
    ppp = [list(arr)]
    for i in range(len(A)): 

        min_idx = i 
        for j in range(i+1, len(A)): 
            if A[min_idx] > A[j]: 
                min_idx = j

        A[i], A[min_idx] = A[min_idx], A[i]
        ppp += [list(arr)]
    plt.imshow(ppp, interpolation='nearest' , cmap='gist_heat')
    plt.show()




def bubbleSort(arr):


    ppp = [list(arr)]

    n = len(arr)

    for i in range(n):

        for j in range(0, n-i-1): 

            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

        ppp += [ list(arr) ]

    plt.imshow(ppp, interpolation='nearest' , cmap='gist_heat')
    plt.show()



def insertionSort(arr):

    ppp = [list(arr)]
    for i in range(1, len(arr)): 

        key = arr[i]  

        j = i-1
        while j >=0 and key < arr[j] : 
            arr[j+1] = arr[j] 
            j -= 1
        arr[j+1] = key 
        ppp += [ list(arr) ]
    #pprint(ppp)    
    plt.imshow(ppp,interpolation='nearest',cmap='gist_heat')
    plt.show()

arr = [ float(random.random()) for x in range(100) ]
shellSort(arr)
for i in range(len(arr)):
    print "%f" %arr[i], 
```

