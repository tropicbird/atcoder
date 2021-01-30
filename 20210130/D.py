N = int(input())
# from itertools import accumulate
# maxnum=N//2+1
#
# for i in range(1,maxnum):
#     count+1
#     if

import math
def getseqs(s):
    count=0
    #print(s)
    p = 2 * s
    for n in range(2, math.ceil(math.sqrt(p))):
        if (p % n == 0):
            q = p // n
            if (((q - n) & 1) == 1):  #compare parity
                #a = (q - n + 1) // 2
                #seq = list(range(a, a+n))
                # print(seq, sum(seq))
                count+=1
    print(count*2+2)

getseqs(N)

#