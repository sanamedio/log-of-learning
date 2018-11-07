# 08-nov-2018

### 1 - Cyclomatic complexity with radon

- https://en.wikipedia.org/wiki/Cyclomatic_complexity
- ```pip install radon```

Code with high cyclometic complexity:
```python
#old.py
class Bird(object):
  name = ''
  flightless = False
  extinct = False

  def get_speed(self):
    if self.extinct:
      return -1 # we do not care about extinct bird speeds
    else:
      if self.flightless:
        if self.name == 'Ostrich':
          return 15
        elif self.name == 'Chicken':
          return 7
        elif self.name == 'Flamingo':
          return 8
        else:
          return -1 # bird name not implemented
      else:
        if self.name == 'Gold Finch':
          return 12
        elif self.name == 'Bluejay':
          return 10
        elif self.name == 'Robin':
          return 14
        elif self.name == 'Hummingbird':
          return 16
        else:
          return -1 # bird not implemented
```
output with radon:
```bash
$ python -m radon cc -s old.py
old.py
    C 1:0 Bird - B (10)
    M 6:2 Bird.get_speed - B (10)
```

Refactored new code with low cyclomatic complexity:
```python
#new.py
class Bird(object):
  name = ''
  flightless = False
  extinct = False

  def get_speed(self):
    raise NotImplementedError

class Robin(Bird):
  name = 'Robin'

  def get_speed(self):
    return 14

class GoldFinch(Bird):
  name = 'Gold Finch'

  def get_speed(self):
    return 12

class Ostrich(Bird):
  name = 'Ostrich'
  flightless = True

  def get_speed(self):
    return 15

class Pterodactyl(Bird):
  name = 'Pterodactyl'
  extinct = True

  def get_speed(self):
    return -1
```
Output of radon on new code:
```bash
$ python -m radon cc -s new.py
new.py
    C 1:0 Bird - A (1)
    M 6:2 Bird.get_speed - A (1)
    C 9:0 Robin - A (1)
    M 12:2 Robin.get_speed - A (1)
    C 15:0 GoldFinch - A (1)
    M 18:2 GoldFinch.get_speed - A (1)
    C 21:0 Ostrich - A (1)
    M 25:2 Ostrich.get_speed - A (1)
    C 28:0 Pterodactyl - A (1)
    M 32:2 Pterodactyl.get_speed - A (1)
```
