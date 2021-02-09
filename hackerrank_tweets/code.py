import re

size = int(input())
m = r'([Hh]acker[Rr]ank)'
cnt =0
for _ in range(size):
    st = input()
    match = re.match(m,st)
    if match is not None:
      cnt+=1
print(cnt)
