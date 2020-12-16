N = int(input())
import sys
A_ls=[]
B_ls=[]
for i in range(1,38):
    A_ls.append(pow(3,i))

for j in range(1,26):
    B_ls.append(pow(5,j))

ans=-1
for i, A in enumerate(A_ls):
    for j, B in enumerate(B_ls):
        if A+B==N:
            ans=str(i+1)+" "+str(j+1)
            print(ans)
            sys.exit()
print(ans)