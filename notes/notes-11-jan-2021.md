# 11-jan-2021

### 1 - converting recursion to stack

https://codeforces.com/topic/49210/

```python
def factorial(n):

    s = []

    s.append([n, "CALL"])
    RESULT = None

    while s:
        data, action = s.pop()
        if action == "CALL":
            n = data
            if n == 1:
                RESULT = 1
            else:
                s.append([n, "RESUME"])
                s.append([n - 1, "CALL"])
        elif action == "RESUME":
            n = data
            fact = n * RESULT
            RESULT = fact

    print(RESULT)


factorial(5)
```
