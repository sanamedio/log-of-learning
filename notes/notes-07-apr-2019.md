# 07-apr-2019

### 3 - function initilaization with mutables

- this is repetitive, but I goofed it up again when someone asked me today
```python
def append(number, number_list=[]):
    number_list.append(number)
    print(number_list)
    return number_list

append(5) # expecting: [5], actual: [5]
append(7) # expecting: [7], actual: [5, 7]
append(2) # expecting: [2], actual: [5, 7, 2]
```

```
# the keyword None is the sentinel value representing empty list
def append(number, number_list=None):
    if number_list is None:
        number_list = []
    number_list.append(number)
    print(number_list)
    return number_list

append(5) # expecting: [5], actual: [5]
append(7) # expecting: [7], actual: [7]
append(2) # expecting: [2], actual: [2]
```


### 2 - conditions object and python multithreading

- using python condition multithreading primitive

```python
import threading
import time
import logging



logging.basicConfig(level=logging.DEBUG, format='(%(threadName)-9s) %(message)s',)




def consumer(cv):

    logging.debug('Consumer thread started')
    with cv:
        logging.debug('Consumer waiting')
        cv.wait()
        logging.debug('Consumer consumed ther resourec')


def producer(cv):

    logging.debug('Producer thread started ')
    with cv:
        logging.debug('make resource available')
        logging.debug('notifying to all customers')
        cv.notifyAll()


if __name__ == '__main__':
    condition = threading.Condition()
    cs1 = threading.Thread(name='consumer1' , target=consumer, args=(condition,))
    cs2 = threading.Thread(name='consumer2' , target=consumer, args=(condition,))
    pd = threading.Thread(name='producer', target=producer, args=(condition,))

    cs1.start()
    time.sleep(2)
    cs2.start()
    time.sleep(2)
    pd.start()
```


### 1 - mocking 


setting up - nice way to quickly start
```
python3 -m venv mocking
source mocking/bin/activate
touch main.py test.py
```

main:
```python
import time


class Calculator:
    def sum(self, a ,b):
        time.sleep(10)
        return a+b

```

tests:
```python
from unittest import TestCase
from main import Calculator

from unittest.mock import patch


class TestCalculator(TestCase):
    def setUp(self):
        self.calc = Calculator()



    @patch('main.Calculator.sum' , return_value = 9 )
    def test_sum(self,sum):
        self.assertEqual(sum(2,3), 9 )
```

we can also do a mock function
```python
import time


class Calculator:
    def sum(self,a,b):
        time.sleep(10)
        return a  +b
from unittest import TestCase
from unittest.mock import patch


def mock_sum(a,b):
    return a + b



class TestCalculator(TestCase):

    @patch('main.Calculator.sum', side_effect=mock_sum)
    def test_sum(self, sum):
        self.assertEqual(sum(2,3) , 5)
        self.assertEqual(sum(7,3), 10)
```



better example:

main.py
```python
import requests


class Blog:

    def __init__(self,name):
        self.name = name


    def posts(self):
        response = requests.get("https://jsonplaceholder.typecode.com/posts")
        return response.json()

    def __repr__(self):
        return '<Blog: {}>'.format(self.name)
```

test.py
```python
from unittest import TestCase
from unittest.mock import patch, Mock
import main

class TestBlog(TestCase):

    @patch('main.Blog')
    def test_blog_posts(self, MockBlog):
        blog = MockBlog()

        blog.posts.return_value =[
                {
                    'userId' : 1,
                    'id' :1,
                    'title' : 'Test Title',
                    'body' : 'Far out in '
                }
            ]

        response = blog.posts()
        self.assertIsNotNone(response)
        self.assertIsInstance(response[0],dict)

        assert MockBlog is main.Blog #the mock is equivalent to rogianl

        assert MockBlog.called #The mock was called

        blog.posts.assert_called_with() #called posts method with no argument

        blog.reset_mock() # reset the mock object


        blog.posts.assert_not_called() # after resetting posts has not been called
```




