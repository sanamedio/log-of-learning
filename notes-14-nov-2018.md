# 14-nov-2018

### 3 - SHA256 for subsequent bytes

```python
>>> hashlib.sha256(b'1').hexdigest()
'6b86b273ff34fce19d6b804eff5a3f5747ada4eaa22f1d49c01e52ddb7875b4b'
>>> hashlib.sha256(b'2').hexdigest()
'd4735e3a265e16eee03f59718b9b5d03019c07d8b6c51f90da3a666eec13ab35'
>>> hashlib.sha256(b'3').hexdigest()
'4e07408562bedb8b60ce05c1decfe3ad16b72230967de01f640b7e4729b49fce'
```

### 2 - Dunder import 

```python
Python 3.6.6 (default, Sep 12 2018, 18:26:19) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> __import__('IPython').embed()
Python 3.6.6 (default, Sep 12 2018, 18:26:19) 
Type 'copyright', 'credits' or 'license' for more information
IPython 7.1.1 -- An enhanced Interactive Python. Type '?' for help.

In [1]: ls                                                                                                                                            
Desktop/	 Downloads/   Music/	  Public/	 Documents/	 Pictures/   __pycache__/	 

In [2]: #in IPython shell                                                                                                                             
```

### 1 - Floating point errors!

```python
Python 3.6.6 (default, Sep 12 2018, 18:26:19) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> [0.1] * 10
[0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
>>> sum( [0.1]*10)
0.9999999999999999
>>> import math
>>> math.fsum([0.1]*10)
1.0
>>> 
```
