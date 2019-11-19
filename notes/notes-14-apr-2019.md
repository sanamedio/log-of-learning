# 14-apr-2019


### 1 - twilio with python for whatsapp

- https://www.twilio.com/console/sms/whatsapp/learn

```python
from twilio.rest import Client 
 
account_sid = '' 
auth_token = '' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='whatsapp:+XXXXXXXXXX',  
                              body='Your appointment is coming up on July 21 at 3PM',      
                              to='whatsapp:+XXXXXXXXXXX' 
                          ) 
 
print(message.sid)
```
- after you reply once, there is a 24-hour 2 way conversation window; all this is to avoid spamming I guess
- earlier firsrt message needed to follow a template, but now it's open template, send anything

```python
from twilio.rest import Client 
 
account_sid = '' 
auth_token = '' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='whatsapp:+ccccc',  
                              body='Hello! This is an editable text message. You are free to change it and write whatever you like.',      
                              to='whatsapp:+ccccc' 
                          ) 
 
print(message.sid)
```
