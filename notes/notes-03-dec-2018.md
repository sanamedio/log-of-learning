# 03-dec-2018

# 3 - Animating using turtle

- from here https://www.daniweb.com/programming/software-development/code/465422/turtle-random-fun-python

```python
''' turtle_star_sky101.py
use Python's turtle module to fill a dark sky with stars
modified to work with Python27 and Python33  by  vegaseat
'''
import turtle as tu
import random as rn
def draw_star(x, y, color, side):
    tu.color(color)
    tu.begin_fill()
    tu.penup()
    tu.goto(x, y)
    tu.pendown()
    for k in range(5):
        tu.forward(side)
        tu.right(144)
        tu.forward(side)
    tu.end_fill()
def random_length():
    return rn.randrange(5, 25)
def random_xy_coord():
    return rn.randrange(-290, 290), rn.randrange(-270, 270) 
tu.title('a star filled sky')
tu.bgcolor('black')
# optional ('normal' is default) ...
# values for speed are 'fastest' (no delay), 'fast', (delay 5ms),
# 'normal' (delay 10ms), 'slow' (delay 15ms), 'slowest' (delay 20ms)
tu.speed('fastest')
colors = ['red', 'orange', 'magenta', 'green', 'blue', 'yellow', 'white']
# number of stars you want to show
stars = 50
for k in range(stars):
    color = rn.choice(colors)
    side = random_length()  # length of side
    x, y  = random_xy_coord()
    draw_star(x, y, color, side)
# keep showing until window corner x is clicked
tu.done()
```

# 2 - modulus and floor div with python

- from here : https://luminousmen.com/post/7

```python
>>> -12 % 10
8
>>> -12 // 10
-2
>>> -12 / 10
-1.2
>>> 
```

# 1 - default argument initialization

- always gets me into thinking otherwise; quite unintiutive at first

```python
>>> def extendList(val, l = [] ):
...     l.append(val)
...     return l
... 
>>> list1 = extendList(10)
>>> list2 = extendList(123,[])
>>> list3 = extendList('a')
>>> list1,list2,list3
([10, 'a'], [123], [10, 'a'])
>>> 
```

