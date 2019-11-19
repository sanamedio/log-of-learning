import os
import re

mds = [ md for md in os.listdir("./notes/") if md.endswith(".md") ]


result = []
k = 1
for md in mds:

    data = open("./notes/"+md).readlines()


    for line in data:
        if re.search("### \d+ - ", line.strip()):
            result += [ ("|"+ str(k)  + "|["+line.strip().split(" - ",1)[1] + "](./notes/"+ md +") |")]
            k = k+1




prefix = """
# =================
# programming-notes
# =================

### """+ str(k-1) + """/100000

| ID  | NAME |
| ------------- | ------------- |
"""


print (prefix + "\n".join(list(reversed(result))))
