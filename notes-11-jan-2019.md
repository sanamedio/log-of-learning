# 11-jan-2019


### 1 - primality test

```python
import random
  
def primality(N,K):
    rs = [ random.randrange(1,N) for x in range(K) ] 
    if all([ pow(a,N-1)%N == 1 for a in rs]):
        return True
    else:
        return False

if __name__ == '__main__':

    while True:
        N,K =  map ( int , input().split())
        print(primality(N,K))
```
