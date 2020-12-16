import math
X=int(input())
maximum=int(math.sqrt(X))
print(maximum)
for i in range(2,maximum+1):
    if X%i==0:
        print(i)
        print('No')
        exit()
print('Yes')

