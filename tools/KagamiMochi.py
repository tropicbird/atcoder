#---my solusion
N=int(input())
L=list()
for i in range(N):
    L.append(int(input()))
print(len(set(L)))


#---other solution
# n = int(input())
# d = [int(input()) for i in range(n)]
# print(len(set(d)))

#---other solution
#print(len(set([int(input())for i in range(int(input()))])))