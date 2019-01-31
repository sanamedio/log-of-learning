# 01-feb-2019

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
