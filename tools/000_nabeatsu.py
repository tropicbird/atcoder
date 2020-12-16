X=int(input())
if X%3==0:
    print('Yes')
    exit()
while X>0:
    if X%10==3:
        print("Yes")
        exit()
    else:
        X=X//10
print('No')