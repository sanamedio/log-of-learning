# 05-nov-2019

### 1 - bisect module is good replacement to lower_bound upper_bound

```python
Python 3.6.8 (default, Oct  7 2019, 12:59:55) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import bisect
>>> float_list = [ 1.0, 1.3, 2.3, 4.5 ] 
>>> bisect.bisect_left(float_list, 2.5)
3
>>> bisect.bisect_left(float_list, 0)
0
>>> bisect.bisect_left(float_list, 1)
0
>>> bisect.bisect_left(float_list, 2)
2
>>> bisect.bisect_left(float_list, 1.3)
1
>>> bisect.bisect_right(float_list, 1.3)
2
>>> 

```
