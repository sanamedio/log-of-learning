# 16-jan-2019

### 1 - flask counter

```python
from flask import Flask
app = Flask(__name__)

num = 0

@app.route('/')
def counter():
    global num
    num = num + 1
    return str(num)

if __name__ == '__main__':
    app.run()
```

- threading issues may happen ?
