N, M = map(int, input().split())
AB_L = [list(map(int, input().split())) for i in range(M)]
# K = int(input())
# CD_L = [list(map(int, input().split())) for i in range(K)]
#
# print(AB_L)
# print(CD_L)
#
#
# for i in range(1,N):
#



n = int(input())
g = [[] for _ in range(100)]
nmax = 0
map(int, input().split())
CD_L = [list(map(int, input().split())) for i in range(n)]
CD_L.
    for i in range(n):
        a, b = CD_L[i]
        nmax = max(nmax, a, b)
        a -= 1
        b -= 1
        g[a].append(b)
        g[b].append(a)

    used = [0] * N #nmax


    def dfs(v, p, b):
        if used[v] == 1:
            b = True
        if p != -1:
            used[v] = 1

        for u in g[v]:
            if u != p:
                b = b or dfs(u, v, b)
        if p == -1 and b:
            used[v] = 1
        return b


    for i in range(N):#(nmax):
        if used[i] == 0 and len(g[i]) > 0:
            dfs(i, -1, False)

    print(used)

    count=0
    for AB in AB_L:
        if (used[AB[0]-1]==1) and (used[AB[1]-1]==1):
            count+=1

    print(count)
#print(sum(used))