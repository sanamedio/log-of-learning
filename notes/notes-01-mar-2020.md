# 01-mar-2020


### 1 - unicode in python3

from MasteringIO.pdf by david beazley

```python
>>> t = "Jalape\xf1o"
>>> t
'Jalapeño'
>>> str(t)
'Jalapeño'
>>> ascii(t)
"'Jalape\\xf1o'"
>>> import sys
>>> sys.maxunicode
1114111
```

can ignore encoding/decoding errors while reading files like :-

```python3
>>> f = open('foo',encoding='ascii',errors='ignore') 
>>> data = f.read()
>>> data
'Jalapeo'
```
but better is to handle it correctly :-

```python
>>> f = open('foo',encoding='utf-8') >>> data = f.read()
>>>
```
