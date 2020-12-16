r1, c1 = map(int, input().split())
r2, c2 = map(int, input().split())

if (r1==r2) and (c1==c2):
    print(0)
    exit()

if abs(r1-r2)+abs(c1-c2)<=3:
    print(1)
    exit()

if (r1+c1)%2==0:
    tmp1='even'
else:
    tmp1='odd'

if (r2+c2)%2==0:
    tmp2='even'
else:
    tmp2='odd'

if tmp1==tmp2:
    if (r2-r1)==(c2-c1):
        print(1)
        exit()
    else:
        print(2)
        exit()
else:
    # ------
    if abs(c2 - (r2 - r1 + c1)) <= 3:
        # print('here1')
        print(2)
        exit()

    if abs(r2 - (c2 - c1 + r1)) <= 3:
        # print(r2 - (c2 - c1 + r1))
        # print('here2')
        print(2)
        exit()

    if abs(r2-r1)+abs(c2-c1)<=6:
        print(2)
        exit()
    # --------
print(3)
