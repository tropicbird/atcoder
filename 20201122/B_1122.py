N, X = map(int, input().split())
S = str(input())

tmp=X
while len(S)>0:
    now=S[0]
    S=S[1:]

    if now=='x':
        tmp-=1
        if tmp==-1:
            tmp=0
    else:
        tmp+=1
print(tmp)
