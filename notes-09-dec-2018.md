# 09-dec-2018

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
