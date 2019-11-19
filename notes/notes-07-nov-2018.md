# 07-nov-2018

### 6- Little theory on pandas

- Pandas is a library for data analysis - ingesting, cleaning, manipulating and writing data.
- Numpy is for numerical crunching and matrix manipulation at fairly low level.
- Matplotlib is for plotting graphs.
- Tools for reading and writing data between in-memory data structures and different formats: CSV and text files, Microsoft Excel, SQL databases, and the fast HDF5 format
- Highly optimized for performance, with critical code paths written in Cython or C.

### 5 - pandas input and output

```python

#pd is pandas
#df is a DataFrame object

pd.read_csv(filename) # From a CSV file
pd.read_table(filename) # From a delimited text file (like TSV)
pd.read_excel(filename) # From an Excel file
pd.read_sql(query, connection_object) # Reads from a SQL table/database
pd.read_json(json_string) # Reads from a JSON formatted string, URL or file.
pd.read_html(url) # Parses an html URL, string or file and extracts tables to a list of dataframes
pd.read_clipboard() # Takes the contents of your clipboard and passes it to read_table()
pd.DataFrame(dict) # From a dict, keys for columns names, values for data as lists

df.to_csv(filename) # Writes to a CSV file
df.to_excel(filename) # Writes to an Excel file
df.to_sql(table_name, connection_object) # Writes to a SQL table
df.to_json(filename) # Writes to a file in JSON format
df.to_html(filename) # Saves as an HTML table
df.to_clipboard() # Writes to the clipboard
```

### 4 - matplotlib with pandas

```python
import matplotlib.pyplot as plt
```

```python
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
```

```python
plt.plot([1,2,3,4])
plt.ylabel('some numbers')
plt.show()
```

```python
In [10]: plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
Out[10]: [<matplotlib.lines.Line2D at 0x7ff1f9c24550>]

In [11]: plt.show()
```

```python
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10,4),index=pd.date_range('1/1/2000',
   periods=10), columns=list('ABCD'))

df.plot()
plt.show()
```

```python
#bar plot
df = pd.DataFrame(np.random.rand(10,4),columns=['a','b','c','d')
df.plot.bar()
plt.show()
```

```python
## histogramms
In [32]: import pandas as pd
    ...: import numpy as np
    ...: 
    ...: df=pd.DataFrame({'a':np.random.randn(1000)+1,'b':np.random.randn(
    ...: 1000),'c':
    ...: np.random.randn(1000) - 1}, columns=['a', 'b', 'c'])
    ...: 
    ...: df.diff().hist(bins=20)
    ...: 
Out[32]: 
array([[<matplotlib.axes._subplots.AxesSubplot object at 0x7ff1f98153d0>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x7ff1f9792110>],
       [<matplotlib.axes._subplots.AxesSubplot object at 0x7ff1f97bae90>,
        <matplotlib.axes._subplots.AxesSubplot object at 0x7ff2017c2c50>]],
      dtype=object)

In [33]: plt.show()
```

```python
In [34]: import pandas as pd
    ...: import numpy as np
    ...: df = pd.DataFrame(np.random.rand(50, 4), columns=['a', 'b', 'c', 
    ...: 'd'])
    ...: df.plot.scatter(x='a', y='b')
    ...: 
Out[34]: <matplotlib.axes._subplots.AxesSubplot at 0x7ff2016de610>

In [35]: plt.show()
```



### 3 - pandas panel ( 3D )

```python
# from random 3d array
import pandas as pd
import numpy as np

data = np.random.rand(2,4,5)
p = pd.Panel(data)
print p
```

```python
#creating an empty panel
import pandas as pd
import numpy as np

data = {'Item1' : pd.DataFrame(np.random.randn(4, 3)), 
        'Item2' : pd.DataFrame(np.random.randn(4, 2))}
p = pd.Panel(data)
print p
```

```python
#creating an empty panel
import pandas as pd
p = pd.Panel()
print p
```

```python
#from dataframes
import pandas as pd
import numpy as np
data = {'Item1' : pd.DataFrame(np.random.randn(4, 3)), 
        'Item2' : pd.DataFrame(np.random.randn(4, 2))}
p = pd.Panel(data)
print p['Item1']
```

```python
import pandas as pd
import numpy as np
data = {'Item1' : pd.DataFrame(np.random.randn(4, 3)), 
        'Item2' : pd.DataFrame(np.random.randn(4, 2))}
p = pd.Panel(data)
print p.major_xs(1)
print p.minor_xs(1)
```




### 2 - pandas dataframe ( 2D )

```python
#empty
import pandas as pd
df = pd.DataFrame()
print df
```

```python
data = [1,2,3,4,5]
df = pd.DataFrame(data)
print df
```

```python
data = [['Alex',10],['Bob',12],['Clarke',13]]
df = pd.DataFrame(data,columns=['Name','Age'])
print df
```

```python
data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data)
print df
```

```python
data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data, index=['rank1','rank2','rank3','rank4'])
print df
```

```python
data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data)
print df
```

```python
data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data, index=['first', 'second'])
```

```python
import pandas as pd

d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
      'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print df
```

```python
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
      'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
```

```python
#column addition
import pandas as pd

d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
      'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)

# Adding a new column to an existing DataFrame object with column label by passing new series

print ("Adding a new column by passing as Series:")
df['three']=pd.Series([10,20,30],index=['a','b','c'])
print df

print ("Adding a new column using the existing columns in DataFrame:")
df['four']=df['one']+df['three']

print df
```

```python
import pandas as pd

d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']), 
     'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print df.loc['b']

print df.iloc[2] # selection by index location
```

```python
import pandas as pd

df = pd.DataFrame([[1, 2], [3, 4]], columns = ['a','b'])
df2 = pd.DataFrame([[5, 6], [7, 8]], columns = ['a','b'])

df = df.append(df2)

# Drop rows with label 0
df = df.drop(0)

print df
```


print df ['one']



### 1 - pandas series ( 1D )

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







