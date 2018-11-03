# 03-nov-2018

### 4 - Python classes are dynamic

- change in class, reflects in alreaady created instances

```python
>>> class Class:
...   def one(self):
...     return 1
... 
>>> c=Class()
>>> c.one()
1
>>> def two(self):
...   return 2
... 
>>> Class.two=two
>>> c.two()
2
>>> Class.three=lambda self:3
>>> c.three()
3
>>> Class.one=lambda self:'New One.'
>>> c.one()
'New One.'
```

### 3 - itertools combination(similar for Pn)

```python
>>> from itertools import combinations
 
>>> teams = ["Packers", "49ers", "Ravens", "Patriots"]
>>> for game in combinations(teams, 2):
...     print game
 
>>> ('Packers', '49ers')
>>> ('Packers', 'Ravens')
>>> ('Packers', 'Patriots')
>>> ('49ers', 'Ravens')
>>> ('49ers', 'Patriots')
>>> ('Ravens', 'Patriots')
```

### 2 - curses in python for terminal draw

```python
import sys,os
import curses

def draw_menu(stdscr):
    k = 0
    cursor_x = 0
    cursor_y = 0

    # Clear and refresh the screen for a blank canvas
    stdscr.clear()
    stdscr.refresh()

    # Start colors in curses
    curses.start_color()
    curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

    # Loop where k is the last character pressed
    while (k != ord('q')):

        # Initialization
        stdscr.clear()
        height, width = stdscr.getmaxyx()

        if k == curses.KEY_DOWN:
            cursor_y = cursor_y + 1
        elif k == curses.KEY_UP:
            cursor_y = cursor_y - 1
        elif k == curses.KEY_RIGHT:
            cursor_x = cursor_x + 1
        elif k == curses.KEY_LEFT:
            cursor_x = cursor_x - 1

        cursor_x = max(0, cursor_x)
        cursor_x = min(width-1, cursor_x)

        cursor_y = max(0, cursor_y)
        cursor_y = min(height-1, cursor_y)

        stdscr.move(cursor_y, cursor_x)

        # Refresh the screen
        stdscr.refresh()

        # Wait for next input
        k = stdscr.getch()

def main():
    curses.wrapper(draw_menu)

if __name__ == "__main__":
    main()
```

### 1 - platform module

```python
import platform
print(platform.architecture())
print(platform.python_version())
print(platform.uname())
```
- https://docs.python.org/2/library/platform.html


