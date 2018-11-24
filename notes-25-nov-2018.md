# 25-nov-2018

### 1 - random number generators

- http://eternallyconfuzzled.com/tuts/algorithms/jsw_tut_rand.aspx
- random number generators

```python
#linear congruential generator

def lcg(seed):
    return (2*seed + 3 ) % 10



if __name__ == '__main__':
    seed = 5

    for i in range(10):
        print(seed)
        seed = lcg(seed)

```


```python
# minimal stanndard genrator
M = 2147483647
A = 16807
Q = M // A
R = M % A

seed = 1

def l_rand():
    global seed
    seed = A * ( seed % Q ) - R * (seed // Q )

    if seed <= 0:
        seed += M

    return seed


if __name__ == '__main__':
    for i in range(10):
        print(l_rand())
```

```
#dual phase linear congruenctial generator
M1 = 2147483647
M2 = 2147483399
A1 = 40015
A2 = 40692
Q1 = M1 // A1
Q2 = M2 // A2
R1 = M1 % A1
R2 = M2 % A2


seed1 = 1
seed2 = 1

# dual phase linear congurnecial generator


def l_rand():
    global seed1,seed2
    seed1 = A1 * ( seed1 % Q1) - R1 * (seed1 // Q1)
    seed2 = A2 * (seed2 % Q2) - R2 * ( seed2 // Q2)

    if seed1 <= 0:
        seed1 += M1
    if seed2 <= 0:
        seed2 += M2

    result = seed1 - seed2

    if result < 1:
        result += M1 - 1

    return result

if __name__ == '__main__':
    for i in range(100):
        print(l_rand())
```


