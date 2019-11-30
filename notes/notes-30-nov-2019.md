# 30-nov-2019


### 1 - headless selenium

```python
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup


options = Options()
options.headless = not False
driver = webdriver.Firefox(options=options)
driver.get("http://google.com/")


soup = BeautifulSoup(driver.page_source)
print(soup.prettify())
```
