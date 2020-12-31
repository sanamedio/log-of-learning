import os
import re
from datetime import datetime

readme_file = open("README.md","w")

def override_print(x):
    readme_file.write(x+"\n")

print = override_print

BLOB_PATH="https://github.com/l0k3ndr/python-notes/blob/master/notes/"

mds = [ md for md in os.listdir("./notes/") if md.endswith(".md") ]

mds.sort(key = lambda date: datetime.strptime(date.split(".")[0].split("notes-")[1], '%d-%b-%Y')) 

date_arr = []

categories = []
result = []
k = 1

last_type = None


for md in mds:
    data = open("./notes/"+md).readlines()

    temp_res = []

    temp_content = []
    for line in data:
        if re.search("### \d+ - ", line.strip()):

            if last_type:
                categories += [last_type]
            else:
                categories += ["general"]
            last_type = None
            
            temp_res += [ ("["+(line.strip().split(" - ",1)[1]).capitalize() + "]("+ BLOB_PATH + md + "#" +  line.strip().lower().replace("###","")[1:].replace(" ","-").replace("?","").replace("(","").replace(")","").replace(",","").replace("_","") + ") ")]
            date_arr += [md.split(".md")[0].split("notes-")[1]]
            k = k+1

        if re.search("^```python", line.strip()) or re.search("python",line.strip(), re.IGNORECASE) or re.search("py", line.strip(), re.IGNORECASE):
            last_type = "python"

    result += list(temp_res)


if last_type:
    categories += [last_type]
else:
    categories += ["general"]
    last_type = None
categories = categories[1:]



prefix = """
# =================
# python-notes
# =================
"""

prefix_sub = """
| LINK |
|------|"""



#print (prefix + "\n".join(list(reversed([ "|" + str(i+1)+"|" + result[i] + "|" + date_arr[i] + "|" for i in range(len(result))]))))

print( prefix)

print("[ "+ str(len(result)) + " ]")

print (prefix_sub)
print ( "\n".join(list(reversed([ "|" +  result[i] + "|" for i in range(len(result))]))))

readme_file.close()
