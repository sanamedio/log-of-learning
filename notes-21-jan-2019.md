# 21-jan-2019


### 1 - probability simulations!

```python
import random

def roll():
    return random.randrange(1,7)
    
def consecutive_roll(X):
    A = X[0]
    B = X[1]
    a = roll()
    b = roll()
    cnt = 1
    while not ( a == A and b == B ):
        a = b
        b = roll()
        cnt = cnt + 1
    return cnt

def simulate( num , f , args ):
   return sum( [ f(args) for x in range(num) ])*1.0/num

if __name__ == '__main__':

    print(simulate( 100000, consecutive_roll, (5,6) ))
    print(simulate( 100000, consecutive_roll, (5,5) ))
```

- the answer looks a little weird; why they have to be same
