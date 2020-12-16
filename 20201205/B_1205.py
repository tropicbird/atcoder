N = int(input())
import math
from functools import reduce

N_ls=[i for i in range(2,N+1)]
# print(N_ls)

def lcm_base(x, y):
    return (x * y) // math.gcd(x, y)

def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)

def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)

tmp=lcm_list(N_ls)
ans=tmp+1
# for i in N_ls:
#     print(ans%i)
print(ans)