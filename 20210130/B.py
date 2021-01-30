N, S, D = map(int, input().split())
L = [list(map(int, input().split())) for i in range(N)]

for l in L:
    if l[0]<S and l[1]>D:
        print('Yes')
        exit()
print('No')