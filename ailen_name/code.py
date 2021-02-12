import re

# size = int(input())
m = r'^([_|\.])(\d+)([a-zA-Z]*)(_)?$'
# m = r'^([_|\.])(\d+)([a-z]*|[A-Z]*)'

lst = [".551001777yBnuSHKYiHVZXRfmU_","_781088233454618218bi"]
size = len(lst)

for _ in range(size):
    # st = input()
    st = lst[_]s
    match = re.search(m,st)
    if match :
        print(st)
        print(match.groups())
        print("VALID")
    else:
        print(st)
        print("INVALID")
