N = int(input())
import numpy as np
#max=int(np.sqrt(N))

for n in range(1,N+1):
    j=0
    min = 1
    max = int(np.sqrt(n/3))+2
    #print(f'max:{max}')
    for x in range(min,max):
        #print(f'max:{max}')
        for y in range(min, max):
            for z in range(min, max):
                if x ** 2 + y ** 2 + z ** 2 + x * y + y * z + z * x > n:
                    break
                if x**2+y**2+z**2+x*y+y*z+z*x==n:
                    #print(f'n!!:{n}')
                    if x == y == z:
                        max=x
                        min=x
                        j += 1
                        #print(x, y, z)
                        #print(f'n:{n}')
                        break
                    if j==0:
                        max = z+1
                        min += 1
                        #min = x
                        #print(x, y, z)
                        #print(f'n:{n}')
                        j += 3
                    # else:
                    #     j += 3

    print(j)






