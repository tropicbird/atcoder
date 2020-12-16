# N, X, T = map(int, input().split())
import numpy as np
N = int(input())
L = list(map(int, input().split()))
# L = [list(map(int, input().split())) for i in range(N)]

ans1=0
for i in L:
    ans1+=abs(i)

ans2=0
for i in L:
    ans2+=i**2
ans2=np.round(np.sqrt(ans2),11)


mi=np.min(L)
ma=np.max(L)
mi=abs(mi)
ma=abs(ma)
ls=[mi,ma]
ans3=np.max(ls)



print(ans1)
print(ans2)
print(ans3)