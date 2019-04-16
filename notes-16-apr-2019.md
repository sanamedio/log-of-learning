# 16-apr-2019

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

```
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
