# 31-jan-2019

### 5 - making functions

```python
def make_functions():
    flist = []

    for i in [1, 2, 3]:
        def print_i():
            print(i)
        flist.append(print_i)

    return flist

functions = make_functions()
for f in functions:
    f()
```

output?? and why?

### 4 - streaming fraud detection kafka

- https://github.com/florimondmanca/kafka-fraud-detector
- needed to modify few things, for testing ```$ docker-compose -f docker-compose.kafka.yml exec broker kafka-console-consumer --bootstrap-server localhost:9092 --topic streaming.transactions.fraud --from-beginning```


generator
```python
"""Produce fake transactions into a Kafka topic."""

import os
from time import sleep
import json

from kafka import KafkaProducer
from transactions import create_random_transaction

TRANSACTIONS_TOPIC = os.environ.get('TRANSACTIONS_TOPIC')
KAFKA_BROKER_URL = os.environ.get('KAFKA_BROKER_URL')
TRANSACTIONS_PER_SECOND = float(os.environ.get('TRANSACTIONS_PER_SECOND'))
SLEEP_TIME = 1 / TRANSACTIONS_PER_SECOND


if __name__ == '__main__':
    producer = KafkaProducer(
        bootstrap_servers=KAFKA_BROKER_URL,
        # Encode all values as JSON
        value_serializer=lambda value: json.dumps(value).encode(),
    )
    while True:
        transaction: dict = create_random_transaction()
        producer.send(TRANSACTIONS_TOPIC, value=transaction)
        print(transaction)  # DEBUG
        sleep(SLEEP_TIME)
```

```python
"""Utilities to model money transactions."""

from random import choices, randint
from string import ascii_letters, digits

account_chars = digits + ascii_letters


def _random_account_id() -> str:
    """Return a random account number made of 12 characters."""
    return ''.join(choices(account_chars, k=12))


def _random_amount() -> float:
    """Return a random amount between 1.00 and 1000.00."""
    return randint(100, 100000) / 100


def create_random_transaction() -> dict:
    """Create a fake, randomised transaction."""
    return {
        'source': _random_account_id(),
        'target': _random_account_id(),
        'amount': _random_amount(),
        # Keep it simple: it's all euros
        'currency': 'EUR',
    }
```


consumer
```python
"""Example Kafka consumer."""

import json
import os

from kafka import KafkaConsumer, KafkaProducer

KAFKA_BROKER_URL = os.environ.get('KAFKA_BROKER_URL')
TRANSACTIONS_TOPIC = os.environ.get('TRANSACTIONS_TOPIC')
LEGIT_TOPIC = os.environ.get('LEGIT_TOPIC')
FRAUD_TOPIC = os.environ.get('FRAUD_TOPIC')


def is_suspicious(transaction):
    """Determine whether a transaction is suspicious."""
    return transaction['amount'] >= 900


if __name__ == '__main__':
    consumer = KafkaConsumer(
        TRANSACTIONS_TOPIC,
        bootstrap_servers=KAFKA_BROKER_URL,
        value_deserializer=lambda value: json.loads(value),
    )
    producer = KafkaProducer(
        bootstrap_servers=KAFKA_BROKER_URL,
        value_serializer=lambda value: json.dumps(value).encode(),
    )
    for message in consumer:
        transaction = message.value
        topic = FRAUD_TOPIC if is_suspicious(transaction) else LEGIT_TOPIC
        producer.send(topic, value=transaction)
        print(topic, transaction)  # DEBUG
```

```Dockerfile
FROM python:3.6

WORKDIR /usr/app

ADD ./requirements.txt ./
RUN pip install -r requirements.txt
ADD ./ ./

CMD ["python3", "app.py"]
```

kafka+zookeeper
```yaml
version: '3'

services:

  zookeeper:
    image: confluentinc/cp-zookeeper:latest
    ports:
            - "2181:2181"
    environment:
      ZOOKEEPER_CLIENT_PORT: 2181
      ZOOKEEPER_TICK_TIME: 2000

  broker:
    image: confluentinc/cp-kafka:latest
    depends_on:
      - zookeeper
    ports:
            - "9092:9092"
    environment:
      KAFKA_BROKER_ID: 1
      KAFKA_ZOOKEEPER_CONNECT: zookeeper:2181
      KAFKA_ADVERTISED_LISTENERS: PLAINTEXT://broker:9092
      KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR: 1

networks:
  default:
    external:
      name: kafka-network
```

generator+consumer
```yaml
version: '3'

services:

  generator:
    build: ./generator
    environment:
      KAFKA_BROKER_URL: broker:9092
      TRANSACTIONS_TOPIC: queueing.transactions
      TRANSACTIONS_PER_SECOND: 1000

  detector:
    build: ./detector
    environment:
      KAFKA_BROKER_URL: broker:9092
      TRANSACTIONS_TOPIC: queueing.transactions
      LEGIT_TOPIC: streaming.transactions.legit
      FRAUD_TOPIC: streaming.transactions.fraud

networks:
  default:
    external:
      name: kafka-network
```






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
