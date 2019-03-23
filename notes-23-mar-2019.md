# 23-mar-2019


### 1 - fastapi

- https://github.com/tiangolo/fastapi

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"hello" :"weorld" }

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return { "item_id" : item_id, "q":q }
```
