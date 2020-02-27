# 27-feb-2020

### 2 - custom serialization

https://hynek.me/articles/serialization/

```python

In [1]: from datetime import datetime
   ...: from functools import singledispatch
   ...:
   ...: @singledispatch
   ...: def to_serializable(val):
   ...:     """Used by default."""
   ...:     return str(val)
   ...:
   ...: @to_serializable.register(datetime)
   ...: def ts_datetime(val):
   ...:     """Used if *val* is an instance of datetime."""
   ...:     return val.isoformat() + "Z"
   ...:

In [2]: import json

In [3]: json.dumps({"msg" : "hi", "ts":  datetime.now()}, default=to_serializable)
Out[3]: '{"msg": "hi", "ts": "2020-02-28T02:43:34.331539Z"}'

In [4]: json.dumps({"msg" : "hi", "ts":  datetime.now()})
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
```


### 1 - cloudpickle

- stronger capabilties than pickle
https://pypi.org/project/cloudpickle/

```python
In [1]: import cloudpickle

In [2]: cube = lambda x : x * x * x

In [3]: cloudpickle.dumps(cube)
Out[3]: b'\x80\x04\x95\x80\x01\x00\x00\x00\x00\x00\x00\x8c\x17cloudpickle.cloudpickle\x94\x8c\x0e_fill_function\x94\x93\x94(h\x00\x8c\x0f_make_skel_func\x94\x93\x94h\x00\x8c\r_builtin_type\x94\x93\x94\x8c\x08CodeType\x94\x85\x94R\x94(K\x01K\x00K\x01K\x02KCC\x0c|\x00|\x00\x14\x00|\x00\x14\x00S\x00\x94N\x85\x94)\x8c\x01x\x94\x85\x94\x8c\x1e<ipython-input-2-d3b880f4deae>\x94\x8c\x08<lambda>\x94K\x01C\x00\x94))t\x94R\x94J\xff\xff\xff\xff}\x94(\x8c\x0b__package__\x94N\x8c\x08__name__\x94\x8c\x08__main__\x94u\x87\x94R\x94}\x94(\x8c\x07globals\x94}\x94\x8c\x08defaults\x94N\x8c\x04dict\x94}\x94\x8c\x0eclosure_values\x94N\x8c\x06module\x94h\x16\x8c\x04name\x94h\x0f\x8c\x03doc\x94N\x8c\x17_cloudpickle_submodules\x94]\x94\x8c\x08qualname\x94h\x0f\x8c\nkwdefaults\x94NutR.'
```
