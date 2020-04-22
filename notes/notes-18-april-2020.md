# 18-apr-2020


### 1 - raise_for_status

This appears cleaner way to raise status than to do raise ```Exception('')```

```python
import requests

url = "https://httpstat.us/403"
r = requests.get(url)
try:
    r.raise_for_status()
except requests.exceptions.HTTPError as e:
    print(e)
```
