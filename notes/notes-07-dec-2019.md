# 07-dec-2019

### 2 - Sorting when element is at max K-place deranged

```python

## check how to implement a priority queue correctly with logk time complexity
class SortedQueue:
  
  q = None
  
  def __init__(self):
    self.q = []
  
  def size(self):
    return len(self.q)
  
  def insert(self,v):
    self.q.append(v)
    self.q = list(sorted(self.q))
    
  def extractMin(self):
    x = self.q[0]
    self.q = self.q[1:]
    return x
  






def sort_k_messed_array(arr, k):
  n = len(arr)
  if n <= k: 
    return list(sorted(arr))
  
  
  window = SortedQueue() 
  
  for i in range(0,k+1):
    window.insert(arr[i])
    
    
  result = []
  # did mistake here first of taking K
  for i in range(k+1,n):
    
    if window.size() >0 :
      result.append(window.extractMin())
    
    window.insert(arr[i])
    
  while window.size() > 0:
    result.append(window.extractMin())
  
  return result
  
```

### 1 - threadlocal in python

[Threadlocal storage in Python](https://stackoverflow.com/questions/1408171/thread-local-storage-in-python)

[Good explanation from Java](http://tutorials.jenkov.com/java-concurrency/threadlocal.html)

```python
import threading
userName = threading.local()

def SessionThread(userName_in):
    userName.val = userName_in
    print(userName.val)   

Session1 = threading.Thread(target=SessionThread("User1"))
Session2 = threading.Thread(target=SessionThread("User2"))
Session1.start()
Session2.start()
Session1.join()
Session2.join()
```
