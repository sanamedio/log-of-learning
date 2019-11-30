# 30-nov-2019


### 2 - Quick Tkinter GUI to help in time boxing

- if you don't hit this counter under 15 seconds; it changes the button to "PUSH YOURSELF"

version2:
```python
from tkinter import *
 
window = Tk()
btn = None
ctn = 0
lbl = None
glb_background = "green"


window.title("~FOCUS~")
window.geometry("200x150") 

import time
last_time = time.time()
 
def clicked():
    global last_time
    global btn
    global ctn
    global glb_background
    c = int (time.time() - last_time)
    ctn = ctn + 1
    
    if c < 15:
        glb_background = "green"
    else:
        glb_background = "red"
    last_time = time.time()
 
def update_time():
    global glb_background
    string = str(int(time.time() - last_time))
    if int(time.time() - last_time) > 15:
        glb_background = "red"

    lbl.config(text = string, background = glb_background)
    lbl.after(1000,update_time)


btn = Button(window, text="BREATHE", command=clicked, height=100, width=200, font = ("calibri" , 25, 'bold'))

lbl =  Label(window, font = ('calibri', 40, 'bold'), 
            background = glb_background, 
            foreground = 'white') 


lbl.pack()
btn.pack() 
 
update_time()

window.mainloop()
```




version1:
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
