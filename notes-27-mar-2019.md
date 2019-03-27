# 27-mar-2019

### 3 - openapi path parameters

- https://fastapi.tiangolo.com/tutorial/path-params/

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id):
    return {"item_id" : item_id }
```

- path parameters with types

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id : int ):
    return {"item_id" : item_id }
```



### 2 - async fastAPI example

```python
from fastapi import FastAPI
  
app = FastAPI()


@app.get("/")
async def root():
    return {"message" : "Hello World" }
```

### 1 - fastAPI models

- https://fastapi.tiangolo.com/

```python
from fastapi import FastAPI
from pydantic import BaseModel



app = FastAPI()



class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None


@app.get("/")
def read_root():
    return {"hello" :"weorld" }

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    return { "item_id" : item_id, "q":q }

@app.put("/items/{item_id}")
def create_item(item_id: int, item: Item):
    return {"item_name" :item.name, "item_id" : item_id }
```


