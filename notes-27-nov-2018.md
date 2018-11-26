# 27-nov-2018

### 5 - spoofing packets

- https://stackoverflow.com/questions/414025/is-there-a-python-library-than-can-simulate-network-traffic-from-different-addre

```python
>>> target='localhost'                                                 
>>> spoofed_ip='1.1.1.1'                                               
>>> port=8000                                                          
>>> p1=IP(dst=target,src=spoofed_ip)/TCP(dport=port,sport=5000,flags='S
...: ') 
...: send(p1)                                                          
.
Sent 1 packets.
>>> seq=12345                                                          
>>> p2=IP(dst=target,src=spoofed_ip)/TCP(dport=port,sport=5000,flags='A
...: ', 
...:                                      ack=seq+1,seq=1)             
>>> send(p2)                                                           
.
Sent 1 packets.
>>> send(p2)                                                           
.
Sent 1 packets.
>>> port = 8002                                                        
>>> p1=IP(dst=target,src=spoofed_ip)/TCP(dport=port,sport=5000,flags='S
...: ') 
...: send(p1)                                                          
.
Sent 1 packets.
>>> seq=12347                                                          
>>> p2=IP(dst=target,src=spoofed_ip)/TCP(dport=port,sport=5000,flags='A
...: ', 
...:                                      ack=seq+1,seq=1)             
>>> send(p2)                                                           
.
Sent 1 packets.
>>>  
```

- shows two new TCP connections in netstat

### 4 - scapy ls() and packet defaults

```python
>> ls(IP)                                                                      
version    : BitField (4 bits)                   = (4)
ihl        : BitField (4 bits)                   = (None)
tos        : XByteField                          = (0)
len        : ShortField                          = (None)
id         : ShortField                          = (1)
flags      : FlagsField (3 bits)                 = (<Flag 0 ()>)
frag       : BitField (13 bits)                  = (0)
ttl        : ByteField                           = (64)
proto      : ByteEnumField                       = (0)
chksum     : XShortField                         = (None)
src        : SourceIPField                       = (None)
dst        : DestIPField                         = (None)
options    : PacketListField                     = ([])
>>> ls(ICMP)                                                                    
type       : ByteEnumField                       = (8)
code       : MultiEnumField (Depends on type)    = (0)
chksum     : XShortField                         = (None)
id         : XShortField (Cond)                  = (0)
seq        : XShortField (Cond)                  = (0)
ts_ori     : ICMPTimeStampField (Cond)           = (70431032)
ts_rx      : ICMPTimeStampField (Cond)           = (70431032)
ts_tx      : ICMPTimeStampField (Cond)           = (70431032)
gw         : IPField (Cond)                      = ('0.0.0.0')
ptr        : ByteField (Cond)                    = (0)
reserved   : ByteField (Cond)                    = (0)
length     : ByteField (Cond)                    = (0)
addr_mask  : IPField (Cond)                      = ('0.0.0.0')
nexthopmtu : ShortField (Cond)                   = (0)
unused     : ShortField (Cond)                   = (0)
unused     : IntField (Cond)                     = (0)
>>> ls(TCP)                                                                     
sport      : ShortEnumField                      = (20)
dport      : ShortEnumField                      = (80)
seq        : IntField                            = (0)
ack        : IntField                            = (0)
dataofs    : BitField (4 bits)                   = (None)
reserved   : BitField (3 bits)                   = (0)
flags      : FlagsField (9 bits)                 = (<Flag 2 (S)>)
window     : ShortField                          = (8192)
chksum     : XShortField                         = (None)
urgptr     : ShortField                          = (0)
options    : TCPOptionsField                     = ([])
>>> ls(UDP)                                                                     
sport      : ShortEnumField                      = (53)
dport      : ShortEnumField                      = (53)
len        : ShortField                          = (None)
chksum     : XShortField                         = (None)
>>> ls(HTTP)                                                                    
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-5-a70c72b721b3> in <module>
----> 1 ls(HTTP)

NameError: name 'HTTP' is not defined
>>>               
```

### 3 - generating packets with specific configs


```python
>>> IP()                                                                                                                                              
<IP  |>
>>> a = IP(dst="176.16.1.40")                                                                                                                         
>>> a                                                                                                                                                 
<IP  dst=176.16.1.40 |>
>>> a.dst                                                                                                                                             
'176.16.1.40'
>>> a.ttl                                                                                                                                             
64

#I want a broadcast MAC address, and IP payload to ketchup.com and to mayo.com, TTL value from 1 to 9, and an UDP payload:

>>> Ether(dst="ff:ff:ff:ff:ff:ff")/IP(dst=["www.google.com", "www.facebook.com"], ttl=(1,9))/UDP()                                                    
<Ether  dst=ff:ff:ff:ff:ff:ff type=0x800 |<IP  frag=0 ttl=(1, 9) proto=udp dst=[Net('www.google.com'), Net('www.facebook.com')] |<UDP  |>>>
>>>   
```

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
