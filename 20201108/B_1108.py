N = int(input())
L = list(map(int, input().split()))
dic={0:0}
for i in range(2,max(L)+1):
    count=0
    for A in L:
        if A%i==0:
            count+=1
    dic[i]=count
import operator
print(max(dic.items(), key=operator.itemgetter(1))[0])

