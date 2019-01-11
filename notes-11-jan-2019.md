# 11-jan-2019


### 1 - primality test

- K is degree of accuracyish , and N is the number whose primality test one wants to do. Higher the K, the better the accuracy

```python
import random
  
def primality(N,K):
    rs = [ random.randrange(1,N) for x in range(K) ] 
    return all([ pow(a,N-1)%N == 1 for a in rs])

if __name__ == '__main__':

    while True:
        N,K =  map ( int , input().split())
        print(primality(N,K))
```
