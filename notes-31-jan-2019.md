# 31-jan-2019


### 1 - flask redis docker docker-compose alpine

- https://docs.docker.com/compose/gettingstarted/

```python
import time

import redis
from flask import Flask


app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)


def get_hit_count():
    retries = 5
    while True:
        try:
            return cache.incr('hits')
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                raise exc
            retries -= 1
            time.sleep(0.5)


@app.route('/')
def hello():
    count = get_hit_count()
    return 'Hello World! I have been seen {} times.\n'.format(count)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
```

docker-compose.yml
```yaml
version : '3'
services:
        web:
                build: .
                ports:
                        - "5000:5000"
        redis:
                image: "redis:alpine"
```

docker-compose.yml ( with volume)
```yaml
version : '3'
services:
        web:
                build: .
                ports:
                        - "5000:5000"
                volumes:
                        - .:/code
        redis:
                image: "redis:alpine"

```

Dockerfile
```Dockerfile
FROM python:3.4-alpine
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt
CMD ["python", "app.py"]
```

requirements.txt
```
flask
redis
```
