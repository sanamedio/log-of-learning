# 10-nov-2018

### 12 - Prover and Verifier part of Graph isomorphism Zero-konwledge proof simulation in python (continued from 11)

- How does Zero knowledge proofs differ from normal proofs?
  - Aren't they proof by contradiction? NO
  - Do they target different problems? Specifically problems where we need to not reveal information? MAYBE. But it's possible that the problem they solve can be reduced to other NPish problems and that way what we achieve with ZKP can help solve other problems.
  - In this Graph isomorphism case, how does information not leak? How can we say that based on the answers of the Prover, Verifer can't find out the true mapping between G1 and G2? This question may be assuming that Verifier will not follow the protocol. Verifier's task is to establish the fact that the Prover knows the correct isomorphisms, not attacking the Zero knowledge protocol for getting information from Prover. But what if a malicious entity enact as verifier? -- So, it is probably that in one round Verifier can only ask one mapping. And in subsequent rounds, the H and mappings will change. Hence he can't derive.
  - The interactive proof can be zero knowledge, in which case a cheating verifier does not learn anything new by talking to the honest prover.
  - http://www.cs.ox.ac.uk/people/gerardo.simari/personal/publications/zkp-simari2002.pdf
  
Prover:
```python
class Prover():

    def __init__(self, G1, G2, isomorphism ):

        # G1 and G2 are known to both parties, but the correct isomorphism between G1 and G2 is known only to the Prover. What Prover wants to get Verified by Verfier is that he knows the isomorphism between G1 and G2, without revealing the isomorphism
        self.G1 = G1 #list of edge tuples
        self.G2 = G2 #list of edge tuples
        self.n = numVertices(G1) #num vertices is separate function to find out vertices, it won't be same as length of G as it's a edge-list represetation
        assert self.n == numVertices(G2)

        self.isomorphism = isomorphism #only prover knows this
        self.state = None


    def sendIsomorphicCopy(self): # First round of protocol, when prover sends information to Verifier

        isomorphism = randomPermutation(self.n) # this is a new random isomorphism, not related to the true isomorphism between G1 and G2 which prover knows, since prover knows this, he can also easily know the inverse of this isomorphism.


        pi = makePermutationFunction(isomorphism) #this isomomrphism was created from a random mapping. 

        H = applyIsomorphism(self.G1, pi) # for each edge in the G1, let's apply the isomorphism, and convert it to a isomophic graph H

        self.state = isomorphism # 
        return H




    def proveIsomorphicTo(self, graphChoice): #Second round of protocol, when Verifier sends informmation to prover, or more like a question
        randomIsomorphism = self.state # self.state will be containing our randomly generated isomorphism which we used to create H from G1 ; which we sent to to the Verifier

        piInverse = makeInversePermutationFunction(randomIsomorphism) # since you know what isomophism was used, creating inverse is easy 

        if graphChoice == 1: # if the Verifier asks for G1
            return piInverse # return the piInverse as it is.
        else:
            f = makePermutationFunction(self.isomorphism) # but here if he asks about G2, now we can use our original true G1 to G2 isomophism only known to prover to create a isomophism function.
            return lambda i : f(piInverse(i)) # we take the fog kind of stuff we already know G1 to H and G1 to G2, so we can find out H to G2. So now Verifier know this information, H-> G1 mapping and H->G2 mapping, where H we have eelected at random
```
Verifier
```
class Verifier():

    def __init__(self, G1, G2): # see the difference, no preknonwn isomorphism here
        self.G1 = G1
        self.G2 = G2
        self.n = numVertices(G1)
        assert self.n == numVertices(G2) # these checks are more programmatical


    def chooseGraph(self, H):
        choice = random.choice([1,2])
        self.state = H , choice # state is just to maintain information between multiple steps of the protocol
        return choice #this gets sent to Prover


    def accepts(self, isomorphism): # last step of protocol
        H, choice = self.state
        graphToCheck =[ self.G1, self.G2][choice - 1]
        f = isomorphism

        isValidIsomorphism = ( graphToCheck == applyIsomorphism(H, f))
        return isValidIsomorphism






def runProtocol(G1, G2, isomorphism):
    p = Prover(G1,G2, isomorphism)
    v = Verifier(G1,G2)

    H = p.sendIsomorphicCopy()
    choice = v.chooseGraph(H)
    witnessIsomorphism = p.proveIsomorphicTo(choice)

    return v.accepts(witnessIsomorphism)
```



### 11 - Generating a random permutation and isomophiic mapping functions

