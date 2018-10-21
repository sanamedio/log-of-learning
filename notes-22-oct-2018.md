# 22-oct-2018


### 2 - Modules written in C (CPython source)

- All C Native modules are present in ```Modules/*module.c``` and generally end with ```module.c```
- These modules get initialized inside Py_Initialize which sits in ```Python/pythonrun.c```


### 1 - Python pre-loaded modules by interpreter

- kind of module cache. When you import modules, it basically checks whether sys.modules already have that or not.
```python
import sys
print sorted(sys.modules.keys())
```



