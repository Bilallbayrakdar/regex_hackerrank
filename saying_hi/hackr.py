import re
# file = open("data.txt", "r")
# data = file.read()

size = int(input())

m = r'^[hH][iI][\s][^dD]'

# data = str(data).split("\n")

for _ in range(size):
    st = input()
    match = re.match(m,st)
    if match is not None:
        print(st)