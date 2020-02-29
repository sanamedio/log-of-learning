# 01-mar-2020

### 2 - joining vs concat has 1000x difference in performance

from MasteringIO.pdf by david beazley

concat is slow
```python
msg = b"" 
while True:
  chunk = s.recv(BUFSIZE) 
  if not chunk:
    break 
  msg += chunk
```

hacky solution for speedup
```python
chunks = [] 
while True:
  chunk = s.recv(BUFSIZE) 
  if not chunk:
    break 
  chunks.append(chunk)
 msg = b"".join(chunks)
```

cleaner solution with bytearray
```python
msg = bytearray() 
while True:
  chunk = s.recv(BUFSIZE) 
  if not chunk:
    break
  msg.extend(chunk)
```

concat: 18.49s
joining: 1.55s
bytearray: 1.78s

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
