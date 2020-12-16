A, B, C = map(int, input().split())
import numpy as np

from itertools import product
if A>divide:
    a_ls = list(range(A-divide, A + 1))
else:
    a_ls = list(range(1, A + 1))

if B>divide:
    b_ls = list(range(B-divide, B + 1))
else:
    b_ls = list(range(1, B + 1))

if C>divide:
    c_ls = list(range(C-divide, C + 1))
else:
    c_ls = list(range(1, C + 1))


compute4(N,M,L,a,b,c):
return np.dot(b*a,c)


divide=998244353
tmp=0
amari=0
for a in range(1,A+1):
    for b in range(1,B+1):
        for c in range(1,C+1):
            tmp=a*b*c
            amari+=tmp%divide

ans=amari%divide
print(ans)