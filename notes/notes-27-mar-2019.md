# 27-mar-2019

### 7 - multiple parameters

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
        user_id: int, 
        item_id: str, 
        q: str = None,
        short: bool = False):
    item = {"item_id" : item_id, "owner_id" : user_id }

    if q:
        item.update({"q" : q })
    if not short:
        item.update({"description" : "This is an amazing item" })
    return item
```

### 6 - bool type in parameters

```python
from fastapi import FastAPI

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item
```

### 5 - sending back objects

```python
from fastapi import FastAPI

app = FastAPI()

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 100):
    return fake_items_db[skip : skip + limit]
```

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def read_item(item_id : str, q: str = None):
    if q:
        return {"item_id" : item_id , "q" : q }
    return {"item_id" :  item_id }

```

### 4 - openapi paths, order matter

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/users/{user_id}")
async def read_user(user_id : str):
    return {"user_id" : user_id }

@app.get("/users/me")
async def read_user_me():
    return {"user_id" : "the curernt user" }
```


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


