# 02-jan-2021

### 1 - counting balanced paranthesis

https://sahandsaba.com/interview-question-generating-all-balanced-parentheses.html

```python
def count_balanced(n):
    table = [1]
    for j in range(1, n + 1):
        result = 0
        for i in range(j):
            x = table[i]
            y = table[j - i - 1]
            result += x * y
        table.append(result)
    return table[n]
```

cooler iterative algo, it relates to how we generate next number in our number systems
```python
def get_balanced_iterative(n):

    s = ["("] * n + [")"] * n

    while True:
        yield "".join(s)

        o, c = 0, 0

        for i in range(1, 2 * n):
            if s[-i] == "(":
                o += 1
                if c > o:
                    s[-i:] = [")"] + ["("] * o + [")"] * (c - 1)
                    break
            else:
                c += 1


G = get_balanced_iterative(5)

for i in range(1, 10):
    print(next(G))
```

counting operations per string
```python
def balanced_iterative_operations(n):

    T, C = 0, 0

    s = ["("] * n + [")"] * n

    while True:

        C += 1
        o, c = 0, 0

        for i in range(1, 2 * n + 1):

            if s[-i] == "(":
                o += 1
                if c > o:
                    T += i
                    s[-i:] = [")"] + ["("] * o + [")"] * (c - 1)
                    break
            else:
                c += 1
        if o == n:
            T += 2 * n
            break
    return T, C


for n in range(1, 20):
    T, C = balanced_iterative_operations(n)
    print(n, T, C, T / C)
```




