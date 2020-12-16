#----my original answer
N, A, B=map(int,input().split())
ans=0
for n in range(N+1):
    temp=sum(map(int,list(str(n))))
    if temp>=A and temp<=B:
        ans+=n
print(ans)


#---other solution
# N,A,B=map(int,input().split())
# print(sum(i*(A<=sum(map(int,str(i)))<=B)for i in range(N+1)))

#---other solution
# N, A, B = map(int, input().split())
#
# N = N + 1
# cnt = 0
# S = 0
#
# S = sum([i for i in range(1, N) \
#          if \
#          A <= \
#          ((i // 10000) \
#           + (i // 1000) - (i // 10000) * 10 \
#           + (i // 100) - (i // 1000) * 10 \
#           + (i // 10) - (i // 100) * 10 \
#           + (i // 1) - (i // 10) * 10) \
#          <= B])
#
# print(S)