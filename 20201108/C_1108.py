N = str(input())
L=[int(n) for n in N]
if int(N)%3==0:
    print(0)
    exit()

from collections import Counter

amari_l=[]
for i in L:
    amari=i%3
    amari_l.append(amari)

S=Counter(amari_l)

sum_all=sum(L)

if len(L)==1:
    print(-1)
    exit()

if sum_all<3:
    print(-1)
    exit()
amari_all=sum_all%3
if amari_all==1:
    if S[1]!=0:
        print(1)
        exit()
    elif S[2]>1:
        if len(L)==2:
            print(-1)
            exit()
        print(2)
        exit()
if amari_all==2:
    if S[2]!=0:
        print(1)
        exit()
    elif S[1]>1:
        if len(L)==2:
            print(-1)
            exit()
        print(2)
        exit()
print(-1)