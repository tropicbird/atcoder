#----my original
# N=int(input())
# L=list(map(int, input().split()))
# count=0
#
# x=True
# while x:
#     for i in range(N):
#         if L[i]%2==0:
#             L[i]=L[i]/2
#         else:
#             print(count)
#             x=False
#             break
#     count+=1

#----my revision
input()
L=list(map(int, input().split()))
count=0

while all(x%2==0 for x in L):
    L=[x/2 for x in L]
    count+=1
print(count)

#----reference
# input()
# A = list(map(int, input().split()))
# count = 0
# while all(a % 2 == 0 for a in A):
#     A = [a/2 for a in A]
#     count += 1
# print(count)