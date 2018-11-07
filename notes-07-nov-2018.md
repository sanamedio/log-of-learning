# 07-nov-2018

### 1 - Pandas

```python
#empty series in pandas
import pandas as pd
s = pd.Series()
print s
```

```python
#create a series from numpy array
import pandas as pd
import numpy as np
data = np.array(['a','b','c','d'])
s = pd.Series(data)
print s
```

```python
#providing indexes to series
import pandas as pd
import numpy as np
data = np.array(['a','b','c','d'])
s = pd.Series(data,index=[100,101,102,103])
print s
```

```python
# dict to series
data = {'a' : 0., 'b' : 1., 'c' : 2.}
s = pd.Series(data)
```

```python
# custom indexes to dict to series
data = {'a' : 0., 'b' : 1., 'c' : 2.}
s = pd.Series(data,index=['b','c','d','a'])
```

```python
#creating series fro ma scalar
s = pd.Series(5, index=[0, 1, 2, 3])
```

```python
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])

#retrieve the first element
print s[0]


#retrieve the first three element
print s[:3]

retrieve a single element
print s['a']


#retrieve multiple elements
print s[['a','c','d']]
```