- Following Zero Knowledge proof tutorial [jeremy-zkp-tutorial-py](https://jeremykun.com/2016/07/05/zero-knowledge-proofs-a-primer/)
- ZEP is a kind of prooving technique where there are two entities Proover and Verifier. The idea is that Proover wants to Prove something and Verify needs to verify that within the constraints that Proover don't want to reveal the information, yet somehow do it.
- https://en.wikipedia.org/wiki/Zero-knowledge_proof
- For example if we want to prove to a blind person that multicolored balls exist then we can play a game with him where he will show us two balls. What he wants to prove is that balls are of same color, whereas we want to prove that they are of different colors, without passing this information via eyes( which sense color,). So he will show us the balls, and then switch/no-switch them behind himself(without showing us) and ask us whether he switched or not. If we can answer correctly it means the balls are of different colors. This has to be repeated as number of trials as Verifiers want to feel confident. If for example, balls were of same colors; there would be 0.5 chance of guessing it correctly. and in N trials the chance of us guessing correctly each time would diminish rapidly. 
- TODO Read alibaba example

```python
Python 3.6.6 (default, Sep 12 2018, 18:26:19) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import random
>>> def randomPermutation(n):
...     L = list(range(n))
...     random.shuffle(L)
...     return L
... 
>>> randomPermutation(1)
[0]
>>> randomPermutation(2)
[1, 0]
>>> randomPermutation(3)
[2, 0, 1]
>>> randomPermutation(4)
[0, 1, 2, 3]
>>> randomPermutation(5)
[1, 2, 4, 3, 0]
>>> randomPermutation(5)
[0, 1, 4, 2, 3]
>>> randomPermutation(5)
[4, 3, 2, 0, 1]
>>> randomPermutation(5)
[3, 4, 2, 0, 1]
>>> randomPermutation(5)
[2, 1, 0, 3, 4]
>>> def makePermutationFunction(L):
...     return lambda i : L[i-1] + 1
... 
>>> makePermutationFunction([0,1,2]) 
<function makePermutationFunction.<locals>.<lambda> at 0x7fd4a98d60d0>
>>> def makeInversePermutationFunction(L): # just shift everything from the previous function to other Hand side and equation will become this. 
...     return lambda i: 1 + L.index(i-1)
... 
>>> def applyIsomorphism(G, f):
...     return [(f(i), f(j)) for (i,j) in G ]
... 
>>> 
```

### 10 - Hunting Traces by hunter module

- it can set traces on modules, functions ,code etc.

```bash
$ python3 -m pip install --user hunter
```

```python
python3
Python 3.6.6 (default, Sep 12 2018, 18:26:19) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import posixpath #not necessary to import
>>> import hunter
>>> hunter.trace(module='posixpath')
<hunter._tracer.Tracer at 0x7f2dd1be25e8: threading_support=False, handler=<hunter._predicates.When: condition=<hunter._predicates.Query: query_eq=(('module', 'posixpath'),)>, actions=(CallPrinter(stream=<colorama.ansitowin32.AnsiToWin32 object at 0x7f2dd30e22b0>, force_colors=False, filename_alignment=40, thread_alignment=12, repr_limit=1024),)>>
>>> import os
>>> os.path.join("a", "b")
         /usr/lib/python3.6/posixpath.py:75    call      => join(a='a')
         /usr/lib/python3.6/posixpath.py:80    line         a = os.fspath(a)
         /usr/lib/python3.6/posixpath.py:81    line         sep = _get_sep(a)
         /usr/lib/python3.6/posixpath.py:41    call         => _get_sep(path='a')
         /usr/lib/python3.6/posixpath.py:42    line            if isinstance(path, bytes):
         /usr/lib/python3.6/posixpath.py:45    line            return '/'
         /usr/lib/python3.6/posixpath.py:45    return       <= _get_sep: '/'
         /usr/lib/python3.6/posixpath.py:82    line         path = a
         /usr/lib/python3.6/posixpath.py:83    line         try:
         /usr/lib/python3.6/posixpath.py:84    line         if not p:
         /usr/lib/python3.6/posixpath.py:86    line         for b in map(os.fspath, p):
         /usr/lib/python3.6/posixpath.py:87    line         if b.startswith(sep):
         /usr/lib/python3.6/posixpath.py:89    line         elif not path or path.endswith(sep):
         /usr/lib/python3.6/posixpath.py:92    line         path += sep + b
         /usr/lib/python3.6/posixpath.py:86    line         for b in map(os.fspath, p):
         /usr/lib/python3.6/posixpath.py:96    line         return path
         /usr/lib/python3.6/posixpath.py:96    return    <= join: 'a/b'
'a/b'
>>> 
```


### 9 - Lispi

- Using python features, writing a lisp interpreter becomes easy
- https://repl.it/talk/learn/PyLisp-LISP-in-Just-Over-100-Lines-of-Python/6712
- This seems very similar to what CPython abstracted over C.

TODO : ~~debug~~ VSCode debugging mode is awesome. 

```python
import re

class Lispi():

    def __init__(self):
        def gen_lambda(sign):
            lamfunc = lambda args: eval(str(args[0]) + sign + str(args[1]))
            return lamfunc


        self.env = {
                '==' : gen_lambda('=='),
                '!=' : gen_lambda('!='),
                '<'  : gen_lambda('<'),
                '<=' : gen_lambda('<='),
                '>'  : gen_lambda('>'),
                '>=' : gen_lambda('>='),
                '+'  : gen_lambda('+'),
                '-'  : gen_lambda('-'),
                '*'  : gen_lambda('*'),
                '/'  : gen_lambda('/'),
                'car': lambda args: args[0][0],
                'cdr': lambda args: args[0][1:],
                'cons': lambda args: [args[0]] + args[1]
            }

    def run(self, code):
        # print('run called : ' + code)
        return self.eval(self.parse(code))

    def parse(self, program):
        # print('parse called : ' + program)
        return self.read(self.tokenize(program))

    def tokenize(self, chars):
        # print('tokenize called: ' + chars)
        tokens = re.sub(r'\s+' , ' ' , chars) 
        tokens = tokens.replace('(' , ' ( ')
        tokens = tokens.replace(')' , ' ) ')
        tokens = tokens.split(' ')
        return [t for t in tokens if t != '' ]


    def read(self, tokens):
        
        # print('read called: ' + str(tokens))
        
        if not tokens:
            return
        token = tokens.pop(0)
        if token == '(' :
            token_list = []
            while tokens[0] != ')':
                token_list.append(self.read(tokens)) # this way it creates recursive structure , a list of list of list of list .....
            tokens.pop(0) # for the )
            return token_list
        elif token == ')':
            raise SyntaxError('unexpected bracket')
        else:
            return self.atom(token)


    def atom(self, token):
        
        if re.compile('\d+').match(token):
            # print("matched " + token)
            return int(token)
        else:
            return token

    def eval(self, exp , env = None):
        # print('eval called : ' + str(exp))

        if env is None:
            env = self.env

        if not exp:
            return

        if isinstance(exp, int):
            return exp
        elif isinstance(exp, str):
            try:
                return env[exp]
            except KeyError:
                return exp
        elif exp[0] == 'if':
            _ , condition, if_clause , else_clause = exp
            condition = str(self.eval(condition))
            result = eval(if_clause,env) if eval(condition,env) else eval(else_clause,env)
            return result

        elif exp[0] == 'define':
            _ , var , e = exp
            env[var] = self.eval(e)
            return env[var]

        elif exp[0] == 'lambda':
            _, params, body  = exp
            return lambda args : self.eval(body, { **env , **dict(zip(params, args)) })

        else:
            # print('fell here ' + str(type(exp)) + " " + str(exp))
            fn = exp[0]
            args = exp[1:]
            args = [self.eval(arg, env) for arg in args]
            return env[fn](args)


    def repl(self):
        while True:
            program = input('%>> ')
            try:
                print(self.run(program))
            except RuntimeError as err:
                print(err)


if __name__ == '__main__':
    lisp = Lispi()
    lisp.repl()
```

Test run:
```bash
$ python3 lispi.py
%>> (define pi 3)
3
%>> (define square ( lambda (x) ( * x x ) ) )
<function Lispi.eval.<locals>.<lambda> at 0x7f142c735ea0>
%>> (define circle-area (lambda (r) ( * pi (square r))))
<function Lispi.eval.<locals>.<lambda> at 0x7f142c6ff400>
%>> (circle-area 10)
300
%>>
```

### 8 - Checking if a function is Async or not

```python
import asyncio

def isAsync(someFunc):
    return asyncio.iscoroutinefunction(someFunc) # it uses inspects iscoroutineblah internally probably
```

- some better approaches here : https://stackoverflow.com/questions/36076619/test-if-function-or-method-is-normal-or-asynchronous

### 7 - Inspect

```python
inspect.ismodule(object)
inspect.isclass(object)
inspect.ismethod(object)
inspect.isfunction(object)
inspect.iscode(object)
inspect.iscoroutinefunction()

inspect.getdoc(object)
inspect.getcomments(object)
inspect.getfile(object) 
inspect.getmodule(object)
```

NOTE: There is no inspect.iscallable, but there is a builins.callble, which is already preloaded. 
```python
>> callable(object) 
True
>> import builtins
>> builtins.callable(object)
True
>> callable is buildins.callable
True
```

or better do:
```python
>>> print(* list(filter(lambda x : x.startswith('is') , dir(inspect))), sep='\n')
isabstract
isasyncgen
isasyncgenfunction
isawaitable
isbuiltin
isclass
iscode
iscoroutine
iscoroutinefunction
isdatadescriptor
isframe
isfunction
isgenerator
isgeneratorfunction
isgetsetdescriptor
ismemberdescriptor
ismethod
ismethoddescriptor
ismodule
isroutine
istraceback
```
- Inspect is really cool module 

### 6 - from modulefinder import ModuleFinder

```python
#test.py
import os
import sys
import traceback
import modulefinder
import google
import datetime

print("hello world")
```

```python
$ python3
Python 3.6.6 (default, Sep 12 2018, 18:26:19) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import sys, modulefinder
>>> finder = modulefinder.ModuleFinder()
>>> finder.run_script('test.py')
>>> finder.report()

  Name                      File
  ----                      ----
m __future__                /usr/lib/python3.6/__future__.py
m __main__                  test.py
m _ast                      
m _bisect                   
m _blake2                   
m _bootlocale               /usr/lib/python3.6/_bootlocale.py
m _bz2                      /usr/lib/python3.6/lib-dynload/_bz2.cpython-36m-x86_64-linux-gnu.so
m _codecs                   
m _collections              
m _collections_abc          /usr/lib/python3.6/_collections_abc.py
m _compat_pickle            /usr/lib/python3.6/_compat_pickle.py
m _compression              /usr/lib/python3.6/_compression.py
m _datetime                 
m _dummy_thread             /usr/lib/python3.6/_dummy_thread.py
m _functools                
m _hashlib                  /usr/lib/python3.6/lib-dynload/_hashlib.cpython-36m-x86_64-linux-gnu.so
m _heapq                    
m _imp                      
m _io                       
m _locale                   
m _lzma                     /usr/lib/python3.6/lib-dynload/_lzma.cpython-36m-x86_64-linux-gnu.so
m _md5                      
m _opcode                   /usr/lib/python3.6/lib-dynload/_opcode.cpython-36m-x86_64-linux-gnu.so
m _operator                 
m _pickle                   
m _posixsubprocess          
m _random                   
m _sha1                     
m _sha256                   
m _sha3                     
m _sha512                   
m _signal                   
m _socket                   
m _sre                      
m _ssl                      /usr/lib/python3.6/lib-dynload/_ssl.cpython-36m-x86_64-linux-gnu.so
m _stat                     
m _string                   
m _strptime                 /usr/lib/python3.6/_strptime.py
m _struct                   
m _thread                   
m _threading_local          /usr/lib/python3.6/_threading_local.py
m _tracemalloc              
m _warnings                 
m _weakref                  
m _weakrefset               /usr/lib/python3.6/_weakrefset.py
m abc                       /usr/lib/python3.6/abc.py
m argparse                  /usr/lib/python3.6/argparse.py
m ast                       /usr/lib/python3.6/ast.py
m atexit                    
m base64                    /usr/lib/python3.6/base64.py
m bdb                       /usr/lib/python3.6/bdb.py
m binascii                  
m bisect                    /usr/lib/python3.6/bisect.py
m builtins                  
m bz2                       /usr/lib/python3.6/bz2.py
m calendar                  /usr/lib/python3.6/calendar.py
m cmd                       /usr/lib/python3.6/cmd.py
m code                      /usr/lib/python3.6/code.py
m codecs                    /usr/lib/python3.6/codecs.py
m codeop                    /usr/lib/python3.6/codeop.py
P collections               /usr/lib/python3.6/collections/__init__.py
m collections.abc           /usr/lib/python3.6/collections/abc.py
m contextlib                /usr/lib/python3.6/contextlib.py
m copy                      /usr/lib/python3.6/copy.py
m copyreg                   /usr/lib/python3.6/copyreg.py
m datetime                  /usr/lib/python3.6/datetime.py
m difflib                   /usr/lib/python3.6/difflib.py
m dis                       /usr/lib/python3.6/dis.py
m doctest                   /usr/lib/python3.6/doctest.py
m dummy_threading           /usr/lib/python3.6/dummy_threading.py
P email                     /usr/lib/python3.6/email/__init__.py
m email._encoded_words      /usr/lib/python3.6/email/_encoded_words.py
m email._header_value_parser /usr/lib/python3.6/email/_header_value_parser.py
m email._parseaddr          /usr/lib/python3.6/email/_parseaddr.py
m email._policybase         /usr/lib/python3.6/email/_policybase.py
m email.base64mime          /usr/lib/python3.6/email/base64mime.py
m email.charset             /usr/lib/python3.6/email/charset.py
m email.contentmanager      /usr/lib/python3.6/email/contentmanager.py
m email.encoders            /usr/lib/python3.6/email/encoders.py
m email.errors              /usr/lib/python3.6/email/errors.py
m email.feedparser          /usr/lib/python3.6/email/feedparser.py
m email.generator           /usr/lib/python3.6/email/generator.py
m email.header              /usr/lib/python3.6/email/header.py
m email.headerregistry      /usr/lib/python3.6/email/headerregistry.py
m email.iterators           /usr/lib/python3.6/email/iterators.py
m email.message             /usr/lib/python3.6/email/message.py
m email.parser              /usr/lib/python3.6/email/parser.py
m email.policy              /usr/lib/python3.6/email/policy.py
m email.quoprimime          /usr/lib/python3.6/email/quoprimime.py
m email.utils               /usr/lib/python3.6/email/utils.py
P encodings                 /usr/lib/python3.6/encodings/__init__.py
m encodings.aliases         /usr/lib/python3.6/encodings/aliases.py
m encodings.mbcs            /usr/lib/python3.6/encodings/mbcs.py
m enum                      /usr/lib/python3.6/enum.py
m errno                     
m fnmatch                   /usr/lib/python3.6/fnmatch.py
m functools                 /usr/lib/python3.6/functools.py
m gc                        
m genericpath               /usr/lib/python3.6/genericpath.py
m getopt                    /usr/lib/python3.6/getopt.py
m gettext                   /usr/lib/python3.6/gettext.py
m glob                      /usr/lib/python3.6/glob.py
m grp                       
m gzip                      /usr/lib/python3.6/gzip.py
m hashlib                   /usr/lib/python3.6/hashlib.py
m heapq                     /usr/lib/python3.6/heapq.py
P html                      /usr/lib/python3.6/html/__init__.py
m html.entities             /usr/lib/python3.6/html/entities.py
P http                      /usr/lib/python3.6/http/__init__.py
m http.client               /usr/lib/python3.6/http/client.py
m http.server               /usr/lib/python3.6/http/server.py
m imp                       /usr/lib/python3.6/imp.py
P importlib                 /usr/lib/python3.6/importlib/__init__.py
m importlib._bootstrap      /usr/lib/python3.6/importlib/_bootstrap.py
m importlib._bootstrap_external /usr/lib/python3.6/importlib/_bootstrap_external.py
m importlib.abc             /usr/lib/python3.6/importlib/abc.py
m importlib.machinery       /usr/lib/python3.6/importlib/machinery.py
m importlib.util            /usr/lib/python3.6/importlib/util.py
m inspect                   /usr/lib/python3.6/inspect.py
m io                        /usr/lib/python3.6/io.py
m ipaddress                 /usr/lib/python3.6/ipaddress.py
m itertools                 
m keyword                   /usr/lib/python3.6/keyword.py
m linecache                 /usr/lib/python3.6/linecache.py
m locale                    /usr/lib/python3.6/locale.py
P logging                   /usr/lib/python3.6/logging/__init__.py
m lzma                      /usr/lib/python3.6/lzma.py
m marshal                   
m math                      
m mimetypes                 /usr/lib/python3.6/mimetypes.py
m modulefinder              /usr/lib/python3.6/modulefinder.py
m ntpath                    /usr/lib/python3.6/ntpath.py
m opcode                    /usr/lib/python3.6/opcode.py
m operator                  /usr/lib/python3.6/operator.py
m optparse                  /usr/lib/python3.6/optparse.py
m os                        /usr/lib/python3.6/os.py
m pdb                       /usr/lib/python3.6/pdb.py
m pickle                    /usr/lib/python3.6/pickle.py
m pkgutil                   /usr/lib/python3.6/pkgutil.py
m platform                  /usr/lib/python3.6/platform.py
m plistlib                  /usr/lib/python3.6/plistlib.py
m posix                     
m posixpath                 /usr/lib/python3.6/posixpath.py
m pprint                    /usr/lib/python3.6/pprint.py
m pwd                       
m py_compile                /usr/lib/python3.6/py_compile.py
m pydoc                     /usr/lib/python3.6/pydoc.py
P pydoc_data                /usr/lib/python3.6/pydoc_data/__init__.py
m pydoc_data.topics         /usr/lib/python3.6/pydoc_data/topics.py
m pyexpat                   
m quopri                    /usr/lib/python3.6/quopri.py
m random                    /usr/lib/python3.6/random.py
m re                        /usr/lib/python3.6/re.py
m readline                  /usr/lib/python3.6/lib-dynload/readline.cpython-36m-x86_64-linux-gnu.so
m reprlib                   /usr/lib/python3.6/reprlib.py
m select                    
m selectors                 /usr/lib/python3.6/selectors.py
m shlex                     /usr/lib/python3.6/shlex.py
m shutil                    /usr/lib/python3.6/shutil.py
m signal                    /usr/lib/python3.6/signal.py
m socket                    /usr/lib/python3.6/socket.py
m socketserver              /usr/lib/python3.6/socketserver.py
m sre_compile               /usr/lib/python3.6/sre_compile.py
m sre_constants             /usr/lib/python3.6/sre_constants.py
m sre_parse                 /usr/lib/python3.6/sre_parse.py
m ssl                       /usr/lib/python3.6/ssl.py
m stat                      /usr/lib/python3.6/stat.py
m string                    /usr/lib/python3.6/string.py
m struct                    /usr/lib/python3.6/struct.py
m subprocess                /usr/lib/python3.6/subprocess.py
m sys                       
m tarfile                   /usr/lib/python3.6/tarfile.py
m tempfile                  /usr/lib/python3.6/tempfile.py
m termios                   /usr/lib/python3.6/lib-dynload/termios.cpython-36m-x86_64-linux-gnu.so
m textwrap                  /usr/lib/python3.6/textwrap.py
m threading                 /usr/lib/python3.6/threading.py
m time                      
m token                     /usr/lib/python3.6/token.py
m tokenize                  /usr/lib/python3.6/tokenize.py
m traceback                 /usr/lib/python3.6/traceback.py
m tracemalloc               /usr/lib/python3.6/tracemalloc.py
m tty                       /usr/lib/python3.6/tty.py
m types                     /usr/lib/python3.6/types.py
P unittest                  /usr/lib/python3.6/unittest/__init__.py
m unittest.case             /usr/lib/python3.6/unittest/case.py
m unittest.loader           /usr/lib/python3.6/unittest/loader.py
m unittest.main             /usr/lib/python3.6/unittest/main.py
m unittest.result           /usr/lib/python3.6/unittest/result.py
m unittest.runner           /usr/lib/python3.6/unittest/runner.py
m unittest.signals          /usr/lib/python3.6/unittest/signals.py
m unittest.suite            /usr/lib/python3.6/unittest/suite.py
m unittest.util             /usr/lib/python3.6/unittest/util.py
P urllib                    /usr/lib/python3.6/urllib/__init__.py
m urllib.parse              /usr/lib/python3.6/urllib/parse.py
m uu                        /usr/lib/python3.6/uu.py
m warnings                  /usr/lib/python3.6/warnings.py
m weakref                   /usr/lib/python3.6/weakref.py
m webbrowser                /usr/lib/python3.6/webbrowser.py
P xml                       /usr/lib/python3.6/xml/__init__.py
P xml.parsers               /usr/lib/python3.6/xml/parsers/__init__.py
m xml.parsers.expat         /usr/lib/python3.6/xml/parsers/expat.py
m zipfile                   /usr/lib/python3.6/zipfile.py
m zipimport                 
m zlib                      

Missing modules:
? _dummy_threading imported from dummy_threading
? _frozen_importlib imported from importlib, importlib.abc
? _frozen_importlib_external imported from importlib, importlib._bootstrap, importlib.abc
? _winapi imported from subprocess
? _winreg imported from platform
? google imported from __main__
? java.lang imported from platform
? msvcrt imported from subprocess
? nt imported from ntpath, os, shutil
? org.python.core imported from copy, pickle
? os.path imported from os, pkgutil, py_compile, tracemalloc, unittest, unittest.util
? vms_lib imported from platform
? winreg imported from mimetypes, platform
```


### 4 - Listing only user-imported modules

```python
Python 3.6.6 (default, Sep 12 2018, 18:26:19) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import sys
>>> set(globals())&set(sys.modules)
{'sys'}
>>> import google
>>> set(globals())&set(sys.modules)
{'sys', 'google'}
>>> 
```
another way:
```python
>>> x = dir()
>>> x = list(dir())
>>> import numpy
>>> y = list(dir())
>>> set(x) - set(y)
set()
>>> set(y) - set(x)
{'numpy'}
>>> 
```

### 3 - default module  and module search paths

- All global (variable/function) names in Python are considered to be in the pseudo-module namespace named ```__main__```.
```python
Python 3.6.6 (default, Sep 12 2018, 18:26:19) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> print(dir())
['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__']
>>> print(dir('__main__')
... )
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
>>> 
```
- module search path
```python
Python 3.6.6 (default, Sep 12 2018, 18:26:19) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import sys,pprint
>>> pprint.pprint(sys.path)
['',
 '/usr/lib/python36.zip',
 '/usr/lib/python3.6',
 '/usr/lib/python3.6/lib-dynload',
 '/home/current_user/.local/lib/python3.6/site-packages',
 '/usr/local/lib/python3.6/dist-packages',
 '/usr/lib/python3/dist-packages']
>>> 
```



### 2 - listing modules

loaded:
```python
Python 3.6.6 (default, Sep 12 2018, 18:26:19) 
[GCC 8.0.1 20180414 (experimental) [trunk revision 259383]] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import sys
>>> sys.modules
{'builtins': <module 'builtins' (built-in)>, 'sys': <module 'sys' (built-in)>, '_frozen_importlib': <module 'importlib._bootstrap' (frozen)>, '_imp': <module '_imp' (built-in)>, '_warnings': <module '_warnings' (built-in)>, '_thread': <module '_thread' (built-in)>, '_weakref': <module '_weakref' (built-in)>, '_frozen_importlib_external': <module 'importlib._bootstrap_external' (frozen)>, '_io': <module 'io' (built-in)>, 'marshal': <module 'marshal' (built-in)>, 'posix': <module 'posix' (built-in)>, 'zipimport': <module 'zipimport' (built-in)>, 'encodings': <module 'encodings' from '/usr/lib/python3.6/encodings/__init__.py'>, 'codecs': <module 'codecs' from '/usr/lib/python3.6/codecs.py'>, '_codecs': <module '_codecs' (built-in)>, 'encodings.aliases': <module 'encodings.aliases' from '/usr/lib/python3.6/encodings/aliases.py'>, 'encodings.utf_8': <module 'encodings.utf_8' from '/usr/lib/python3.6/encodings/utf_8.py'>, '_signal': <module '_signal' (built-in)>, '__main__': <module '__main__' (built-in)>, 'encodings.latin_1': <module 'encodings.latin_1' from '/usr/lib/python3.6/encodings/latin_1.py'>, 'io': <module 'io' from '/usr/lib/python3.6/io.py'>, 'abc': <module 'abc' from '/usr/lib/python3.6/abc.py'>, '_weakrefset': <module '_weakrefset' from '/usr/lib/python3.6/_weakrefset.py'>, 'site': <module 'site' from '/usr/lib/python3.6/site.py'>, 'os': <module 'os' from '/usr/lib/python3.6/os.py'>, 'errno': <module 'errno' (built-in)>, 'stat': <module 'stat' from '/usr/lib/python3.6/stat.py'>, '_stat': <module '_stat' (built-in)>, 'posixpath': <module 'posixpath' from '/usr/lib/python3.6/posixpath.py'>, 'genericpath': <module 'genericpath' from '/usr/lib/python3.6/genericpath.py'>, 'os.path': <module 'posixpath' from '/usr/lib/python3.6/posixpath.py'>, '_collections_abc': <module '_collections_abc' from '/usr/lib/python3.6/_collections_abc.py'>, '_sitebuiltins': <module '_sitebuiltins' from '/usr/lib/python3.6/_sitebuiltins.py'>, 'sysconfig': <module 'sysconfig' from '/usr/lib/python3.6/sysconfig.py'>, '_sysconfigdata_m_linux_x86_64-linux-gnu': <module '_sysconfigdata_m_linux_x86_64-linux-gnu' from '/usr/lib/python3.6/_sysconfigdata_m_linux_x86_64-linux-gnu.py'>, '_bootlocale': <module '_bootlocale' from '/usr/lib/python3.6/_bootlocale.py'>, '_locale': <module '_locale' (built-in)>, 'types': <module 'types' from '/usr/lib/python3.6/types.py'>, 'functools': <module 'functools' from '/usr/lib/python3.6/functools.py'>, '_functools': <module '_functools' (built-in)>, 'collections': <module 'collections' from '/usr/lib/python3.6/collections/__init__.py'>, 'operator': <module 'operator' from '/usr/lib/python3.6/operator.py'>, '_operator': <module '_operator' (built-in)>, 'keyword': <module 'keyword' from '/usr/lib/python3.6/keyword.py'>, 'heapq': <module 'heapq' from '/usr/lib/python3.6/heapq.py'>, '_heapq': <module '_heapq' (built-in)>, 'itertools': <module 'itertools' (built-in)>, 'reprlib': <module 'reprlib' from '/usr/lib/python3.6/reprlib.py'>, '_collections': <module '_collections' (built-in)>, 'weakref': <module 'weakref' from '/usr/lib/python3.6/weakref.py'>, 'collections.abc': <module 'collections.abc' from '/usr/lib/python3.6/collections/abc.py'>, 'importlib': <module 'importlib' from '/usr/lib/python3.6/importlib/__init__.py'>, 'importlib._bootstrap': <module 'importlib._bootstrap' (frozen)>, 'importlib._bootstrap_external': <module 'importlib._bootstrap_external' (frozen)>, 'warnings': <module 'warnings' from '/usr/lib/python3.6/warnings.py'>, 'importlib.util': <module 'importlib.util' from '/usr/lib/python3.6/importlib/util.py'>, 'importlib.abc': <module 'importlib.abc' from '/usr/lib/python3.6/importlib/abc.py'>, 'importlib.machinery': <module 'importlib.machinery' from '/usr/lib/python3.6/importlib/machinery.py'>, 'contextlib': <module 'contextlib' from '/usr/lib/python3.6/contextlib.py'>, 'mpl_toolkits': <module 'mpl_toolkits' (namespace)>, 'zope': <module 'zope' from '/usr/lib/python3/dist-packages/zope/__init__.py'>, 'sitecustomize': <module 'sitecustomize' from '/usr/lib/python3.6/sitecustomize.py'>, 'apport_python_hook': <module 'apport_python_hook' from '/usr/lib/python3/dist-packages/apport_python_hook.py'>, 'readline': <module 'readline' from '/usr/lib/python3.6/lib-dynload/readline.cpython-36m-x86_64-linux-gnu.so'>, 'atexit': <module 'atexit' (built-in)>, 'rlcompleter': <module 'rlcompleter' from '/usr/lib/python3.6/rlcompleter.py'>}
>>> sys.modules.keys()
dict_keys(['builtins', 'sys', '_frozen_importlib', '_imp', '_warnings', '_thread', '_weakref', '_frozen_importlib_external', '_io', 'marshal', 'posix', 'zipimport', 'encodings', 'codecs', '_codecs', 'encodings.aliases', 'encodings.utf_8', '_signal', '__main__', 'encodings.latin_1', 'io', 'abc', '_weakrefset', 'site', 'os', 'errno', 'stat', '_stat', 'posixpath', 'genericpath', 'os.path', '_collections_abc', '_sitebuiltins', 'sysconfig', '_sysconfigdata_m_linux_x86_64-linux-gnu', '_bootlocale', '_locale', 'types', 'functools', '_functools', 'collections', 'operator', '_operator', 'keyword', 'heapq', '_heapq', 'itertools', 'reprlib', '_collections', 'weakref', 'collections.abc', 'importlib', 'importlib._bootstrap', 'importlib._bootstrap_external', 'warnings', 'importlib.util', 'import
```

for all installed modules:
```bash
pydoc3 modules
```

### 1 - listing builtins

- Python3 has only dunder builtins but python2 has dunder builtin and dunder builtins

```python
>>> dir(__builtins__)
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'ZeroDivisionError', '_', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip']
```
- printing them better using zip and iter style grouping
```python
>>> print(*list(zip(*(iter(dir(__builtins__)),) * 8)),sep='\n')
('ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning')
('ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis')
('EnvironmentError', 'Exception', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit')
('IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError')
('KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented')
('NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError')
('ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError')
('SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError')
('UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'ZeroDivisionError', '_')
('__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__')
('abs', 'all', 'any', 'ascii', 'bin', 'bool', 'bytearray', 'bytes')
('callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr')
('dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter')
('float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help')
('hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len')
('license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next')
('object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit')
('range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted')
('staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip')
```


