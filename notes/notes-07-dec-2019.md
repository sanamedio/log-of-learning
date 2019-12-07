# 07-dec-2019


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
