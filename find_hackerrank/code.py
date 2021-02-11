import re

# res = ["i love hackerrank","hackerrank is an awesome place for programmers","hackerrank","i think hackerrank is a great place to hangout"]


size = int(input())

for _ in range(size):
    st = input()
    # st = res[_]
    # st = "hackerrank"
    if re.search(r'^(hackerrank)(.*hackerrank)?$', st) :
    
        print(0)
    elif re.search(r'(.|\s)+(hackerrank)$', st) :
        print(2)
    elif re.search(r'^(hackerrank)(.|\s)*', st) :
        print(1)
    else:
        print(-1)

