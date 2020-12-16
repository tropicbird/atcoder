N, W = map(int, input().split())
L = [list(map(int, input().split())) for i in range(N)]
#import numpy as np
#listofzeros = [0] * N
#listofzeros=np.array(listofzeros)

#y=1000000007

tmax = 2*(10**5)+1
ww=[0]*tmax

for l in L:
    S=l[0]
    T=l[1]
    P=l[2]
    #print(l)
    #print(T)
    ww[S]+=P
    ww[T]-=P
    #print(ww)

psum=0
for i in range(tmax):
    psum+=ww[i]

    if psum > W:
        print("No")
        exit()
print("Yes")




# if max(listofzeros)>W:
#     print("No")
# else:
#     print("Yes")
#print(listofzeros)
