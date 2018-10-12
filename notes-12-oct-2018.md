# notes-12-oct-2018

### 6 docstring

```python
class MyClass:
	"This is my second class"
	a = 10
	def func(self):
		print('Hello')

# Output: 10
print(MyClass.a)

# Output: <function MyClass.func at 0x0000000003079BF8>
print(MyClass.func)

# Output: 'This is my second class'
print(MyClass.__doc__)
```

### 5 __new__ vs __init__

- https://stackoverflow.com/questions/4859129/python-and-python-c-api-new-versus-init

### 4 C3 Linearization for Multiple Interitance

- https://en.wikipedia.org/wiki/C3_linearization
- Class.mro()

### 3 WSGI

- Web Server Gateway Interface
- Set of specs in Python to standardize interaction between Webserver and Web APP framework.

### 2 built-in help

```python
help(object)
dir(object)
type(object)
#object? ipython
```

### 1 - Celery

- https://tests4geeks.com/python-celery-rabbitmq-tutorial/
- https://www.agiliq.com/blog/2015/07/getting-started-with-celery-and-redis/
- https://www.digitalocean.com/community/tutorials/how-to-use-celery-with-rabbitmq-to-queue-tasks-on-an-ubuntu-vps
- Can work with redis, RabbitMQ and other brokers as well as databases


