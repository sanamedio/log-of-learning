# 13-jan-2019

### 2 - pycuber

- nice library to manipulate rubic cube.
- need to keep it for later use in a solver https://github.com/adrianliaw/PyCuber
```python
Python 3.6.7 (default, Oct 22 2018, 11:32:17) 
[GCC 8.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import pycuber as pc
>>> mycube = pc.Cube()
>>> print(mycube)
         [y][y][y]
         [y][y][y]
         [y][y][y]
[r][r][r][g][g][g][o][o][o][b][b][b]
[r][r][r][g][g][g][o][o][o][b][b][b]
[r][r][r][g][g][g][o][o][o][b][b][b]
         [w][w][w]
         [w][w][w]
         [w][w][w]

>>> mycube("R U R' U'")
>>> print(mycube)
         [y][y][r]
         [y][y][g]
         [y][y][g]
[b][r][r][g][g][w][o][o][y][b][o][o]
[r][r][r][g][g][y][b][o][o][b][b][b]
[r][r][r][g][g][g][y][o][o][b][b][b]
         [w][w][o]
         [w][w][w]
         [w][w][w]

>>> 
```


### 1 - uninstalling things with pip

- When you do multiple pip uninstalls; they remove packages from multiple places. In order to delete a package completely; keep doing it until it does not show any new uninstall
