import  re

m = r'^([+]|[-])?((([0-9]|([1-8][0-9]))([\.][\d]+)?)|90(\.0+)?),\s*([+]|[-])?((([0-9]|([1-9][0-9])|(1[0-7][0-9]))([\.][\d]+)?)|180(\.0+)?)$'

size = int(input())

for _ in range(size) :
    st = input()
    if re.search(m,st.replace("(","").replace(")","")):
        print("Valid")
    else:
        print("Invalid")