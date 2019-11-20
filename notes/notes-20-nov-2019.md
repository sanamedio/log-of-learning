# 20-nov-2019

### 3 - turtle animation of sine

- took basics from here https://learn.wecode24.com/animation-with-turtle-graphics/

```python3
import turtle
from math import pi, sin as sine


screen = turtle.Screen()
screen.setup(800,600)
screen.tracer(0)            
don = turtle.Turtle()
don.speed(0)
don.width(5)
don.hideturtle()            





def draw_sine(start_angle):
    screen.setworldcoordinates(0, -1.25, 2 * pi, 1.25)
    angle = 0.0 
    don.penup()
    don.goto(angle,sine(angle+start_angle))
    don.pendown()
    
    while angle < 2*pi :
        don.goto(angle, sine(angle+start_angle))
        angle += 0.05
    don.penup()

angle = 0.0

import time


while True :
    draw_sine(angle)
    screen.update()
    angle += 0.01
    time.sleep(0.05)
    don.clear()
```




### 2 - Diagnosing memory leaks using guppy

- https://chase-seibert.github.io/blog/2013/08/03/diagnosing-memory-leaks-python.html

```bash
pip install guppy3
```

```python3
from guppy import hpy
hp = hpy()
before = hp.heap()

print("Hello world") # do some memory intensive stuff, not hello world 

after = hp.heap()
leftover = after - before
import pdb; pdb.set_trace()

(Pdb) leftover.bytype
Partition of a set of 28 objects. Total size = 4148 bytes.
 Index  Count   %     Size   % Cumulative  % Type
     0      8  29     1664  40      1664  40 dict
     1      2   7      840  20      2504  60 types.FrameType
     2      6  21      408  10      2912  70 tuple
     3      5  18      398  10      3310  80 str
     4      1   4      368   9      3678  89 _sre.SRE_Pattern
     5      1   4      144   3      3822  92 types.CodeType
     6      1   4      136   3      3958  95 SyntaxError
     7      2   7      112   3      4070  98 guppy.etc.Glue.Owner
     8      2   7       78   2      4148 100 bytes
```





### 1 - Dumping process's memory

- https://serverfault.com/questions/173999/dump-a-linux-processs-memory-to-file
```bash
#!/bin/bash

grep rw-p /proc/$1/maps \
| sed -n 's/^\([0-9a-f]*\)-\([0-9a-f]*\) .*$/\1 \2/p' \
| while read start stop; do \
    gdb --batch --pid $1 -ex \
        "dump memory $1-$start-$stop.dump 0x$start 0x$stop"; \
done
```


