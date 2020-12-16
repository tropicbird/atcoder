X, Y, A, B = map(int, input().split())
import math
ans=0

ex=math.log(B/X,A)
#print(ex)
if ex <0:
    ex=0
else:
    ex=int(ex)
#print(ex)

if Y/X==A:
    ex1=0
else:
    ex1=math.log(Y/X,A)
    #print(ex1)
    ex1=int(ex1)
    #print(ex1)
#ex1=int(ex1)


if ex>ex1:
    ex=int(ex1)

# while X_new*A<B:
#     ans+=1
#     X_new=X_new*A

X_new=A**ex*X
#print(X_new)

if (Y-X_new)==B:
    ex2=0
else:
    if (Y-X_new)%B==0:
        ex2 = int(((Y - X_new) / B)-1)
    else:
        ex2=int((Y-X_new)/B)
#print(ex2)

ans=ex+ex2
print(ans)