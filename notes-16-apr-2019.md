# 16-apr-2019

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
