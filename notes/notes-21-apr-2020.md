# 21-apr-2020

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
