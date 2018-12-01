# 02-dec-2018 


### 1 - secrets

- In particularly, secrets should be used in preference to the default pseudo-random number generator in the random module, which is designed for modelling and simulation, not security or cryptography.

```
Python 3.6.7 (default, Oct 22 2018, 11:32:17) 
Type 'copyright', 'credits' or 'license' for more information
IPython 7.1.1 -- An enhanced Interactive Python. Type '?' for help.

In [1]: import secrets                                                                                             

In [2]: import string                                                                                              

In [3]: alphabet = string.ascii_letters + string.digits                                                            

In [4]: alphabet                                                                                                   
Out[4]: 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

In [5]: password = ''.join(secrets.choice(alphabet)  for i in range(10))                                           

In [6]: password                                                                                                   
Out[6]: 'cnXRWUqt2M'

In [7]: import random                                                                                              

In [8]: ''.join(random.choice(alphabet) for i in range(10))                                                        
Out[8]: 'JeCHRZPt6t'

In [9]:  
```
