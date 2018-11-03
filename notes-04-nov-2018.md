# 04-nov-2018

### 3 - Flask JWT example

- https://pythonhosted.org/Flask-JWT/

```python
from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from flask_jwt import JWT, jwt_required, current_identity



app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS']
app.secret_key = 'loki'
api = Api(app)


class User(object):
    def __init__(self, id , username, password):
        self.id = id
        self.username = username
        self.password = password

    def __str__(self):
        return "User(id='%s')" % self.id 

users = [
    User(1, 'user1', 'abcxyz'),
    User(2, 'user2', 'abcxyz')
]

username_table = { u.username: u for u in users}
userid_table = { u.id: u for u in users }

def authenticate(username, password):
    user = username_table.get(username, None)
    if user and user.password.encode('utf-8') ==   password.encode('utf-8'):
        return user
    
def identity(payload):
    user_id = payload['identity']
    return userid_table.get(user_id, None)




jwt = JWT(app, authenticate, identity)

items = [

	{ 'name' : 'foo' , 'price' : 1} ,
	{ 'name' : 'bar' ,  'price' : 2} 
]


class Item(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help="This field cannot be left blank!"
    )

    @jwt_required()
    def get(self, name):
        return {'item' : next( filter(lambda x : x['name' == name, items])  , None)} 

    
    @jwt_required()
    def post(self, name):
        if next(filter(lambda x : x['name']== name, items),None) is None:
            return {'message' : "An item with name '{}' already exists".format(name)}
        
        data = Item.parser.parse_args()

        item = {'name' : name , 'price' : data['price']}
        items.append(item)
        return item


    @jwt_required()
    def delete(self, name):
        global items
        items = list(filter( lambda x : x['name'] != name, items))
        return {'message' : 'Item deleted'}
    
    @jwt_required()
    def put(self, name):
        data = Item.parser.parse_args()
        item = next(filter(lambda x : x['name'] == name,items), None)
        if item is None:
            item = {'name' : name, 'price' : data['price']}
            items.append(item)
        else:
            item.update(data)
        return item

    
class ItemList(Resource):
    def get(self):
        return {'items' : items }


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')


if __name__ == '__main__':
    app.run(debug=True)
    

# request JWT token first with /auth url, and providing username and passsword in body
# then call items, and from list of items use either to call item, like item/foo, and in body provide a price
```


### 2 - pyenv and pipenv

- Pyenv helps in managing different python versions. It can automatically install and stuff different versions, even jython and pypy also.
- pipenv is pip + virtualenv combined but depends on already install versions of python.
- pipenv (atleast on my system) is not able to directly refer to all pyenv pythons. It tries and fails. A workaround is to use pyenv to global that particular python which we want to use for pipenv beforehand and that way it works.

### 1 - Python Fire to expose internals and debugging

```bash
pip install fire
```

```python
#filename : t.py
import fire

if __name__ == "__main__":
        fire.Fire(); exit()
```

```bash
python t.py fire
```



