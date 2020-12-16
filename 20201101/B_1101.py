N = int(input())
L = [list(map(int, input().split())) for i in range(N)]
ans=0
for AB in L:
    all=AB[1]*(AB[1]+1)/2
    first=(AB[0]-1)*(AB[0])/2
    ans+=all-first
print(int(ans))
