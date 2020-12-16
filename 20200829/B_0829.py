def main():
import numpy as np
S = str(input())
T = str(input())
len_T=len(T)
ls=[]
for i, t in enumerate(T):
    count = 0
    #print(i)
    for j, s in enumerate(S):
        #print(j)
        #print(t,s)
        if (len_T + j - i > len(S)):
            #print(j,i,t,s)
            break

        if (j - i < 0):
            continue

        if t == s:
            #print(t,s)
            #print(j, i, t, s)
            tmp=S[j-i:len_T+j-i]
            #print(tmp)
            #print(tmp)
            for x, y in zip(tmp,T):
                if x!=y:
                    count+=1
            ls.append(count)
                #break
#print(ls)
if len(ls)==0:
    print(len_T)
else:
    print(np.min(ls))

if __name__ == '__main__':
    main()