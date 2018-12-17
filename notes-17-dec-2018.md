# 17-dec-2018

### 1 - pampy

- seems like a very useful library

```python
Python 3.6.7 (default, Oct 22 2018, 11:32:17) 
Type 'copyright', 'credits' or 'license' for more information
IPython 7.1.1 -- An enhanced Interactive Python. Type '?' for help.

In [1]: from pampy import match, _                                                                                                                                                                                                            

In [2]: input = [1,2,3]                                                                                                                                                                                                                       

In [3]: pattern = [1,2,_]                                                                                                                                                                                                                     

In [4]: action = lambda x: "it's {}".format(x)                                                                                                                                                                                                

In [5]: match(input, pattern, action)                                                                                                                                                                                                         
Out[5]: "it's 3"

In [6]:            
```
