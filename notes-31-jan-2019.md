# 31-jan-2019

### 3 - django docker-compose postgres 

- https://docs.docker.com/compose/django/


Dockerfile for django server
```Dockerfile
FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
```

docker-compose.yml
```yaml
version: '3'

services:
        db:
                image: postgres
        web:
                build: .
                command: python manage.py runserver 0.0.0.0:8000
                volumes:
                        - .:/code
                ports:
                        - "8000:8000"
                depends_on:
                        - db
```




requirements.txt
```
Django>=2.0,<3.0
psycopg2>=2.7,<3.0
```

creating project inside the image(which is mapped to current directory volume)
```
docker-compose run web django-admin startproject composeexample .
```

change permissions from root:root to $USER:$USER
```
sudo chown -R $USER:$USER .
```
- modify settings.py for postgres db config
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER' : 'postgres',
        'HOST': 'db',
        'PORT' : 5432,
    }
}
```

run!
```
docker-compose up
```


### 2 - PYTHONUNBUFFERED=1 why?

- https://www.reddit.com/r/learnpython/comments/5ebkq6/what_does_pythonunbuffered1_do/

```python
import time
for i in range(10):
    print(i, end=" ")
    time.sleep(.2)
print()
```

```python
import time
for i in range(10):
    print(i, end=" ", flush=True)
    time.sleep(.2)
print()
```

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
