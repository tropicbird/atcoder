N = int(input())
L = list(map(int, input().split()))
# import numpy as np
# L = np.random.randint(10, size=200000).tolist()
from itertools import accumulate
L_tmp=list(accumulate(L))
L_new=[0]
L_new.extend(L_tmp)
print(L_new)
L_new=list(accumulate(L_new))
print(L_new)
L_tmp=[0]
L_tmp2=L
L_tmp.extend(L_tmp2)

# L_tmp.extend(L_tmp2)
# print(f'L_tmp:{L_tmp}')
#L_new2=[i*2+j for i,j in zip(L_new,L_tmp)]
print(f'L_new:{L_new}')
print(f'L_tmp:{L_tmp}')
L_new2=[i*2+j for i,j in zip(L_new,L_tmp)]
print(L_new2)
max_value = max(L_new2)
print(max_value)
#max_index = L_new.index(max_value)
#print(max_index)

