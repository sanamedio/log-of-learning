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
