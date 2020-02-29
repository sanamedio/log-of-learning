# 01-mar-2020

### 6 - FileIO object

```python
f = io.FileIO("somefile","r") 
data = f.read(4096) 
f.seek(16384,os.SEEK_SET)
```

### 5 - return type of open call

```python
>>> open("foo.txt","rt")
<_io.TextIOWrapper name='foo.txt' encoding='UTF-8'> 

>>> open("foo.txt","rb")
<_io.BufferedReader name='foo.txt'>

>>> open("foo.txt","rb",buffering=0)
<_io.FileIO name='foo.txt' mode='rb'>
```

### 4 - memoryview

- from david beazley masteringIO.pdf

```python
>>> a = bytearray(b'Hello World') 
>>> b = memoryview(a)
>>> b
<memory at 0x1007014d0>
>>> b[-5:] = b'There'
>>> a
bytearray(b'Hello There') 
>>>
```

### 3 - run a bytearray through xor cipher

- from david beazley masteringIO.pdf
- notice the we used comprehension in a function argument directly!

```python
>>> s = b"Hello World"
>>> t = bytes(x^42 for x in s) 
>>> t
b'bOFFE\n}EXFN'
>>> bytes(x^42 for x in t) 
b'Hello World'
>>>
```

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
