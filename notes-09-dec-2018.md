# 09-dec-2018

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


def bubbleSort(arr):

    
	ppp = [arr]

	n = len(arr)
 
	for i in range(n):
 
		for j in range(0, n-i-1):
 
			if arr[j] > arr[j+1] :
				arr[j], arr[j+1] = arr[j+1], arr[j]

		ppp += [ list(arr) ]

	plt.imshow(ppp, interpolation='nearest' , cmap='gist_heat')
	plt.show()



def insertionSort(arr): 

	ppp = [arr]
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
bubbleSort(arr) 
for i in range(len(arr)): 
	print "%f" %arr[i], 
```
