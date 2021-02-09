import re
import sys
file = open("data.txt","r")
data =file.read()



line = ""

amount=-1

for ele in data:
    if ele != "\n":
        line += ele
    else:
        if amount==-1:
            amount=line
        else:
            pattern = r'([\d]{1,3})([-\s])?([\d]{1,3})\2([\d]{4,10})'
            match=re.fullmatch(pattern,line)
            if match is not None:
                print("CountryCode={a},LocalAreacode={b},Number={c}".format(a=match.groups()[0],b=match.groups()[2],c=match.groups()[3]))
        line=""