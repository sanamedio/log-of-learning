# 07-apr-2019


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




