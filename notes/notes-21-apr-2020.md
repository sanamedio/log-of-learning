# 21-apr-2020

### 9 - walrus operator with list comprehension

```python
>>> letters = list('this is to produce a list of letters')
>>> letters
['t', 'h', 'i', 's', ' ', 'i', 's', ' ', 't', 'o', ' ', 'p', 'r', 'o', 'd', 'u', 'c', 'e', ' ', 'a', ' ', 'l', 'i', 's', 't', ' ', 'o', 'f', ' ', 'l', 'e', 't', 't', 'e', 'r', 's']
>>> import random
>>> vowels = [letter.upper() for _ in range(0, 10) if (letter := random.choice(letters)) in list('aeoui')]
>>> vowels
['I', 'O', 'O', 'O', 'O']
```

### 8 - .closed for file

```python
>>> with open(".bash_profile") as f:
...     pass
...
>>> f.closed
True
>>>
```

### 7 - why isinstance over type

```python
>>> def check_type(number):
...     if type(number) == int:
...         print('do something with an int')
...     if isinstance(number, (int, float)):
...         print('do something with an int or float')
... 
>>> check_type(5)
do something with an int
do something with an int or float
>>> check_type(4.2)
do something with an int or float
```

### 6 - passing functions into max

```python
>>> winnings = [ 'j', 'b', 'b', 's', 'b', 'j']
>>> max( set(winnings), key = winnings.count)
'b'
>>> max((winnings), key = winnings.count)
'b'
>>>

>>> model_scores = {'model_a': 100, 'model_z': 198, 'model_t': 150}
>>> # workaround
>>> keys, values = list(model_scores.keys()), list(model_scores.values())
>>> keys[values.index(max(values))]
'model_z'
>>> # one-line
>>> max(model_scores, key=model_scores.get)
'model_z'
```


### 5 - isdisjoint with set and use of filter

[source](https://medium.com/better-programming/30-simple-tricks-to-level-up-your-python-coding-5b625c15b79a)

```python
>>> def good_word(x: str):
...     has_vowels = not set('aeiou').isdisjoint(x.lower())
...     long_enough = len(x) > 7
...     good_start = x.lower().startswith('pre')
...     return has_vowels & long_enough & good_start
... 
>>> words = ['Good', 'Presentation', 'preschool', 'prefix']
>>> list(filter(good_word, words))
['Presentation', 'preschool']
```

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

>>> a = ['j', 'a', 'k', 'd', 'c']
>>> if (n := len(a))%2 == 1:
...     print(f'The number of letters is {n}, which is odd.')
...
The number of letters is 5, which is odd.

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
