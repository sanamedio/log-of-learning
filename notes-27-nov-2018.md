# 27-nov-2018

### 2 - scapy packet crafting

- I really like this library. 

```python
>>> IP()                                                                                                                                              
<IP  |>
>>> target="www.google.com"                                                                                                                           
>>> ip = IP(dst=target)                                                                                                                               
>>> ip                                                                                                                                                
<IP  dst=Net('www.google.com') |>
>>> target="www.google.com/30"                                                                                                                        
>>> ip = IP(dst=target)                                                                                                                               
>>> ip                                                                                                                                                
<IP  dst=Net('www.google.com/30') |>
>>> [p for p in ip]                                                                                                                                   
[<IP  dst=216.58.197.36 |>,
 <IP  dst=216.58.197.37 |>,
 <IP  dst=216.58.197.38 |>,
 <IP  dst=216.58.197.39 |>]
>>> ip=IP(dst="www.facebook.com/30")                                                                                                                  
>>> [p for p in ip]                                                                                                                                   
[<IP  dst=157.240.23.32 |>,
 <IP  dst=157.240.23.33 |>,
 <IP  dst=157.240.23.34 |>,
 <IP  dst=157.240.23.35 |>]
>>> ip = IP(dst="localhost/30")                                                                                                                       
>>> [p for p in ip]                                                                                                                                   
[<IP  dst=127.0.0.0 |>,
 <IP  dst=127.0.0.1 |>,
 <IP  dst=127.0.0.2 |>,
 <IP  dst=127.0.0.3 |>]
>>> ip = IP(dst="localhost")                                                                                                                          
>>> [ p for p in ip ]                                                                                                                                 
[<IP  dst=127.0.0.1 |>]
>>> ip = IP(dst="localhost/255")                                                                                                                      
>>> [p for p in ip ]                                                                                                                                  
[<IP  dst=127.0.0.1 |>]
>>> ip = IP(dst="www.google.com/255")                                                                                                                 
>>> [ p for p in ip ]                                                                                                                                 
[<IP  dst=216.58.197.36 |>]
>>> ip = IP(dst="www.google.com/64")                                                                                                                  
>>> [ p for p in ip ]                                                                                                                                 
[<IP  dst=216.58.197.36 |>]
>>> ip = IP(dst="www.google.com/31")                                                                                                                  
>>> [ p for p in ip ]                                                                                                                                 
[<IP  dst=216.58.197.36 |>,
 <IP  dst=216.58.197.37 |>]
>>> ip = IP(dst="www.google.com/29")                                                                                                                  
>>> [ p for p in ip ]                                                                                                                                 
[<IP  dst=216.58.197.32 |>,
 <IP  dst=216.58.197.33 |>,
 <IP  dst=216.58.197.34 |>,
 <IP  dst=216.58.197.35 |>,
 <IP  dst=216.58.197.36 |>,
 <IP  dst=216.58.197.37 |>,
 <IP  dst=216.58.197.38 |>,
 <IP  dst=216.58.197.39 |>]
>>>     
```

### 1 - scapy hello

- scapy library is for packet level fun.

```python
>>> p = sniff(count=10)                                                                                                                               
>>> print(p)                                                                                                                                          
<Sniffed: TCP:10 UDP:0 ICMP:0 Other:0>
>>> p.display()                                                                                                                                       
0000 Ether / IP / TCP 5.175.26.232:https > 192.168.1.14:55846 A
0001 Ether / IP / TCP 5.175.26.232:https > 192.168.1.14:55848 A
0002 Ether / IP / TCP 192.168.1.14:55844 > 5.175.26.232:https A
0003 Ether / IP / TCP 192.168.1.14:55840 > 5.175.26.232:https A
0004 Ether / IP / TCP 5.175.26.232:https > 192.168.1.14:55844 A
0005 Ether / IP / TCP 5.175.26.232:https > 192.168.1.14:55840 A
0006 Ether / IP / TCP 192.168.1.14:55846 > 5.175.26.232:https PA / Raw
0007 Ether / IP / TCP 192.168.1.14:55846 > 5.175.26.232:https FA
0008 Ether / IP / TCP 192.168.1.14:55848 > 5.175.26.232:https PA / Raw
0009 Ether / IP / TCP 192.168.1.14:55848 > 5.175.26.232:https FA
>>> p.plot(lambda x:len(x))    
<Matplotlib plot>
```
