N, K = map(int, input().split())
L = [list(map(int, input().split())) for i in range(N)]
ans=0
from itertools import permutations

p_list = list(permutations(range(1,N),N-1))
#print(p_list)
for i in p_list:
    total=0
    next=0
    for j in i:
        total+=L[next][j]
        next = j
    total += L[next][0]
    if total==K:
        ans+=1
print(ans)