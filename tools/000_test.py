# import sys
# print(sys.getrecursionlimit())
# while True:
#     N=int(input())
#     if N==1:
#         print('YES')
#         exit()
#         #sys.exit()

#再帰関数
import sys
sys.setrecursionlimit(10**6)
def recu_test(n):
    if n < 1:
        #print(n)
        #print('Finish')
        return 0
    return n + recu_test(n - 1)

print(recu_test(10))