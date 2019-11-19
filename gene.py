import os
import re

mds = [ md for md in os.listdir(".") if md.endswith(".md") ]


result = []
k = 1
for md in mds:

    data = open(md).readlines()


    for line in data:
        if re.search("### \d+ - ", line.strip()):
            result += [ ("|"+ str(k)  + "|["+line.strip().split(" - ",1)[1] + "](./"+ md +") |")]
            k = k+1




prefix = """
# =================
# programming-notes
# =================

### """+ str(k) + """/100000

| ID  | NAME |
| ------------- | ------------- |
"""


print (prefix + "\n".join(list(reversed(result))))
