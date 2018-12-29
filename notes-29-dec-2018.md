# 29-dec-2018

### 4 - Modulus and deterministic functions of state

- any sequence which is based on some state data; like fibonacci depends on last two numbers of the sequence, would repeat over a modulus; In other words; in a modular world -> there are only so many states of all the variables and things start repeating after a certain point.

```python
# fibonacci modulus series with modulus M
a = 1
b = 1

M = 1000

setme = set()

for i in xrange(15001):
    c = (a + b)%M
    b = (a)%M


    if (c,b) not in setme:
        setme.add( (c,b))
    else:
        print(i)
        print("Repeating states now")
        break



    a = c

```

### 3 - two player optimal play

- The game is like there is a collection of sticks. At every turn a player can pick either 1 or 2 sticks. Two players are playing. from the base state and building a recursive game play; all the optimal moves can be reached.

```python
def test(k):
    if k<= 1:
        return False
    elif k == 2:
        return True
    elif k == 3:
        return True
    else:
        return not ( test(k-1) or test(k-2))



for k in xrange(100):
    print( k, test(k) )
```


### 2 - building list of factors in inefficient way

- http://www.codeabbey.com/index/task_view/integer-factorization
- should do faster with sieve, but this is fun too.

```python
x = int(raw_input())

l = [x]

didSomething = True


while didSomething :
    out = []
    didSomething=False
    for c in l:
        for i in range(2,(c+1)/2+1):
            if c%i == 0:
                didSomething=True
                out.append(c/i)
                out.append(i)
                break
        else:
            out.append(c)
                
    l = out

print(l)
```

### 1 - negative numbers python

- infinite precision causes it to not act like a normal 32-bit negative

```python
bin(-1+(1<<32))
#'0b11111111111111111111111111111111'

bin(-1)
#'-0b1'
```
