# 22-jan-2019


### 1 - Simple function call parallelization

If there are two function calls like :-
```python

function_a(arg1,arg2,arg3)
function_b(arg1,arg2,arg3)
```

we can parallelize them like :-

```
from concurrent.futures import ThreadPoolExecutor

executor = ThreadPoolExecutor(max_workers=10)

task_a_job = executor.submit(function_a,arg1,arg2, arg3)
task_b_job = executor.submit(function_b,arg1, arg2, arg3)

wait([task_a_job, task_b_job])

task_a = task_a.result()
task_b = task_b.result()

executor.shutdown(wait=False)
```

We can also use Processes instead of thread if we are more into CPU intensive operations (opposite of network/io bound tasks) by replacing ThreadPoolExecutor with ProcessPoolExecutor

