# 15-aug-2020


### 1 - Creating a gchat git commit notifier

- get a URL webhook of a google chat room
- put this script in the checkout out repo
- add execution to cron
- I did this to remember `git whatchanged` command which is totally awesome

```python
#!/usr/bin/env python
import os

from json import dumps
from httplib2 import Http

def send_message(x):
    """Hangouts Chat incoming webhook quickstart."""
    url = "<my gchat webhook URL>"
    def log(x):
        print(x)
        return x

    data = os.popen(log("git whatchanged --since=\"15 minutes ago\""+ " " + x)).read()
    if len(data)>1:
        bot_message = {
            'text' : str(x).upper() + "\n\n" +  data}
    else:
        raise SystemExit
    
    message_headers = {'Content-Type': 'application/json; charset=UTF-8'}

    http_obj = Http()

    response = http_obj.request(
        uri=url,
        method='POST',
        headers=message_headers,
        body=dumps(bot_message),
    )

    #print(response)

if __name__ == '__main__':
    send_message("upstream/master")
```
