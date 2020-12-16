N = int(input())
s = str(input())

t=''
count=0
for i in s:
    t+=i
    #print(t)
    if t[-3:]=='fox':
        count+=1
        t=t[:-3]
# print(t)
print(len(t))

#
#
#
#
#
#
#
#
#
# import re
# s=s.replace('fox','0')
# s=s.replace('ox','3')
# s=s.replace('fo','4')
# s=s.replace('x','4')
# s=s.replace('f','3')
#
# y = re.sub(r"[a-z]", "@", s)
# print(y)
# y = y.replace("@3", "93")
# print(y)
# y = y.replace("@4", "94")
# y = y.replace("3@", "39")
# y = y.replace("4@", "49")
# y = y.replace(r"@", "")
#
# print(y)
#
# for i in y:
#     if i ==9:
#         eee
#     else:
#         tmp.append(i)
#
# #
# #
# # ans[1]=ans[1].replace('ox','3')
# # ans[1]=ans[1].replace('x','4')
# # ans[0]=ans[0].replace('fo','4')
# # ans[0]=ans[0].replace('f','3')
# #
# #
# # # num=s.count('fox')
# # # ans=s.split('fox')
# # ans=s.split('fox')
# #
# #
# # print(ans)
# # ans[1]=ans[1].replace('ox','3')
# # ans[1]=ans[1].replace('x','4')
# # ans[0]=ans[0].replace('fo','4')
# # ans[0]=ans[0].replace('f','3')
# # print(ans[0][::-1])
# # print(ans[1])
# # print(ans)
