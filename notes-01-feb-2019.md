# 01-feb-2019


### 2 - creating a dynamodb table

```python
import boto3
d = boto3.resource('dynamodb')

d.create_table(TableName="test", KeySchema=[ {'AttributeName':'id', 'KeyType' :'HASH'}], AttributeDefinitions= [ { 'AttributeType' :'N', 'AttributeName' : 'id'}], ProvisionedThroughput = { 'ReadCapacityUnits' : 1, 'WriteCapacityUnits':1})
```


### 1 - converting python ds to dynamodb supported ds

```python
def dict_to_item(raw):
    """
    Coverts a standard Python dictionary to a Boto3 DynamoDB item
    """
    if isinstance(raw, dict):
        return {
            'M': { k: dict_to_item(v) for k, v in raw.items() }
        }
    elif isinstance(raw, list):
        return {
            'L': [dict_to_item(v) for v in raw]
        }
    elif isinstance(raw, str):
        return {'S': raw}
    elif isinstance(raw, int):
        return {'N': str(raw)}

```
