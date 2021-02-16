import re

m = r'^[A-Z]{5}[0-9]{4}[A-Z]$'
sz = int(input())

# sz =3
# st_lst =[
#     "ABCDS1234Y",
#     "ABAB12345Y",
#     "avCDS1234Y"
# ]

for _ in range(sz):
    st = input()
    # st = st_lst[_]
    match = re.search(m,st)
    if match:
        print("YES")
    else:
        print("NO")