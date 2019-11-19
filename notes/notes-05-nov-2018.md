# 05-nov-2018

### 11 - Simple virtual machine implementation in python

```python
class Machine:


    def __init__(  self, program):
        # program is tutple of tuple which represents instructions
        self.program = program


        self.a = self.b = self.t = None # registers

        #whether to branch
        self.flag = False


        # ocde pointer
        self.pc = 0



    def execute(self):
        while self.pc is not None:
            i = self.program[self.pc]
            print( self.pc, self.a, self.b , self.t, self.flag, i )
            instr , rest = i[0],i[1:]
            self.pc += 1 # don't forget to inrement the counter
            getattr( self, 'i_' + instr)(*rest)


    def i_copy(self, a, b):
        """Duplicates register b in a"""
        setattr(self, a , getattr(self,b))


    def i_set(self,a, b):
        setattr(self,a,b)


    def i_exec(self, reg, op, *args):
        """Calls op and stores the result in reg"""
        setattr(self, reg ,getattr(self,'o_' + op )(*args))

    def i_test(self, op , *rest):
        if getattr(self, 'o_' + op, )(*rest):
            self.flag = True
        else:
            self.flag = False
        
    def i_branch(self,line):
        """Jump to line if flag is set"""
        if self.flag : self.pc = line


    def i_jump(self, line):
        """jump to line"""
        self.pc = line

    def o_zero(self, reg):
        """ is reg zero? """
        return getattr(self,reg) == 0

    def o_lt(self, a, b):
        return getattr(self,a) < getattr(self,b)


    def o_sub(self, a , b):
        return getattr(self,a) - getattr(self,b)




m = Machine((

    ('test', 'zero', 'b'),
    ('branch', None),
    ('copy' , 't', 'a'),

    ('test', 'lt', 't', 'b'),
    ('branch' , 7),

    ('exec', 't', 'sub', 't', 'b'),
    ('jump',3),

    ('copy', 'a', 'b'),
    ('copy', 'b', 't'),
    ('jump', 0),
)
)

m.a = 56
m.b = 12
m.execute()
print (m.a)

```

output:
```bash
0 56 12 None False ('test', 'zero', 'b')
1 56 12 None False ('branch', None)
2 56 12 None False ('copy', 't', 'a')
3 56 12 56 False ('test', 'lt', 't', 'b')
4 56 12 56 False ('branch', 7)
5 56 12 56 False ('exec', 't', 'sub', 't', 'b')
6 56 12 44 False ('jump', 3)
3 56 12 44 False ('test', 'lt', 't', 'b')
4 56 12 44 False ('branch', 7)
5 56 12 44 False ('exec', 't', 'sub', 't', 'b')
6 56 12 32 False ('jump', 3)
3 56 12 32 False ('test', 'lt', 't', 'b')
4 56 12 32 False ('branch', 7)
5 56 12 32 False ('exec', 't', 'sub', 't', 'b')
6 56 12 20 False ('jump', 3)
3 56 12 20 False ('test', 'lt', 't', 'b')
4 56 12 20 False ('branch', 7)
5 56 12 20 False ('exec', 't', 'sub', 't', 'b')
6 56 12 8 False ('jump', 3)
3 56 12 8 False ('test', 'lt', 't', 'b')
4 56 12 8 True ('branch', 7)
7 56 12 8 True ('copy', 'a', 'b')
8 12 12 8 True ('copy', 'b', 't')
9 12 8 8 True ('jump', 0)
0 12 8 8 True ('test', 'zero', 'b')
1 12 8 8 False ('branch', None)
2 12 8 8 False ('copy', 't', 'a')
3 12 8 12 False ('test', 'lt', 't', 'b')
4 12 8 12 False ('branch', 7)
5 12 8 12 False ('exec', 't', 'sub', 't', 'b')
6 12 8 4 False ('jump', 3)
3 12 8 4 False ('test', 'lt', 't', 'b')
4 12 8 4 True ('branch', 7)
7 12 8 4 True ('copy', 'a', 'b')
8 8 8 4 True ('copy', 'b', 't')
9 8 4 4 True ('jump', 0)
0 8 4 4 True ('test', 'zero', 'b')
1 8 4 4 False ('branch', None)
2 8 4 4 False ('copy', 't', 'a')
3 8 4 8 False ('test', 'lt', 't', 'b')
4 8 4 8 False ('branch', 7)
5 8 4 8 False ('exec', 't', 'sub', 't', 'b')
6 8 4 4 False ('jump', 3)
3 8 4 4 False ('test', 'lt', 't', 'b')
4 8 4 4 False ('branch', 7)
5 8 4 4 False ('exec', 't', 'sub', 't', 'b')
6 8 4 0 False ('jump', 3)
3 8 4 0 False ('test', 'lt', 't', 'b')
4 8 4 0 True ('branch', 7)
7 8 4 0 True ('copy', 'a', 'b')
8 4 4 0 True ('copy', 'b', 't')
9 4 0 0 True ('jump', 0)
0 4 0 0 True ('test', 'zero', 'b')
1 4 0 0 True ('branch', None)
4
```


