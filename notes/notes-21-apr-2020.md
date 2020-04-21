# 21-apr-2020

### 4 - new walrus operator for inline assignment

```python
Python 3.8.0 (default, Apr 21 2020, 09:37:48)
[Clang 11.0.0 (clang-1100.0.33.16)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> if x:= 0:
...     print(x)
...
>>>
>>> if x := 9:
...     print(x)
...
9
>>>
```

### 3 - providing more than one input to map

```python
>>> numbers = (1, 2, 4, 6)
>>> indices = (2, 1, 0.5, 2)
>>> # use map()
>>> list(map(pow, numbers, indices))
[1, 2, 2.0, 36]
>>> # list comprehensions
>>> [pow(x, y) for x, y in zip(numbers, indices)]
[1, 2, 2.0, 36]
```

### 2 - embedding conditional in print

```python
>>> for i in range(5):
...     print(i, end=', ' if i < 4 else '\n')
... 
0, 1, 2, 3, 4
>>> for i in range(5):
...     print(f'{i} & {i*i}', end=', ' if i < 4 else '\n')
... 
0 & 0, 1 & 1, 2 & 4, 3 & 9, 4 & 16
```

### 1 - zip in python

If you zip the zipped, it returns the original

```python
>>> students = ('John', 'Mary', 'Mike')
>>> ages = (15, 17, 16)
>>> scores = (90, 88, 82, 17, 14)
>>> for student, age, score in zip(students, ages, scores):
...     print(f'{student}, age: {age}, score: {score}')
... 
John, age: 15, score: 90
Mary, age: 17, score: 88
Mike, age: 16, score: 82
>>> zipped = zip(students, ages, scores)
>>> a, b, c = zip(*zipped)
>>> print(b)
(15, 17, 16)
```
