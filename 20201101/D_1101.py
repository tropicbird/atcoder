S = str(int(input()))
if int(S)==8:
    print('Yes')
    exit()

tmp=""
if len(S)==2:
    if int(S)%8==0:
        print("Yes")
        exit()
    tmp=S[1]+S[0]
    if int(tmp)%8==0:
        print("Yes")
        exit()


ls=list(S)
import itertools
# for comb in itertools.permutations(ls):
#     length=len(comb)
#     string=""
#     for i in range(length):
#         string+=str(comb[i])
#     print(string)
#     if int(string)%8==0:
#         print("Yes")
#         exit()
# print("No")

from collections import Counter

# set_ls=set(ls)
# #print(set_ls)
# if len(set_ls)==1:
#     set_ls=list(set_ls)
#     set_ls=[set_ls[0],set_ls[0],set_ls[0]]
# elif len(set_ls)==2:
ls1=[]
ls2=[]
ls3=[]
c=Counter(ls)
for items in c.items():
    if items[1]>=3:
        ls3.append(items[0])
    if items[1]==2:
        ls2.append(items[0])
    if items[1]==1:
        ls1.append(items[0])

for i in ls3:
    string=str(i)+str(i)+str(i)
    if int(string)%8==0:
        print("Yes")
        exit()
for i in ls2:
    for j in set(ls3+ls1):
    set_comb = str(i) + str(i) + str(j)

for i in ls3:
    for j in set(ls2+ls1):
    set_comb = str(i) + str(i) + str(j)


print(set_ls)

set_comb=set(itertools.permutations(set_ls,3))
for comb in set_comb:
    length=len(comb)
    string=""
    for i in range(length):
        string+=str(comb[i])
    #print(string)
    if int(string)%8==0:
        print("Yes")
        exit()
print("No")

