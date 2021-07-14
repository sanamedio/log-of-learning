# 14-jul-2021

### 2 - fakeuseragent

simplified library to fake user agents

```python
import requests
from fake_useragent import UserAgent
ua = UserAgent()
header = {'User-Agent':str(ua.chrome)}
response = requests.get(url, headers=header)
```

### 1 - nth multiple in fibonacci

[link](https://www.geeksforgeeks.org/nth-multiple-number-fibonacci-series/)

```python
def findPosition(k, n):
    f1 = 0
    f2 = 1
    i = 2;
    while i != 0:
        f3 = f1 + f2;
        f1 = f2;
        f2 = f3;
 
        if f2 % k == 0:
            return n * i
 
        i += 1
         
    return
 
# This code is contributed
```
