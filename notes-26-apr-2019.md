# 26-apr-2019


### 1 - server/client in bash for quick use


client:
```bash
#!/bin/sh

while true; do
  msg="$(date '+%Y-%m-%d %H:%M:%S') hello from ${HOSTNAME}"
  echo ${msg}
  echo ${msg} | nc -w 1 localhost 4242
  sleep 1
done;
```


server:
```bash
#!/bin/sh

port="4242"
echo "starting server on ${port}"

while true; do 
  nc -l -p ${port} -vv -k -q 60
done;
```
