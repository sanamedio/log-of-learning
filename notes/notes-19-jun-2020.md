# 19-jun-2020

### 1 - weird scoping rules

```python
>>> powers_of_x = [ lambda x: x**i for i in range(10) ]
>>> [ f(2) for f in powers_of_x ]
[512, 512, 512, 512, 512, 512, 512, 512, 512, 512]
>>>
```