### 10 - GIL implementation in python 

- https://rushter.com/blog/python-gil-thread-scheduling/
- Basically, the job of the GIL is to pause the while loop for all threads except for a thread that currently owns the GIL. For example, if you have three threads, two of them will be suspended. Typically but not necessarily, only one Python thread can execute Python opcodes at a time, and the rest will be waiting a split second of time until the GIL will be switched to them.

### 9 - socks5 proxy in python minimal

- https://rushter.com/blog/python-socks-server/
- struct pack and unpack are very useful while communicating over bytes, but format strings need to know
- SOCKS is a generic proxy protocol that relays TCP connections from one point to another using intermediate connection (socks server). Originally, SOCKS proxies were mostly used as a circuit-level gateways, that is, a firewall between local and external resources (the internet).
- https://www.ietf.org/rfc/rfc1928.txt

```python
from socketserver import ThreadingMixIn, TCPServer, StreamRequestHandler
import struct,select,socket


SOCKS_VERSION=5


# we can replace ThreadingMixIn with ForkingTCPServer
class ThreadingTCPServer(ThreadingMixIn, TCPServer):
    pass



class SocksProxy( StreamRequestHandler):


    username= 'username'
    password = 'password'


    def handle( self ):
        #out main logic
        
        # header
        # read and unpack 2 2bytes from a client
        # version and method both are one bytes
        # we are implementing a subset

        #!BB means , format string, two bytes and network-endianess

        header = self.connection.recv(2)
        version, nmethods = struct.unpack("!BB", header)

        assert version == SOCKS_VERSION
        assert nmethods > 0


        methods =   self.get_available_methods(nmethods)


        # username/password
        if 2 not in set(methods):
            #close connection
            #self.connection.sendall(struct.pack("!BB", SOCKS_VERSION, 255))
            self.server.close_request(self.request)
            return

        #send server choice
        self.connection.sendall(struct.pack("!BB", SOCKS_VERSION,2))


        if not self.verify_credentials():
            return

        #request

        version,  cmd,  _ , address_type = struct.unpack("!BBBB", self.connection.recv(4))
        assert version == SOCKS_VERSION

        if address_type == 1: #ipv4
            address = socket.inet_ntoa(self.connection.recv(4))
        elif address_type == 3: #dominaname
            domain_length = ord(self.connection.recv(1)[0])
            address = self.connection.recv(domain_length)
        
        port = struct.unpack('!H', self.connection.recv(2))[0]

        #reply

        try:
            if cmd == 1: #connect
                remote = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                remote.connect((address,port))
                bind_address = remote.getsockname()
            else:
                self.server.close_request(self.request)

            addr = struct.unpack("!I", socket.inet_aton(bind_address[0]))[0]

            port = bind_address[1]

            reply = struct.pack("!BBBBIH", SOCKS_VERSION, 0,0, address_type, addr, port)
        
        except Exception as err:
            reply = self.generate_failed_reply(address_type, 5)
        
        self.connection.sendall(reply)


        #establish data exchange

        if reply[1] == 0 and cmd == 1:
            self.exchange_loop(self.connection, remote)




    def get_available_methods(self, n):
        methods = []
        for i in range(n):
            methods.append(ord(self.connection.recv(1)))
        return methods


    def verify_credentials(self):
        version = ord(self.connection.recv(1))
        assert version == 1

        username_len = ord(self.connection.recv(1))
        username = self.connection.recv(username_len).decode('utf-8')

        password_len = ord(self.connection.recv(1))
        password = self.connection.recv(password_len).decode('utf-8')

        if username == self.username and password == self.password:
            # sucess, statu s= 0
            response = struct.pack("!BB", version, 0 )
            self.connection.sendall(response)
            return True
    
        #failure
        response = struct.pack("!BB", version, 0xFF)
        self.connection.sendall(response)
        self.server.close_request(self.request)
        return False
    

    def generate_failed_reply(self, address_type, error_number):
        return struct.pack("!BBBBIH", SOCKS_VERSION, error_number , 0 , address_type, 0, 0  )

    def exchange_loop(self, client, remote):

        while True:

            #wait until client or remote is avl to read
	    # reading from both client and remote , and select is helping here, https://docs.python.org/2/library/select.html
            r , w , e = select.select([client, remote], [], [])


            if client in r: # if read data is from mclient, then send it to remote
                data = client.recv(4096)
                if remote.send(data) <= 0:
                    break

            if remote in r:# vice versea
                data = remote.recv(4096)
                if client.send(data) <= 0:
                    break



if __name__ == '__main__':
    with ThreadingTCPServer(('127.0.0.1', 9013), SocksProxy) as server:
        server.serve_forever()
    
```

