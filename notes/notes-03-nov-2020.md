# 03-nov-2020

### 1 - freezegun

- nice library https://github.com/spulec/freezegun
- used to freeze time for unit tests

```
>>> from freezegun import freeze_time
>>> freezer = freeze_time("2020-01-14 12:00:01")
>>> freezer.start()
<freezegun.api.FrozenDateTimeFactory object at 0x106289668>
>>> from datetime import datetime
>>> datetime.now()
FakeDatetime(2020, 1, 14, 12, 0, 1)
>>> datetime.now()
FakeDatetime(2020, 1, 14, 12, 0, 1)
>>> datetime.now()
FakeDatetime(2020, 1, 14, 12, 0, 1)
>>> freezer.stop()
>>> datetime.now()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/i0814/test2/venv/lib/python3.6/site-packages/freezegun/api.py", line 360, in now
    result = now + cls._tz_offset()
  File "/Users/i0814/test2/venv/lib/python3.6/site-packages/freezegun/api.py", line 390, in _tz_offset
    return tz_offsets[-1]
IndexError: list index out of range
>>>
```
