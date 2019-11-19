# 16-apr-2019

### 5 - using valgrind with python

```
:~$ export PYTHONMALLOC=malloc
:~$ cat > test.py
#!/usr/bin/python3
print("ahasdasd")
:~$ chmod +x test.py
:~$ ./test.py
ahasdasd
:~$ valgrind ./test.py
==8923== Memcheck, a memory error detector
==8923== Copyright (C) 2002-2017, and GNU GPL'd, by Julian Seward et al.
==8923== Using Valgrind-3.15.0 and LibVEX; rerun with -h for copyright info
==8923== Command: ./test.py
==8923== 
ahasdasd
==8923== 
==8923== HEAP SUMMARY:
==8923==     in use at exit: 932,854 bytes in 7,627 blocks
==8923==   total heap usage: 69,889 allocs, 62,262 frees, 9,744,995 bytes allocated
==8923== 
==8923== LEAK SUMMARY:
==8923==    definitely lost: 0 bytes in 0 blocks
==8923==    indirectly lost: 0 bytes in 0 blocks
==8923==      possibly lost: 362,459 bytes in 2,368 blocks
==8923==    still reachable: 570,395 bytes in 5,259 blocks
==8923==         suppressed: 0 bytes in 0 blocks
==8923== Rerun with --leak-check=full to see details of leaked memory
==8923== 
==8923== For lists of detected and suppressed errors, rerun with: -s
==8923== ERROR SUMMARY: 0 errors from 0 contexts (suppressed: 0 from 0)
:~$ 
```


### 4 - JWT in python

```python
Python 3.6.7 (default, Oct 22 2018, 11:32:17) 
[GCC 8.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import jwt
>>> encoded = jwt.encode({'some': 'payload'}, 'secret', algorithm='HS256')
>>> encoded
b'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzb21lIjoicGF5bG9hZCJ9.Joh1R2dYzkRvDkqv3sygm5YyK8Gi4ShZqbhK2gxcs2U'
>>> jwt.decode(encoded, 'secret', algorithms=['HS256'])
{'some': 'payload'}
>>> 
```

### 3 - executing web assembly with python

- https://github.com/wasmerio/wasmer

```python
from wasmer import Instance

wasm_bytes = open('Downloads/simple.wasm','rb').read()

instance = Instance(wasm_bytes)

result = instance.exports.sum(5, 37)

print(result)
```

### 2 - pysolr

- https://lucidworks.com/2015/11/03/solr-on-docker-2/
- https://stackoverflow.com/questions/33336626/connect-to-solr-server-running-on-localhost

```python
import pysolr

solr = pysolr.Solr('http://localhost:8983/solr/gettingstarted', timeout=10)

# How you would index data.
solr.add([  
    {
        "id": "doc_1",
        "title": "A very small test document about elmo",
    }
])


solr.commit()
results = solr.search('*')
print("Saw {0} result(s).".format(len(results)))
```



### 1 - range is a sequence

range is not a list
range is not a simple exhaustable interator
it's so clever O_O

https://stackoverflow.com/questions/30081275/why-is-1000000000000000-in-range1000000000000001-so-fast-in-python-3?rq=1
