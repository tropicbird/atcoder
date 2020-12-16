#----my original
A=int(input())
B=int(input())
C=int(input())
X=int(input())

count=0
for a in range(A+1):
    for b in range(B+1):
        for c in range(C+1):
            if X==a*500+b*100+c*50:
                count+=1
print(count)

#-----reference
# A = int(input().rstrip())
# B = int(input().rstrip())
# C = int(input().rstrip())
# X = int(input().rstrip())
# ans = 0
#
# for i in range(A + 1):
#     a = 500 * i
#     for j in range(B + 1):
#         b = 100 * j
#         k = X - a - b
#         if k >= 0 and k % 50 == 0 and k / 50 <= C:
#             ans += 1
#
# print(ans)