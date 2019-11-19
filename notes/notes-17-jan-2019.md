# 17-jan-2019

### 1 - https://locust.io/

- very simple load testing library
- for testing ```localhost:8000/``` the following script will do

```python
# script.py
from locust import HttpLocust, TaskSet, task

class WebsiteTasks(TaskSet):

    @task
    def index(self):
        self.client.get("/")



class WebsiteUser(HttpLocust):
    task_set = WebsiteTasks
    min_wait = 5000
    max_wait = 15000
```

```locust -f script.py --host localhost:8000```


