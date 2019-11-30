# 30-nov-2019


### 2 - Quick Tkinter GUI to help task completition

- if you don't hit this counter under 15 seconds; it changes the button to "PUSH YOURSELF"

```python
from tkinter import *
 
window = Tk()
btn = None
ctn = 0

window.title("~FOCUS~")
 
window.geometry("200x100") 

import time
last_time = time.time()
 
def clicked():
    global last_time
    global btn
    global ctn
    c = int (time.time() - last_time)
    ctn = ctn + 1
    
    if c < 15:
        btn.configure(text="YOU ARE FOCUSSED " + str(ctn))
    else:
        btn.configure(text="PUSH YOURSELF !! " + str(ctn) )
    last_time = time.time()
 

btn = Button(window, text="HIT ME", command=clicked, height=100, width=200)


btn.pack() 
 
window.mainloop()
```

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
