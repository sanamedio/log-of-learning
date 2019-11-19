# 03-mar-2019

### 1 - str2dict

```python
str2 = "k:1|k1:2|k2:3|k3:4"

def str2dict(str1):
    dict1 = {}
    for iterms in str1.split('|'):
        key,value = iterms.split(':'):
            dict1[key] = value
    return dict1

print( str2dict(str2) )

```
