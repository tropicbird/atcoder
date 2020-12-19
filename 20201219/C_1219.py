N = int(input())

ls=[]
for i in range(1,N+1):
    tmp=list(str(i))
    if '7' in tmp:
        ls.append(i)
#print(ls)

ls_oct=[]
for i in range(1,N+1):
    tmp=list(str(oct(i)))
    if '7' in tmp:
        ls_oct.append(i)
#print(ls_oct)

ans=ls+ls_oct
ans=set(ans)
#print(len(ans))
print(N-len(ans))