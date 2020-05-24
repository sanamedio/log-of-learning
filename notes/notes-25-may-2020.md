# 25-may-2020

### 1 - asyncio repl

```python
asyncio REPL 3.8.0 (default, Apr 21 2020, 09:37:48)
[Clang 11.0.0 (clang-1100.0.33.16)] on darwin
Use "await" directly instead of "asyncio.run()".
Type "help", "copyright", "credits" or "license" for more information.
>>> import asyncio
>>> async def foo():
...     await asyncio.sleep(5)
...     print("done")
...
>>> await foo()
done
>>>
```
