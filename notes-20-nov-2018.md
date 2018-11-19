# 20-nov-2018


### 1 - visualizing python object space with json

- firefox renders json nicely
- expose a nested object created from python dir() output to a certain depth using flask

```python
## crappy code starts, need to work on writing better 
def visit_node__(node,parent, depth, spaces ):

    if depth == 0 :
        return {}

    else: 
        if len(set([parent,node]) & set(['dd_g_','dd_','visit_node__', 'flag__','expose_api__'])) >0 :
            return None
        print(spaces*" ", parent, " -> ", node ) 
        dd_ = {}
        try:
            for x in eval('dir(' + node + ')'):
                dd_[str(x)] = visit_node__(x,node, depth -1 , spaces + 1)
        except:
            pass
        finally:
            return dd_
    return None

from flask import Flask
app = Flask(__name__)


@app.route('/')
def expose_api__():
    from flask import jsonify
    return jsonify(dd_g_)

if __name__ == '__main__':
   
    global flag__
    flag__= set()
    global dd_g_
    dd_g_ = {}

    for x in eval('dir()'):
        dd_g_[x] = visit_node__(x ,"root",depth=10,spaces=1)

    import json


#    with open("test.json", 'w') as t:
#        json.dump(dd_g_,t )

    app.run()
```
