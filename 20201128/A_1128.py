a, b, x, y = map(int, input().split())

if b>a:
    ans = min(2*x*(b-a)+x, y*(b-a)+x)
    # if 2*x<y:
    #     ans=2*x*(b-a)+x
    # else:
    #     ans=y*(b-a)+x
    print(ans)
    exit()

if b==a:
    print(x)
    exit()

if a>b:
    if (a-b)==1:
        ans=x
        print(ans)
        exit()
    ans = min((a-b-1)*x+x, (a-b-1)*y + x)
    print(ans)
    exit()

    # elif (a-b)*(2*x) > (a-b-1)*y+x:
    #     ans=(a-b-1)*y+x
    #     print(ans)
    # else:
    #     ans=(a-b)*(2*x)
    #     print(ans)