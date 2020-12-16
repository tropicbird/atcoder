L=[list(map(int, input().split())) for i in range(int(input()))]
position=[0,0,0]
for l in L:
    flag=0
    if l[0]-position[0] < abs(l[1])-abs(position[1]) + abs(l[2])-abs(position[2]):
        print('No')
        break
    elif abs(l[1])-abs(position[1]) + abs(l[2])-abs(position[2])==0:
        if (l[0]-position[0])%2==1:
            print('No')
            break
        else:
            flag=1
            position=l
            continue
    else:
        if abs((abs(l[1]) - abs(position[1])) + abs(abs(l[2]) - abs(position[2])))==1:
            if (l[0]-position[0])%2==1:
                flag = 1
                position = l
                continue
            else:
                print('No')
                break
        modulo=(l[0]-position[0]) % abs((abs(l[1])-abs(position[1])) + abs(abs(l[2])-abs(position[2])))
        if modulo%2==0:
            flag = 1
            position = l
            continue
        else:
            print('No')
            break
if flag==1:
    print('Yes')


#-----solution....
# n = int(input())
# li = list()
# x = 0
# y = 0
# t = 0
#
# for i in range(n):
#     li = [int(i) for i in input().split()]
#     if (li[0] - t) < abs(li[1] - x) + abs(li[2] - y):
#         print('No')
#         exit()
#     else:
#         if ((li[0] - t) - (abs(li[1] - x) + abs(li[2] - y))) % 2 == 1:
#             print('No')
#             exit()
#     x, y = li[1], li[2]
#     t = li[0]
# print('Yes')







    # if l[0] % (abs(l[1]) + abs(l[2]))!=2:
    #     print('No')
    #     break
    # else:
    #     print('Yes')
#
#
#     else:
#         min_step=abs(l[1]) + abs(l[2])
#         for n in reversed(range(l[0]-abs(l[1]) - abs(l[2])+1)):
#             if l[0] == min_step+2*n:
#                 flag=1
#                 break
#         if flag==0:
#             print('No')
#             break
#     # else:
#     #     continue
# if flag==1:
#     print('Yes')
