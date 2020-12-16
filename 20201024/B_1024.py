N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
CD = [list(map(int, input().split())) for i in range(M)]
import sys

ls=[]
for y in CD:
    #print(y)
    for z in y:
        #print(z)
        ls.append(z)

ls=list(set(ls))

alones=set(list(range(1,N+1)))-set(ls)

for i in alones:
    if A[i-1]!=B[i-1]:
        print(i)
        print("No")
        sys.exit()

keep_ls= []
for k in ls:
    keep = []
    for cd in CD:
        if k == cd[0]:
            for cd2 in CD:
                if cd[1]==cd2

            keep.extend(cd)
        elif k == cd[1]:
            keep.extend(cd)
    keep_ls.append(keep)

print(keep_ls)


# print(N)
# print(M)
# print(A)
# print(B)
# print(CD)

