n = int(input())

import decimal

# if n==1:
#     print(1)
#     exit()

def solv_quadratic_equation(a, b, c):
    """ 2次方程式を解く  """
    #D = math.sqrt((b**2 - 4*a*c))
    #decimal.Decimal
    d = decimal.Decimal(b ** 2 - 4 * a * c)

    D=d.sqrt()

    #print(D)
    x_1 = (-b + D) / (2 * a)
    #print(x_1)
    #x_2 = (-b - D) / (2 * a)

    #print(x_1)
    #print(int(x_1))

    return x_1
    #return x_1, x_2

tmp=int(solv_quadratic_equation(1,1,-2*(n+1)))+1-2
#print(tmp)
ans=n-tmp
print(ans)
