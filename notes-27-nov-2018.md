# 27-nov-2018

### 10 - using scrapy to download files from svn

- Scraping subversion web view over HTTP
- https://doc.scrapy.org/en/latest/intro/tutorial.html

```python
import scrapy

class SvnSpider(scrapy.Spider):
    name = "svn"
    http_user = 'a@b.com'
    http_pass = '12345'

    allowed_domains = ["abc.company.com"]

    start_urls = (
        'https://abc.company.com/svn/',
    )
    def parse(self, response):
        page = response.url.split("/")[-1]
        if response.url.endswith('.java'):
            yield {
                    'url' : response.url,
                    'filename': page,
                    'content' : response.text
                }
        for a in  response.css('a'):
            yield response.follow(a, callback=self.parse)
```


### 9 - Stepping into a function using IPython

```python
In [1]: def foo(a, b):
   ...:     print a + b
   ...:

In [2]: import ipdb

In [3]: ipdb.runcall(foo, 1, 2)
> <ipython-input-1-2e565fd9c4a4>(2)foo()
      1 def foo(a, b):
----> 2     print a + b
      3

ipdb>
```
or
```
>> %debug foo(1,2)
```
or
```
from IPython.core.debugger import Pdb; ipdb=Pdb()
```

### 8 - Sending and recieving packets

- ```sr()``` The sr() function is for sending packets and receiving answers. The function returns a couple of packet and answers, and the unanswered packets.
- ```sr1()``` This function is a variant that only return one packet that answered thesent packet (or the packet set) sent.When using sr() or sr1() the packets must be layer 3 packets (IP, ARP, etc.)
- ```srp()``` The function srp() does the same for layer 2 packets (Ethernet, 802.3, etc).

```python
>>> h  = sr1(IP(dst="10.1.99.2")/ICMP())                               
Begin emission:
.Finished sending 1 packets.

......^C
Received 7 packets, got 0 answers, remaining 1 packets
>>> h  = sr1(IP(dst="www.google.com")/ICMP())                          
Begin emission:
Finished sending 1 packets.
*
Received 1 packets, got 1 answers, remaining 0 packets
>>> h                                                                  
<IP  version=4 ihl=5 tos=0x0 len=28 id=0 flags= frag=0 ttl=56 proto=icmp chksum=0x23cc src=216.58.197.36 dst=192.168.1.14 options=[] |<ICMP  type=echo-reply code=0 chksum=0x0 id=0x0 seq=0x0 |>>
>>> h.show()                                                           
###[ IP ]### 
  version= 4
  ihl= 5
  tos= 0x0
  len= 28
  id= 0
  flags= 
  frag= 0
  ttl= 56
  proto= icmp
  chksum= 0x23cc
  src= 216.58.197.36
  dst= 192.168.1.14
  \options\
###[ ICMP ]### 
     type= echo-reply
     code= 0
     chksum= 0x0
     id= 0x0
     seq= 0x0

>>> h = sr1(IP(dst="www.google.com")/ICMP()/"Helloworld")              
Begin emission:
Finished sending 1 packets.
*
Received 1 packets, got 1 answers, remaining 0 packets
>>> h.show()                                                           
###[ IP ]### 
  version= 4
  ihl= 5
  tos= 0x0
  len= 38
  id= 0
  flags= 
  frag= 0
  ttl= 56
  proto= icmp
  chksum= 0x23c2
  src= 216.58.197.36
  dst= 192.168.1.14
  \options\
###[ ICMP ]### 
     type= echo-reply
     code= 0
     chksum= 0xffdf
     id= 0x0
     seq= 0x0
###[ Raw ]### 
        load= 'Helloworld'

>>> p=sr(IP(dst="www.facebook.com")/TCP(dport=23))                     
Begin emission:
.Finished sending 1 packets.
^C
Received 1 packets, got 0 answers, remaining 1 packets
>>> p=sr(IP(dst="www.facebook.com")/TCP(dport=443))                    
Begin emission:
.Finished sending 1 packets.
*
Received 2 packets, got 1 answers, remaining 0 packets
>>> p                                                                  
(<Results: TCP:1 UDP:0 ICMP:0 Other:0>,
 <Unanswered: TCP:0 UDP:0 ICMP:0 Other:0>)
>>> ans,uans = p                                                       
>>> ans.summary()                                                      
IP / TCP 192.168.1.14:ftp_data > 157.240.23.35:https S ==> IP / TCP 157.240.23.35:https > 192.168.1.14:ftp_data SA
>>> p=sr(IP(dst="www.google.com")/TCP(dport=[23,80,53,443]))           
Begin emission:
.Finished sending 4 packets.
*.............................................................................................................................................................................................................................................................................................................................................................................................................................................................................
```


### 7 - lsc() listing all functions in scapy

