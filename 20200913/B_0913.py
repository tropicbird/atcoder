def main():
    a, b, c, d = map(int, input().split())
    if (a>=0) and (b>=0) and (c>=0) and (d>=0): #A
        ans=b*d
    elif (b<=0) and (d<=0):#E
        ans=a*c
    elif (a<=0) and (b>=0) and (c<=0) and (d>=0):#F
        tmp1=a*c
        tmp2=b*d
        if tmp1>tmp2:
            ans=tmp1
        else:
            ans=tmp2
    elif (a>=0) and (b>=0) and (d<=0):#H
        ans=a*d
    elif (c>=0) and (d>=0) and (b<=0):#C
        ans=b*c
    elif (a<=0) and (b>=0) and (c<=0) and (d<=0):#I
        ans=a*c
    elif (a<=0) and (b<=0) and (c<=0) and (d>=0):#D
        ans=a*c
    elif (a>=0) and (b>=0) and (c<=0) and (d>=0):#G
        ans=b*d
    elif (a<=0) and (b>=0) and (c>=0) and (d>=0):#B
        ans=b*d
    print(ans)


if __name__ == '__main__':
    main()