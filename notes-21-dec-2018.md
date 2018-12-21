# 21-dec-2018


### 1 - default arguments check

```python
# you can also inspect the default values given to a function
def showing_func_defaults(b=99):
    print ("b is %s, and the default value for b is %s" % (b, showing_func_defaults.func_defaults[0]))

showing_func_defaults(88)
# prints 'b is 88, and the default value for b is 99'

# this trick can be used to test if a value was given to a default parameter
def did_i_get_default(b=object()):
    if b is did_i_get_default.func_defaults[0]:
        print ("No value was passed for b")
    else:
        print("a value of %s was passed for b" % b)

did_i_get_default() # prints "no value was passed for b"
did_i_get_default(b=88) # prints "a value of 88 was passed for b
```
