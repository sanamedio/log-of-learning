# 25-feb-2020


### 1 - aspectlib for AOP in python

https://python-aspectlib.readthedocs.io/en/latest/testing.html

```python
>>> from aspectlib import weave,test
>>> class ProductionClass(object):
...     def method(self):
...         return 'stuff'
>>> real = ProductionClass()
>>> patch = weave(real.method, [test.mock(3)])
>>> real.method(3, 4, 5, key='value')
3
```
