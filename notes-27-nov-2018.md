# 27-nov-2018

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
