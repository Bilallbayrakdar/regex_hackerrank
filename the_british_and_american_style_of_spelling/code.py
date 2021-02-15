import re

st = ""
sz = int(input())
for _ in range(sz):
    st += (" "+input())

c_sz = int(input())

m = r'([a-z]+)[sz]e\b'
# sz=8
# st_lst = [
#         "citizen mrs newly cream brother head unkind citizen sir catalyz",
#         "realize behalf plate person useless realize breathing band crop colonis",
#         "catalyze late unlike front also technical separated devoted prisoner afraid",
#         "rather colonise spider amount hello used recognize false disappointment statue",
#         "lack prepare cloth association recognise polish backwards paint bye multiply",
#         "used him strong outer alone maximum delighted realise lose damp",
#         "wild related freeze catalyse make red shot classic scratch tradition",
#         "car partly absorb internet fishing total old embarrassing materialise non"
#     ]

# ck_size = 7
# ck_lst = [
#         "recognize",
#         "colonize",
#         "paralyze",
#         "materialize",
#         "caramelize",
#         "catalyze",
#         "realize"]

# for _ in range(sz):
#     st += (" "+st_lst[_])

res = {}
match = re.findall(m,st)
m_set = set(match)

for ele in m_set:
    res[ele] = match.count(ele)

# for ele in ck_lst:
#     try:
#         print(res[ele[:-2]])
#     except:
#         print(0)

for i in range(c_sz):
    ts = input()
    try:
        print(res[ts[:-2]])
    except:
        print(0)