import re

b = "C:CPP:JAVA:PYTHON:PERL:PHP:RUBY:CSHARP:HASKELL:CLOJURE:BASH:SCALA:ERLANG:CLISP:LUA:BRAINFUCK:JAVASCRIPT:GO:D:OCAML:R:PASCAL:SBCL:DART:GROOVY:OBJECTIVEC".replace(":","|")

m = r'^[0-9]+\s('+b+')$'

# print(m)

sz = int(input())
# # # # # # # # # # # # 
# sz = 3
# st_lst = [
#     "11011 C",
#     "11022 CPP",
#     "11044 X"
# ]
# # # # # # # # # # #

for _ in range(sz):
    st = input()
    # # st = st_lst[_]
    match = re.search(m,st)
    if match:
        print("VALID")
    else :
        print("INVALID")
        
