# 28-oct-2018

### 1 - Deduplication 

```python
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)
            

#for unhashable type, a key can be provided as lamda during function call in the following


def dedupe(items , key= None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)
            
a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]

print( list(dedupe(a,key=lambda t: t['x'])))
```