```bash
 curl -v  --socks5 127.0.0.1:9011 -U username:password https://github.com
```


### 8 - dbus python

- https://en.wikipedia.org/wiki/D-Bus
- Tried installing with pip didn't work, so tried apt-get and it worked. Mostly whatever doesn't get installed via pip, usually needs apt-get
- https://gkbrk.com/2018/02/simple-dbus-service-in-python/ (TODO GET IT WORKING, NOT WORKED YET )

### 7 - macropy library and "with trace"

```python
#target.py
from macropy.tracing import macros, trace

with trace:
    sum([i for i in range(5)])
```

```python
#run.py

import macropy.activate
import target
```
```bash
python run.py
```
output:
```python
sum([ i for i in range(5) ])
range(5) -> range(0, 5)
[i for i in range(5)] -> [0, 1, 2, 3, 4]
sum([ i for i in range(5) ]) -> 10
```


### 6 - While writing a library ( like Django ) things to take care of for portability between VMs

- https://jacobian.org/writing/python-implementation-details/
  - Using the \_\_builtins__ super-global instead of import \_\_builtin__.
  - Assumptions about the terminal that’s available. Not all terminals will support curses, so anything involving term colors or even isatty is a bit suspect.
  - Assumptions about what’s available in the os module. os.access, os.chmod, os.getpid, may not be available.
  - Relying on features of “old-style” classes, or dynamically creating classes at runtime based on types.ClassType. In general, avoid old-style classes completely if at all possible.
  - Assumptions about function internals, especially im_func.func_code.
  - Assumptions about dict ordering. Remember that dict really is unordered; just because you “usually” get the same order doesn’t mean that you’ve gotten a magic ordered dict.
  - Making code that requires gc.collect.
  - Relying on built-in exception message strings; some (IndexError) differ between VMs.
  - Not paying close attention to type conversion at boundaries (sockets, databases); you might get a boxed type (i.e. a java.lang.String) from the underlying VM where you’re not expecting it.
  - Not thinking carefully about PYTHONPATH, or ignoring things like JYTHONPATH.
  - Not using \_\_import__ properly. Use importlib instead.
  - Assuming the existence or format of .pyc or .pyo objects, or assuming that Python modules must be \*.py, or really any assumptions about the names of files.


### 5 - FUSE : filesystem in userspace

