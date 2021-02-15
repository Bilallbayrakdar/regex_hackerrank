import re

t=r'([a-z]+our[a-z]*)?([a-z]+or[a-z]*)?'

st = "odour"

match = re.search(t,st)

print(match.groups())