# 23-nov-2018

# 1 - Typing usage

```python
from typing import List

Vector = List[float]
Matrix = List[Vector]

def addMatrix(a : Matrix, b : Matrix) -> Matrix:
  result = []
  for i,row in enumerate(a):
    result_row =[]
    for j, col in enumerate(row):
      result_row += [a[i][j] + b[i][j]]
    result += [result_row]
  return result

x = [[1.0, 0.0], [0.0, 1.0]]
y = [[2.0, 1.0], [0.0, -2.0]]

z = addMatrix(x, y)
print(z)
```