- https://en.wikipedia.org/wiki/Filesystem_in_Userspace
- ```sudo apt install fusepy``` (no idea how to install for python3)
- The code below is taken from https://www.stavros.io/posts/python-fuse-filesystem/

```python
from __future__ import with_statement

import os
import sys
import errno

from fuse import FUSE, FuseOSError, Operations


class Passthrough(Operations):
    def __init__(self, root):
        self.root = root

    # Helpers
    # =======

    def _full_path(self, partial):
        partial = partial.lstrip("/")
        path = os.path.join(self.root, partial)
        return path

    # Filesystem methods
    # ==================

    def access(self, path, mode):
        full_path = self._full_path(path)
        if not os.access(full_path, mode):
            raise FuseOSError(errno.EACCES)

    def chmod(self, path, mode):
        full_path = self._full_path(path)
        return os.chmod(full_path, mode)

    def chown(self, path, uid, gid):
        full_path = self._full_path(path)
        return os.chown(full_path, uid, gid)

    def getattr(self, path, fh=None):
        full_path = self._full_path(path)
        st = os.lstat(full_path)
        return dict((key, getattr(st, key)) for key in ('st_atime', 'st_ctime',
                     'st_gid', 'st_mode', 'st_mtime', 'st_nlink', 'st_size', 'st_uid'))

    def readdir(self, path, fh):
        full_path = self._full_path(path)

        dirents = ['.', '..']
        if os.path.isdir(full_path):
            dirents.extend(os.listdir(full_path))
        for r in dirents:
            yield r

    def readlink(self, path):
        pathname = os.readlink(self._full_path(path))
        if pathname.startswith("/"):
            # Path name is absolute, sanitize it.
            return os.path.relpath(pathname, self.root)
        else:
            return pathname

    def mknod(self, path, mode, dev):
        return os.mknod(self._full_path(path), mode, dev)

    def rmdir(self, path):
        full_path = self._full_path(path)
        return os.rmdir(full_path)

    def mkdir(self, path, mode):
        return os.mkdir(self._full_path(path), mode)

    def statfs(self, path):
        full_path = self._full_path(path)
        stv = os.statvfs(full_path)
        return dict((key, getattr(stv, key)) for key in ('f_bavail', 'f_bfree',
            'f_blocks', 'f_bsize', 'f_favail', 'f_ffree', 'f_files', 'f_flag',
            'f_frsize', 'f_namemax'))

    def unlink(self, path):
        return os.unlink(self._full_path(path))

    def symlink(self, name, target):
        return os.symlink(name, self._full_path(target))

    def rename(self, old, new):
        return os.rename(self._full_path(old), self._full_path(new))

    def link(self, target, name):
        return os.link(self._full_path(target), self._full_path(name))

    def utimens(self, path, times=None):
        return os.utime(self._full_path(path), times)

    # File methods
    # ============

    def open(self, path, flags):
        full_path = self._full_path(path)
        return os.open(full_path, flags)

    def create(self, path, mode, fi=None):
        full_path = self._full_path(path)
        return os.open(full_path, os.O_WRONLY | os.O_CREAT, mode)

    def read(self, path, length, offset, fh):
        os.lseek(fh, offset, os.SEEK_SET)
        return os.read(fh, length)

    def write(self, path, buf, offset, fh):
        os.lseek(fh, offset, os.SEEK_SET)
        return os.write(fh, buf)

    def truncate(self, path, length, fh=None):
        full_path = self._full_path(path)
        with open(full_path, 'r+') as f:
            f.truncate(length)

    def flush(self, path, fh):
        return os.fsync(fh)

    def release(self, path, fh):
        return os.close(fh)

    def fsync(self, path, fdatasync, fh):
        return self.flush(path, fh)


def main(mountpoint, root):
    FUSE(Passthrough(root), mountpoint, nothreads=True, foreground=True)

if __name__ == '__main__':
    main(sys.argv[2], sys.argv[1])
```
Tested to mount one folder into another as mount:
```bash
python myfuse.py ~/Downloads/ ~/test_mount/
```


### 4 - using pandas to directly load data ( pandas is kinda awesome)

