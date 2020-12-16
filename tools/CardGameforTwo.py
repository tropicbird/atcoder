#----my original solution
input()
# L=list(map(int, input().split()))
# L.sort(reverse=True)

L=sorted(map(int,input().split()))[::-1]#-----[::-1] is useful

a=0
b=0
for (num,val) in zip(range(len(L)),L):
    if num%2==0:
        a+=val
    else:
        b+=val
print(a-b)

#-----other solution
# input()
# A=sorted(map(int, input().split()))[::-1]
# print(sum(A[::2])-sum(A[1::2]))