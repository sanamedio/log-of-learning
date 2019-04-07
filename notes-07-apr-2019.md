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