- from here http://web.archive.org/web/20120401161821/http://packetstorm.linuxsecurity.com/papers/general/blackmagic.txt
- Scapy has a send, receive and a send&receive mode.
- Scapy can send packets at layer 2 (datalink) and layer 3 (network)
- Scapy has several highlevel functions such as p0f() and arpcachepoison
  that can do most of what common security tools do
- Responses are easy to dissect and reuse
- It is easy
- Scapy's downside is that it is relatively slow, which may make some uses
  impossible. Therefor it's most suitable for reconnaisance, not for DoS
  for example

```python
>>> lsc()                                                              
IPID_count          : Identify IP id values classes in a list of packets
arpcachepoison      : Poison target's cache with (your MAC,victim's IP) couple
arping              : Send ARP who-has requests to determine which hosts are up
bind_layers         : Bind 2 layers on some specific fields' values
bridge_and_sniff    : Forward traffic between interfaces if1 and if2, sniff and return
chexdump            :  Build a per byte hexadecimal representation
computeNIGroupAddr  : Compute the NI group Address. Can take a FQDN as input parameter
corrupt_bits        : Flip a given percentage or number of bits from a string
corrupt_bytes       : Corrupt a given percentage or number of bytes from a string
defrag              : defrag(plist) -> ([not fragmented], [defragmented],
defragment          : defrag(plist) -> plist defragmented as much as possible 
dhcp_request        : --
dyndns_add          : Send a DNS add message to a nameserver for "name" to have a new "rdata"
dyndns_del          : Send a DNS delete message to a nameserver for "name"
etherleak           : Exploit Etherleak flaw
fletcher16_checkbytes:  Calculates the Fletcher-16 checkbytes returned as 2 byte binary-string.
fletcher16_checksum :  Calculates Fletcher-16 checksum of the given buffer.
fragleak            : --
fragleak2           : --
fragment            : Fragment a big IP datagram
fuzz                : Transform a layer into a fuzzy layer by replacing some default values by random objects
getmacbyip          : Return MAC address corresponding to a given IP address
getmacbyip6         : Returns the MAC address corresponding to an IPv6 address
hexdiff             : Show differences between 2 binary strings
hexdump             :  Build a tcpdump like hexadecimal view
hexedit             : --
hexstr              : --
import_hexcap       : --
is_promisc          : Try to guess if target is in Promisc mode. The target is provided by its ip.
linehexdump         :  Build an equivalent view of hexdump() on a single line
ls                  : List  available layers, or infos on a given layer class or name
neighsol            : Sends an ICMPv6 Neighbor Solicitation message to get the MAC address of the neighbor with specified IPv6 address addr
overlap_frag        : Build overlapping fragments to bypass NIPS
promiscping         : Send ARP who-has requests to determine which hosts are in promiscuous mode
rdpcap              : Read a pcap or pcapng file and return a packet list
report_ports        : portscan a target and output a LaTeX table
restart             : Restarts scapy
send                : Send packets at layer 3
sendp               : Send packets at layer 2
sendpfast           : Send packets at layer 2 using tcpreplay for performance
sniff               : 
split_layers        : Split 2 layers previously bound
sr                  : Send and receive packets at layer 3
sr1                 : Send packets at layer 3 and return only the first answer
sr1flood            : Flood and receive packets at layer 3 and return only the first answer
srbt                : send and receive using a bluetooth socket
srbt1               : send and receive 1 packet using a bluetooth socket
srflood             : Flood and receive packets at layer 3
srloop              : Send a packet at layer 3 in loop and print the answer each time
srp                 : Send and receive packets at layer 2
srp1                : Send and receive packets at layer 2 and return only the first answer
srp1flood           : Flood and receive packets at layer 2 and return only the first answer
srpflood            : Flood and receive packets at layer 2
srploop             : Send a packet at layer 2 in loop and print the answer each time
tcpdump             : Run tcpdump or tshark on a list of packets
traceroute          : Instant TCP traceroute
traceroute6         : Instant TCP traceroute using IPv6
traceroute_map      : Util function to call traceroute on multiple targets, then
tshark              : Sniff packets and print them calling pkt.summary(), a bit like text wireshark
wireshark           : Run wireshark on a list of packets
wrpcap              : Write a list of packets to a pcap file
>>>  
```

### 6 - Scapy sending simple ICMP packet

- from https://theitgeekchronicles.files.wordpress.com/2012/05/scapyguide1.pdf

```python
>>> send(IP(dst="www.google.com")/ICMP()/"Helloworld")                 
.
Sent 1 packets.
>>> send(IP(dst="www.google.com",src="www.google.com")/ICMP()/"Helloworld")
.
Send 1 packets.
>>> send(IP(dst="www.google.com",src="www.facebook.com")/ICMP()/"helloworld")
.
Send 1 packets.

>>> send(IP(ttl=120,dst="www.google.com",src="www.facebook.com")/ICMP()/"helloworld")
.
Send 1 packets.
>>> send(IP(ttl=120,dst="www.google.com",src="www.facebook.com")/ICMP(type=0)/"helloworld")
.
Send 1 packets.
```

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
