N = int(input())
#L=[list(map(int, input().split())) for i in range(int(input()))]

L=list(map(int, input().split()))
#print(L)
#L=[list(map(int, input().split())) for i in range(N)]
L_odd=L[::2]
j=0
for i in L_odd:
    #print(i)
    if i%2==1:
        j+=1
print(j)