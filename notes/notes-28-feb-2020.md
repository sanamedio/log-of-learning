# 28-feb-2020

### 1 - reading variables from previous frames in python

- The current state of a python program; the function stack and variables etc. can be inspected using inspect module, and we can easily read variables from previous frames.

```python
import inspect

print(inspect.stack())
#prints all the frames

print(inspect.stack()[-1].frame.f_locals)
```
