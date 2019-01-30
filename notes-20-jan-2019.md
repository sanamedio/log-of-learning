# 20-jan-2019

### 1 - dynamodb flask counter

- https://medium.freecodecamp.org/how-to-create-a-serverless-service-in-15-minutes-b63af8c892e5

```python
import boto3
from flask import Flask, jsonify

app = Flask(__name__)

# Initialize dynamodb access
dynamodb = boto3.resource('dynamodb')
db = dynamodb.Table('myservice-dev')

@app.route('/counter', methods=['GET'])
def counter_get():
  res = db.get_item(Key={'id': 'counter'})
  return jsonify({'counter': res['Item']['counter_value']})

@app.route('/counter/increase', methods=['POST'])
def counter_increase():
  res = db.get_item(Key={'id': 'counter'})
  value = res['Item']['counter_value'] + 1
  res = db.update_item(
    Key={'id': 'counter'},
    UpdateExpression='set counter_value=:value',
    ExpressionAttributeValues={':value': value},
  )
  return jsonify({'counter': value})
```
