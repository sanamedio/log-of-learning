# 29-may-2020


### 1 - lstrip and rstrip weirdness

```python
'abcdef'.lstrip('abc')      # returns 'def' as "expected"
'abcbadefed'.lstrip('abc')  # returns 'defed' not at all as expected
```

This happens because lstrip treats abc as a set to be removed from left. There is a new suggestion to add cutprefix and cutsuffix to do better than this.
