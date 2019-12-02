import os
import re
from datetime import datetime


mds = [ md for md in os.listdir("./notes/") if md.endswith(".md") ]

mds.sort(key = lambda date: datetime.strptime(date.split(".")[0].split("notes-")[1], '%d-%b-%Y')) 

date_arr = []

result = []
k = 1
for md in mds:
    data = open("./notes/"+md).readlines()

    temp_res = []
    for line in data:
        if re.search("### \d+ - ", line.strip()):
            temp_res += [ ("["+(line.strip().split(" - ",1)[1]).capitalize() + "](./notes/"+ md +") ")]
            date_arr += [md.split(".md")[0].split("notes-")[1]]
            k = k+1
    result += list(reversed(temp_res))




prefix = """
# =================
# programming-notes
# =================

### """+ str(k-1) + """/100000

| SNO | LINK| DATE |
|-----|----|-----|
"""


print (prefix + "\n".join(list(reversed([ "|" + str(i+1)+"|" + result[i] + "|" + date_arr[i] + "|" for i in range(len(result))]))))
