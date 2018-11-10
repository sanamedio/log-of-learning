# 11-nov-2018

### 1 - Retry Decorator with exponential backoff

- https://wiki.python.org/moin/PythonDecoratorLibrary#Retry

```python
import time,math


def retry(tries, delay=3, backoff=2):

    if backoff <= 1 : raise ValueError("backoff must be greater than 1")
    tries = math.floor(tries)
    if tries < 0 : raise ValueError("tries must be 0 or greater")
    if delay <= 0: raise ValueError("delay must be greatear than 0")

    def deco_retry(f):
        def f_retry(*args, **kwargs):
            mtries, mdelay = tries, delay

            rv = f(*args, **kwargs)

            while mtries >0:
                if rv: return True

                mtries -= 1
                time.sleep(mdelay)
                mdelay *= backoff

                rv = f(*args, **kwargs)

            
            return False

        return f_retry

    return deco_retry



@retry(10,1,1.1)
def keep_trying():
    print("Trying")
    return False



if '__main__'  == __name__:
    keep_trying()
```
