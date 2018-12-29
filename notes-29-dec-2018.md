# 29-dec-2018

## 2 - building list of factors in inefficient way

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

## 1 - negative numbers python

- infinite precision causes it to not act like a normal 32-bit negative

```python
bin(-1+(1<<32))
#'0b11111111111111111111111111111111'

bin(-1)
#'-0b1'
```
