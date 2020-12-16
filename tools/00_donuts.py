def solution(A):
    #import numpy as np
    # write your code in Python 3.6
    maximum=max(A)
    set_A = set(A)
    #set_B = set(np.arange(1, maximum+1))
    set_B ={i for i in range(1, maximum + 1)}
    #set_B = set(np.arange(1, maximum + 1))
    print(set_A)
    print(set_B)
    set_C = set_B - set_A
    print(set_C)

    if set_C == {}:
        return maximum+2



    print(min(set_C))


A=[1,2,3]
solution(A)