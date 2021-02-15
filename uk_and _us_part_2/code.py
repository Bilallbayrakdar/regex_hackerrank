import re

st = ""
sz = int(input())
for _ in range(sz):
    st += (" "+input())

c_sz = int(input())

m = r'([a-z]+)o[u]?r([a-z]*)'

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# sz=10
# st_lst = [
#     "splendour wealth piece recognition savoury endeavour oil cannot reality fish",
#     "sincere savor argument vigour chain awake cap surprising savoury jump",
#     "natural study process immoral flag vigour habit assist candy pet",
#     "shoulder aside slightly onto crash later disagreement savour rumour entrance",
#     "splendour petrol unable inevitably crowd growth fasten leading responsibility artificially",
#     "equally alarmed also knowledge ok splendor armory pick sale be",
#     "activity rumour ending alcoholic savory curve splendour honestly enjoyable rumour",
#     "determined used rumor union affair odor granddaughter elect endeavor alter",
#     "savor hour enjoyable waiter divorce at mental prepared folding primary",
#     "cheaply vegetable upon splendor disease savor it cast hear cardboard"
#     ]

# c_sz = 9
# ck_lst = [
#         "endeavour",
#         "savoury",
#         "savour",
#         "vigour",
#         "valour",
#         "splendour",
#         "rumour",
#         "odour",
#         "armoury"
#     ]

# for _ in range(sz):
#     st += (" "+st_lst[_])
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


res = {}
match = [ele[0]+ele[1] for ele in re.findall(m,st)]

# print(match)

m_set = set(match)

for ele in m_set:
    res[ele] = match.count(ele)

t=r'([a-z]+our[a-z]*)?([a-z]+or[a-z]*)?'

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# for ele in ck_lst:
#     match = re.search(t,ele)
#     if match.groups()[0] is not None:
#         val = match.groups()[0].replace("our","")
#     elif match.groups()[1] is not None:
#         val = match.groups()[1].replace("or","")
#     try:
#         print(res[val])
#     except:
#         print(0)
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

for i in range(c_sz):
    ts = input()
    match = re.search(t,ts)
    if match.groups()[0] is not None:
        val = match.groups()[0].replace("our","")
    elif match.groups()[1] is not None:
        val = match.groups()[1].replace("or","")
    try:
        print(res[val])
    except:
        print(0)