install:
```bash
pip install pandas
```

run:
```python
Python 3.7.0 (default, Nov  4 2018, 00:07:25) 
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import pandas as pd
>>> 
>>> direct_link = 'http://www.randalolson.com/wp-content/uploads/percent-bachelors-degrees-women-usa.csv'
>>> women_majors = pd.read_csv(direct_link)
>>> 
>>> print(women_majors.info())
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 42 entries, 0 to 41
Data columns (total 18 columns):
Year                             42 non-null int64
Agriculture                      42 non-null float64
Architecture                     42 non-null float64
Art and Performance              42 non-null float64
Biology                          42 non-null float64
Business                         42 non-null float64
Communications and Journalism    42 non-null float64
Computer Science                 42 non-null float64
Education                        42 non-null float64
Engineering                      42 non-null float64
English                          42 non-null float64
Foreign Languages                42 non-null float64
Health Professions               42 non-null float64
Math and Statistics              42 non-null float64
Physical Sciences                42 non-null float64
Psychology                       42 non-null float64
Public Administration            42 non-null float64
Social Sciences and History      42 non-null float64
dtypes: float64(17), int64(1)
memory usage: 6.0 KB
None
>>> women_majors.head()
   Year             ...               Social Sciences and History
0  1970             ...                                      36.8
1  1971             ...                                      36.2
2  1972             ...                                      36.1
3  1973             ...                                      36.4
4  1974             ...                                      37.3

[5 rows x 18 columns]
>>> 
```

### 3 - test data generation in python using mimesis

```python
Python 3.7.0 (default, Nov  4 2018, 00:07:25) 
[GCC 5.4.0 20160609] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> from mimesis import Person
>>> person = Person('en')
>>> person.full_name()
'Sheldon Mcdonald'
>>> person.occupation()
'Preacher'
>>> person.occupation()
'Scrap Dealer'
>>> person.telephone()
'436.227.0495'
>>> person.identifier()
'53-04/14'
>>> person.identifier(mask='####/##-#')
'0299/48-5'
```

### 2 - better way to refer to libc

```python
>>> import ctypes
>>> import ctypes.util
>>> libc = ctypes.CDLL(ctypes.util.find_library("c")
... )
>>> libc
<CDLL 'libc.so.6', handle 7fae30f804e0 at 0x7fae2fb44a58>
>>> 
```

### 1 - type hints for python 3

- Can generate types automatically using instagram's https://github.com/Instagram/MonkeyType
- using typing module, the type hints can be read and appropriate exception can be raised like follows

```python
from typing import get_type_hints
from functools import wraps
from inspect import getfullargspec

def validate_input( obj, **kwargs ):

	hints = get_type_hints(obj)

	# iterate all type hints

	for attr_name, attr_type in hints.items():
		if attr_name == 'return':
			continue


		if not isinstance(kwargs[attr_name], attr_type ):
			raise TypeError(
				'Argument %r is not of the type %s' % (attr_name, attr_type))


def type_check(f):
	@wraps(f)
	def wrapped_decorator( *args, **kwargs):
		func_args = getfullargspec(f)[0]
		kwargs.update(dict(zip(func_args, args)))
		
		validate_input(f, **kwargs)
		return f(**kwargs)

	return wrapped_decorator


@type_check
def addition(number : int , other_number: int ) -> int :
	return number + other_number

print(addition ( 1,2 ))

print( addition( 1, '2' )) 
```

output:
```bash
3
Traceback (most recent call last):
  File "test2.py", line 41, in <module>
    print( addition( 1, '2' ))
           └ <function addition at 0x7f43edbea510>
  File "test2.py", line 29, in wrapped_decorator
    validate_input(f, **kwargs)
    │              │    └ {'number': 1, 'other_number': '2'}
    │              └ <function addition at 0x7f43edbea488>
    └ <function validate_input at 0x7f43eef26b70>
  File "test2.py", line 18, in validate_input
    'Argument %r is not of the type %s' % (attr_name, attr_type))
TypeError: Argument 'other_number' is not of the type <class 'int'>

```
 
