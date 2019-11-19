# 02-apr-2019

### 2 - Taking tables from webpages using pandas

- this is coolest thing! No need to parse HTML
- https://medium.com/@ageitgey/quick-tip-the-easiest-way-to-grab-data-out-of-a-web-page-in-python-7153cecfca58

```python
import pandas as pd
tables= pd.read_html("https://www.spoj.com/users/xilinx/")
print(tables[0])
```

### 1 - Schema Validation in FastAPI

- https://fastapi.tiangolo.com/tutorial/body-schema/

```python
from fastapi import FastAPI,Body
from pydantic import BaseModel, Schema


app= FastAPI()


class Item(BaseModel):
    name: str
    description: str = Schema(None,title="thsdlks sldkfj sdk",max_length=30)
    price: float = Schema(..., gt=0, description="the price must be gt>0")
    tax: float = None



@app.put("/items/{item_id}")
async def update_item(*, item_id: int, item:  Item = Body(..., embed=True)):
    results = {"item_id" : item_id, "item" : item }
    return results
```
with example:
```python
from fastapi import FastAPI,Body
from pydantic import BaseModel, Schema


app= FastAPI()


class Item(BaseModel):
    name: str
    description: str = Schema(None,title="thsdlks sldkfj sdk",max_length=30)
    price: float = Schema(..., gt=0, description="the price must be gt>0")
    tax: float = None



@app.put("/items/{item_id}")
async def update_item(
        *,
        item_id: int,
        item:  Item = Body(
            ...,
            example={
                "name" : "foo",
                "description" : "a very nice example",
                "price" : 35.4,
                "tax" : 3.2,
                },
            )):
    results = {"item_id" : item_id, "item" : item }
    return results
```
