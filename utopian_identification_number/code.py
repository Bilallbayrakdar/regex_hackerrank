import re

m = r'^[a-z]{0,3}[\d]{2,8}[A-Z]{3,}$'

size = int(input())

for _ in range(size):
    st = input()
    if re.search(m,st):
        print("VALID")
    else:
        print("INVALID")

