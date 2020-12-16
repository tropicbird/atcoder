#-----my original solution
N, Y=map(int, input().split())
flag=False
for x in range(N+1):
    for y in range(N+1-x):
        z = N-x-y
        if x*10000+y*5000+z*1000==Y:
            flag=True
            print(x,y,z)
            break
    if flag:
        break
if flag==False:
    print(-1,-1,-1)

#----other solution
# a0,a1 = map(int, input().split())
# a1=a1//1000
# out = (-1,-1,-1)
# for i in range(min(a0+1,a1//10+1)):
#     b=(a1-10*i)-(a0-i)
#     if b%4==0 and b>=0 and a0-i-b//4>=0:
#         out = (i,b//4,a0-i-b//4)
#         break
# print(out[0],out[1],out[2])