def main():
    import numpy as np
A,B,C=map(int,input().split())
K=int(input())
flag = 0

if K==0:
    if B > A and C > B:
        print('Yes')
        flag = 1
    else:
        pass
elif K>0:
    if B<=A:
        for k in range(K):
            if B*(k+1)*2>A:
                Bnew=B*(k+1)*2
                print(f'k:{k}')
                print(f'A:{A}')
                print(f'newB:{Bnew}')
                newK = K - k - 1
                print(f'newK:{newK}')
                for newk in range(newK):
                    if C * (newk + 1) * 2 > Bnew:
                        print('Yes')
                        flag=1
                        break
                break
    else:
        for k in range(K):
            if C * (k + 1) * 2 > B:
                print('Yes')
                flag = 1
                break

if flag == 0:
    print('No')

if __name__ == '__main__':
    main()