N, M, T = map(int, input().split())
# X = int(input())
# L = list(map(int, input().split()))
# H = int(input())
L = [list(map(int, input().split())) for i in range(M)]

tmp=N
old=0
for AB in L:
    down=AB[0]-old
    tmp-=(down+0.5)
    if tmp<=0:
        print('No')
        exit()

    charge=AB[1]-AB[0]
    tmp+=(charge+0.5)
    if tmp>=N:
        tmp=N
    old=AB[1]

down=T-old
tmp-=(down+0.5)
if tmp<0:
    print('No')
else:
    print('Yes')
