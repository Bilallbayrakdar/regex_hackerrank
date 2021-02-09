import re
file = open("data.txt", "r")
data = file.read()
m = r'^[hH][iI][\s][^dD]'

data = str(data).split("\n")

for ele in data:
    print(ele)
    match = re.match(m,ele)
    if match is not None:
        print(ele)